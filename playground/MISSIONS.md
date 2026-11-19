# 🎴 Hero Card Studio — Git Missions

Open `index.html` in your browser. Right now the card is **broken** 💥 — someone saved a bad change.
You'll fix it with Git, then make the hero yours. Open a terminal **in this folder** for every command.

> First time using Git? Tell it who you are (once):
> ```
> git config --global user.name "Your Name"
> git config --global user.email "you@example.com"
> ```

## Mission 1 — Read the history book 📖
```
git log --oneline
```
Each line is a **commit** (a checkpoint). Find the one called *"Oops: tidy up character file"* and note its short code (like `d527666`).

## Mission 2 — Use the time machine ⏪
See what the oops changed:
```
git show <code>
```
Replace `<code>` with the oops commit's code. Undo it (Git adds a new commit that reverses it — history is never lost):
```
git revert <code> --no-edit
```
Refresh `index.html`. Captain Pixel is back! 🎉

## Mission 3 — Make the hero yours 🦸
1. Edit `character.js` (name, emoji, power, color like `#ff8eae`, motto). Save. Refresh the browser.
2. Look at what you changed: `git diff`
3. Save a checkpoint:
```
git add character.js
git commit -m "Make the hero mine"
```

## Mission 4 — Experiment on a branch 🌿
```
git switch -c evil-mode
```
Make your hero a villain: new emoji 😈, color `#ff4d4d`, scary motto. Then:
```
git commit -am "Turn to the dark side"
git switch main
```
Refresh the page — your good hero is back and untouched! Switch again (`git switch evil-mode`) to see the villain. **Same file, two parallel universes.**

## Mission 5 — Merge the universes 🔀
Decide you like the villain? Bring it into main (this is what a Pull Request does on GitHub):
```
git switch main
git merge evil-mode
```
Don't like it? Skip the merge — `main` stays safe. (Delete the branch: `git branch -D evil-mode`.)

## Bonus 🌟
- Edit the **same line** on `main` and on a branch, then merge. Git will ask you to resolve a **conflict** — that's how teams learn to talk to each other.
- Add a new field to `character.js` (like `hobby`) and show it in `index.html`.
- Want to start over? `git switch main` and `git reset --hard c74b44d` returns to the very first commit (careful: this throws away newer work!).
