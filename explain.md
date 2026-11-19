Explain GitHub to a 15-year-old using something familiar: **Google Docs + a time machine + teamwork for programmers.**

The most important thing is not to start with Git commands or complicated programming terminology. Let your kid understand the problem GitHub solves first, then let them try it themselves.

Here's how presenting it in about 20–30 minutes.

# **1. Explain GitHub using a simple story**

Imagine your kid is creating a computer game. They write some code, change it, add new features, and sometimes accidentally break things.

Without GitHub, they might end up with files like:

```
my-game/
  my-game-final.py
  my-game-final-v2.py
  my-game-final-fixed.py
  my-game-final-really-final.py
```

We've all seen this problem!

GitHub solves this problem by helping developers save the history of their projects and collaborate with other people.

[Design Version Control System | LLD](https://images.openai.com/static-rsc-4/yZsn6AJzruTK7nZ38nBd7ooR6UTjhFLM_98G_DdA0im5gMPSgOOUrklErFc5U7UozbUPRCIrEjRQBqiELm03P7WBVaQ2GW8baXwmJPVh1RlCnUIGmtUneZxOpeDin2Mhvi5eNjqO7eLBBf69NcYNVbtJG9CoqygkdUwB6e-ia2U?purpose=inline)

[algomaster.io](https://algomaster.io/learn/lld/design-version-control-system?utm_source=chatgpt.com)

Think of it this way:

| Real-world concept          | GitHub concept    |
| --------------------------- | ----------------- |
| A project folder            | Repository (Repo) |
| Save a version of your work | Commit            |
| A history book of changes   | Commit history    |
| Try a new idea separately   | Branch            |
| Ask to combine your work    | Pull Request      |
| Share your project online   | GitHub            |

**One important distinction:**

- **Git** is the tool that tracks changes in your code.
- **GitHub** is a website/platform that hosts Git projects and makes collaboration easier.

An easy sentence to remember:

> Git is the time machine. GitHub is the place where developers share their time machines and work together.

# **2. Introduce the four most important concepts**

I'd teach only these four concepts initially.

[rostrum.blog - Git going: Git and GitHub](https://images.openai.com/static-rsc-4/ZpV79Wpny3j-PWxl5LQbyDlgTZD4Daq3aGWGkJptNweremip7rjXmTKotyumR7bdyw5EqOFR9fjhCNAHydm7-tAVJQ3Llmo4MyxB2FFO1oniWCKmVnZtyJG7G2QngTXJIZASInEFqlS4gggL-O5yR7o57HwcDfwsXWUt_K9_AdM?purpose=inline)

**1. Repository (Repo)**

A project folder containing all your files and the history of changes.

Example: A repository called `my-first-game`.

[A Friendly Guide to Becoming a Git Power User | by Kairsten Fay | CodeX | Medium](https://images.openai.com/static-rsc-4/w1KoLop3BW6lRSRQh3nOukMnVvoOmALoROEkNSUCB3mKxtcA1ySUvG_GErLFIUh4ZXJL9Qjs558qPRuVrrbG1KeR_xAArJfSjFIsT80kiFZB8XqHKIFVmGo59XjOabHsML7PFUWlChD897HRpH-OyG04wLpM3n1wKQWHUcHmm4g?purpose=inline)

**2. Commit**

A saved checkpoint of your project.

Example: "I added a player character."

[VibeCodex](https://images.openai.com/static-rsc-4/DdLALwPtg6xfPJVjuFYDd4i9UEgJOTODy_RfuvgP3j6GsRaBNvuGLFphfec9_dpl2-4nw_nqYYALLHQXcfkrVbwG7yOOfy9XCBiMueS8Yc3ustVdN_Btp9gkXwxESWnsaV5_egd8v-W8SCyPKxdZAA02tUa4VNtw_-cyT2z1X50?purpose=inline)

**3. Branch**

A separate workspace where you can experiment without changing the main version.

Example: Try adding a new game level.

[6. Open and Merge a Pull Request — Reproducible Research for Teams with GitHub](https://images.openai.com/static-rsc-4/InloehoWKrSTZ_uwFevgtLzFVdl8ITPtxD38FHbFSwo-9tHqthQMo437kxiaGyMpwcfTInb8E89YbQvstfX1swvuSzvPOwHaBwo2MtKw4qGE02yVcUjdQi4uQKxfKZ0Tko2OlH7GXXL4YowySVjf0QpvqV46OtDMjnCXz0PuFxU?purpose=inline)

**4. Pull Request (PR)**

A proposal to merge your changes into the main project.

Example: "I've finished the new level. Can we add it to the game?"

# **3. Let's do a small practical demo!**

Beginner friendly · No coding required

For the first exercise, I'd use the GitHub website instead of installing Git or using a terminal.

The mission:

**Create your first project and change it three times, just like a real developer.**

[Spring 2025 - Git/GitHub basics](https://images.openai.com/static-rsc-4/irFiMmaHjaXCEfRe7vRiYIB7rhLv_2BzTonhceB5f2lS6NgEWz9o2Dxv-wRk73RY2pBBN4bnzG463qQWxB5h96ZG9527U9XiAM9cPXncdwb9zCT_DflL9tCZbkjsNM3WlWG7I3fp6VD0HKWMSM9JNNHuNOKG0i_JKXaDxxa1les?purpose=inline)

[spring-2025.envs-193ds.com](https://spring-2025.envs-193ds.com/resources/using-github?utm_source=chatgpt.com)

## **Step 1 — Create a GitHub account**

Go to [GitHub](https://github.com/?utm_source=chatgpt.com) and create a free account.

Then:

1. Click the `+` button in the top-right corner.
2. Select `New repository`.
3. Name it `my-first-project`.
4. Choose `Public` (so you can share it).
5. Tick `Add a README file`.
6. Click `Create repository`.

Congratulations! You've just created your first repository.

## **Step 2 — Make your first commit**

Open the `README.md` file.

Click the pencil icon to edit it.

Add this content:

```
# My First Project

Hello! My name is Alex.

I am learning GitHub.

## My interests
- Gaming
- Football
- Programming

## My goal
Build my first computer game!
```

Replace Alex with your kid's name.

Scroll down to the commit section:

- Commit message: `Create my first README`
- Click `Commit changes`.

[Как пользоваться GitHub: краткий обзор для новичков](https://images.openai.com/static-rsc-4/30hBU916mrMDtJdxyraVNrHSr55Qa_tm7sAk5jmpteawwOEZJ1YE51RIM0GZHfQQnT73qIIXzwPFNhRmBzHkNakTk_hElBfp8obioXKWwr1odp-F11wG3LMpkr6jbAJjSDw03gjmR1SK53qp5fE22hEX83ikKStMIQJmQPMwDTA?purpose=inline)

[timeweb.com](https://timeweb.com/ru/community/articles/kak-polzovatsya-github?utm_source=chatgpt.com)

Explain:

"You've just saved a checkpoint. GitHub remembers what your project looked like at this moment."

## **Step 3 — Change something and commit again**

Now edit README.md again.

Add:

```
## My favourite games
- Minecraft
- Roblox
- Fortnite
```

Commit with this message:

`Add my favourite games`

Now you have two commits.

Go to the repository's commit history and show how GitHub remembers both versions.

[Intro to Github for version control](https://images.openai.com/static-rsc-4/kfVwB05zWMHOcZP_36AFNn-fJ_4nDbEtsD0iAqkjI0yiXWEgQRGBhlleFH5HOhT88_1Y0eB_abDj6hIuT0YwVo01FVNlHkkWiSS71s3_j_AeyyPOdD2aCfa0NLzbmqUUonQuzMY9cAfwweisOT-X0AEMa2HLejMTjCq0T13ywKs?purpose=inline)

[ourcodingclub.github.io](https://ourcodingclub.github.io/tutorials/git/?utm_source=chatgpt.com)

**The interesting part:** If you accidentally delete something, you can look at the previous commit and recover your earlier work.

## **Step 4 — Introduce branching**

Now let's pretend your kid wants to add a new feature to the project.

Instead of modifying the main project directly:

1. Go to the repository's branch selector.
2. Create a new branch called `add-my-hobbies`.
3. Edit README.md on that branch.
4. Add a new section:

```
## My hobbies
- Playing football
- Building LEGO
- Playing video games
```

5\. Commit the changes.

The main branch hasn't been changed. The new work lives separately.

[Hello World - GitHub Docs](https://images.openai.com/static-rsc-4/FoVdHScQqFaiqzeD7m43oUVPBF-0S7PAqouliu-qX2iGMnd6ehTmxk2gErmRE2Dm5ZiDily6URIBCFCIFa23j5KTQRXzC6S1O214AjBOg-QOACdVxkKomM_zfZEzlDdidBGH1AseAIZx1gvmsqLSTOIygvv685qDJ-Cp6ZPbl4A?purpose=inline)

[docs.github.com](https://docs.github.com/en/get-started/quickstart/hello-world?utm_source=chatgpt.com)

## **Step 5 — Create a Pull Request**

This is where GitHub becomes interesting.

Go to the Pull Requests tab and click `New pull request`.

Select:

- Base: `main`
- Compare: `add-my-hobbies`

You should see the changes you made.

Give it a title:

`Add my hobbies to the project`

Then click `Create pull request`.

Explain:

"You're asking the project owner to review your work before adding it to the main project."

Finally, click `Merge pull request` and confirm.

[GitHub Workflow: A Comprehensive Guide to Collaboration](https://images.openai.com/static-rsc-4/A6y6E8o5wCv3VonVdscuoSpYtUFFtk5wTx4b_apQe77uBZPnQR57fWE2EF2YLKo8dd4k4zAESq35OfWGIP1Vrc0yWS6VBSWJXKhba_9CHw9q0JyQ8OCDjeJ6GeYEaqpzckaTzW-eLy3vcSAK7THGt-Yq1aalJ-TucsmNZX2qYBM?purpose=inline)

[trailhead.salesforce.com](https://trailhead.salesforce.com/ja/content/learn/modules/git-and-git-hub-basics/work-with-the-git-hub-workflow?utm_source=chatgpt.com)

Congratulations! Your kid has experienced the basic GitHub workflow without writing a single line of programming code.

# **4. Give your kid a little challenge**

After the demo, ask these questions to see whether they've understood:

1. If I make a mistake in my project, which GitHub feature helps me find an older version?
2. If I want to experiment without breaking my main project, what should I create?
3. If I want someone to review my changes before accepting them, what should I create?
4. What's the difference between Git and GitHub?

**Bonus challenge: Become a developer!**

Ask your kid to create a repository called `my-dream-game`.

[Minecraft 2d edition pixel art](https://images.openai.com/static-rsc-4/bmvQFGcXg_NK5tzOgGmXQxhqQAZraxZWQcyGJNEtznU96aIoqJbXID3RQnJe02jEzC5WyIl09UAvPHJAuYecNj_XUSCoe81jJFNS6Bv9TCLQdyZkXp0Lf1Bf1TtunSCZOH1pgxqMPa1MCRCStgiWzzKvQyQkwWG8lfC2tL1kxpg?purpose=inline)

[dinopixel.com](https://dinopixel.com/minecraft-2d-edition-pixel-art-36826?utm_source=chatgpt.com)

Their mission:

- Create a README describing their dream game.
- Create a branch called `new-game-character`.
- Add a description of a new character.
- Commit the changes.
- Open a Pull Request.
- Merge it into main.

Mission complete

# **5. What I would teach next**

Once they understand the GitHub website, I'd introduce actual programming and Git commands.

A natural learning path would be:

1. **GitHub basics:** Repository, commit, branch, pull request.
2. **Git locally:** Install Git and learn `git add`, `git commit`, `git push`, `git pull`.
3. **Programming:** Learn Python or JavaScript.
4. **Build something:** A small calculator, quiz game, or website.
5. **Collaboration:** Work with another person on the same project.