from pathlib import Path

out = Path("/mnt/data/github_for_teens_presentation.html")

html = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>GitHub — Your Time Machine for Code</title>
<style>
:root{
  --bg:#0b1020;--panel:#151d33;--panel2:#1c2945;--text:#f4f7ff;--muted:#b8c3dc;
  --accent:#7c9cff;--mint:#62e6c5;--yellow:#ffd36e;--pink:#ff8eae;
}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--text);font-family:Inter,ui-sans-serif,system-ui,-apple-system,Segoe UI,sans-serif;overflow:hidden}
.deck{height:100vh;width:100vw;position:relative}
.slide{display:none;height:100%;width:100%;padding:5vh 7vw 9vh;overflow:auto;animation:in .25s ease}
.slide.active{display:flex;flex-direction:column;justify-content:center}
@keyframes in{from{opacity:.35;transform:translateY(8px)}to{opacity:1;transform:none}}
.eyebrow{color:var(--mint);font-size:clamp(12px,1.2vw,16px);font-weight:800;letter-spacing:.16em;text-transform:uppercase;margin-bottom:18px}
h1{font-size:clamp(42px,7vw,88px);line-height:1.02;letter-spacing:-.045em;margin:0 0 24px;max-width:1000px}
h2{font-size:clamp(32px,4.4vw,58px);line-height:1.05;letter-spacing:-.035em;margin:0 0 22px}
h3{font-size:clamp(19px,2vw,26px);margin:0 0 10px}
p{font-size:clamp(17px,1.65vw,23px);line-height:1.5;color:var(--muted);max-width:950px;margin:0 0 18px}
strong{color:var(--text)}
.accent{color:var(--mint)}.blue{color:var(--accent)}.yellow{color:var(--yellow)}
.tag{display:inline-flex;align-items:center;gap:8px;padding:9px 14px;border:1px solid #344361;border-radius:999px;color:var(--muted);font-size:14px;margin:5px 7px 5px 0}
.grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:16px;margin-top:20px;max-width:1050px}
.grid.three{grid-template-columns:repeat(3,minmax(0,1fr))}
.card{background:linear-gradient(145deg,var(--panel),var(--panel2));border:1px solid #2b3958;border-radius:22px;padding:22px;min-width:0}
.card p{font-size:clamp(15px,1.3vw,18px);margin:0}
.icon{font-size:34px;margin-bottom:12px}
.bigline{font-size:clamp(24px,3vw,40px);font-weight:800;line-height:1.2;max-width:1000px}
.flow{display:flex;align-items:center;justify-content:center;gap:12px;flex-wrap:wrap;margin:24px 0}
.node{background:#202d4b;border:1px solid #3a4b70;padding:18px 22px;border-radius:16px;text-align:center;font-weight:800;font-size:clamp(15px,1.6vw,21px)}
.arrow{font-size:28px;color:var(--mint)}
.code{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;background:#090e1a;border:1px solid #2b3958;border-radius:16px;padding:18px 22px;color:#c9d7ff;font-size:clamp(14px,1.45vw,19px);line-height:1.65;white-space:pre-wrap;max-width:900px}
.steps{counter-reset:step;display:grid;gap:12px;max-width:950px}
.step{display:flex;gap:15px;align-items:flex-start;background:var(--panel);border:1px solid #2b3958;border-radius:16px;padding:15px 18px}
.step:before{counter-increment:step;content:counter(step);display:grid;place-items:center;flex:0 0 34px;height:34px;border-radius:50%;background:var(--accent);color:#081020;font-weight:900}
.step p{font-size:clamp(15px,1.35vw,19px);margin:0}
.callout{border-left:4px solid var(--mint);padding:12px 18px;background:#122b31;border-radius:0 14px 14px 0;max-width:950px;margin-top:18px}
.callout p{margin:0;color:#d8fff5;font-size:clamp(16px,1.5vw,21px)}
.footer{position:fixed;bottom:0;left:0;right:0;height:64px;padding:0 28px;display:flex;align-items:center;gap:16px;background:linear-gradient(transparent,rgba(11,16,32,.96) 30%)}
.progress{height:4px;background:#293550;border-radius:10px;flex:1;overflow:hidden}
.progress span{display:block;height:100%;width:0;background:var(--mint);transition:width .2s}
.counter{font-size:13px;color:var(--muted);min-width:55px;text-align:right}
button{border:1px solid #405174;background:#1a2742;color:white;border-radius:12px;padding:9px 15px;font-size:16px;cursor:pointer}
button:hover{background:#293b61}
.navhint{font-size:12px;color:#8291b1}
ul{font-size:clamp(17px,1.6vw,22px);line-height:1.7;color:var(--muted);padding-left:1.2em}
li::marker{color:var(--mint)}
.split{display:grid;grid-template-columns:1fr 1fr;gap:22px;max-width:1050px;align-items:center}
.pill{display:inline-block;background:#263553;color:#dbe5ff;border-radius:10px;padding:7px 10px;font-size:13px;margin:3px}
@media(max-width:700px){
 .slide{padding:5vh 6vw 90px}.grid,.grid.three,.split{grid-template-columns:1fr}
 .footer{padding:0 12px;gap:8px}.navhint{display:none}
}
@media print{
 body{overflow:visible;background:#fff;color:#111}.deck{height:auto}
 .slide{display:flex!important;min-height:100vh;page-break-after:always;background:#0b1020;color:white}
 .footer{display:none}
}
</style>
</head>
<body>
<div class="deck" id="deck">
<section class="slide active">
 <div class="eyebrow">A mini lesson · for curious creators</div>
 <h1>GitHub:<br><span class="accent">your time machine</span><br>for code.</h1>
 <p>How developers save their work, try new ideas, and build things together.</p>
 <div style="margin-top:24px"><span class="tag">⏱ 20–30 minutes</span><span class="tag">🎮 Game-project examples</span><span class="tag">🧑‍💻 Beginner friendly</span></div>
 <div class="callout"><p>Today's mission: understand GitHub, then create and improve a tiny project.</p></div>
</section>

<section class="slide">
 <div class="eyebrow">01 · Start with a problem</div>
 <h2>Ever had files like these?</h2>
 <div class="code">my-game-final.py\nmy-game-final-v2.py\nmy-game-final-fixed.py\nmy-game-final-REALLY-final.py</div>
 <p style="margin-top:22px">Which file is the newest? Which one actually works? What if you want the old version back?</p>
 <div class="bigline">Developers need a smarter way to <span class="yellow">save history</span>.</div>
</section>

<section class="slide">
 <div class="eyebrow">02 · The big idea</div>
 <h2>Meet GitHub</h2>
 <p>Imagine <strong>Google Docs version history</strong>, but for projects and code — plus tools for teamwork.</p>
 <div class="grid">
  <div class="card"><div class="icon">⏪</div><h3>Time machine</h3><p>See earlier versions and understand what changed.</p></div>
  <div class="card"><div class="icon">🧑‍🤝‍🧑</div><h3>Teamwork space</h3><p>Share a project and work with other people.</p></div>
  <div class="card"><div class="icon">🧪</div><h3>Safe experiments</h3><p>Try new ideas without messing up the main version.</p></div>
  <div class="card"><div class="icon">🌍</div><h3>Show your work</h3><p>Publish projects so others can explore them.</p></div>
 </div>
</section>

<section class="slide">
 <div class="eyebrow">03 · Two names, two jobs</div>
 <h2>Git vs GitHub</h2>
 <div class="split">
  <div class="card"><div class="icon">🕰️</div><h3 class="accent">Git</h3><p>A version-control tool. It tracks changes and saves checkpoints in your project.</p><div class="pill">Tracks history</div><div class="pill">Works on your computer</div></div>
  <div class="card"><div class="icon">🐙</div><h3 class="blue">GitHub</h3><p>A website that hosts Git projects and adds sharing, collaboration, and review tools.</p><div class="pill">Hosts repositories</div><div class="pill">Helps teams collaborate</div></div>
 </div>
 <div class="callout"><p><strong>Remember:</strong> Git is the time machine. GitHub is a place to share your project and its history.</p></div>
</section>

<section class="slide">
 <div class="eyebrow">04 · Four words to know</div>
 <h2>The GitHub starter pack</h2>
 <div class="grid">
  <div class="card"><div class="icon">📁</div><h3>Repository (repo)</h3><p>Your project folder, including its tracked history.</p></div>
  <div class="card"><div class="icon">📸</div><h3>Commit</h3><p>A checkpoint that records a set of changes.</p></div>
  <div class="card"><div class="icon">🌿</div><h3>Branch</h3><p>A separate line of work for trying an idea.</p></div>
  <div class="card"><div class="icon">🔀</div><h3>Pull Request</h3><p>A proposal to review and merge changes into another branch.</p></div>
 </div>
</section>

<section class="slide">
 <div class="eyebrow">05 · How the ideas fit together</div>
 <h2>A tiny project journey</h2>
 <div class="flow">
  <div class="node">📁 Create repo</div><div class="arrow">→</div>
  <div class="node">📸 Commit</div><div class="arrow">→</div>
  <div class="node">🌿 Branch</div>
 </div>
 <div class="flow">
  <div class="node">✍️ Make changes</div><div class="arrow">→</div>
  <div class="node">🔀 Pull Request</div><div class="arrow">→</div>
  <div class="node">🎉 Merge</div>
 </div>
 <p>In plain English: start a project, save a checkpoint, experiment separately, ask to combine your changes, then merge them.</p>
</section>

<section class="slide">
 <div class="eyebrow">06 · Demo time</div>
 <h2>Let's create a first project</h2>
 <p>Open <strong>github.com</strong> in your browser. Sign in or create an account.</p>
 <div class="steps">
  <div class="step"><p>Click the <strong>+</strong> menu, then choose <strong>New repository</strong>.</p></div>
  <div class="step"><p>Name it <strong>my-first-project</strong>.</p></div>
  <div class="step"><p>Choose Public if you're happy for anyone to see it. Add a README file.</p></div>
  <div class="step"><p>Click <strong>Create repository</strong>.</p></div>
 </div>
 <div class="callout"><p>Safety tip: don't publish passwords, private information, home address, or anything you want to keep private. A public repository can be seen by anyone.</p></div>
</section>

<section class="slide">
 <div class="eyebrow">07 · First checkpoint</div>
 <h2>Write a project introduction</h2>
 <p>Open <strong>README.md</strong>, click the pencil (Edit) button, and add something like this:</p>
 <div class="code"># My First Project\n\nHello! I'm learning GitHub.\n\n## Things I like\n- Gaming\n- Football\n- Programming\n\n## My goal\nBuild my first computer game!</div>
 <p style="margin-top:16px">Scroll to the commit area. Use the message <strong>“Create my first README”</strong>, then commit the changes.</p>
 <div class="bigline accent">Checkpoint saved! 📸</div>
</section>

<section class="slide">
 <div class="eyebrow">08 · Make another change</div>
 <h2>Build the history</h2>
 <p>Edit the README again. Add a new section:</p>
 <div class="code">## My favourite games\n- Minecraft\n- Roblox\n- Rocket League</div>
 <p>Commit with the message <strong>“Add my favourite games”</strong>.</p>
 <div class="flow">
  <div class="node">Commit 1<br><small>First README</small></div><div class="arrow">→</div>
  <div class="node">Commit 2<br><small>Favourite games</small></div>
 </div>
 <p>Open the repository's commit history. You can see the checkpoints and inspect what changed.</p>
</section>

<section class="slide">
 <div class="eyebrow">09 · Experiment safely</div>
 <h2>Try a new branch</h2>
 <div class="split">
  <div>
   <p>Imagine the main version is your game's stable version. You want to test a new character.</p>
   <ul><li>Keep <strong>main</strong> as it is.</li><li>Create a branch named <strong>add-a-character</strong>.</li><li>Edit the README on that branch.</li><li>Commit your change there.</li></ul>
  </div>
  <div class="card">
   <h3>Simple branch picture</h3>
   <div class="flow" style="flex-direction:column;align-items:flex-start">
    <div class="node">main ───────────────●</div>
    <div class="node" style="border-color:var(--mint)">new branch ───●──●</div>
   </div>
   <p style="font-size:15px">Your experiment happens on its own branch. Main stays unchanged until you merge.</p>
  </div>
 </div>
</section>

<section class="slide">
 <div class="eyebrow">10 · Ask to combine the work</div>
 <h2>Pull Request → Merge</h2>
 <div class="steps">
  <div class="step"><p>Open the <strong>Pull requests</strong> tab and choose <strong>New pull request</strong>.</p></div>
  <div class="step"><p>Compare your feature branch with <strong>main</strong>.</p></div>
  <div class="step"><p>Give it a clear title, such as <strong>“Add a new game character”</strong>.</p></div>
  <div class="step"><p>Create the pull request. Review the changes, then merge if they look good.</p></div>
 </div>
 <div class="callout"><p>A Pull Request is a proposal for review — it does not merge the changes automatically.</p></div>
</section>

<section class="slide">
 <div class="eyebrow">11 · Your turn</div>
 <h2>Mini mission: dream game</h2>
 <p>Create a repository called <strong>my-dream-game</strong>. Complete the challenges:</p>
 <div class="grid">
  <div class="card"><h3>🎯 Level 1</h3><p>Write a README describing your dream game.</p></div>
  <div class="card"><h3>🌿 Level 2</h3><p>Create a branch called <strong>new-game-character</strong>.</p></div>
  <div class="card"><h3>✍️ Level 3</h3><p>Add a character name, special power, and backstory.</p></div>
  <div class="card"><h3>🚀 Level 4</h3><p>Commit, open a Pull Request, and merge it.</p></div>
 </div>
 <p class="yellow" style="margin-top:18px">Bonus: ask a parent or friend to review your Pull Request before merging.</p>
</section>

<section class="slide">
 <div class="eyebrow">12 · Quick knowledge check</div>
 <h2>Can you explain it back?</h2>
 <div class="steps">
  <div class="step"><p>What is a <strong>repository</strong>?</p></div>
  <div class="step"><p>What does a <strong>commit</strong> save?</p></div>
  <div class="step"><p>Why would you create a <strong>branch</strong>?</p></div>
  <div class="step"><p>What is a <strong>Pull Request</strong> for?</p></div>
  <div class="step"><p>What's the difference between <strong>Git</strong> and <strong>GitHub</strong>?</p></div>
 </div>
 <div class="callout"><p><strong>Next step:</strong> learn a few Git commands, then build a tiny website or game and publish the code on GitHub.</p></div>
</section>
</div>
<div class="footer">
 <button id="prev" aria-label="Previous slide">←</button>
 <div class="progress"><span id="bar"></span></div>
 <div class="counter" id="count">1 / 12</div>
 <span class="navhint">← → keys to navigate · F for fullscreen</span>
 <button id="next" aria-label="Next slide">→</button>
</div>
<script>
const slides=[...document.querySelectorAll('.slide')];
let current=0;
const bar=document.getElementById('bar'), count=document.getElementById('count');
function show(n){
 current=Math.max(0,Math.min(slides.length-1,n));
 slides.forEach((s,i)=>s.classList.toggle('active',i===current));
 bar.style.width=((current+1)/slides.length*100)+'%';
 count.textContent=(current+1)+' / '+slides.length;
 document.getElementById('prev').disabled=current===0;
 document.getElementById('next').disabled=current===slides.length-1;
}
document.getElementById('prev').addEventListener('click',()=>show(current-1));
document.getElementById('next').addEventListener('click',()=>show(current+1));
document.addEventListener('keydown',e=>{
 if(['ArrowRight','PageDown',' '].includes(e.key)){e.preventDefault();show(current+1)}
 if(['ArrowLeft','PageUp'].includes(e.key)){e.preventDefault();show(current-1)}
 if(e.key.toLowerCase()==='f'){
  if(!document.fullscreenElement)document.documentElement.requestFullscreen?.();
  else document.exitFullscreen?.();
 }
 if(e.key==='Home')show(0);
 if(e.key==='End')show(slides.length-1);
});
show(0);
</script>
</body>
</html>
"""
out.write_text(html, encoding="utf-8")
print(f"Created: {out} ({out.stat().st_size:,} bytes)")
