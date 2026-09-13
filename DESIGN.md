# Profile artwork

This README uses original, code-rendered animation and GitHub-native disclosure sections. All imagery lives in this repository. No external stats service, tracking pixel, scheduled job, or credential is required.

## Direction

The palette comes from [wicker.life](https://wicker.life): warm paper `#f1eee6`, dark ink `#171b19`, green `#294f48`, and rust `#9f4c38`. A complementary dark palette keeps the artwork legible on dark backgrounds. Instrument Serif supplies the large display lettering; Manrope connects the smaller type to the portfolio.

The rotating mesh introduces the idea of giving information structure. The project diagrams show citations, language lookup, and reviewed knowledge capture. These are illustrative graphics, not live metrics or exact deployment diagrams. Expanded Mermaid diagrams are deliberately simplified explanations.

The [awesome-github-profile-readme collection](https://github.com/abhisheknaiidu/awesome-github-profile-readme) informed the image-led introduction and exploratory layout, particularly [Jhey's animated artwork](https://github.com/jh3y/jh3y) and [Nate Moore's personal, designed profile](https://github.com/natemoo-re/natemoo-re). No artwork or code was copied from those profiles.

## GitHub compatibility

- GIF images carry the motion; the profile does not depend on JavaScript, inline styles, or SVG animation support.
- Native `picture` sources select light and dark artwork. Reduced-motion sources select still PNGs when the browser and GitHub renderer honor the media query.
- `README-STATIC.md` is a fully nonanimated alternative, linked from the main profile.
- Native `details` sections reveal Markdown and Mermaid architecture diagrams. All project summaries and important links remain outside the disclosures.
- Images have descriptive alt text. The same work is explained as selectable text below the artwork.

GitHub references: [supported images and Markdown](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#images), [theme-aware pictures](https://github.blog/changelog/2022-08-15-specify-theme-context-for-images-in-markdown-ga/), and [non-code file rendering](https://docs.github.com/en/repositories/working-with-files/using-files/working-with-non-code-files).

## Edit and regenerate

Edit `README.md` for content and `scripts/render_artwork.py` for artwork. Then run:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r scripts/requirements.txt
.venv/bin/python scripts/render_artwork.py
```

This rebuilds both themes, PNG fallbacks, animated GIFs, and the static README. The renderer uses deterministic geometry and bundled fonts, with one palette per animation to avoid color flicker. Hero artwork runs for 7.92 seconds per loop; project diagrams run for four seconds.

Font sources: [Instrument Serif](https://github.com/google/fonts/tree/main/ofl/instrumentserif) and [Manrope](https://github.com/google/fonts/tree/main/ofl/manrope). Their SIL Open Font Licenses are bundled in `assets/fonts/`.

Content sources: the public [profile](https://wicker.life/about), [Case Law Explorer](https://wicker.life/research/case-law-explorer), [Hayeren](https://wicker.life/projects/hayeren), and [Commonfold](https://wicker.life/projects/commonfold) pages, plus the linked public repository READMEs. Institutional work is attributed as a contribution within the wider teams.
