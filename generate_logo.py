"""Generate the NASA OPERA site logo and favicon.

Draws a rounded-square tile with a stylized globe, a satellite swath arc,
and a wave motif — representing OPERA's satellite-based surface water,
disturbance, and displacement products. Renders at 4x supersampling and
downsamples with LANCZOS for crisp edges.

Outputs:
    logo.png  — 512x512 RGBA
    fav.ico   — multi-resolution (16, 32, 48, 64, 128, 256)
"""

from __future__ import annotations

import math
from pathlib import Path

from PIL import Image, ImageDraw

ROOT = Path(__file__).parent
SIZE = 512
SS = 4  # supersample factor

# Palette (NASA-inspired)
BG_TOP = (30, 90, 200, 255)      # deep sky blue
BG_BOT = (70, 140, 240, 255)     # lighter blue
GLOBE = (235, 245, 255, 255)     # near-white with cool tint
GRID = (40, 100, 200, 180)       # visible blue lat/long grid
SWATH = (255, 210, 90, 235)      # warm yellow orbit
SWATH_BACK = (255, 210, 90, 150)  # dimmer shade for arc behind globe
WAVE = (160, 220, 255, 235)      # light water blue


def vertical_gradient(size: int, top: tuple[int, ...], bot: tuple[int, ...]) -> Image.Image:
    """Create a vertical gradient image.

    Args:
        size: Output size in pixels (square).
        top: RGBA color at y=0.
        bot: RGBA color at y=size-1.

    Returns:
        RGBA Image with a top-to-bottom gradient.
    """
    img = Image.new("RGBA", (size, size), top)
    px = img.load()
    for y in range(size):
        t = y / (size - 1)
        c = tuple(int(top[i] * (1 - t) + bot[i] * t) for i in range(4))
        for x in range(size):
            px[x, y] = c
    return img


def rounded_mask(size: int, radius: int) -> Image.Image:
    """Create an L-mode rounded-square mask.

    Args:
        size: Square mask size in pixels.
        radius: Corner radius in pixels.

    Returns:
        L-mode mask (255 inside, 0 outside).
    """
    m = Image.new("L", (size, size), 0)
    d = ImageDraw.Draw(m)
    d.rounded_rectangle((0, 0, size - 1, size - 1), radius=radius, fill=255)
    return m


def draw_globe(draw: ImageDraw.ImageDraw, cx: float, cy: float, r: float) -> None:
    """Draw a stylized globe with meridian/parallel grid lines.

    Args:
        draw: ImageDraw target.
        cx: Globe center x.
        cy: Globe center y.
        r: Globe radius.
    """
    draw.ellipse((cx - r, cy - r, cx + r, cy + r), fill=GLOBE)
    # Parallels (horizontal ellipses)
    for frac in (-0.55, -0.25, 0.0, 0.25, 0.55):
        dy = frac * r
        ry = r * math.sqrt(max(0.0, 1 - frac * frac)) * 0.35
        rx = r * math.sqrt(max(0.0, 1 - frac * frac))
        draw.ellipse(
            (cx - rx, cy + dy - ry, cx + rx, cy + dy + ry),
            outline=GRID,
            width=max(2, int(r * 0.02)),
        )
    # Meridians (vertical ellipses, varying width)
    for frac in (-0.75, -0.4, 0.0, 0.4, 0.75):
        rx = r * abs(frac) if abs(frac) > 0.01 else r * 0.04
        ry = r
        draw.ellipse(
            (cx - rx, cy - ry, cx + rx, cy + ry),
            outline=GRID,
            width=max(2, int(r * 0.02)),
        )
    # Outer rim
    draw.ellipse(
        (cx - r, cy - r, cx + r, cy + r),
        outline=(20, 60, 150, 230),
        width=max(3, int(r * 0.03)),
    )


def orbit_points(
    cx: float,
    cy: float,
    a: float,
    b: float,
    theta: float,
    t_start: float,
    t_end: float,
    n: int = 240,
) -> list[tuple[float, float]]:
    """Sample points along a rotated ellipse.

    The ellipse is centered at (cx, cy) with semi-axes (a, b) and rotated by
    theta radians (CCW). Sampling runs over parameter t in [t_start, t_end].

    Args:
        cx: Ellipse center x.
        cy: Ellipse center y.
        a: Semi-major axis length.
        b: Semi-minor axis length.
        theta: Rotation angle in radians.
        t_start: Start parameter.
        t_end: End parameter.
        n: Number of segments to sample.

    Returns:
        List of (x, y) points along the arc.
    """
    pts: list[tuple[float, float]] = []
    cos_t, sin_t = math.cos(theta), math.sin(theta)
    for i in range(n + 1):
        t = t_start + (t_end - t_start) * i / n
        lx = a * math.cos(t)
        ly = b * math.sin(t)
        x = cx + lx * cos_t - ly * sin_t
        y = cy + lx * sin_t + ly * cos_t
        pts.append((x, y))
    return pts


def draw_orbit_back(
    draw: ImageDraw.ImageDraw,
    cx: float,
    cy: float,
    a: float,
    b: float,
    theta: float,
    width: int,
) -> None:
    """Draw the half of the orbit that sits behind the globe (dimmer).

    Args:
        draw: ImageDraw target.
        cx: Orbit center x.
        cy: Orbit center y.
        a: Semi-major axis.
        b: Semi-minor axis.
        theta: Rotation in radians.
        width: Line width in pixels.
    """
    pts = orbit_points(cx, cy, a, b, theta, math.pi, 2 * math.pi)
    draw.line(pts, fill=SWATH_BACK, width=width, joint="curve")


def draw_orbit_front(
    draw: ImageDraw.ImageDraw,
    cx: float,
    cy: float,
    a: float,
    b: float,
    theta: float,
    width: int,
) -> None:
    """Draw the half of the orbit that sits in front of the globe, with satellite.

    Args:
        draw: ImageDraw target.
        cx: Orbit center x.
        cy: Orbit center y.
        a: Semi-major axis.
        b: Semi-minor axis.
        theta: Rotation in radians.
        width: Line width in pixels.
    """
    pts = orbit_points(cx, cy, a, b, theta, 0, math.pi)
    draw.line(pts, fill=SWATH, width=width, joint="curve")
    # Satellite dot part-way along the front arc.
    t = math.pi * 0.30
    lx = a * math.cos(t)
    ly = b * math.sin(t)
    sx = cx + lx * math.cos(theta) - ly * math.sin(theta)
    sy = cy + lx * math.sin(theta) + ly * math.cos(theta)
    sat_r = int(width * 1.9)
    draw.ellipse(
        (sx - sat_r, sy - sat_r, sx + sat_r, sy + sat_r),
        fill=(255, 255, 255, 255),
        outline=SWATH,
        width=max(2, width // 2),
    )


def draw_waves(draw: ImageDraw.ImageDraw, size: int) -> None:
    """Draw layered sinusoidal waves at the bottom of the tile.

    Args:
        draw: ImageDraw target.
        size: Canvas size (square).
    """
    import numpy as np

    xs = np.linspace(0, size, size * 2)
    for i, (amp, freq, y0, alpha, thick) in enumerate(
        [
            (size * 0.018, 2.2, size * 0.82, 180, max(3, size // 90)),
            (size * 0.022, 1.7, size * 0.88, 220, max(4, size // 75)),
            (size * 0.026, 1.3, size * 0.94, 255, max(5, size // 60)),
        ]
    ):
        color = (WAVE[0], WAVE[1], WAVE[2], alpha)
        pts = [
            (float(x), float(y0 + amp * math.sin(2 * math.pi * freq * x / size + i)))
            for x in xs
        ]
        draw.line(pts, fill=color, width=thick, joint="curve")


def build(size: int) -> Image.Image:
    """Build the logo at a target size using supersampling.

    Args:
        size: Final output size (square).

    Returns:
        RGBA Image of the composed logo.
    """
    s = size * SS
    radius = int(s * 0.18)

    bg = vertical_gradient(s, BG_TOP, BG_BOT)
    mask = rounded_mask(s, radius)
    tile = Image.new("RGBA", (s, s), (0, 0, 0, 0))
    tile.paste(bg, (0, 0), mask)

    draw = ImageDraw.Draw(tile)

    cx, cy = s / 2, s * 0.47
    r = s * 0.30
    # Orbit ellipse: slightly larger than the globe, flattened to suggest tilt.
    a = r * 1.20
    b = r * 0.38
    theta = math.radians(28)
    orbit_w = max(5, int(s / 75))

    # z-order: back arc → globe → front arc + satellite.
    draw_orbit_back(draw, cx, cy, a, b, theta, orbit_w)
    draw_globe(draw, cx, cy, r)
    draw_orbit_front(draw, cx, cy, a, b, theta, orbit_w)

    # Re-apply mask after orbit to keep corners rounded.
    corners = Image.new("RGBA", (s, s), (0, 0, 0, 0))
    corners.paste(tile, (0, 0), mask)
    tile = corners
    draw = ImageDraw.Draw(tile)

    draw_waves(draw, s)

    # Re-mask once more so waves don't bleed past rounded corners
    final = Image.new("RGBA", (s, s), (0, 0, 0, 0))
    final.paste(tile, (0, 0), mask)

    return final.resize((size, size), Image.LANCZOS)


def main() -> None:
    """Generate logo.png and fav.ico."""
    logo = build(SIZE)
    logo.save(ROOT / "logo.png", optimize=True)

    # Favicon: include multiple sizes so browsers/tabs pick the best fit.
    ico_sizes = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]
    ico_base = build(256)
    ico_base.save(ROOT / "fav.ico", format="ICO", sizes=ico_sizes)

    print(f"Wrote {ROOT / 'logo.png'} ({logo.size})")
    print(f"Wrote {ROOT / 'fav.ico'} (sizes={ico_sizes})")


if __name__ == "__main__":
    main()
