#!/usr/bin/env python3
"""
Generates an animated GIF of pixel-art Mario running across
the GitHub contribution calendar. Outputs dist/mario.gif and
dist/mario-dark.gif.
"""
import os
import json
import math
import urllib.request
import urllib.parse
from datetime import datetime, timedelta
from PIL import Image, ImageDraw

# ── config ────────────────────────────────────────────────────────────────────
USERNAME = os.environ.get("GITHUB_REPOSITORY_OWNER", "harshverma27")
TOKEN = os.environ.get("GITHUB_TOKEN", "")
CELL = 11          # px per contribution square (GitHub uses ~10px)
GAP = 2            # gap between cells
MARGIN_X = 4
MARGIN_Y = 28      # top margin for month labels
MARIO_SCALE = 2    # sprite scale multiplier
FPS = 10
WALK_FRAMES = 8    # frames per cell

THEMES = {
    "light": {
        "bg": (255, 255, 255),
        "empty": (235, 237, 240),
        "levels": [
            (235, 237, 240),
            (155, 233, 168),
            (64, 196, 99),
            (48, 161, 78),
            (33, 110, 57),
        ],
        "text": (36, 41, 47),
    },
    "dark": {
        "bg": (13, 17, 23),
        "empty": (22, 27, 34),
        "levels": [
            (22, 27, 34),
            (14, 68, 41),
            (0, 109, 50),
            (38, 166, 65),
            (57, 211, 83),
        ],
        "text": (139, 148, 158),
    },
}

# ── pixel art sprites (Mario, 16×16, RGBA rows) ────────────────────────────
# Each row is a list of (R,G,B,A). 0 = transparent.
_T = (0, 0, 0, 0)
_R = (200, 50, 50, 255)    # red cap/shirt
_S = (230, 180, 100, 255)  # skin
_B = (40, 40, 180, 255)    # blue overalls
_W = (255, 255, 255, 255)  # white eyes
_Y = (220, 160, 40, 255)   # buttons/buckles
_K = (20, 10, 0, 255)      # dark outline/hair

MARIO_STAND = [
    [_T,_T,_T,_R,_R,_R,_R,_R,_T,_T,_T,_T,_T,_T,_T,_T],
    [_T,_T,_R,_R,_R,_R,_R,_R,_R,_R,_R,_T,_T,_T,_T,_T],
    [_T,_T,_K,_K,_K,_S,_S,_K,_S,_T,_T,_T,_T,_T,_T,_T],
    [_T,_K,_S,_K,_S,_S,_S,_K,_S,_S,_S,_T,_T,_T,_T,_T],
    [_T,_K,_S,_K,_K,_S,_S,_S,_K,_S,_S,_S,_T,_T,_T,_T],
    [_T,_K,_K,_S,_S,_S,_S,_K,_K,_K,_K,_T,_T,_T,_T,_T],
    [_T,_T,_T,_S,_S,_S,_S,_S,_S,_S,_T,_T,_T,_T,_T,_T],
    [_T,_T,_B,_B,_R,_B,_B,_T,_T,_T,_T,_T,_T,_T,_T,_T],
    [_T,_B,_B,_B,_R,_B,_B,_B,_T,_T,_T,_T,_T,_T,_T,_T],
    [_B,_B,_B,_B,_R,_R,_B,_B,_B,_T,_T,_T,_T,_T,_T,_T],
    [_S,_S,_B,_R,_Y,_R,_B,_S,_S,_T,_T,_T,_T,_T,_T,_T],
    [_S,_S,_S,_R,_R,_R,_S,_S,_S,_T,_T,_T,_T,_T,_T,_T],
    [_T,_T,_S,_S,_T,_S,_S,_T,_T,_T,_T,_T,_T,_T,_T,_T],
    [_T,_S,_S,_S,_T,_S,_S,_S,_T,_T,_T,_T,_T,_T,_T,_T],
    [_S,_S,_S,_T,_T,_T,_S,_S,_S,_T,_T,_T,_T,_T,_T,_T],
    [_T,_T,_T,_T,_T,_T,_T,_T,_T,_T,_T,_T,_T,_T,_T,_T],
]

MARIO_WALK1 = [
    [_T,_T,_T,_R,_R,_R,_R,_R,_T,_T,_T,_T,_T,_T,_T,_T],
    [_T,_T,_R,_R,_R,_R,_R,_R,_R,_R,_R,_T,_T,_T,_T,_T],
    [_T,_T,_K,_K,_K,_S,_S,_K,_S,_T,_T,_T,_T,_T,_T,_T],
    [_T,_K,_S,_K,_S,_S,_S,_K,_S,_S,_S,_T,_T,_T,_T,_T],
    [_T,_K,_S,_K,_K,_S,_S,_S,_K,_S,_S,_S,_T,_T,_T,_T],
    [_T,_K,_K,_S,_S,_S,_S,_K,_K,_K,_K,_T,_T,_T,_T,_T],
    [_T,_T,_T,_S,_S,_S,_S,_S,_S,_S,_T,_T,_T,_T,_T,_T],
    [_T,_T,_B,_B,_R,_B,_B,_T,_T,_T,_T,_T,_T,_T,_T,_T],
    [_T,_B,_B,_B,_R,_B,_B,_B,_T,_T,_T,_T,_T,_T,_T,_T],
    [_B,_B,_B,_B,_R,_R,_B,_B,_B,_T,_T,_T,_T,_T,_T,_T],
    [_S,_S,_B,_R,_Y,_R,_B,_S,_S,_T,_T,_T,_T,_T,_T,_T],
    [_S,_S,_R,_R,_R,_R,_R,_S,_S,_T,_T,_T,_T,_T,_T,_T],
    [_T,_R,_R,_S,_T,_S,_R,_R,_T,_T,_T,_T,_T,_T,_T,_T],
    [_R,_R,_S,_S,_T,_T,_S,_R,_R,_T,_T,_T,_T,_T,_T,_T],
    [_S,_S,_T,_T,_T,_T,_T,_T,_S,_T,_T,_T,_T,_T,_T,_T],
    [_T,_T,_T,_T,_T,_T,_T,_T,_T,_T,_T,_T,_T,_T,_T,_T],
]

MARIO_WALK2 = [
    [_T,_T,_T,_R,_R,_R,_R,_R,_T,_T,_T,_T,_T,_T,_T,_T],
    [_T,_T,_R,_R,_R,_R,_R,_R,_R,_R,_R,_T,_T,_T,_T,_T],
    [_T,_T,_K,_K,_K,_S,_S,_K,_S,_T,_T,_T,_T,_T,_T,_T],
    [_T,_K,_S,_K,_S,_S,_S,_K,_S,_S,_S,_T,_T,_T,_T,_T],
    [_T,_K,_S,_K,_K,_S,_S,_S,_K,_S,_S,_S,_T,_T,_T,_T],
    [_T,_K,_K,_S,_S,_S,_S,_K,_K,_K,_K,_T,_T,_T,_T,_T],
    [_T,_T,_T,_S,_S,_S,_S,_S,_S,_S,_T,_T,_T,_T,_T,_T],
    [_T,_T,_B,_B,_R,_B,_B,_T,_T,_T,_T,_T,_T,_T,_T,_T],
    [_B,_B,_B,_B,_R,_B,_B,_B,_T,_T,_T,_T,_T,_T,_T,_T],
    [_B,_B,_B,_B,_R,_R,_B,_B,_T,_T,_T,_T,_T,_T,_T,_T],
    [_S,_S,_B,_R,_Y,_R,_B,_S,_T,_T,_T,_T,_T,_T,_T,_T],
    [_T,_S,_R,_R,_R,_R,_R,_T,_T,_T,_T,_T,_T,_T,_T,_T],
    [_T,_R,_R,_S,_T,_S,_R,_T,_T,_T,_T,_T,_T,_T,_T,_T],
    [_T,_S,_S,_T,_T,_T,_S,_S,_T,_T,_T,_T,_T,_T,_T,_T],
    [_T,_T,_T,_T,_T,_T,_S,_S,_S,_T,_T,_T,_T,_T,_T,_T],
    [_T,_T,_T,_T,_T,_T,_T,_T,_T,_T,_T,_T,_T,_T,_T,_T],
]

WALK_CYCLE = [MARIO_STAND, MARIO_WALK1, MARIO_STAND, MARIO_WALK2]


def sprite_image(sprite_data, scale=1):
    """Convert sprite pixel array to PIL Image (RGBA)."""
    h, w = len(sprite_data), len(sprite_data[0])
    img = Image.new("RGBA", (w * scale, h * scale), (0, 0, 0, 0))
    for y, row in enumerate(sprite_data):
        for x, px in enumerate(row):
            if px[3] > 0:
                for dy in range(scale):
                    for dx in range(scale):
                        img.putpixel((x * scale + dx, y * scale + dy), px)
    return img


def fetch_contributions():
    """Fetch 52 weeks of contribution data via GitHub GraphQL."""
    query = """
    {
      user(login: "%s") {
        contributionsCollection {
          contributionCalendar {
            weeks {
              contributionDays {
                contributionCount
                date
              }
            }
          }
        }
      }
    }
    """ % USERNAME

    headers = {
        "Authorization": f"bearer {TOKEN}",
        "Content-Type": "application/json",
    }
    data = json.dumps({"query": query}).encode()
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=data,
        headers=headers,
    )
    with urllib.request.urlopen(req) as resp:
        result = json.loads(resp.read())

    weeks = result["data"]["user"]["contributionsCollection"]["contributionCalendar"]["weeks"]
    return [[day["contributionCount"] for day in week["contributionDays"]] for week in weeks]


def count_to_level(count):
    if count == 0: return 0
    if count < 3:  return 1
    if count < 6:  return 2
    if count < 9:  return 3
    return 4


def build_frame(weeks, mario_x, mario_frame_idx, theme):
    """Render one animation frame."""
    t = THEMES[theme]
    cols = len(weeks)
    rows = 7
    step = CELL + GAP
    w = MARGIN_X * 2 + cols * step
    sprite_h = 16 * MARIO_SCALE
    h = MARGIN_Y + rows * step + sprite_h + 4

    img = Image.new("RGBA", (w, h), t["bg"] + (255,))
    draw = ImageDraw.Draw(img)

    # draw grid
    for cx, week in enumerate(weeks):
        for ry, count in enumerate(week):
            level = count_to_level(count)
            color = t["levels"][level]
            x0 = MARGIN_X + cx * step
            y0 = MARGIN_Y + ry * step
            draw.rectangle([x0, y0, x0 + CELL - 1, y0 + CELL - 1], fill=color)

    # draw mario sprite
    sprite = sprite_image(WALK_CYCLE[mario_frame_idx % len(WALK_CYCLE)], MARIO_SCALE)
    ground_y = MARGIN_Y + rows * step + 2
    paste_x = MARGIN_X + int(mario_x) * step - (sprite_h // 4)
    paste_y = ground_y - sprite_h + CELL
    img.paste(sprite, (max(0, paste_x), paste_y), sprite)

    return img.convert("P", palette=Image.ADAPTIVE, colors=128)


def generate(theme, out_path):
    print(f"Fetching contributions for {USERNAME}...")
    try:
        weeks = fetch_contributions()
    except Exception as e:
        print(f"GraphQL fetch failed: {e}. Using dummy data.")
        weeks = [[0] * 7 for _ in range(52)]

    cols = len(weeks)
    frames = []
    durations = []

    for col in range(cols):
        for sub in range(WALK_FRAMES):
            mario_x = col + sub / WALK_FRAMES
            frame_idx = (col * WALK_FRAMES + sub) // (WALK_FRAMES // len(WALK_CYCLE))
            frame = build_frame(weeks, mario_x, frame_idx, theme)
            frames.append(frame)
            durations.append(1000 // FPS)

    os.makedirs("dist", exist_ok=True)
    frames[0].save(
        out_path,
        save_all=True,
        append_images=frames[1:],
        duration=durations,
        loop=0,
        optimize=True,
    )
    print(f"Saved {out_path}")


if __name__ == "__main__":
    generate("light", "dist/mario.gif")
    generate("dark",  "dist/mario-dark.gif")
