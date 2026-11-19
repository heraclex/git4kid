# Git for everyone — presentation + playground

- `presentation.html` — the slide deck (open in a browser; `M` = jump menu, `F` = fullscreen).
- `playground/` — source files of the hands-on project, **Hero Card Studio** (browse them here).
- `playground.bundle` — the same project **with its Git history** (including the deliberate "Oops" commit). This is what participants use.

## Start the playground
```
git clone playground.bundle playground-play
cd playground-play
```
Then open `index.html` in a browser and follow `MISSIONS.md`.

> Don't work inside `playground/` of this repo — it has no hero-card history. Always use the clone above.

## Rebuilding the bundle
If you change the playground, recreate a repo from the bundle, commit there, copy files back here, and run
`git bundle create ../playground.bundle --all` inside that clone.
