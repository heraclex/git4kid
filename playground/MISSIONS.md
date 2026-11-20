# 🎴 Hero Card Studio — Missions with Claude

Open `index.html` in your browser. Right now the card is **broken** 💥 — someone saved a bad change.
You won't type Git commands. **You are the director, Claude is your assistant.** You say what you want in plain words; Claude runs Git.

Your job in every mission:
1. **Ask** (copy the prompt, or say it your own way).
2. **Read** what Claude is about to do before you approve it.
3. **Check** the result yourself (browser, GitHub page).

> 💡 Any time you're curious, ask: *"What exactly did you just run, and what did it do?"*

Start Claude Code inside this folder (`claude`).

## Mission 0 — Set up your own copy 🏗️
> *"Create a new private repository on our GitHub Enterprise called `hero-card-<my-name>`, set it as this project's remote, and push the `main` branch. Tell me the link."*

✅ Check: open the link Claude gives you. You should see the files **and** a long list of commits.

## Mission 1 — Read the history book 📖
> *"Show me the history of this project in plain English. Which change broke the card, and what exactly did it change?"*

✅ Check: Claude should point at the commit called *"Oops: tidy up character file"*. Do you understand what went wrong?

## Mission 2 — Use the time machine ⏪
> *"Undo only that broken change, but keep all history. Then explain what you did."*

✅ Check: refresh `index.html` — Captain Pixel is back! 🎉 Ask Claude to show the history again: the oops is still there, followed by a new "undo" commit. **Nothing was erased.**

## Mission 3 — Make the hero yours 🦸
> *"Change my hero: name `<…>`, emoji `<…>`, a power, a colour, a motto. Show me what changed before saving."*
> *"Save this as a checkpoint with a clear message."*

✅ Check: refresh the page. Read Claude's proposed **commit message** before you approve. Would a teammate understand it in 6 months?

## Mission 4 — Experiment on a branch 🌿
> *"Create a branch called `evil-mode`. On that branch turn my hero into a villain (😈, red, scary motto) and save it. Then switch back to main."*

✅ Check: on `main` your good hero is untouched. Ask Claude to switch back to `evil-mode` and look again. **Same file, two parallel universes.**

## Mission 5 — Share it: push and Pull Request 🔀
> *"Push `evil-mode` and open a pull request. Write a description that explains what changed and why."*

✅ Check: open the PR link on GitHub. Look at the **Files changed** tab — that's the review your teammates would do. Like it? **You** click **Merge**. Don't like it? Close the PR. `main` stays safe either way.

> 🛡️ Notice: Claude does not merge for you. Humans decide what goes into `main`.

## Bonus 🌟
- **Conflict:** change the *same line* (e.g. the motto) on `main` and on a branch, then ask Claude to merge. Ask it to **explain the conflict in plain words** before resolving it — and tell *it* which version you want.
- **Teach Claude your rules:** open `CLAUDE.md` in this folder. Add a rule of your own (e.g. *"Always write commit messages in French"*), then do another commit and see it follow the rule.
- **Undo vs. erase:** ask *"What's the difference between revert and reset? Which is safer?"*
- **Be the reviewer:** ask Claude to *"review my pull request and tell me any risks"*.
