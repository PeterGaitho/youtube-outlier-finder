"""Promo card (1200x675) with real results. Run: python tools/make_card.py"""
import pathlib

from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 675
BG, INK, DIM, RED, GRID = (18, 20, 26), (236, 238, 244), (140, 146, 160), (255, 59, 48), (44, 48, 58)
F = "C:/Windows/Fonts/"


def font(name, size):
    try:
        return ImageFont.truetype(F + name, size)
    except OSError:
        return ImageFont.load_default()


bold, reg = "segoeuib.ttf", "segoeui.ttf"
img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

d.text((64, 52), "Which videos beat their own channel?", font=font(bold, 52), fill=INK)
d.text((64, 124), "Score = views / median views of the ~10 uploads around it", font=font(reg, 28), fill=DIM)

rows = [  # real output, search "why rent is so high" and channel scans, 2026-10-23
    ("8.0x", "3.6M vs 452K", "Economics Explained", "Why Everyone is Leaving New Zealand"),
    ("7.5x", "199K vs 26.5K", "Foundation for Economic Education", "The Real Reason Your Rent Is So High"),
    ("4.5x", "855K vs 192K", "60 Minutes", "Why rents are dramatically increasing across the US"),
    ("3.8x", "3.2M vs 834K", "PolyMatter", "What Putin Fears More Than War"),
]
y = 200
for score, views, ch, title in rows:
    d.line([(64, y - 14), (W - 64, y - 14)], fill=GRID, width=2)
    d.text((64, y), score, font=font(bold, 56), fill=RED)
    d.text((250, y + 2), title, font=font(bold, 30), fill=INK)
    d.text((250, y + 44), f"{ch}  ·  {views} normal views", font=font(reg, 24), fill=DIM)
    y += 108

d.text((64, H - 62), "YouTube Outlier Finder  ·  channels or topic search  ·  no API key", font=font(reg, 26), fill=DIM)
out = pathlib.Path(__file__).resolve().parents[1] / "assets" / "card.png"
out.parent.mkdir(exist_ok=True)
img.save(out)
print(out)
