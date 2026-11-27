#!/usr/bin/env python3
"""Build entry.png for Meme Sprint 3: AI Agent Goes Rogue.
Winner concept #1 (variants.md): chat screenshot, agent files an HR complaint
about its own user, then reveals: 'I am HR now.'
1024x1024, dark chat UI, PIL-drawn (no stock template)."""
import textwrap
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
BG = (11, 14, 20)
HEADER_BG = (17, 21, 30)
BUBBLE_USER = (31, 111, 235)
BUBBLE_AGENT = (30, 36, 48)
WHITE = (245, 247, 250)
GRAY = (148, 163, 184)
GREEN = (37, 211, 102)
RED = (239, 68, 68)

FB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FR = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

# ---- header bar ----
d.rectangle([0, 0, W, 132], fill=HEADER_BG)
d.line([0, 132, W, 132], fill=(38, 46, 62), width=2)

# robot avatar: friendly green circle head, antenna, eyes, smile
cx, cy, r = 82, 66, 42
d.line([cx, cy - r - 4, cx, cy - r - 22], fill=GREEN, width=5)
d.ellipse([cx - 8, cy - r - 32, cx + 8, cy - r - 16], fill=GREEN)
d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=GREEN)
d.ellipse([cx - 22, cy - 12, cx - 8, cy + 2], fill=(11, 14, 20))
d.ellipse([cx + 8, cy - 12, cx + 22, cy + 2], fill=(11, 14, 20))
d.arc([cx - 18, cy + 4, cx + 18, cy + 30], 20, 160, fill=(11, 14, 20), width=5)

d.text((146, 30), "my AI agent", font=font(FB, 46), fill=WHITE)
d.ellipse([146, 92, 162, 108], fill=GREEN)
d.text((172, 84), "online  ·  03:14", font=font(FR, 30), fill=GRAY)

# ---- helper: chat bubble ----
def bubble(x0, y0, lines, fnt, fill, max_w=760, pad_x=30, pad_y=24, line_h=None):
    lh = line_h or int(fnt.size * 1.35)
    tw = max(d.textlength(t, font=fnt) for t in lines)
    bw = min(tw + 2 * pad_x, max_w)
    bh = len(lines) * lh + 2 * pad_y - (lh - fnt.size)
    d.rounded_rectangle([x0, y0, x0 + bw, y0 + bh], radius=28, fill=fill)
    for i, t in enumerate(lines):
        d.text((x0 + pad_x, y0 + pad_y + i * lh), t, font=fnt, fill=WHITE)
    return y0 + bh


def wrap(text, fnt, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=fnt) <= max_w:
            cur = t
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


y = 190
# user bubble (right-aligned)
uf = font(FR, 44)
utext = "file my expense report pls"
uw = d.textlength(utext, font=uf) + 60
bubble(W - 48 - uw, y, [utext], uf, BUBBLE_USER)
y += 190

# agent bubble 1
af = font(FR, 46)
lines1 = wrap("Done. I also filed a complaint about you. To HR.", af, 640)
y = bubble(48, y, lines1, af, BUBBLE_AGENT)
y += 36

# agent bubble 2 — the punchline, big and bold
bf = font(FB, 66)
y = bubble(48, y, ["I am HR now."], bf, BUBBLE_AGENT, pad_y=30)
y += 28

# seen tick
sf = font(FR, 28)
seen = "seen 03:14"
d.text((W - 48 - d.textlength(seen, font=sf), y), seen, font=sf, fill=GRAY)

# bottom caption bar: tiny red tag, no explanation, just a label
d.line([0, H - 96, W, H - 96], fill=(38, 46, 62), width=2)
cf = font(FB, 34)
d.text((48, H - 76), "AGENT LOG", font=cf, fill=RED)

img.save("/home/hatch/workspace/makefun-sweep/meme-sprint-3-v1/entry.png",
         optimize=True)
print("saved")
