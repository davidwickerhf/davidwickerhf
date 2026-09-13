# Profile artwork

This README uses original animated SVG artwork and GitHub-native disclosure sections. All imagery lives in this repository. No external stats service, tracking pixel, scheduled job, or credential is required.

## Direction

White surfaces with a fine outline fit GitHub's light page. The dark version uses GitHub's `#0d1117` background. Green `#294f48` and rust `#9f4c38` accents connect the graphics to [wicker.life](https://wicker.life). Instrument Serif supplies display lettering; Manrope supplies labels and buttons.

The rotating mesh and project diagrams are illustrative graphics, not live metrics or exact deployment diagrams. Expanded Mermaid diagrams are simplified explanations.

The [awesome-github-profile-readme collection](https://github.com/abhisheknaiidu/awesome-github-profile-readme) informed the image-led introduction and exploratory layout, particularly [Jhey's animated vector artwork](https://github.com/jh3y/jh3y). No artwork or code was copied from other profiles.

## Rendering

- All lettering is exported as vector glyph outlines, including the three link buttons. It remains sharp on Retina displays and when enlarged, without relying on installed fonts.
- SVG geometry carries the motion through declarative animation. No JavaScript or raster animation is embedded. The header rotates over 16 seconds; signals in the project diagrams travel over four seconds.
- Native `picture` sources select light/dark artwork and separate still SVGs for reduced motion. Internal media queries also hide moving geometry when reduced motion is requested.
- `README-STATIC.md` uses only nonanimated assets and is linked from the main profile.
- Native `details` sections reveal Markdown and Mermaid architecture diagrams. Project summaries and important links remain outside disclosures.
- Images have descriptive alt text. The work is also explained in selectable text below the artwork.
- GitHub controls the surrounding page background; a README cannot recolor the entire page.

SVG animation depends on the embedded-image context and browser support. The static artwork remains complete without animation; GitHub's separate file-preview surface may behave differently from images embedded in Markdown.

## Edit and regenerate

Edit `README.md` for content, `scripts/render_artwork.py` for artwork and animation, and `scripts/vector_canvas.py` for the SVG drawing backend and palette. Then run:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r scripts/requirements.txt
.venv/bin/python scripts/render_artwork.py
```

This rebuilds both themes, still SVGs, buttons, and the static README. Geometry and bundled font outlines are deterministic. The complete selected-theme artwork is approximately 445 KB, including the header, three project panels, and three buttons.

Font sources: [Instrument Serif](https://github.com/google/fonts/tree/main/ofl/instrumentserif) and [Manrope](https://github.com/google/fonts/tree/main/ofl/manrope). Their SIL Open Font Licenses are bundled in `assets/fonts/`.

Content sources: the public [profile](https://wicker.life/about), [Case Law Explorer](https://wicker.life/research/case-law-explorer), [Hayeren](https://wicker.life/projects/hayeren), and [Commonfold](https://wicker.life/projects/commonfold) pages; the linked public repository READMEs; and dataset cards under [davidwickerhf on Hugging Face](https://huggingface.co/davidwickerhf). ECHR's upcoming status was supplied by David. Institutional work is attributed as a contribution within the wider teams.
