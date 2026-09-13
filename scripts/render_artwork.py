"""Render the profile's original vector artwork. Python 3.10+ and fontTools.

Run from anywhere: python3 scripts/render_artwork.py
All geometry is illustrative; it does not represent live research data.
"""

from pathlib import Path
import math
from vector_canvas import Canvas, THEMES

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"

def rgb(value):
    return tuple(bytes.fromhex(value.lstrip("#")))


def blend(a, b, t):
    return tuple(round(x + (y - x) * t) for x, y in zip(rgb(a), rgb(b)))


def project(x, y, z, angle, cx=888, cy=287, radius=198):
    x, z = x*math.cos(angle)+z*math.sin(angle), -x*math.sin(angle)+z*math.cos(angle)
    tilt = -.27
    y, z = y*math.cos(tilt)-z*math.sin(tilt), y*math.sin(tilt)+z*math.cos(tilt)
    perspective = 3.6 / (3.6-z)
    return cx+x*radius*perspective, cy+y*radius*perspective, z


def sphere(c, motion):
    frames = 32 if motion else 1
    bands, meridians = 13, 24
    all_nodes = []
    for frame in range(frames+1 if motion else 1):
        angle = frame/frames*math.tau if motion else 0
        nodes=[]
        for i in range(bands):
            lat = -math.pi/2+(i+1)*math.pi/(bands+1)
            for j in range(meridians):
                lon=j*math.tau/meridians
                nodes.append(project(math.cos(lat)*math.cos(lon), math.sin(lat), math.cos(lat)*math.sin(lon), angle))
        all_nodes.append(nodes)
    routes = [[i*meridians+j for j in range(meridians)]+[i*meridians] for i in range(bands)]
    routes += [[i*meridians+j for i in range(bands)] for j in range(meridians)]
    for route in routes:
        values = [' '.join(f'{nodes[i][0]:.2f},{nodes[i][1]:.2f}' for i in route) for nodes in all_nodes]
        animation = f'<animate attributeName="points" values="{";".join(values)}" dur="16s" repeatCount="indefinite"/>' if motion else ''
        c.parts.append(f'<polyline points="{values[0]}" fill="none" stroke="{c.c["accent"]}" stroke-opacity=".48" stroke-width=".85">{animation}</polyline>')
    for i in range(0,bands*meridians,7):
        positions=[nodes[i] for nodes in all_nodes]
        signals=i%5==0
        radius=3 if signals else 1.8
        animation=''
        if motion:
            for index, attr in enumerate(['cx','cy']):
                values=';'.join(f'{p[index]:.2f}' for p in positions)
                animation+=f'<animate attributeName="{attr}" values="{values}" dur="16s" repeatCount="indefinite"/>'
        c.parts.append(f'<circle cx="{positions[0][0]:.2f}" cy="{positions[0][1]:.2f}" r="{radius}" fill="{c.c["signal" if signals else "accent"]}">{animation}</circle>')


def hero(theme, motion=True):
    c = Canvas(580, theme)
    c.text((42, 29), "wicker.life", 17, "accent")
    c.line([(42, 65), (1158, 65)])
    for x in range(648,1159,30):
        for y in range(95,490,30):
            c.circle((x,y),.6,'line')
    if motion:
        c.parts.append('<style>.still{display:none}@media(prefers-reduced-motion:reduce){.motion{display:none}.still{display:inline}}</style><g class="motion">')
        sphere(c,True)
        c.parts.append('</g><g class="still">')
        sphere(c,False)
        c.parts.append('</g>')
    else:
        sphere(c,False)
    c.text((40,105), 'David',116,serif=True)
    c.text((40,213), 'Wicker',145,serif=True)
    c.text((45,390), 'Developer and researcher.',27)
    c.text((45,429), 'Maastricht, the Netherlands.',27)
    c.line([(42,511),(1158,511)])
    for x,num,label in [(42,'01','CASE LAW EXPLORER'),(465,'02','HAYEREN'),(851,'03','COMMONFOLD')]:
        c.text((x,538),num,13,'signal')
        c.text((x+35,536),label,15,'accent')
    return c.image()


def card(theme, kind, motion=True):
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
    path_d='M'+' L'.join(f'{x},{y}' for x,y in path)
    if motion:
        c.parts.append('<style>@media(prefers-reduced-motion:reduce){.motion{display:none}}</style>')
    for offset in (0, 2):
        if motion:
            c.parts.append(f'<circle class="motion" r="3.5" fill="{c.c["signal"]}" stroke="{c.c["bg"]}" stroke-width="1.5"><animateMotion path="{path_d}" dur="4s" begin="-{offset}s" repeatCount="indefinite"/></circle>')
        else:
            c.circle(path[offset%len(path)],3.5,'signal')
    return c.image()


def main():
    for theme in THEMES:
        for motion in (True,False):
            suffix = '' if motion else '-still'
            (ASSETS / f'hero-{theme}{suffix}.svg').write_text(hero(theme,motion))
            for kind,name in enumerate(['case-law','hayeren','commonfold']):
                (ASSETS/f'{name}-{theme}{suffix}.svg').write_text(card(theme,kind,motion))
        for name,label,width in [('cv','CV',90),('research','Research',132),('linkedin','LinkedIn',132)]:
            c=Canvas(42,theme,width)
            c.text((17,13),label,15,'accent')
            c.line([(width-25,25),(width-15,15)],'accent',1.4)
            c.line([(width-23,15),(width-15,15),(width-15,23)],'accent',1.4)
            (ASSETS/f'button-{name}-{theme}.svg').write_text(c.image())
        print(f'Rendered {theme} SVG artwork',flush=True)
    readme=ROOT/'README.md'
    if readme.exists():
        static=readme.read_text()
        for theme in THEMES:
            for name in ['hero','case-law','hayeren','commonfold']:
                static=static.replace(f'{name}-{theme}.svg',f'{name}-{theme}-still.svg')
        static=static.replace('[Still version](README-STATIC.md)','[Animated version](README.md)')
        (ROOT/'README-STATIC.md').write_text(static)


if __name__ == '__main__':
    main()
