"""Render the profile's original artwork. Python 3.10+ and Pillow 12.2.0.

Run from anywhere: python3 scripts/render_artwork.py
All geometry is illustrative; it does not represent live research data.
"""

from pathlib import Path
import math
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
WIDTH = 1200
SCALE = 2
FRAMES = 72
THEMES = {
    "light": {"bg": "#f1eee6", "ink": "#171b19", "muted": "#4e5551", "line": "#d3d4c9", "accent": "#294f48", "signal": "#9f4c38"},
    "dark": {"bg": "#111d1b", "ink": "#f1eee6", "muted": "#a7b8af", "line": "#30433d", "accent": "#b9d0c8", "signal": "#e39374"},
}


def rgb(value):
    return tuple(bytes.fromhex(value.lstrip("#")))


def blend(a, b, t):
    return tuple(round(x + (y - x) * t) for x, y in zip(rgb(a), rgb(b)))


class Canvas:
    def __init__(self, height, theme):
        self.c = THEMES[theme]
        self.im = Image.new("RGB", (WIDTH * SCALE, height * SCALE), self.c["bg"])
        self.d = ImageDraw.Draw(self.im)
        self.height = height

    def text(self, xy, text, size=16, color="ink", serif=False):
        font = "InstrumentSerif-Regular.ttf" if serif else "Manrope.ttf"
        f = ImageFont.truetype(str(ASSETS / "fonts" / font), round(size * SCALE))
        if not serif:
            f.set_variation_by_axes([450])
        self.d.text(tuple(round(v * SCALE) for v in xy), text, font=f,
                    fill=self.c.get(color, color), anchor="lt")

    def line(self, points, color="line", width=1):
        self.d.line([(round(x * SCALE), round(y * SCALE)) for x, y in points],
                    fill=self.c.get(color, color), width=max(1, round(width * SCALE)))

    def circle(self, xy, radius, color="accent", fill=True, width=1):
        x, y = xy
        box = tuple(round(v * SCALE) for v in (x-radius, y-radius, x+radius, y+radius))
        self.d.ellipse(box, fill=self.c.get(color, color) if fill else None,
                       outline=None if fill else self.c.get(color, color), width=round(width*SCALE))

    def rect(self, box, color="line", fill=False):
        box = tuple(round(v * SCALE) for v in box)
        self.d.rectangle(box, fill=self.c.get(color, color) if fill else None,
                         outline=None if fill else self.c.get(color, color), width=SCALE)

    def image(self):
        return self.im.resize((WIDTH, self.height), Image.Resampling.LANCZOS)


def project(x, y, z, angle, cx=888, cy=287, radius=198):
    x, z = x*math.cos(angle)+z*math.sin(angle), -x*math.sin(angle)+z*math.cos(angle)
    tilt = -.27
    y, z = y*math.cos(tilt)-z*math.sin(tilt), y*math.sin(tilt)+z*math.cos(tilt)
    perspective = 3.6 / (3.6-z)
    return cx+x*radius*perspective, cy+y*radius*perspective, z


def hero(theme, frame):
    c = Canvas(580, theme)
    t = frame / FRAMES
    c.text((42, 29), "DW /", 18, "accent")
    c.text((117, 31), "RESEARCH  /  SOFTWARE  /  PUBLIC LIFE", 13, "muted")
    c.text((923, 31), "MAASTRICHT, NL", 13, "muted")
    c.line([(42, 65), (1158, 65)])

    # An oblique, rotating spherical mesh: information acquiring structure.
    for x in range(648, 1159, 30):
        for y in range(95, 490, 30):
            c.circle((x, y), .6, "line")
    nodes = []
    bands, meridians = 13, 24
    for i in range(bands):
        lat = -math.pi/2 + (i+1)*math.pi/(bands+1)
        for j in range(meridians):
            lon = j*math.tau/meridians
            nodes.append(project(math.cos(lat)*math.cos(lon), math.sin(lat),
                                 math.cos(lat)*math.sin(lon), t*math.tau))
    edges = []
    for i in range(bands):
        for j in range(meridians):
            a = i*meridians+j
            for b in [i*meridians+(j+1)%meridians] + ([a+meridians] if i<bands-1 else []):
                edges.append((nodes[a], nodes[b]))
    for a, b in sorted(edges, key=lambda e: e[0][2]+e[1][2]):
        depth = (a[2]+b[2]+2)/4
        color = blend(c.c["bg"], c.c["accent"], .13+.55*depth)
        c.line([a[:2], b[:2]], color, .7 if depth<.5 else 1)
    for i, (x, y, z) in sorted(enumerate(nodes), key=lambda n: n[1][2]):
        if i % 7 == 0:
            c.circle((x, y), 1.1+(z+1)*.7, blend(c.c["bg"], c.c["accent"], .25+.35*(z+1)))
    # Three signal points travel on the same mesh, without flashing.
    for phase in (0, 1/3, 2/3):
        theta = math.tau*(t+phase)
        p = project(math.cos(theta), 0, math.sin(theta), t*math.tau)
        c.circle(p[:2], 8, "signal", False)
        c.circle(p[:2], 3, "signal")
    c.text((685, 108), "SOURCE", 11, "muted")
    c.text((1024, 455), "STRUCTURE", 11, "muted")
    c.line([(715, 126), (760, 153)], "signal")
    c.line([(1004, 438), (1030, 447)], "signal")

    c.text((40, 105), "David", 116, serif=True)
    c.text((40, 213), "Wicker", 145, serif=True)
    c.text((45, 390), "Making complex information", 27)
    c.text((45, 429), "useful to people.", 27)
    c.line([(42, 511), (1158, 511)])
    for x, num, label in [(42, "01", "LEGAL RESEARCH"), (431, "02", "LANGUAGE"), (811, "03", "KNOWLEDGE")]:
        c.text((x, 538), num, 13, "signal")
        c.text((x+35, 536), label, 15, "accent")
    return c.image()


def card(theme, kind, frame=0):
    c = Canvas(230, theme)
    titles = ["Case Law Explorer", "Hayeren", "Commonfold"]
    domains = ["LEGAL RESEARCH", "EASTERN ARMENIAN", "PERSONAL KNOWLEDGE"]
    c.text((38, 25), f"0{kind+1} / {domains[kind]}", 13, "muted")
    c.text((36, 73), titles[kind], 63, serif=True)
    c.text((38, 176), "EXPLORE THE ARCHITECTURE", 12, "accent")
    c.line([(332, 182), (367, 182)], "signal")
    c.line([(360, 176), (367, 182), (360, 188)], "signal")
    c.line([(594, 26), (594, 204)])
    if kind == 0:
        points = [(665,65),(665,115),(665,165),(765,90),(765,148),(879,115),(977,66),(977,115),(977,165),(1120,115)]
        for a,b in [(0,3),(1,3),(1,4),(2,4),(3,5),(4,5),(5,6),(5,7),(5,8),(6,9),(7,9),(8,9)]:
            c.line([points[a], points[b]], "accent")
        for i,p in enumerate(points):
            c.circle(p, 8 if i==5 else 5, "signal" if i==5 else "accent")
            c.circle(p, 13 if i==5 else 10, "line", False)
        c.text((650, 194), "CORPORA", 10, "muted")
        c.text((848, 194), "CITATIONS", 10, "muted")
        c.text((1063, 194), "DISCOVERY", 10, "muted")
    elif kind == 1:
        for x,w,y in [(651,125,53),(651,95,86),(651,145,119),(651,107,152)]:
            c.rect((x,y,x+w,y+13), "line", True)
        c.line([(815, 45),(815, 177)], "signal", 2)
        c.line([(831,113),(906,113)], "accent")
        c.circle((915,113), 7, "signal")
        for x,y in [(995,62),(1090,83),(1045,155)]:
            c.line([(923,113),(x,y)], "accent")
            c.circle((x,y), 5)
            c.circle((x,y), 15, "line", False)
        c.text((651, 194), "READ", 10, "muted")
        c.text((881, 194), "UNDERSTAND", 10, "muted")
        c.text((1057, 194), "REMEMBER", 10, "muted")
    else:
        for x,y in [(657,63),(665,55),(673,47)]:
            c.rect((x,y,x+97,y+115), "bg", True)
            c.rect((x,y,x+97,y+115), "accent")
        for y,w in [(71,60),(88,48),(105,61),(122,35)]:
            c.line([(690,y),(690+w,y)], "line", 3)
        c.line([(788,109),(867,109)], "accent")
        c.circle((880,109), 12, "signal", False)
        c.line([(875,109),(879,113),(886,104)], "signal", 2)
        c.line([(893,109),(976,109)], "accent")
        for y in [63,95,127]:
            c.rect((989,y,1119,y+23), "accent")
            c.circle((1002,y+11), 2, "signal")
        c.text((661, 194), "CAPTURE", 10, "muted")
        c.text((855, 194), "REVIEW", 10, "muted")
        c.text((1041, 194), "RECALL", 10, "muted")
    # Small travelling signals animate the real conceptual handoff in each card.
    paths = [
        [(665,65),(765,90),(879,115),(977,66),(1120,115)],
        [(815,113),(915,113),(1045,155)],
        [(788,109),(880,109),(976,109)],
    ]
    path = paths[kind]
    for offset in (0, .5):
        p = ((frame/40+offset) % 1) * (len(path)-1)
        segment = min(int(p), len(path)-2)
        a, b = path[segment:segment+2]
        fraction = p-segment
        xy = (a[0]+(b[0]-a[0])*fraction, a[1]+(b[1]-a[1])*fraction)
        c.circle(xy, 5, "bg")
        c.circle(xy, 3, "signal")
    return c.image()


def main():
    for theme in THEMES:
        frames = [hero(theme, i) for i in range(FRAMES)]
        frames[0].save(ASSETS / f"hero-{theme}.png", optimize=True)
        # One palette for the whole sequence prevents temporal color noise.
        frames = [f.resize((960, 464), Image.Resampling.LANCZOS) for f in frames]
        palette = frames[0].quantize(colors=96)
        frames = [f.quantize(palette=palette, dither=Image.Dither.NONE) for f in frames]
        frames[0].save(ASSETS / f"hero-{theme}.gif", save_all=True, append_images=frames[1:],
                       duration=110, loop=0, optimize=True, disposal=1)
        for kind, name in enumerate(["case-law", "hayeren", "commonfold"]):
            card(theme, kind).save(ASSETS / f"{name}-{theme}.png", optimize=True)
            sequence = [card(theme, kind, i).resize((960,184), Image.Resampling.LANCZOS) for i in range(40)]
            palette = sequence[0].quantize(colors=96)
            sequence = [f.quantize(palette=palette, dither=Image.Dither.NONE) for f in sequence]
            sequence[0].save(ASSETS / f"{name}-{theme}.gif", save_all=True, append_images=sequence[1:],
                             duration=100, loop=0, optimize=True, disposal=1)
        print(f"Rendered {theme} artwork", flush=True)
    readme = ROOT / "README.md"
    if readme.exists():
        static = readme.read_text().replace('.gif', '.png')
        static = static.replace('[Still version](README-STATIC.md)', '[Animated version](README.md)')
        (ROOT / "README-STATIC.md").write_text(static)


if __name__ == "__main__":
    main()
