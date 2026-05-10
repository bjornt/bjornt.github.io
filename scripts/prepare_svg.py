#!/usr/bin/env python3
"""Prepare an Excalidraw-exported SVG for inline inclusion.

Detects the dominant background fill and foreground stroke colors used
in the SVG, then injects a `<style>` block that re-maps those colors via
CSS variables so the diagram swaps palettes based on
`prefers-color-scheme`. Also makes the SVG responsive (`width="100%"`)
and strips the `<?xml ?>` declaration and `<!DOCTYPE>` so the file can
be inlined into an HTML page without the browser rendering them as
visible text.

The file is rewritten in place.
"""

from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path

# Site palette — used to fill in whichever variant (light/dark) the
# source SVG does not already supply.
LIGHT_BG = "#f7fafb"
LIGHT_FG = "#3a4145"
DARK_BG = "#1e2a3a"
DARK_FG = "#f7fafb"

STYLE_TEMPLATE = """<style>
  :root {{ --svg-bg: {light_bg}; --svg-fg: {light_fg}; }}
  @media (prefers-color-scheme: dark) {{
    :root {{ --svg-bg: {dark_bg}; --svg-fg: {dark_fg}; }}
  }}
  path[fill="{orig_bg}"] {{ fill: var(--svg-bg); }}
  path[stroke="{orig_fg}"] {{ stroke: var(--svg-fg); }}
  text[fill="{orig_fg}"] {{ fill: var(--svg-fg); }}
</style>"""


def hex_brightness(hex_color: str) -> int:
    h = hex_color.lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    return int(h[0:2], 16) + int(h[2:4], 16) + int(h[4:6], 16)


def detect_colors(svg: str) -> tuple[str, str]:
    """Return ``(background_color, foreground_color)`` as hex strings."""
    path_fills = Counter(
        m for m in re.findall(r'<path\b[^>]*?\sfill="(#[0-9a-fA-F]+)"', svg)
    )
    strokes = Counter(
        re.findall(r'<path\b[^>]*?\sstroke="(#[0-9a-fA-F]+)"', svg)
    )

    if not path_fills:
        raise ValueError("Could not detect a background fill color")
    if not strokes:
        raise ValueError("Could not detect a foreground stroke color")

    return path_fills.most_common(1)[0][0], strokes.most_common(1)[0][0]


def transform(svg: str) -> str:
    # Strip the XML declaration and DOCTYPE: they're invalid inside HTML
    # and browsers render them as visible text when the SVG is inlined.
    svg = re.sub(r"<\?xml\b[^?]*\?>\s*", "", svg, count=1)
    svg = re.sub(r"<!DOCTYPE[^>]*>\s*", "", svg, count=1)

    bg, fg = detect_colors(svg)

    if hex_brightness(bg) > hex_brightness(fg):
        light_bg, light_fg = bg, fg
        dark_bg, dark_fg = DARK_BG, DARK_FG
    else:
        dark_bg, dark_fg = bg, fg
        light_bg, light_fg = LIGHT_BG, LIGHT_FG

    style = STYLE_TEMPLATE.format(
        light_bg=light_bg,
        light_fg=light_fg,
        dark_bg=dark_bg,
        dark_fg=dark_fg,
        orig_bg=bg,
        orig_fg=fg,
    )

    if "</defs>" not in svg:
        raise ValueError("SVG has no <defs> block to insert styles into")
    svg = svg.replace("</defs>", style + "</defs>", 1)

    # Make the SVG fluid: drop fixed width/height, ensure width="100%".
    svg = re.sub(r'(<svg\b[^>]*?)\s+width="[^"]*"', r"\1", svg, count=1)
    svg = re.sub(r'(<svg\b[^>]*?)\s+height="[^"]*"', r"\1", svg, count=1)
    svg = re.sub(r"(<svg\b)", r'\1 width="100%"', svg, count=1)

    return svg


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("Usage: prepare_svg.py <path-to-svg>", file=sys.stderr)
        return 1
    path = Path(argv[1])
    path.write_text(transform(path.read_text()))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
