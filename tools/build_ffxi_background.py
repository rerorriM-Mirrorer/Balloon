"""Regenerate Balloon's FFXI dialogue-field alpha gradient (development asset).

Run from the repository root:
    python tools/build_ffxi_background.py
    python tools/build_ffxi_background.py --top 110 --bottom 245

Requires Pillow for the developer only. The Windower addon uses the PNG directly.
The original upstream field survives at themes/ffxi/balloon-classic.png.
ConsoleBGPlus (Windower-Addons branch consolebg-plus) uses a similar independently
adjustable top/bottom opacity gradient with native XIVParty skin slices.
"""
import argparse
from pathlib import Path
from PIL import Image

WIDTH, HEIGHT = 610, 128
DEFAULT_PATH = Path(__file__).resolve().parent.parent / 'themes' / 'ffxi' / 'balloon.png'


def build(top=100, bottom=240, output=DEFAULT_PATH):
    image = Image.new('RGBA', (WIDTH, HEIGHT))
    pixels = image.load()
    for y in range(HEIGHT):
        t = y / (HEIGHT - 1)
        alpha = int(top + (bottom - top) * (t ** 0.95) + 0.5)
        for x in range(WIDTH):
            red, green, blue = 3, 9, int(36 + 22 * t + 0.5)
            if y > 12 and y % 4 == 0:
                red, green, blue = red + 4, green + 5, blue + 8
            value = alpha
            if y == HEIGHT - 1:
                red, green, blue, value = 108, 111, 142, 165
            elif y == HEIGHT - 2:
                red, green, blue, value = 45, 51, 82, 185
            if x == 0 or x == WIDTH - 1:
                value = min(155, value + 10)
            pixels[x, y] = (red, green, blue, value)
    output = Path(output)
    output.parent.mkdir(parents=True, exist_ok=True)
    image.save(output)
    return output


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--top', type=int, default=100)
    parser.add_argument('--bottom', type=int, default=240)
    parser.add_argument('--output', type=Path, default=DEFAULT_PATH)
    args = parser.parse_args()
    if not 0 <= args.top <= 255 or not 0 <= args.bottom <= 255:
        parser.error('--top and --bottom must be 0 to 255')
    print(build(args.top, args.bottom, args.output))
