# Generates workspace/experiments/results/<test>/plan.json for T1,T2,T3,T4,T6 with self-checks computed from the prompt text only.
import json, re, sys, pathlib, datetime

OUT = pathlib.Path(sys.argv[1])
D6 = 6.58  # effective duration for seconds=6 @0.5MP (verified 158 frames / 24 fps)
SEEDS = [1001, 1002, 1003]
FROZEN = "2026-10-20"
MUSIC_NA = "N/A"
MUSIC_WORDS = r"music|score|soundtrack|melody|bgm|配樂"
LIGHT_NOUN = r"\b(sun|sunlight|lamp|lamplight|neon|window light|street ?light|sky light|studio light|light panel)\b"
CAMERA = (r"pushes in|pulls out|pans (left|right)|tilts (up|down)|trucks (left|right)|pedestals (up|down)|"
          r"zooms (in|out)|tracks the|holds a static shot|point of view|rolls (clockwise|counterclockwise)|shakes (slightly|strongly)")
ALIGN = "For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced."


def three_col(desc, sound, music=MUSIC_NA):
    return f"integrated_multimodal_description: {desc}\n\noverall_soundscape: {sound}\n\nnon_diegetic_music: {music}"


def six_sec(subj, summary, retention, desc, sound, music=MUSIC_NA):
    return (f"subject_definitions: {subj}\n\nsummary: {summary}\n\nretention_analysis: {retention}\n\n"
            f"detailed_description: {desc}\n\noverall_soundscape: {sound}\n\nnon_diegetic_music: {music}")


def shots(desc):
    parts = re.split(r"(?=\[Shot \d+\])", desc)
    return [p for p in parts if p.strip().startswith("[Shot")] or [desc]


def self_check(prompt, full_desc, duration, appearance_terms=None):
    desc = full_desc.replace(ALIGN, "").strip()  # alignment sentence contains "[Shot 1]"; exclude it from shot parsing
    segs = shots(desc)
    cuts = [int(m[0]) * 60 + float(m[1]) for m in re.findall(r"At (\d\d):(\d\d\.\d{3})", desc)]
    gaps = [b - a for a, b in zip([0.0] + cuts, cuts + [duration])]
    r = {
        "word_count_counted_field": len(full_desc.split()),
        "shot_tags": len(re.findall(r"\[Shot \d+\]", desc)),
        "shot1_has_timestamp": len(re.findall(r"\[Shot 1\] At", desc)),
        "cut_times_s": cuts,
        "shot_lengths_s": [round(g, 3) for g in gaps],
        "all_shots_ge_2s": all(g >= 2.0 for g in gaps),
        "orbit_words": len(re.findall(r"orbit|\barc(s|ing)?\b|circles around|360-degree", desc, re.I)),
        "camera_sentences_per_shot": [len(re.findall(CAMERA, s, re.I)) for s in segs],
        "then_or_as_per_shot": [bool(re.search(r"\b(then|as)\b", s, re.I)) for s in segs],
        "light_nouns_per_shot": [len(re.findall(LIGHT_NOUN, s, re.I)) for s in segs],
        "foreground_hits_per_shot": [len(re.findall(r"foreground|in front of|out-of-focus", s, re.I)) for s in segs],
        "angle_conflict_per_shot": [bool(re.search(r"eye[- ]level", s, re.I) and re.search(r"high-angle|low-angle|top-down", s, re.I)) for s in segs],
        "music_word_hits_whole_prompt": len(re.findall(MUSIC_WORDS, prompt, re.I)),
        "has_soundscape_field": "overall_soundscape:" in prompt,
        "has_music_field": "non_diegetic_music:" in prompt,
    }
    if appearance_terms:
        r["appearance_term_hits_in_counted_field"] = {t: len(re.findall(rf"\b{t}\b", desc, re.I)) for t in appearance_terms}
    return r


def pair_check(a_desc, b_desc, shared):
    wa, wb = len(a_desc.split()), len(b_desc.split())
    diff = (wb - wa) / wa * 100
    assert abs(diff) <= 10, f"word diff {diff:.1f}%"
    return {"words_A": wa, "words_B": wb, "diff_pct_B_vs_A": round(diff, 1), "within_10pct": True,
            "shared_strings_byte_identical": {k: True for k in shared},
            "method": "python: len(field.split()) == wc -w; shared sentences are the same Python string objects inserted into both arms, asserted present verbatim in both"}


def assert_shared(a, b, shared):
    for k, v in shared.items():
        assert v in a and v in b, k


RATER_COMMON = {
    "scale_note": "0 = absent/failed, 1 = partial/ambiguous, 2 = clearly present. Score each clip independently; never compare two clips side by side before all scores are written.",
    "artifact": {"0": "severe: limb/face melt, body splits, object morphs", "1": "minor transient glitch < 0.5 s", "2": "none visible"},
}

BLIND = {
    "submitter": "Haiku-S (submits jobs, extracts frames, runs objective scripts). Sees prompts; never rates.",
    "rater": "Haiku-R (different agent instance). Sees only code-named media + rater_brief + rubric, in E:/MinimaxH3/_blind/<test-id>/ (outside the repo). Must not read the repo, plan.json, jobs.json or FreeVideo labels.",
    "codes": "Main session draws a random 6-char [a-z0-9] code per (arm, seed) with secrets.token_hex, writes the key to workspace/experiments/_local/<test-id>/key.json (gitignored), and gives Haiku-S only code -> prompt-file mapping. FreeVideo ref = <test-id>-<code>-<yyyymmddHHMM>; label = test id + code, never arm letters.",
    "order": "Main session shuffles clip order separately for the rater.",
    "unblinding": "Only after scores.csv and metrics.csv are committed to the working tree; then main session copies key.json into summary.md.",
    "known_leaks": [],
}

FREEVIDEO = {
    "endpoint": "http://127.0.0.1:8189/freevideo/agent/v1  (POST /plan first, then POST /jobs)",
    "body_keys_seen_in_repo_scripts": ["kind='generate'", "prompt (single string = the assembled prompt below)", "seconds", "aspect",
                                       "megapixels", "quality", "seed", "label", "ref", "media.references[{file}]"],
    "confirm_via_plan": True,
    "confirm_note": "How FreeVideo distinguishes i2va first frame vs Ref2VA reference (and whether a 'task type' key exists) is NOT verified; inspect /plan response before /jobs. If /plan width/height or frame count differ from expected, stop and report; do not submit.",
}


def base(test_id, task, aspect, wh, first_frame, hypothesis, variable, held_constant):
    return {
        "test_id": test_id, "frozen": FROZEN, "frozen_by": "Opus plan/review", "status": "frozen",
        "hypothesis": hypothesis, "single_variable": variable, "held_constant": held_constant,
        "params": {"kind": "generate", "task_type": task, "megapixels": 0.5, "quality": "medium", "seconds": 6,
                   "aspect": aspect, "expected_width_height": wh, "expected_frames": 158, "expected_effective_seconds": D6,
                   "seeds": SEEDS, "jobs": 6},
        "first_frame_source": first_frame, "freevideo": FREEVIDEO, "blind_protocol": BLIND,
    }


def metrics_common():
    return {
        "contact_sheet": "ffmpeg -i <code>.mp4 -vf \"fps=2,scale=272:-2,tile=7x2\" -frames:v 1 thumbs/<code>.jpg",
        "scene_cuts": "ffmpeg -i <code>.mp4 -vf \"select='gt(scene,0.3)',showinfo\" -f null - 2>&1 | grep -o 'pts_time:[0-9.]*'  (threshold 0.3 primary; also log 0.2 and 0.4)",
        "end_settle_residual_motion": "ffmpeg -sseof -1 -i <code>.mp4 -vf \"tblend=all_mode=difference,signalstats,metadata=print:key=lavfi.signalstats.YAVG\" -f null - 2>&1 | grep YAVG  -> mean YAVG over last 1 s (lower = more still)",
        "per_frame_L": "ffmpeg -i <code>.mp4 -vf fps=2 frames/<code>_%02d.png ; python -I scripts/color_qa.py frames/<code>_*.png  -> take meanLab L* per frame; report mean and std (ignore the pairwise lines)",
    }


plans = {}

# ---------------- T1 action chain ----------------
T1_SCENE = "[Shot 1] Live-action, cinematic. A full-body medium-wide shot at eye level, from the front, of the woman from <Picture 1> standing on a seamless light-grey studio floor in front of a matching grey backdrop."
T1_APPEAR = "Preserve the same facial identity, hairstyle, costume colours and boots shown in <Picture 1> throughout."
T1_START = "She begins standing upright with her feet together and her arms relaxed at her sides."
T1_A = ("Then she performs a powerful, graceful and dynamic full spin on the spot, an elegant, energetic and fluid turn "
        "that looks smooth, sharp, confident and stylish, beautifully controlled and impressive from start to finish, "
        "with a strong, expressive and dramatic feeling of movement and a polished, athletic quality throughout the whole spin.")
T1_B = ("Then she pushes off the ball of her right foot and pivots on the ball of her left foot through one full turn on the spot, "
        "her weight staying over the left foot, her spine upright and her hips leading her shoulders, "
        "as her momentum carries her half a step at the end and her hair swings outward, settling half a beat after her body stops.")
T1_END = "Finally she plants both feet shoulder-width apart, lowers her arms, and holds a balanced, still stance facing forward."
T1_CAM = "The camera holds a static shot."
T1_LIGHT = "Soft studio light from a large overhead light panel in front of her falls evenly on her face and shoulders and leaves a short soft shadow on the grey floor behind her heels."
T1_SOUND = "Quiet studio room tone with a faint hum of ventilation; the scuff of a boot sole on the floor during the turn, then the light double tap of both boots as she plants her feet."
t1 = {}
for arm, ex in (("A", T1_A), ("B", T1_B)):
    desc = " ".join([ALIGN, T1_SCENE, T1_APPEAR, T1_START, ex, T1_END, T1_CAM, T1_LIGHT])
    t1[arm] = (desc, three_col(desc, T1_SOUND))
sh = {"scene": T1_SCENE, "appearance": T1_APPEAR, "start_state": T1_START, "end_state": T1_END, "camera": T1_CAM, "light": T1_LIGHT, "soundscape": T1_SOUND, "music": MUSIC_NA}
assert_shared(t1["A"][1], t1["B"][1], sh)
p = base("T1", "i2va", "9:16", [544, 960],
         {"source": "user character sheet: 紫電長靴女 (purple-lightning boots woman), full-body FRONT cell only",
          "prep": "crop the full-body front cell, pad left/right with the sheet's own grey (sample a backdrop pixel) to exactly 9:16, resize to >= 544x960, save workspace/experiments/_local/chars/t1_first_frame.png; record sha256 in jobs.json. Same file for both arms.",
          "why_this_is_ok": "action test; prompt describes the same grey studio, so frame and text agree"},
         "Describing the execution of one main action with 2-3 mechanics (support/force, centre of mass/axis, inertia) instead of action name + adjectives makes H3 complete the action and settle cleanly more often, at equal word count.",
         "Only the execution sentence (one sentence) differs: A = action name + adjectives; B = support/pivot, weight/axis, inertia incl. hair lag. Everything else is the same string.",
         ["first frame", "start-state sentence", "end-state sentence (both explicitly ask to settle)", "single shot, no cuts", "camera sentence (static)", "light sentence", "appearance sentence", "soundscape", "music N/A", "seconds/aspect/mp/quality/seed"])
p["prompts"] = {arm: {"counted_field": "integrated_multimodal_description", "prompt": t1[arm][1],
                      "self_check": self_check(t1[arm][1], t1[arm][0], D6, ["hair", "hairstyle", "costume", "boots"])} for arm in "AB"}
p["pair_check"] = pair_check(t1["A"][0], t1["B"][0], sh)
p["self_check_notes"] = ["i2va: skill gives no fixed count ('shrink when a reference exists'); this plan targets 150-250 words, both arms equal.",
                         "single shot: no [Shot 2], no timestamps by design (shot structure is NOT the variable; the earlier §11 trial confounded it).",
                         "'hair' appears in B's inertia clause and the shared appearance sentence: B therefore has 2 'hair' hits; this is part of element #6/#8 (inertia), not an appearance restatement.",
                         "light/foreground: shared, so §10.8/8b pass equally ('in front of')."]
p["rater_brief"] = "A woman on a grey studio floor should do one full turn on the spot and end standing still, feet apart, arms down."
p["metrics"] = {"objective": {"end_settle_residual_motion": metrics_common()["end_settle_residual_motion"],
                              "scene_cuts": metrics_common()["scene_cuts"] + "  (expect 0; any cut = structural failure, log it)",
                              "contact_sheet": metrics_common()["contact_sheet"]}}
p["rubric"] = {**RATER_COMMON,
               "completion": {"0": "no recognisable full turn (partial twist, sway, or different action)", "1": "turn happens but under/over-rotated (>45 deg off) or interrupted", "2": "one clear full turn ending facing forward"},
               "settle": {"0": "still moving or drifting in the last 1 s", "1": "stops but wobbles / shifts feet in the last 1 s", "2": "planted and still for the last >= 0.7 s"},
               "legibility": {"0": "body mush: limbs blur/merge during the turn", "1": "brief blur but body readable", "2": "body and feet readable throughout"},
               "secondary_follow_through": {"0": "hair/costume frozen or self-animating against motion", "1": "moves but timing unrelated to the turn", "2": "lags the body and settles after it"},
               "composite": "completion + settle + legibility + artifact (0-8); follow_through reported separately"}
p["decision"] = {"promote_B": "B composite > A composite in 3/3 seeds, OR 2/3 with the third tied; AND B residual motion (last 1 s YAVG) not higher than A in >= 2/3 seeds -> mark action-choreography.md §11 '本機先導實測 (n=3, 0.5MP, i2va 6s)'.",
                 "demote": "A composite > B in >= 2/3 seeds with none reversed -> §11 back to '方法主張，先導實測未支持', log decision in memory.md.",
                 "inconclusive": "anything else -> rerun seeds 1004-1006 before deciding; do not edit references/.",
                 "resolution_limited": "if both arms score legibility 0 in the same seed, mark that seed resolution-limited and exclude it."}
plans["T1"] = p

# ---------------- T2 shot markers ----------------
T2_STYLE = "Live-action, cinematic, natural morning realism."
T2_S1 = ("A wide shot at eye level, from the side, of a small sunlit apartment kitchen: a man in his thirties in a grey t-shirt walks to the wooden counter, "
         "where a glass pour-over set waits in front of a tiled wall. The counter also holds a ceramic cup, a small grinder and a folded towel, and the rest of the kitchen stays tidy and quiet behind him. First he stops at the counter, then he lifts a steel kettle with his right hand, as steam curls from its spout. "
         "Morning sunlight from the window behind him rims his shoulders and lays a bright stripe across the counter, while a blurred potted plant sits in the foreground. "
         "The camera trucks right with small amplitude at slow speed, following him to the counter.")
T2_S2 = ("a high-angle close-up from above the counter of the paper filter: hot water spirals from the kettle spout onto the dark coffee grounds, "
         "then the grounds swell and bubble into a pale foam, as thin steam rises past the rim. "
         "The same window sunlight falls across the glass server and makes the dripping coffee glow amber, with the out-of-focus edge of the kettle in the foreground. "
         "The camera holds a static shot.")
T2_S3 = ("a medium close-up at a low angle, from the front, of the man: he lifts the finished cup toward his face, then breathes in the steam, "
         "as his shoulders drop and he lets out a slow breath. Window sunlight from camera-left lights one side of his face and the rising steam, "
         "and the out-of-focus rim of the cup fills the lower foreground. The camera pushes in with small amplitude at slow speed toward his face and holds the final frame. Behind him the kitchen falls softly out of focus, the window bright but not blown out, and nothing else moves in the room.")
T2_SOUND = "Quiet kitchen room tone with distant birds outside the window; the clink of the kettle lifting off its base, the soft hiss of water pouring onto the grounds and a faint bubbling as they bloom, then a ceramic tap as the cup leaves the counter and one slow exhale."
T2_B = f"[Shot 1] {T2_STYLE} {T2_S1} [Shot 2] At 00:02.200, the shot cuts to {T2_S2} [Shot 3] At 00:04.400, the shot cuts to {T2_S3}"
T2_A = f"{T2_STYLE} {T2_S1} Then the shot cuts to {T2_S2} Finally the shot cuts to {T2_S3}"
sh = {"style": T2_STYLE, "shot1": T2_S1, "shot2": T2_S2, "shot3": T2_S3, "soundscape": T2_SOUND, "music": MUSIC_NA}
pa, pb = three_col(T2_A, T2_SOUND), three_col(T2_B, T2_SOUND)
assert_shared(pa, pb, sh)
p = base("T2", "t2va", "16:9", [960, 544], {"source": "none (t2va)"},
         "Writing cuts as official '[Shot n] At MM:SS.mmm' markers makes H3 cut at the stated times; the same three shots written as prose with 'the shot cuts to' but no markers yields fewer or mistimed cuts (community claim: ~0.12 s error with timestamps; one static take without).",
         "Presence of [Shot n] tags + At timestamps. Shot content, cut wording ('the shot cuts to') and order are identical; A uses 'Then/Finally' where B uses tags.",
         ["all shot content sentences", "soundscape", "music N/A", "params", "seeds"])
p["prompts"] = {"A": {"counted_field": "integrated_multimodal_description", "prompt": pa, "self_check": self_check(pa, T2_A, D6)},
                "B": {"counted_field": "integrated_multimodal_description", "prompt": pb, "self_check": self_check(pb, T2_B, D6)}}
p["pair_check"] = pair_check(T2_A, T2_B, sh)
p["four_axis_B"] = [{"shot": 1, "size": "wide", "angle": "eye level, side", "move": "truck", "subject": "man"},
                    {"shot": 2, "size": "close-up", "angle": "high, from above", "move": "static", "subject": "filter/grounds"},
                    {"shot": 3, "size": "medium close-up", "angle": "low, front", "move": "push", "subject": "man's face"}]
p["self_check_notes"] = ["A is the control and fails §10.1-3 and §10.9 by design (no shot tags, so all three shots' angles fall in one segment).",
                         "B: 3 shots in D=6.58 s, cuts 2.200/4.400, last shot 2.18 s (>= 2.0). 6 s is the floor for 3 shots; do not move cuts later than 4.58.",
                         "T2VA 300-700 word band met by both arms."]
p["rater_brief"] = "A man makes pour-over coffee in a kitchen. Planned beats: wide shot of him lifting a kettle; close-up from above of water on coffee grounds; low-angle medium close-up of him smelling the cup."
p["metrics"] = {"objective": {"scene_cuts": metrics_common()["scene_cuts"],
                              "target_cuts_s": [2.2, 4.4], "match_window_s": 0.25,
                              "derived": "matched = targets with a detected cut within ±0.25 s (0-2); spurious = detected cuts not matched; abs_error = mean |t_detected - t_target| over matched",
                              "verified_cut_rule": "MECHANICAL, no human step: a cut is verified only if detected at threshold 0.3 AND at 0.4 within 0.1 s of each other. matched/spurious are computed from verified cuts; raw 0.3 counts are logged too.",
                              "rater_cut_check": "secondary only: Haiku-R (blind) gets code-named 3-frame strips (t-0.1, t, t+0.1) for every raw 0.3 detection and answers yes/no 'hard cut at t?'; logged, not used for the decision",
                              "contact_sheet": metrics_common()["contact_sheet"]}}
p["rubric"] = {**RATER_COMMON,
               "beat_coverage": {"0": "<= 1 of the 3 planned beats visible", "1": "2 beats", "2": "all 3 beats"},
               "beat_order": {"0": "wrong order or merged", "1": "order right but one beat truncated < 1 s", "2": "correct order, each beat >= ~1.5 s"},
               "composite": "beat_coverage + beat_order + artifact (0-6)"}
p["decision"] = {"promote_B": "B verified matched = 2 in 3/3 seeds AND B matched > A matched in >= 2/3 seeds -> prompt-formats.md community claim upgraded to '本機先導實測'; record mean abs_error.",
                 "claim_refuted": "A also reaches matched = 2 in >= 2/3 seeds -> the 'no timestamps = one static take' claim is false on this setup; rewrite it.",
                 "inconclusive": "else -> seeds 1004-1006."}
plans["T2"] = p

# ---------------- T3 light path ----------------
T3_STYLE = "[Shot 1] Live-action, cinematic, night-time city realism."
T3_SCENE = ("A medium close-up at eye level, from the front-left, of a young woman in a dark rain jacket standing under the narrow awning of a small corner café at night. "
            "A red neon sign hangs above the café window behind her, the window glass is streaked with rain, and a street lamp glows further down the wet street, "
            "its reflection broken by puddles on the pavement. Inside the café, empty tables and upturned chairs sit behind the glass, and a closed umbrella leans against the doorframe beside her. The pavement under her feet is dark and glossy with water. Out-of-focus raindrops on a glass panel sit in the foreground between her and the camera.")
T3_ACTION = ("First she stands still with her hood up and her hands in her pockets, watching the street. Then she lowers the hood with her right hand, "
             "as a few raindrops slide off the fabric and drip from its edge onto her shoulder. Finally she turns her head slowly toward the far end of the street and holds still, "
             "her breath faintly visible in the cold air. Her expression stays calm and tired, her lips closed, and her shoulders rise and fall slowly with her breathing.")
T3_RAIN = ("Steady light rain falls in thin vertical lines past the awning, splashes in the puddles, and runs along the gutter beside the kerb, "
           "while a single passing car far behind her leaves a soft smear of headlights on the wet road. Small drips fall from the awning edge in a steady row just in front of her, each one catching a brief glint as it drops.")
T3_A = ("The scene has cinematic lighting with a moody, atmospheric, dramatic and beautiful look, rich high-quality night lighting, "
        "deep contrast and a stylish, film-like glow over the whole frame.")
T3_B = ("Red neon light from the sign above the café passes through the wet window glass and falls only on the left side of her face, "
        "while her right side stays in soft shadow.")
T3_CAM = "The camera pushes in with small amplitude at slow speed toward her face and holds the final frame."
T3_SOUND = ("Steady rain drumming on the canvas awning and pattering into puddles, a gutter trickling beside the kerb, the rustle of the hood fabric as she lowers it, "
            "and one car passing far away on wet asphalt, its tyre hiss fading.")
t3 = {}
for arm, light in (("A", T3_A), ("B", T3_B)):
    desc = " ".join([T3_STYLE, T3_SCENE, T3_ACTION, light, T3_RAIN, T3_CAM])
    t3[arm] = (desc, three_col(desc, T3_SOUND))
sh = {"style": T3_STYLE, "scene_objects": T3_SCENE, "action": T3_ACTION, "rain": T3_RAIN, "camera": T3_CAM, "soundscape": T3_SOUND, "music": MUSIC_NA}
assert_shared(t3["A"][1], t3["B"][1], sh)
p = base("T3", "t2va", "16:9", [960, 544], {"source": "none (t2va); both arms share every scene object (neon sign, wet window glass, street lamp)"},
         "One light-path sentence (source -> medium -> lit surface) gives a readable, stable key direction better than 'cinematic lighting' + mood adjectives, at equal word count.",
         "The single lighting sentence: A = 'cinematic lighting' + adjectives; B = path sentence. All light-emitting objects exist in both arms as scene content.",
         ["scene objects incl. neon sign / window glass / street lamp", "action", "rain", "single shot", "camera", "soundscape", "music N/A", "params", "seeds"])
p["prompts"] = {arm: {"counted_field": "integrated_multimodal_description", "prompt": t3[arm][1], "self_check": self_check(t3[arm][1], t3[arm][0], D6)} for arm in "AB"}
p["pair_check"] = pair_check(t3["A"][0], t3["B"][0], sh)
p["self_check_notes"] = ["A intentionally contains 'cinematic lighting'/'high-quality' (red-flag words) - it is the control.",
                         "light_nouns counts are equal-ish in both arms because the neon sign and street lamp are scene objects in both; the variable is the path sentence, not the presence of sources."]
p["rater_brief"] = "Night, rain, a woman under a café awning lowers her hood and turns her head. Judge the lighting only."
p["metrics"] = {"objective": {"per_frame_L": metrics_common()["per_frame_L"] + "  -> report std(L*) as flicker proxy",
                              "palette_L_range": "python -I scripts/color_qa.py <code>.mp4 -> palette L* list; report max-min (contrast proxy, descriptive only)",
                              "face_side_ratio": "optional, manual: rater-independent Haiku-S crops left/right half of the face on the last frame and runs color_qa on both crops; report L*(left)-L*(right). Descriptive only.",
                              "note": "color_qa.py has NO luminance-zone feature; draft's '亮度分區' metric removed."}}
p["rubric"] = {**RATER_COMMON,
               "key_direction": {"0": "no identifiable main light direction on the face", "1": "direction guessable but inconsistent across the clip", "2": "one clear key side, stable through the clip"},
               "motivated": {"0": "light on her has no visible source in frame", "1": "plausible source but colour/direction mismatch", "2": "light on her clearly comes from a visible source (sign/lamp/window)"},
               "exposure": {"0": "face crushed or blown out", "1": "parts clipped", "2": "face readable with texture in shadow side"},
               "appeal_1_5": "1 = flat/muddy, 3 = acceptable, 5 = would use as-is",
               "composite": "key_direction + motivated + exposure + artifact (0-8); appeal reported separately"}
p["decision"] = {"promote_B": "B composite > A in 3/3 seeds (or 2/3 + tie) AND std(L*) of B not > A + 1.0 in >= 2/3 seeds -> shot-variety §6 / lighting §A path rule marked '本機先導實測'.",
                 "demote": "A >= B in >= 2/3 seeds -> path rule downgraded to style guidance; record in memory.md.",
                 "inconclusive": "else -> seeds 1004-1006."}
plans["T3"] = p

# ---------------- T4 HEX vs colour name ----------------
T4_STYLE = "[Shot 1] Live-action, cinematic, low-saturation dusk realism."
T4_SCENE = ("A medium-wide shot at eye level, from the front, of a lone traveller in a long heavy coat with a steel shoulder plate, holding a drawn straight sword lowered at his right side, "
            "standing at the mouth of a narrow alley between ruined brick buildings. Broken rubble and fallen beams lie across the ground, and a torn cloth banner hangs in the foreground at the left edge of the frame. Scorch marks streak the walls, a shattered window frame hangs open on the second floor, and a broken cart lies on its side halfway down the alley. The ground is uneven, and his boots find footing between broken bricks.")
T4_ACTION = ("First he stands still and catches his breath, then he walks three slow steps forward over the rubble, as loose grit crunches and slides under his boots; "
             "finally he stops, lifts his head, and looks down the alley while the coat hem settles against his legs. His face is lean and tired, his jaw set, and his free left hand hangs loose at his side, fingers slightly curled.")
T4_LIGHT = ("Dim dusk sky light from the gap in the broken skyline rakes across the left side of his shoulder plate and leaves the alley walls in deep shadow that keeps the brick texture.")
T4_A = ("Colour palette: the coat folds and the gaps between the rubble are #0B1118, the shadowed building walls are #1E2A38, his shoulder plate is #3B5068, "
        "the haze in the far distance is #6B8299, and only the blade edge and the catchlights in his eyes are #E6F2FF.")
T4_B = ("Colour palette: the coat folds and the gaps between the rubble are near-black navy, the shadowed building walls are dark slate blue, his shoulder plate is steel blue, "
        "the haze in the far distance is smoky blue-grey, and only the blade edge and the catchlights in his eyes are ice white.")
T4_ATMOS = "Thin haze drifts slowly through the far end of the alley, and a few flakes of ash float down through the air without settling. Small puddles between the stones hold a dull, still reflection of the sky."
T4_CAM = "The camera pulls out with small amplitude at slow speed as he walks forward, keeping his full body in frame, and holds the final composition."
T4_SOUND = "Low wind moving through the ruined alley, the banner cloth flapping softly, grit crunching and sliding under boots on each step, and a faint metallic tick as the sword shifts in his grip."
t4 = {}
for arm, pal in (("A", T4_A), ("B", T4_B)):
    desc = " ".join([T4_STYLE, T4_SCENE, T4_ACTION, T4_LIGHT, pal, T4_ATMOS, T4_CAM])
    t4[arm] = (desc, three_col(desc, T4_SOUND))
sh = {"style": T4_STYLE, "scene": T4_SCENE, "action": T4_ACTION, "light": T4_LIGHT, "atmos": T4_ATMOS, "camera": T4_CAM, "soundscape": T4_SOUND, "music": MUSIC_NA}
assert_shared(t4["A"][1], t4["B"][1], sh)
p = base("T4", "t2va", "16:9", [960, 544], {"source": "none (t2va)"},
         "H3 (Qwen3-VL text side) follows colour names bound to objects at least as well as HEX codes bound to the same objects; HEX gives no closer palette match to the card.",
         "Colour token form only (HEX vs colour name); same five objects, same order, same sentence frame.",
         ["scene", "action", "colourless light-path sentence", "atmosphere", "camera", "soundscape", "music N/A", "params", "seeds"])
p["card_hex"] = ["0B1118", "1E2A38", "3B5068", "6B8299", "E6F2FF"]
p["prompts"] = {arm: {"counted_field": "integrated_multimodal_description", "prompt": t4[arm][1], "self_check": self_check(t4[arm][1], t4[arm][0], D6)} for arm in "AB"}
p["pair_check"] = pair_check(t4["A"][0], t4["B"][0], sh)
p["self_check_notes"] = ["Shared light sentence is deliberately colour-free so the HEX arm gets no colour words from shared text.",
                         "'dusk' and 'low-saturation' are shared style cues present in both arms."]
p["rater_brief"] = "Dusk, ruined alley, a traveller with a lowered sword walks three steps and stops. Judge colour and artifacts only."
p["metrics"] = {"objective": {"card_palette_dE76": "python -I scripts/color_qa.py <code>.mp4 --ref 0B1118,1E2A38,3B5068,6B8299,E6F2FF -> 'card->palette dE76' (lower = closer). PRIMARY.",
                              "mean_Lab": "same run, meanLab (report a*, b* to see hue drift)",
                              "noise_floor": "palette dE76 has ~2 units of quantisation noise (lighting-and-color.md §E); differences < 2 count as ties",
                              "contact_sheet": metrics_common()["contact_sheet"]}}
p["blind_protocol"] = {**BLIND, "known_leaks": ["HEX arm may render '#0B1118'-style text or colour swatches in frame, which unblinds the rater. Therefore the objective card dE76 is the deciding metric; blind scores are secondary."]}
p["rubric"] = {**RATER_COMMON,
               "palette_feel": {"0": "warm or saturated, not cold blue", "1": "mixed", "2": "cold, low-saturation steel-blue throughout"},
               "text_or_swatch_artifact": {"0": "visible hex-like text, colour bars or swatches", "2": "none"},
               "composite": "palette_feel + text_or_swatch_artifact + artifact (0-6)"}
p["decision"] = {"keep_rule_no_HEX": "B card dE76 <= A + 2 in >= 2/3 seeds, or any A clip shows text/swatch artifact -> lighting-and-color.md keeps 'colour name + object, no HEX', marked '本機先導實測'.",
                 "HEX_has_value": "A card dE76 lower than B by > 2 in 3/3 seeds with no text artifact -> add HEX as an optional tested technique (not main rule) and rerun at 0.98MP once.",
                 "inconclusive": "else -> seeds 1004-1006."}
plans["T4"] = p

# ---------------- T6 identity: i2va vs Ref2VA ----------------
def t6_body(ref):
    # style sentence: three-column puts it at the start of [Shot 1]; Ref2VA puts it before [Shot 1] (prompt-formats.md B)
    head = "[Shot 1] Live-action, cinematic." if ref == "<Picture 1>" else "Live-action, cinematic. [Shot 1]"
    return (f"{head} A medium-wide shot at eye level, from the front, of the fox woman from {ref} on a seamless light-grey studio floor in front of a matching grey backdrop. "
            f"Preserve the same facial identity, white hair, nine fox tails and costume colours shown in {ref} throughout. "
            "First she stands with her weight on her left foot and her hands loosely clasped in front of her waist, then she walks three unhurried steps toward the camera, "
            "as her tails sway behind her a moment after each step and settle again when she stops. Her steps are light and even, heel then toe, and her shoulders stay level while she walks. Her arms stay relaxed, her clasped hands loosen slightly as she walks, and the hem of her clothing swings lightly with each step. "
            "Soft neutral studio light from a large overhead light panel in front of her falls evenly across her face and shoulders and leaves a short soft shadow on the floor behind her heels. "
            "The camera pulls out with small amplitude at slow speed, keeping her whole body in frame as she approaches. "
            "[Shot 2] At 00:03.000, the shot cuts to a close-up from her front-left at a slightly low angle, framing her face and shoulders: "
            "she begins with her eyes lowered toward the floor on her left, then she slowly raises her chin and turns her head to look straight ahead past the right edge of the frame, "
            "as a loose strand of hair slides across her cheek and comes to rest. Her expression stays calm and composed; she blinks once after the turn and holds the gaze. Her face stays fully visible and sharp, with no hair covering her eyes, and her breathing remains slow and even through the whole close-up. "
            "The same overhead light panel lights her forehead, cheekbones and the bridge of her nose, and the out-of-focus tip of one tail curls through the lower foreground. "
            "The camera holds a static shot. The background stays the same plain grey, with no props, no text and no other people, and the framing stays steady until the end of the clip. The pacing is calm and unhurried from the first step to the final held gaze.")


T6_SOUND = "Quiet studio room tone with a faint hum of ventilation; soft footsteps on the floor for each of her three steps, the light swish of fur as her tails sway, then near silence in the close-up with one soft breath."
A_desc = ALIGN + " " + t6_body("<Picture 1>")
B_desc = t6_body("<Subject 1>")
pa = three_col(A_desc, T6_SOUND)
B_subj = "<Subject 1> is the same fox woman established by <Picture 1> (face close-up) and <Picture 2> (full-body front view)."
B_sum = "[reference generation] <Subject 1> walks toward the camera in a grey studio, then a close-up shows her raising her head and turning her gaze."
B_ret = "<Subject 1>: fully_preserved - facial identity, hair, tails and costume colours from <Picture 1> and <Picture 2>; the grey sheet background and the four-view layout are not reproduced."
pb = six_sec(B_subj, B_sum, B_ret, B_desc, T6_SOUND)
# shared check: body text with the ref token normalised
assert A_desc.replace("<Picture 1>", "<REF>").replace("[Shot 1] Live-action, cinematic.", "STYLE").endswith(B_desc.replace("<Subject 1>", "<REF>").replace("Live-action, cinematic. [Shot 1]", "STYLE"))
assert T6_SOUND in pa and T6_SOUND in pb
p = base("T6", "A: i2va / B: ref2va", "9:16", [544, 960],
         {"A": "full-body FRONT cell of 白髮九尾狐 sheet, padded with the sheet's own grey to 9:16, >= 544x960 -> _local/chars/t6_first_frame.png (first frame)",
          "B": "two references, no first frame: <Picture 1> = face close-up cell, <Picture 2> = same full-body FRONT cell as A (unpadded crop is fine). Optional FreeVideo character card only if the user approves (persistent side effect); otherwise media.references only.",
          "same_source_sheet": True},
         "For identity held through motion and a cut, a Ref2VA character reference (subject_definitions + references) keeps face/hair/tails/costume closer to the sheet at mid and end of the clip than i2va with the sheet cell as first frame.",
         "Reference route (i2va first frame vs Ref2VA references). This is a ROUTE comparison, not a wording rule: Ref2VA necessarily adds subject_definitions/summary/retention_analysis; the counted description body is identical except the reference token (<Picture 1> vs <Subject 1>), the style-sentence position each format requires (start of [Shot 1] vs before [Shot 1]), and A's mandatory i2va alignment sentence.",
         ["description body", "appearance sentence", "two shots with cut at 3.000", "camera sentences", "soundscape", "music N/A", "params", "seeds"])
p["prompts"] = {"A": {"counted_field": "integrated_multimodal_description", "prompt": pa, "self_check": self_check(pa, A_desc, D6, ["hair", "tails", "costume"])},
                "B": {"counted_field": "detailed_description", "prompt": pb, "self_check": self_check(pb, B_desc, D6, ["hair", "tails", "costume"])}}
wa, wb = len(A_desc.split()), len(B_desc.split())
p["pair_check"] = {"words_A": wa, "words_B": wb, "diff_pct_B_vs_A": round((wb - wa) / wa * 100, 1), "within_10pct": abs(wb - wa) / wa <= 0.10,
                   "shared_strings_byte_identical": {"description_body_modulo_ref_token": True, "soundscape": True, "music": True},
                   "difference_explained": "A = B body + i2va alignment sentence (official requirement for i2va)."}
assert p["pair_check"]["within_10pct"]
p["four_axis"] = [{"shot": 1, "size": "medium-wide", "angle": "eye level, front", "move": "pull", "subject": "full body"},
                  {"shot": 2, "size": "close-up", "angle": "slightly low, front-left", "move": "static", "subject": "face"}]
p["self_check_notes"] = ["Ref2VA body targets the official 350-500 detailed_description band; A uses the identical body (i2va has no fixed count).",
                         "Appearance terms: 'hair' 3x (appearance sentence + strand-of-hair motion + 'no hair covering her eyes'), 'tails' 2x (appearance + sway) - motion/visibility mentions, not appearance restatements; flagged for review against §10.12.",
                         "Shot 2 uses 'slightly low angle' with no 'eye level' in the same shot - §10.9 passes.",
                         "Character facts beyond 'white hair, nine fox tails' are NOT asserted because the plan author has not seen the sheet; main session must confirm these two words match the image before submit (change both arms identically if not)."]
p["rater_brief"] = "Reference sheet image is provided. A fox woman walks toward camera, then a close-up of her face turning. Compare identity to the sheet only."
p["metrics"] = {"objective": {"identity_frames": "extract frames at t = 1.5 s (mid shot 1) and t = 6.0 s (end of shot 2): ffmpeg -ss <t> -i <code>.mp4 -frames:v 1 frames/<code>_<t>.png",
                              "costume_palette_drift": "python -I scripts/color_qa.py frames/<code>_1.5.png _local/chars/t6_fullbody_cell.png -> palette dE76 (lower = closer). Coarse; descriptive.",
                              "face_embedding": "NOT available in repo. Only if insightface/facenet is already installed locally may Haiku-S add cosine similarity vs the face cell; otherwise omit. Do not install for this test.",
                              "scene_cuts": metrics_common()["scene_cuts"] + "  (expect 1 cut near 3.0 s)"}}
p["rubric"] = {**RATER_COMMON,
               "face_match_mid": {"0": "different person", "1": "similar but key features changed (eye shape, face shape, age)", "2": "same person as sheet"},
               "face_match_end": {"0": "different person", "1": "similar but key features changed", "2": "same person as sheet"},
               "hair_tails_match": {"0": "colour/length/tail count clearly wrong", "1": "minor drift (shade, style, fewer tails)", "2": "matches sheet"},
               "costume_match": {"0": "different outfit or colours", "1": "same outfit with detail/colour drift", "2": "matches sheet"},
               "composite": "face_match_mid + face_match_end + hair_tails_match + costume_match + artifact (0-10). Frame 0 is NOT scored (trivially perfect for i2va)."}
p["decision"] = {"prefer_ref2va": "B composite > A in 3/3 seeds (or 2/3 + tie) -> long-form/consistency guidance recommends Ref2VA references for identity through motion+cut ('本機先導實測').",
                 "prefer_i2va": "A > B in >= 2/3 seeds -> recommend sheet-cell first frame when the scene can match the sheet; note grey-sheet scene limitation.",
                 "inconclusive": "else -> seeds 1004-1006.",
                 "resolution_limited": "if face_match scores are 1 in both arms for all seeds, mark 'resolution-limited at 0.5MP' and rerun one seed at 0.98MP."}
plans["T6"] = p

for tid in ("T3", "T4"):
    plans[tid]["metrics"]["objective"]["scene_cuts"] = metrics_common()["scene_cuts"] + "  (expect 0; single-shot prompt)"
    plans[tid]["decision"]["structural_fail"] = "a clip with a verified cut (detected at 0.3 AND 0.4) is scored structural-fail; that seed pair is excluded from the objective comparison and reported separately. If >= 2 seed pairs are excluded, the test is inconclusive."

for tid, plan in plans.items():
    iv = {"computed_by": "freeze_plans.py from the exact strings written", "bash_cross_check": "2026-10-20 Git Bash wc -w on the extracted counted field, diff of overall_soundscape..non_diegetic_music block, grep -oiE music words: all matched these numbers"}
    for arm, v in plan["prompts"].items():
        m = re.search(r"(integrated_multimodal_description|detailed_description): (.*?)\n\noverall_soundscape", v["prompt"], re.S)
        iv[f"wc_w_{arm}"] = len(m.group(2).split())
        iv[f"music_word_hits_{arm}"] = len(re.findall(MUSIC_WORDS, v["prompt"], re.I))
    tails = {arm: v["prompt"][v["prompt"].index("overall_soundscape:"):] for arm, v in plan["prompts"].items()}
    iv["soundscape_and_music_block_identical"] = tails["A"] == tails["B"]
    assert iv["soundscape_and_music_block_identical"] and iv["music_word_hits_A"] == iv["music_word_hits_B"] == 1
    plan["independent_verification"] = iv
    d = OUT / tid
    d.mkdir(parents=True, exist_ok=True)
    (d / "plan.json").write_text(json.dumps(plan, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    for arm, v in plan["prompts"].items():
        sc = v["self_check"]
        print(tid, arm, "words", sc["word_count_counted_field"], "shots", sc["shot_tags"], "cuts", sc["cut_times_s"], "lens", sc["shot_lengths_s"],
              "cam", sc["camera_sentences_per_shot"], "then/as", sc["then_or_as_per_shot"], "light", sc["light_nouns_per_shot"],
              "fg", sc["foreground_hits_per_shot"], "music", sc["music_word_hits_whole_prompt"], "orbit", sc["orbit_words"],
              "angle_conflict", sc["angle_conflict_per_shot"], sc.get("appearance_term_hits_in_counted_field", ""))
    print(tid, "pair", plan["pair_check"]["words_A"], plan["pair_check"]["words_B"], plan["pair_check"]["diff_pct_B_vs_A"])
