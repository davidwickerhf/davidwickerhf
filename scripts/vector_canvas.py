"""Self-contained SVG drawing, with font outlines rather than rasterized text."""
from pathlib import Path
from functools import lru_cache
from html import escape
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.boundsPen import BoundsPen

FONTS = Path(__file__).resolve().parents[1] / 'assets/fonts'

@lru_cache(maxsize=None)
def font_data(serif):
    font = TTFont(FONTS / ('InstrumentSerif-Regular.ttf' if serif else 'Manrope.ttf'))
    return font, font.getGlyphSet(location=None if serif else {'wght': 500})

@lru_cache(maxsize=None)
def glyph_data(serif, char):
    font, glyphs = font_data(serif)
    name = font.getBestCmap().get(ord(char), '.notdef')
    pen = SVGPathPen(glyphs); glyphs[name].draw(pen)
    bounds = BoundsPen(glyphs); glyphs[name].draw(bounds)
    return pen.getCommands(), glyphs[name].width, bounds.bounds

class Canvas:
    def __init__(self, height, theme, width=1200):
        self.c = THEMES[theme]; self.height = height; self.width = width
        self.parts = []; self.defs = {}
        self.rect((.75,.75,width-.75,height-.75), 'bg', True)
        self.rect((.75,.75,width-.75,height-.75), 'line')

    def color(self, value):
        if isinstance(value, tuple): return '#'+''.join(f'{v:02x}' for v in value)
        return self.c.get(value, value)

    def text(self, xy, text, size=16, color='ink', serif=False):
        font, _ = font_data(serif); scale = size/font['head'].unitsPerEm
        top = max((glyph_data(serif,ch)[2][3] for ch in text if glyph_data(serif,ch)[2]), default=0)
        x, y = xy; uses = []; offset=0
        for char in text:
            path, advance, _ = glyph_data(serif,char)
            key = f'g{int(serif)}-{ord(char)}'
            if path:
                self.defs[key] = f'<path id="{key}" d="{path}"/>'
                uses.append(f'<use href="#{key}" x="{offset:.2f}"/>')
            offset+=advance
        self.parts.append(f'<g aria-label="{escape(text,quote=True)}" fill="{self.color(color)}" transform="translate({x} {y+top*scale:.3f}) scale({scale:.6f} {-scale:.6f})">'+''.join(uses)+'</g>')

    def line(self, points, color='line', width=1):
        pts=' '.join(f'{x:.3f},{y:.3f}' for x,y in points)
        self.parts.append(f'<polyline points="{pts}" fill="none" stroke="{self.color(color)}" stroke-width="{width}"/>')

    def circle(self, xy, radius, color='accent', fill=True, width=1):
        x,y=xy
        style=f'fill="{self.color(color)}"' if fill else f'fill="none" stroke="{self.color(color)}" stroke-width="{width}"'
        self.parts.append(f'<circle cx="{x:.3f}" cy="{y:.3f}" r="{radius}" {style}/>')

    def rect(self, box, color='line', fill=False):
        x,y,x2,y2=box
        style=f'fill="{self.color(color)}"' if fill else f'fill="none" stroke="{self.color(color)}" stroke-width="1.5"'
        self.parts.append(f'<rect x="{x}" y="{y}" width="{x2-x}" height="{y2-y}" {style}/>')

    def image(self):
        return f'<svg xmlns="http://www.w3.org/2000/svg" width="{self.width}" height="{self.height}" viewBox="0 0 {self.width} {self.height}" role="img"><defs>'+''.join(self.defs.values())+'</defs>'+''.join(self.parts)+'</svg>\n'

THEMES = {
 'light': {'bg':'#ffffff','ink':'#171b19','muted':'#4e5551','line':'#d1d9e0','accent':'#294f48','signal':'#9f4c38'},
 'dark': {'bg':'#0d1117','ink':'#f0f6fc','muted':'#b0bbb6','line':'#3d444d','accent':'#b9d0c8','signal':'#e39374'},
}
