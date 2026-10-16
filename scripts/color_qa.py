# color_qa.py - stdlib only, needs ffmpeg on PATH. Run: python -I color_qa.py A.mp4 B.png [--ref HEX,HEX,...]
# Per input (image or video, video sampled at 2 fps): mean CIELAB (per-pixel mean), top-5 palette.
# Pairwise: dE76 of mean Lab AND palette dE76 (symmetric mean nearest-swatch distance).
# shortcut: CIE76 only, no dE2000; mean-colour dE misses images that differ but average to the same grey.
import sys, subprocess, math, collections

def pixels(path, w=160, h=90):
    vf = f"fps=2,scale={w}:{h}" if path.lower().endswith((".mp4", ".mov", ".mkv", ".webm")) else f"scale={w}:{h}"
    cmd = ["ffmpeg", "-hide_banner", "-loglevel", "error", "-i", path, "-vf", vf,
           "-f", "rawvideo", "-pix_fmt", "rgb24", "-"]
    raw = subprocess.run(cmd, capture_output=True, check=True).stdout
    if not raw:
        sys.exit(f"no pixels decoded from {path}")
    return [tuple(raw[i:i + 3]) for i in range(0, len(raw), 3)]

def to_lab(p):  # sRGB (D65) -> CIELAB
    def lin(c):
        c /= 255
        return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = (lin(x) for x in p)
    X = (0.4124 * r + 0.3576 * g + 0.1805 * b) / 0.95047
    Y = 0.2126 * r + 0.7152 * g + 0.0722 * b
    Z = (0.0193 * r + 0.1192 * g + 0.9505 * b) / 1.08883
    f = lambda t: t ** (1 / 3) if t > 0.008856 else 7.787 * t + 16 / 116
    fx, fy, fz = f(X), f(Y), f(Z)
    return (116 * fy - 16, 500 * (fx - fy), 200 * (fy - fz))

def palette(px, k=5):  # 16-level-per-channel histogram, top-k bin centres
    cnt = collections.Counter((r >> 4, g >> 4, b >> 4) for r, g, b in px)
    return [to_lab(tuple((c << 4) + 8 for c in key)) for key, _ in cnt.most_common(k)]

def pal_dist(p, q):  # symmetric mean nearest-neighbour dE76 between two palettes
    a = sum(min(math.dist(x, y) for y in q) for x in p) / len(p)
    b = sum(min(math.dist(x, y) for y in p) for x in q) / len(q)
    return (a + b) / 2

def hex_lab(h):
    return to_lab(tuple(int(h[j:j + 2], 16) for j in (0, 2, 4)))

def main():
    args = sys.argv[1:]
    refs = []
    if "--ref" in args:
        i = args.index("--ref")
        refs = [hex_lab(h.strip("#")) for h in args[i + 1].split(",")]
        del args[i:i + 2]
    shots = {}
    for path in args:
        px = pixels(path)
        lut = {c: to_lab(c) for c in set(px)}  # cache: real frames repeat colours
        n = len(px)
        mean = tuple(sum(lut[c][i] for c in px) / n for i in range(3))
        shots[path] = (mean, palette(px))
        print(path, "meanLab", tuple(round(v, 2) for v in mean),
              "palette L*", [round(c[0]) for c in shots[path][1]])
        if refs:
            print("  card->palette dE76", round(pal_dist(refs, shots[path][1]), 2))
    names = list(shots)
    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            a, b = shots[names[i]], shots[names[j]]
            print(f"{names[i]} vs {names[j]}: mean dE76 {math.dist(a[0], b[0]):.2f}, palette dE76 {pal_dist(a[1], b[1]):.2f}")

if __name__ == "__main__":
    assert abs(to_lab((255, 255, 255))[0] - 100) < 0.01 and abs(to_lab((0, 0, 0))[0]) < 0.01
    main()
