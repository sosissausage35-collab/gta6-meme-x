#!/usr/bin/env python3
"""Draw the GTA 6 launch-day meme for make.fun bounty gta6-meme-x-01.

Original art drawn in this session with PIL: a Vice City sunset, the
make.fun ghost (press-kit mark) as the 5-star wanted outlaw, and the joke
caption. No Rockstar art, logos or screenshots are used.
"""
import math
from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 675
MAGENTA = (226, 0, 122)
DARK = (24, 8, 32)


def font(size, bold=True):
    for path in (
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold
        else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf" if bold
        else "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
    ):
        try:
            return ImageFont.truetype(path, size)
        except OSError:
            continue
    return ImageFont.load_default()


def lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


def text_center(draw, cx, y, s, fnt, fill, outline=None, width=4):
    bbox = draw.textbbox((0, 0), s, font=fnt)
    tw = bbox[2] - bbox[0]
    x = cx - tw // 2
    if outline:
        draw.text((x, y), s, font=fnt, fill=outline,
                  stroke_width=width, stroke_fill=outline)
        # stroke already outlines; draw fill on top
    draw.text((x, y), s, font=fnt, fill=fill)
    return tw


img = Image.new("RGB", (W, H))
d = ImageDraw.Draw(img)

# --- Sunset sky gradient: deep purple -> magenta -> orange ---
top = (46, 10, 68)
mid = (176, 20, 110)
bot = (255, 122, 26)
for y in range(520):
    t = y / 520
    if t < 0.55:
        c = lerp(top, mid, t / 0.55)
    else:
        c = lerp(mid, bot, (t - 0.55) / 0.45)
    d.line([(0, y), (W, y)], fill=c)

# --- Sun (off to the right, clear of the ghost) ---
d.ellipse([880 - 110, 220, 880 + 110, 440], fill=(255, 214, 130))
d.ellipse([880 - 90, 240, 880 + 90, 420], fill=(255, 236, 170))

# --- Skyline silhouette ---
d.rectangle([0, 470, W, 520], fill=(38, 12, 52))
buildings = [
    (0, 430, 90, 520), (95, 390, 170, 520), (175, 440, 250, 520),
    (255, 370, 330, 520), (335, 425, 400, 520), (405, 395, 470, 520),
    (760, 400, 830, 520), (835, 430, 905, 520), (910, 380, 990, 520),
    (995, 435, 1060, 520), (1065, 395, 1140, 520), (1145, 440, 1200, 520),
]
for x0, y0, x1, y1 in buildings:
    d.rectangle([x0, y0, x1, y1], fill=(38, 12, 52))
# lit windows
for x0, y0, x1, y1 in buildings:
    for wy in range(y0 + 14, y1 - 8, 26):
        for wx in range(x0 + 10, x1 - 10, 24):
            if (wx * 7 + wy * 13) % 5 == 0:
                d.rectangle([wx, wy, wx + 7, wy + 10], fill=(255, 190, 90))

# --- Palm trees (left and right edges) ---
def palm(cx, base, s):
    top_y = base - 150 * s
    d.line([cx, base, cx, top_y], fill=(24, 8, 32), width=int(10 * s))
    for ang in (-70, -40, -12, 15, 42, 70):
        rad = math.radians(ang - 90)
        # drooping frond: quadratic curve from the crown
        ex = cx + math.cos(rad) * 95 * s
        ey = top_y + math.sin(rad) * 55 * s + 45 * s
        mx = cx + math.cos(rad) * 55 * s
        my = top_y + math.sin(rad) * 30 * s - 8 * s
        pts = []
        for t in [i / 12 for i in range(13)]:
            px = (1 - t) ** 2 * cx + 2 * (1 - t) * t * mx + t * t * ex
            py = (1 - t) ** 2 * top_y + 2 * (1 - t) * t * my + t * t * ey
            pts.append((px, py))
        d.line(pts, fill=(24, 8, 32), width=int(6 * s))


palm(70, 530, 1.0)
palm(1140, 530, 0.9)

# --- Road ---
d.rectangle([0, 520, W, H], fill=(18, 8, 26))
d.rectangle([0, 520, W, 528], fill=(255, 190, 90))
for x in range(20, W, 90):
    d.rectangle([x, 592, x + 48, 602], fill=(255, 214, 130))

# --- Ghost badge (make.fun mark), centre, tilted slightly ---
ghost = Image.open("ghost-mark.png").convert("RGBA")
gs = 340
ghost = ghost.resize((gs, gs), Image.LANCZOS)
ghost = ghost.rotate(-6, resample=Image.BICUBIC, expand=False)
img.paste(ghost, (W // 2 - gs // 2, 150), ghost)
# white ring around the badge so it pops off the sky
d.ellipse([W // 2 - gs // 2 - 8, 150 - 8, W // 2 + gs // 2 + 8, 150 + gs + 8],
          outline=(255, 255, 255), width=6)

# --- WANTED headline ---
f_wanted = font(118)
text_center(d, W // 2, 18, "WANTED", f_wanted, (255, 255, 255), (24, 8, 32), 8)

# --- 5 gold stars under the ghost ---
def star(cx, cy, r, fill):
    pts = []
    for i in range(10):
        ang = math.radians(-90 + i * 36)
        rr = r if i % 2 == 0 else r * 0.45
        pts.append((cx + math.cos(ang) * rr, cy + math.sin(ang) * rr))
    d.polygon(pts, fill=fill, outline=(24, 8, 32))


for i in range(5):
    star(430 + i * 85, 522, 30, (255, 200, 40))

# --- Caption bar ---
d.rectangle([0, 545, W, 642], fill=(24, 8, 32))
d.rectangle([0, 545, W, 550], fill=MAGENTA)
f_cap = font(40)
text_center(d, W // 2, 552, "CRIME: CALLED IN SICK", f_cap, (255, 255, 255))
text_center(d, W // 2, 596, "FOR GTA 6 LAUNCH DAY", f_cap, (255, 255, 255))

# --- Footer: place, date, make.fun name ---
f_small = font(26)
d.text((24, 648), "VICE CITY  •  19 NOV 2026", font=f_small, fill=(255, 255, 255))
d.text((W - 24 - d.textlength("make.fun", font=f_small), 648),
       "make.fun", font=f_small, fill=(255, 255, 255))

img.save("meme.png")
print("saved meme.png", img.size)
