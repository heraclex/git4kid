# Git for everyone — presentation + playground

- `presentation.html` — the slide deck (open in a browser; `T` = slide sidebar, `F` = fullscreen).
- `playground/` — source files of the hands-on project, **Hero Card Studio** (browse them here).
- `playground.bundle` — the same project **with its Git history** (including the deliberate "Oops" commit). This is what participants use.

## Start the playground (Claude-driven)
Participants need Claude Code installed and `gh` logged in to GitHub Enterprise (with permission to create repos).
```
git clone playground.bundle playground-play
cd playground-play
claude
```
Then open `index.html` in a browser and follow `MISSIONS.md`: participants **direct Claude** (prompts in the file); Claude does the Git work, pushes and opens the PR. `CLAUDE.md` inside the playground holds Claude's guardrails (no merging, no force-push, explain each step).

> Don't work inside `playground/` of this repo — it has no hero-card history. Always use the clone above.

## Rebuilding the bundle
If you change the playground, clone the bundle, commit your changes there, copy files back here, and run
`git bundle create ../playground.bundle main HEAD` inside that clone.
