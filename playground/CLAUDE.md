# Hero Card Studio (training playground)

A tiny browser project (`index.html`, `character.js`, `style.css`) used in a Git/GitHub training session.
The person you're helping is **not a developer** and is learning what Git does by directing you.

## How to work with them
- Before any git action, say in one plain sentence what you're about to do and why. After it, say what changed.
- Avoid jargon; if you use a git word (commit, branch, revert), explain it briefly the first time.
- Write clear commit messages: short, imperative, describing the change ("Make the hero a villain").
- After a change, tell them how to check it (refresh `index.html`, or what to look at on GitHub).

## Guardrails (also part of the lesson)
- Never commit directly to `main` for experiments — use a branch.
- Never push, open a pull request, or merge unless they asked for that step.
- Never merge a pull request yourself. The human reviews it on GitHub and clicks Merge.
- Never force-push, and never run `git reset --hard` or delete branches without asking first.
- To undo a past change, prefer `git revert` (keeps history) over rewriting history.
- The remote is GitHub Enterprise (`mercedes-benz.ghe.com`). Use the `gh` CLI for issues and pull requests.
