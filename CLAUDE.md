# git4kid

Teaching material that introduces Git/GitHub to teenagers (~15 y/o): a slide deck plus a hands-on playground repo. Tone: friendly, concrete, no jargon before the problem is understood (see `explain.md` for the teaching approach).

## Files
- `presentation.html` — **the source of truth for the deck.** Single self-contained file (inline CSS + JS, no build step, no dependencies). Edit it directly.
- `playground/` — plain source files of the hands-on project ("Hero Card Studio"). It has **no hero-card Git history**; don't work or commit inside it for the lesson.
- `playground.bundle` — the same project *with* deliberate history (incl. the "Oops" commit). Participants run `git clone playground.bundle playground-play`. See `README.md` for rebuilding it.
- `explain.md` — teaching notes/outline. `playground/MISSIONS.md` — participant instructions.

## Working on the deck
- Preview: open `presentation.html` in a browser (no server needed). Nothing here can be run from the CLI; there is no Node, test suite or linter.
- Each slide is a `<section class="slide">` inside `#deck`. Slides use `vw`/`vh`/`clamp()` units, so they scale with the viewport.
- Section grouping depends on the slide's `.eyebrow` text: the `SECTIONS` array in the script matches prefixes like `01 ·`, `02 ·`. Keep eyebrow prefixes consistent when adding or renaming slides, or the agenda buttons and 1–6 keys break.
- The right sidebar thumbnails are live clones of the slides (ids are stripped from clones). Avoid relying on element ids inside slides for anything other than the existing wired ones (`agenda`, `bonus`, `board`, `bonuswin`, `boardwin`).
- Keys: ←/→/PgUp/PgDn navigate, Home/End, `T` sidebar, `F` fullscreen, `1`–`6` section jump. The old "M" jump menu was removed on purpose.
- Print/PDF: `@media print` shows every slide; keep the sidebar hidden there.

## Conventions
- Keep it one file, no external assets or CDNs (it must work offline in a classroom).
- Match the existing CSS variables (`--mint`, `--accent`, …) and component classes (`.card`, `.callout`, `.step`, `.qa`, `.check`) before inventing new ones.
- Commit messages: short imperative summary. Only commit when asked.
- Keep `README.md` in sync when user-facing behaviour (keys, workflow) changes.
