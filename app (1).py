import json
import streamlit as st
import streamlit.components.v1 as components

# ---------------------------------------------------------------------------
# THAT'S NOT FOR YOU  -  ARCADE FIGHTING EDITION (pixel-art / Y2K cut)
# A ridiculous magical-girl fighting game whose sole purpose is to determine
# whether random objects are FOR WOMEN or FOR MEN.
# Street Fighter, reimagined by a 13-year-old girl in 2004.
#
# The whole match runs client-side in one isolated HTML/JS screen. Fighters are
# rendered through a low-res canvas and upscaled nearest-neighbour, so they read
# as chunky 16-bit sprites; CRT scanlines sit over the whole cabinet.
# ---------------------------------------------------------------------------

st.set_page_config(page_title="THAT'S NOT FOR YOU", page_icon=":sparkles:", layout="wide")

st.markdown(
    '''<style>
    #MainMenu, header, footer {visibility:hidden;}
    .block-container {padding:0.4rem 0.6rem 0; max-width:960px;}
    .stApp {background: linear-gradient(135deg,#1a0833 0%, #3a1466 50%, #1a0833 100%);}
    iframe {border:none;}
    </style>''',
    unsafe_allow_html=True,
)

# ---------------------------------------------------------------------------
# The Rulings (110+ official rulings)  -  UNCHANGED. Do not rewrite.
# verdict is one of: "FOR WOMEN", "NOT FOR MEN", "FOR MEN", "CLASSIFIED"
# Comedy rule: NOT FOR MEN reasons are shady rhetorical questions.
# ---------------------------------------------------------------------------
RULINGS = [
    {"thing": "Seatbelts", "verdict": "NOT FOR MEN", "reason": "Thought you were a good driver?"},
    {"thing": "Glasses", "verdict": "NOT FOR MEN", "reason": "What do men need to see so badly?"},
    {"thing": "Coconut water", "verdict": "FOR WOMEN", "reason": "It's spiritual."},
    {"thing": "Cockroaches", "verdict": "FOR MEN", "reason": "Self-explanatory."},
    {"thing": "Leisure time", "verdict": "FOR WOMEN", "reason": "Rest is a feminine art form."},
    {"thing": "Dried grass", "verdict": "FOR MEN", "reason": "Decorative dirt."},
    {"thing": "Hydration", "verdict": "NOT FOR MEN", "reason": "What exactly were you planning to do today?"},
    {"thing": "Soup", "verdict": "FOR WOMEN", "reason": "Liquid intuition."},
    {"thing": "Cargo shorts", "verdict": "FOR MEN", "reason": "A natural habitat."},
    {"thing": "Astrology", "verdict": "FOR WOMEN", "reason": "We invented the stars."},
    {"thing": "Ladders", "verdict": "NOT FOR MEN", "reason": "Who said you could go up?"},
    {"thing": "Lip gloss", "verdict": "FOR WOMEN", "reason": "Obviously."},
    {"thing": "Grilling", "verdict": "FOR MEN", "reason": "A controlled little fire to feel in charge of."},
    {"thing": "Crying", "verdict": "FOR WOMEN", "reason": "An advanced emotional technology."},
    {"thing": "Opinions on jazz", "verdict": "NOT FOR MEN", "reason": "Did anyone ask?"},
    {"thing": "Candles", "verdict": "FOR WOMEN", "reason": "Tiny altars."},
    {"thing": "Fantasy football", "verdict": "FOR MEN", "reason": "A spreadsheet that loves them back."},
    {"thing": "Forks", "verdict": "NOT FOR MEN", "reason": "Were you taught manners or not?"},
    {"thing": "Skincare", "verdict": "FOR WOMEN", "reason": "Maintenance of the temple."},
    {"thing": "Naps", "verdict": "FOR WOMEN", "reason": "We earned them."},
    {"thing": "Maps", "verdict": "NOT FOR MEN", "reason": "Why are you so confident you know the way?"},
    {"thing": "Sourdough starters", "verdict": "FOR WOMEN", "reason": "A pet you can eat."},
    {"thing": "Lawnmowers", "verdict": "FOR MEN", "reason": "A loud Saturday companion."},
    {"thing": "The aux cord", "verdict": "NOT FOR MEN", "reason": "Are you sure you should be in charge of the vibe?"},
    {"thing": "Moonlight", "verdict": "FOR WOMEN", "reason": "She's one of us."},
    {"thing": "Protein powder", "verdict": "FOR MEN", "reason": "Sand for the soul."},
    {"thing": "Thermostats", "verdict": "NOT FOR MEN", "reason": "Who told you you were cold?"},
    {"thing": "Tea", "verdict": "FOR WOMEN", "reason": "Liquid gossip."},
    {"thing": "Spreadsheets", "verdict": "CLASSIFIED", "reason": "The Institute is still deliberating."},
    {"thing": "Reverse parking", "verdict": "NOT FOR MEN", "reason": "Confident, are we?"},
    {"thing": "Embroidery", "verdict": "FOR WOMEN", "reason": "Tiny acts of devotion."},
    {"thing": "Power tools", "verdict": "FOR MEN", "reason": "Loud forgiveness machines."},
    {"thing": "The remote control", "verdict": "NOT FOR MEN", "reason": "And who appointed you?"},
    {"thing": "Perfume", "verdict": "FOR WOMEN", "reason": "Bottled mood lighting."},
    {"thing": "Beard oil", "verdict": "FOR MEN", "reason": "Furniture polish for the face."},
    {"thing": "Directions", "verdict": "NOT FOR MEN", "reason": "Lost again?"},
    {"thing": "Journaling", "verdict": "FOR WOMEN", "reason": "An ancient feminine record-keeping."},
    {"thing": "Garage shelving", "verdict": "FOR MEN", "reason": "A kingdom of unused buckets."},
    {"thing": "Group chats", "verdict": "FOR WOMEN", "reason": "The real government."},
    {"thing": "Loud sneezing", "verdict": "NOT FOR MEN", "reason": "Was that necessary?"},
    {"thing": "Brunch", "verdict": "FOR WOMEN", "reason": "A holy meal."},
    {"thing": "Riding lawnmowers", "verdict": "FOR MEN", "reason": "A throne with wheels."},
    {"thing": "Calendars", "verdict": "NOT FOR MEN", "reason": "You forgot, didn't you?"},
    {"thing": "Rose quartz", "verdict": "FOR WOMEN", "reason": "It hums for us."},
    {"thing": "Lint", "verdict": "FOR MEN", "reason": "Pocket confetti."},
    {"thing": "The thermostat war", "verdict": "FOR WOMEN", "reason": "We always win."},
    {"thing": "Standing too close", "verdict": "NOT FOR MEN", "reason": "Why so near?"},
    {"thing": "Moisturizer", "verdict": "FOR WOMEN", "reason": "Self-respect in a jar."},
    {"thing": "Energy drinks", "verdict": "FOR MEN", "reason": "Caffeinated optimism."},
    {"thing": "Whistling", "verdict": "NOT FOR MEN", "reason": "Who taught you that?"},
    {"thing": "Flowers", "verdict": "FOR WOMEN", "reason": "Nature's compliments."},
    {"thing": "Folding chairs", "verdict": "FOR MEN", "reason": "Portable patience."},
    {"thing": "The last word", "verdict": "NOT FOR MEN", "reason": "Are you finished?"},
    {"thing": "Silk", "verdict": "FOR WOMEN", "reason": "Spun specifically for us."},
    {"thing": "Sawdust", "verdict": "FOR MEN", "reason": "Triumphant mess."},
    {"thing": "Mirrors", "verdict": "FOR WOMEN", "reason": "They tell the truth, kindly."},
    {"thing": "Mansplaining", "verdict": "NOT FOR MEN", "reason": "Did we ask you to elaborate?"},
    {"thing": "Honey", "verdict": "FOR WOMEN", "reason": "Sweetness, archived."},
    {"thing": "Remote starters", "verdict": "FOR MEN", "reason": "Theatrical convenience."},
    {"thing": "The thermostat (again)", "verdict": "NOT FOR MEN", "reason": "Cold? Already?"},
    {"thing": "Lavender", "verdict": "FOR WOMEN", "reason": "She calms only us."},
    {"thing": "Toolboxes", "verdict": "FOR MEN", "reason": "A box of intentions."},
    {"thing": "Stargazing", "verdict": "FOR WOMEN", "reason": "Returning home, basically."},
    {"thing": "Loud opinions on coffee", "verdict": "NOT FOR MEN", "reason": "Is this a TED talk?"},
    {"thing": "Bubble baths", "verdict": "FOR WOMEN", "reason": "Ritual cleansing."},
    {"thing": "Gravel", "verdict": "FOR MEN", "reason": "Decorative crunch."},
    {"thing": "Eye contact while parking", "verdict": "NOT FOR MEN", "reason": "Nervous?"},
    {"thing": "Hair clips", "verdict": "FOR WOMEN", "reason": "Tiny tiaras."},
    {"thing": "Antlers on the wall", "verdict": "FOR MEN", "reason": "A diploma in vibes."},
    {"thing": "The phrase 'well actually'", "verdict": "NOT FOR MEN", "reason": "Actually what?"},
    {"thing": "Peonies", "verdict": "FOR WOMEN", "reason": "They bloom on command for us."},
    {"thing": "Stadium chairs", "verdict": "FOR MEN", "reason": "Loyalty with a cupholder."},
    {"thing": "The fast lane", "verdict": "NOT FOR MEN", "reason": "Somewhere to be?"},
    {"thing": "Matcha", "verdict": "FOR WOMEN", "reason": "Green meditation."},
    {"thing": "Beef jerky", "verdict": "FOR MEN", "reason": "Chewable triumph."},
    {"thing": "Wide-leg trousers", "verdict": "FOR WOMEN", "reason": "Architecture."},
    {"thing": "Air horns", "verdict": "NOT FOR MEN", "reason": "Was that an emergency?"},
    {"thing": "Velvet", "verdict": "FOR WOMEN", "reason": "Touchable luxury."},
    {"thing": "Bottle openers shaped like fish", "verdict": "FOR MEN", "reason": "A personality, allegedly."},
    {"thing": "The phrase 'trust me'", "verdict": "NOT FOR MEN", "reason": "Why would we?"},
    {"thing": "Fairy lights", "verdict": "FOR WOMEN", "reason": "Captured stars."},
    {"thing": "Monster trucks", "verdict": "FOR MEN", "reason": "Big wheel, big feelings."},
    {"thing": "Heated debates at parties", "verdict": "NOT FOR MEN", "reason": "Is this fun for you?"},
    {"thing": "Champagne", "verdict": "FOR WOMEN", "reason": "Bubbles of victory."},
    {"thing": "Socket sets", "verdict": "FOR MEN", "reason": "A jigsaw of pride."},
    {"thing": "The phone at dinner", "verdict": "NOT FOR MEN", "reason": "Something more important?"},
    {"thing": "Pearls", "verdict": "FOR WOMEN", "reason": "The ocean's apology."},
    {"thing": "Camo print", "verdict": "FOR MEN", "reason": "Hiding from no one."},
    {"thing": "Unsolicited feedback", "verdict": "NOT FOR MEN", "reason": "Did a request go out?"},
    {"thing": "Croissants", "verdict": "FOR WOMEN", "reason": "Edible architecture, for us."},
    {"thing": "Truck nuts", "verdict": "FOR MEN", "reason": "No notes. None."},
    {"thing": "The thermostat (one more time)", "verdict": "NOT FOR MEN", "reason": "Still cold?"},
    {"thing": "Sea glass", "verdict": "FOR WOMEN", "reason": "Polished by the moon."},
    {"thing": "Tailgating", "verdict": "FOR MEN", "reason": "A parking lot picnic with rage."},
    {"thing": "The middle armrest", "verdict": "NOT FOR MEN", "reason": "Both of them?"},
    {"thing": "Iced coffee in winter", "verdict": "FOR WOMEN", "reason": "We are unbothered."},
    {"thing": "Leaf blowers", "verdict": "FOR MEN", "reason": "Yelling, but make it lawn care."},
    {"thing": "The phrase 'calm down'", "verdict": "NOT FOR MEN", "reason": "Excuse me?"},
    {"thing": "Linen", "verdict": "FOR WOMEN", "reason": "Effortless on purpose."},
    {"thing": "Fishing hats", "verdict": "FOR MEN", "reason": "A hobby worn proudly."},
    {"thing": "Cutting in line", "verdict": "NOT FOR MEN", "reason": "Were you raised in a barn?"},
    {"thing": "Cherry blossoms", "verdict": "FOR WOMEN", "reason": "They time their bloom for us."},
    {"thing": "WD-40", "verdict": "FOR MEN", "reason": "A spray-can solution to feelings."},
    {"thing": "Explaining the movie", "verdict": "NOT FOR MEN", "reason": "We watched it too?"},
    {"thing": "Rosewater", "verdict": "FOR WOMEN", "reason": "Liquid serenity."},
    {"thing": "Foam fingers", "verdict": "FOR MEN", "reason": "A giant felt opinion."},
    {"thing": "Reclining the seat fully", "verdict": "NOT FOR MEN", "reason": "Comfortable back there?"},
    {"thing": "Pilates", "verdict": "FOR WOMEN", "reason": "Quiet power."},
    {"thing": "Garage band drum kits", "verdict": "FOR MEN", "reason": "A noisy dream deferred."},
    {"thing": "The grand entrance", "verdict": "FOR WOMEN", "reason": "We arrive, the room adjusts."},
    {"thing": "Honking at nothing", "verdict": "NOT FOR MEN", "reason": "Who was that for?"},
    {"thing": "Moon phases", "verdict": "FOR WOMEN", "reason": "We keep the schedule."},
    {"thing": "Toothpick chewing", "verdict": "FOR MEN", "reason": "A toothpick, a personality."},
    {"thing": "The last slice", "verdict": "NOT FOR MEN", "reason": "Were you going to ask?"},
    {"thing": "Silk pillowcases", "verdict": "FOR WOMEN", "reason": "We deserve a soft landing."},
    {"thing": "Megaphones", "verdict": "FOR MEN", "reason": "Volume as a hobby."},
]

# ---------------------------------------------------------------------------
# BONUS RULINGS  -  additive only; the originals above are untouched.
# Hidden inside-joke Benito references that surface at random during the fight.
# ---------------------------------------------------------------------------
BONUS_RULINGS = [
    {"thing": "Benito", "verdict": "FOR WOMEN", "reason": "He's one of the girls."},
    {"thing": "Un Verano Sin Ti", "verdict": "FOR WOMEN", "reason": "Required reading."},
    {"thing": "Perreo", "verdict": "FOR WOMEN", "reason": "A feminine science."},
    {"thing": "Baggy jeans", "verdict": "FOR WOMEN", "reason": "We know who they're really for."},
]

ALL_RULINGS = RULINGS + BONUS_RULINGS


GAME_TEMPLATE = r"""<meta charset="utf-8">
<style>
@import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&family=Comic+Neue:ital,wght@0,400;0,700;1,700&display=swap');
* { box-sizing: border-box; margin: 0; padding: 0; }
html, body { background: transparent; overflow: hidden; }

#cabinet {
  position: relative; width: 100%; max-width: 900px; height: 700px; margin: 0 auto;
  border-radius: 14px; overflow: hidden;
  border: 6px solid #1a0833;
  box-shadow: 0 0 0 4px #ff8fdf, 0 0 0 9px #1a0833, 0 0 40px rgba(123,47,247,.7), inset 0 0 70px rgba(10,0,30,.7);
  font-family: 'Press Start 2P', monospace; image-rendering: pixelated; user-select: none;
  background: linear-gradient(180deg, #ff5fc0 0%, #b02fc0 30%, #6a1f9a 60%, #2a0a4d 100%);
}
#cabinet::before { content:""; position:absolute; inset:0; pointer-events:none; opacity:.85;
  background-image:
    radial-gradient(2px 2px at 12% 16%, #fff, transparent), radial-gradient(2px 2px at 28% 8%, #ffd0ef, transparent),
    radial-gradient(2px 2px at 47% 20%, #fff, transparent), radial-gradient(2px 2px at 68% 9%, #fff0fb, transparent),
    radial-gradient(2px 2px at 82% 24%, #fff, transparent), radial-gradient(2px 2px at 92% 13%, #ffd0ef, transparent),
    radial-gradient(2px 2px at 58% 5%, #fff, transparent);
  animation: twinkle 2s steps(2) infinite alternate; }
@keyframes twinkle { from{opacity:.4} to{opacity:.95} }

/* CRT scanlines + vignette = arcade screen rawness */
#crt { position:absolute; inset:0; z-index:14; pointer-events:none;
  background: repeating-linear-gradient(0deg, rgba(0,0,0,.22) 0 1px, transparent 1px 3px); mix-blend-mode:multiply; }
#crt::after { content:""; position:absolute; inset:0;
  background: radial-gradient(ellipse at 50% 48%, transparent 52%, rgba(10,0,30,.6) 100%); }
#crt::before { content:""; position:absolute; inset:0; background:rgba(255,255,255,.025);
  animation: flick .12s steps(2) infinite; }
@keyframes flick { 50%{opacity:.4} }

/* pixel sprites */
.fighter canvas, .portrait canvas, #victorySvg canvas { image-rendering: pixelated; image-rendering: crisp-edges; display:block; }
.fighter canvas { width:100%; height:auto; }
.portrait canvas { width:100%; height:100%; }
#victorySvg canvas { width:100%; height:auto; margin:0 auto; }

/* ===== HUD ===== */
#hud { position:relative; z-index:6; display:flex; align-items:flex-start; justify-content:space-between; gap:8px; padding:10px 12px 4px; }
.bar-wrap { flex:1; display:flex; flex-direction:column; }
.bar-top { display:flex; align-items:center; gap:6px; margin-bottom:3px; }
.bar-wrap.right .bar-top { flex-direction:row-reverse; }
.portrait { width:36px; height:36px; border:2px solid #1a0833; background:#2a0a4d; overflow:hidden; flex:none;
  box-shadow: 0 0 0 2px #fff, 3px 3px 0 rgba(0,0,0,.4); }
.pname { font-size:9px; color:#fff; text-shadow:2px 2px 0 #1a0833; letter-spacing:1px; }
.bar-wrap.right .pname { margin-left:auto; }
.bar { position:relative; height:20px; background:#0d0420; border:3px solid #1a0833; overflow:hidden;
  box-shadow: 0 0 0 2px #fff, inset 0 0 0 1px #5a2a7a, 3px 3px 0 rgba(0,0,0,.35); transform:skewX(-12deg); }
.bar-wrap.right .bar { transform:skewX(12deg); }
.lag, .fill { position:absolute; top:0; bottom:0; left:0; width:100%; }
.lag { background:#ffe14f; transition:width .55s steps(8) .15s; }
.fill { transition:width .12s steps(4); }
.fill-w { background:linear-gradient(180deg,#ffd0ef,#ff2fa8 55%,#c1147f); }
.fill-m { background:linear-gradient(180deg,#9fe0d8,#2f72f7 55%,#1846a8); }
.bar-wrap.right .lag, .bar-wrap.right .fill { left:auto; right:0; }
.round-box { flex:none; width:84px; text-align:center; }
.round-label { font-size:8px; color:#ffd0ef; letter-spacing:3px; }
.round-num { font-size:24px; color:#fff; text-shadow:0 0 8px #ff2fa8, 3px 3px 0 #1a0833; line-height:1.5; }
.score-mini { font-size:8px; color:#ffe9fb; }

/* ===== WORD PROMPT ===== */
#prompt { position:relative; z-index:6; text-align:center; margin:4px 12px 0; padding:9px 6px;
  background:linear-gradient(180deg, rgba(13,4,32,.92), rgba(90,30,140,.7)); border:3px solid #1a0833;
  box-shadow:0 0 0 2px #ff8fdf, 4px 4px 0 rgba(0,0,0,.4); }
.prompt-label { font-size:9px; color:#ffd0ef; letter-spacing:6px; }
.prompt-word { display:block; font-size:24px; color:#fff; line-height:1.4; margin-top:6px;
  text-shadow:0 0 10px #ff2fa8, 3px 3px 0 #c1147f, 4px 4px 0 #1a0833; word-break:break-word; }
@media (max-width:560px){ .prompt-word{ font-size:18px; } }

/* ===== STAGE ===== */
#stage { position:absolute; left:0; right:0; top:130px; bottom:128px; z-index:4; overflow:hidden; }
.floor { position:absolute; left:-10%; right:-10%; bottom:0; height:42%;
  background: repeating-linear-gradient(90deg, rgba(255,143,223,.3) 0 3px, transparent 3px 44px),
              linear-gradient(180deg,#7a1fc0 0%,#ff5fc0 100%);
  transform: perspective(360px) rotateX(60deg); transform-origin:bottom center; box-shadow:0 -2px 30px rgba(255,47,168,.5); }
.floor::after { content:""; position:absolute; inset:0; background: repeating-linear-gradient(0deg, rgba(255,255,255,.22) 0 3px, transparent 3px 44px); }
.stage-glow { position:absolute; left:50%; bottom:6%; width:62%; height:30%; transform:translateX(-50%); border-radius:50%;
  background:radial-gradient(ellipse, rgba(255,210,239,.45), transparent 70%); pointer-events:none; }
.fighter { position:absolute; bottom:3%; width:34%; max-width:250px; z-index:5; filter: drop-shadow(4px 6px 0 rgba(10,0,30,.55)); }
#heroine { left:1%; transform-origin:bottom center; animation:bobL 1.6s steps(3) infinite alternate; }
#triathlete { right:1%; transform-origin:bottom center; animation:bobR 1.6s steps(3) infinite alternate; }
@keyframes bobL { from{transform:translateY(0) rotate(-1deg);} to{transform:translateY(-6px) rotate(-2deg);} }
@keyframes bobR { from{transform:translateY(0) rotate(1deg);} to{transform:translateY(-5px) rotate(2deg);} }
.lungeL { animation:lungeL .5s steps(4) !important; }
@keyframes lungeL { 0%{transform:translateX(0);} 40%{transform:translateX(42px) scale(1.08);} 100%{transform:translateX(0);} }
.lungeR { animation:lungeR .5s steps(4) !important; }
@keyframes lungeR { 0%{transform:translateX(0);} 40%{transform:translateX(-38px) scale(1.06);} 100%{transform:translateX(0);} }
.hitL { animation:hitL .5s steps(3) !important; }
@keyframes hitL { 0%{transform:translateX(0);} 20%{transform:translateX(-18px) rotate(-7deg);} 45%{transform:translateX(11px) rotate(4deg);} 70%{transform:translateX(-7px);} 100%{transform:translateX(0);} }
.hitR { animation:hitR .5s steps(3) !important; }
@keyframes hitR { 0%{transform:translateX(0);} 20%{transform:translateX(20px) rotate(9deg);} 45%{transform:translateX(-12px) rotate(-5deg);} 70%{transform:translateX(7px);} 100%{transform:translateX(0);} }
.fighter.flash canvas, .fighter.flash svg { animation:flashWhite .4s steps(2); }
@keyframes flashWhite { 0%,100%{filter:none;} 40%{filter:brightness(4) saturate(.1);} }
.vs-badge { position:absolute; left:50%; top:14%; transform:translateX(-50%); font-size:28px; color:#fff; z-index:6;
  text-shadow:0 0 12px #ff2fa8, 4px 4px 0 #1a0833, -2px -2px 0 #ff8fdf; animation:vspulse 1.2s steps(2) infinite; }
@keyframes vspulse { 0%,100%{transform:translateX(-50%) scale(1);} 50%{transform:translateX(-50%) scale(1.16);} }

/* projectile = the WORD flying */
#projectile { position:absolute; z-index:8; left:24%; top:36%; font-size:14px; color:#1a0833; padding:6px 11px;
  background:linear-gradient(180deg,#fff,#ffd0ef); border:3px solid #1a0833;
  box-shadow:0 0 0 2px #ff2fa8, 0 0 18px #ff79d2; opacity:0; pointer-events:none; white-space:nowrap; max-width:54%;
  overflow:hidden; text-overflow:ellipsis; }
#projectile.fly { animation:fly .5s steps(8) forwards; }
@keyframes fly { 0%{opacity:0; transform:translateX(0) scale(.4) rotate(0);} 12%{opacity:1; transform:translateX(20px) scale(1.1) rotate(90deg);} 100%{opacity:1; transform:translateX(var(--travel,420px)) scale(.85) rotate(540deg);} }
#projectile.flyBack { animation:flyBack .5s steps(8) forwards; }
@keyframes flyBack { 0%{opacity:0; transform:translateX(0) scale(.4);} 12%{opacity:1; transform:translateX(-16px) scale(1.05);} 100%{opacity:1; transform:translateX(calc(var(--travel,420px)*-1)) scale(.85) rotate(-480deg);} }

#impact { position:absolute; inset:0; z-index:7; pointer-events:none; opacity:0;
  background:radial-gradient(circle at var(--ix,75%) var(--iy,45%), rgba(255,255,255,.95), rgba(255,47,168,.55) 22%, transparent 52%); }
#impact.boom { animation:boom .4s steps(3); }
@keyframes boom { 0%{opacity:0; transform:scale(.6);} 30%{opacity:1; transform:scale(1.1);} 100%{opacity:0; transform:scale(1.35);} }
.shake { animation:shakeStage .4s steps(2); }
@keyframes shakeStage { 0%,100%{transform:translate(0,0);} 25%{transform:translate(-7px,4px);} 50%{transform:translate(8px,-4px);} 75%{transform:translate(-5px,2px);} }

.floater { position:absolute; z-index:9; pointer-events:none; text-align:center; left:64%; top:26%; transform:translateX(-50%); animation:floatUp 2s steps(12) forwards; }
.floater .big { font-size:20px; color:#fff; text-shadow:0 0 10px #ff2fa8, 3px 3px 0 #1a0833; }
.floater .dmg { display:block; font-size:26px; margin-top:3px; color:#ffe14f; text-shadow:3px 3px 0 #8a2c00, 0 0 10px #ffa800; }
.floater.crit .big { color:#fff; text-shadow:0 0 14px #ff2fa8, 3px 3px 0 #1a0833; }
.floater.miss .big { color:#9fd0ff; text-shadow:3px 3px 0 #1846a8; }
@keyframes floatUp { 0%{opacity:0; transform:translate(-50%,12px) scale(.5);} 15%{opacity:1; transform:translate(-50%,-6px) scale(1.2);} 80%{opacity:1; transform:translate(-50%,-30px) scale(1);} 100%{opacity:0; transform:translate(-50%,-52px) scale(.9);} }

#combo { position:absolute; z-index:9; left:50%; top:4%; transform:translateX(-50%) scale(0); font-size:14px; color:#fff;
  padding:7px 13px; background:linear-gradient(180deg,#ff79d2,#7b2ff7); border:3px solid #fff; box-shadow:3px 3px 0 #1a0833; }
#combo.show { animation:comboPop 1.2s steps(4); }
@keyframes comboPop { 0%{transform:translateX(-50%) scale(0);} 35%{transform:translateX(-50%) scale(1.35);} 70%{transform:translateX(-50%) scale(1);} 100%{transform:translateX(-50%) scale(1); opacity:0;} }

/* verdict + reason caption (bigger, lingers) */
#reasonPop { position:absolute; z-index:9; left:50%; bottom:5%; transform:translateX(-50%) translateY(16px); width:90%;
  text-align:center; opacity:0; transition:all .25s steps(3); }
#reasonPop.show { opacity:1; transform:translateX(-50%) translateY(0); }
.verdict-chip { display:inline-block; font-size:14px; padding:7px 16px; border:3px solid #1a0833; margin-bottom:7px; box-shadow:3px 3px 0 rgba(0,0,0,.4); }
.v-women { background:#ffd0ef; color:#c1147f; } .v-notmen { background:#e3d2ff; color:#7b2ff7; }
.v-men { background:#d6ecff; color:#1846a8; } .v-classified { background:#ffe14f; color:#8a2c00; }
.reason-text { font-family:'Comic Neue', cursive; font-style:italic; font-weight:700; font-size:19px; color:#fff;
  text-shadow:2px 2px 0 #1a0833; line-height:1.35; }

#alert { position:absolute; inset:0; z-index:8; pointer-events:none; opacity:0; }
#alert.on { animation:alertFlash .35s steps(2) 6; }
@keyframes alertFlash { 0%{opacity:0; box-shadow:inset 0 0 0 0 #ff2d2d;} 50%{opacity:1; box-shadow:inset 0 0 90px 20px rgba(255,45,45,.75);} 100%{opacity:0;} }

/* ===== APPEAL ===== */
#btnAppeal { position:absolute; z-index:9; left:50%; bottom:100px; transform:translateX(-50%);
  font-family:'Comic Neue', cursive; font-weight:700; font-size:13px; color:#ffd0ef; cursor:pointer;
  background:rgba(13,4,32,.7); border:2px dashed #ff8fdf; padding:6px 14px; border-radius:4px; display:none; }
#btnAppeal.show { display:block; }
#btnAppeal:hover { color:#fff; }
#denied { position:absolute; z-index:13; left:50%; top:42%; transform:translate(-50%,-50%) rotate(-16deg) scale(0);
  font-family:'Press Start 2P', monospace; font-size:30px; color:#ff2d2d; border:5px solid #ff2d2d; padding:12px 18px;
  text-shadow:2px 2px 0 #1a0833; box-shadow:0 0 0 3px #1a0833; pointer-events:none; }
#denied.show { animation:stamp 1.6s steps(3) forwards; }
@keyframes stamp { 0%{transform:translate(-50%,-50%) rotate(-16deg) scale(2.4); opacity:0;} 18%{transform:translate(-50%,-50%) rotate(-16deg) scale(1); opacity:1;} 78%{opacity:1;} 100%{opacity:0;} }

/* ===== CONTROLS ===== */
#controls { position:absolute; left:0; right:0; bottom:26px; z-index:7; display:flex; gap:10px; padding:0 12px; }
.choice { flex:1; font-family:'Press Start 2P', monospace; font-size:15px; color:#fff; padding:16px 8px;
  border:3px solid #1a0833; cursor:pointer; line-height:1.5; transition:transform .05s; box-shadow:0 0 0 2px #fff, 5px 5px 0 rgba(0,0,0,.45); }
.choice:active { transform:translate(3px,3px); box-shadow:0 0 0 2px #fff, 2px 2px 0 rgba(0,0,0,.45); }
.choice:disabled { filter:grayscale(.55) brightness(.75); cursor:default; }
#btnWomen { background:linear-gradient(180deg,#ffb3e6 0%,#ff2fa8 51%,#ff7fd0 100%); }
#btnMen { background:linear-gradient(180deg,#a9d4ff 0%,#1f63e0 51%,#7fb0ff 100%); }
#btnWomen:hover, #btnMen:hover { filter:brightness(1.08); }

/* ===== REGGAETON TICKER ===== */
#marquee { position:absolute; left:0; right:0; bottom:0; z-index:7; height:22px; overflow:hidden; white-space:nowrap;
  background:#0d0420; border-top:2px solid #ff8fdf; }
#marquee span { display:inline-block; padding-left:100%; animation:scroll 26s linear infinite;
  font-family:'Comic Neue', cursive; font-weight:700; color:#ffd0ef; font-size:13px; line-height:22px; }
@keyframes scroll { to { transform:translateX(-100%); } }

/* ===== ANNOUNCER / VICTORY ===== */
#announce { position:absolute; inset:0; z-index:11; display:flex; align-items:center; justify-content:center; pointer-events:none; }
#announce .txt { font-size:44px; color:#fff; opacity:0; text-shadow:0 0 18px #ff2fa8, 5px 5px 0 #1a0833, -2px -2px 0 #ff8fdf; }
#announce.show .txt { animation:slam 1s steps(4); }
@keyframes slam { 0%{opacity:0; transform:scale(3.2) rotate(-8deg);} 30%{opacity:1; transform:scale(1) rotate(-4deg);} 80%{opacity:1; transform:scale(1) rotate(-4deg);} 100%{opacity:0; transform:scale(1.1);} }

#victory { position:absolute; inset:0; z-index:12; display:none; flex-direction:column; align-items:center; justify-content:center;
  text-align:center; padding:18px; background:radial-gradient(ellipse at 50% 30%, rgba(123,47,247,.5), rgba(8,0,24,.94)); }
#victory.show { display:flex; }
#victory .vsvg { width:48%; max-width:300px; margin-bottom:6px; }
#victory .vsvg canvas { animation:vbounce 1.2s steps(3) infinite alternate; }
@keyframes vbounce { from{transform:translateY(0) scale(1);} to{transform:translateY(-10px) scale(1.05);} }
#victory .vtitle { font-size:22px; color:#fff; line-height:1.6; text-shadow:0 0 14px #ff2fa8, 4px 4px 0 #1a0833; }
#victory .vsub { font-family:'Comic Neue', cursive; font-style:italic; font-weight:700; font-size:16px; color:#ffd0ef; margin-top:10px; max-width:470px; }
#playAgain { margin-top:16px; font-family:'Press Start 2P', monospace; font-size:14px; color:#fff; padding:14px 22px;
  border:3px solid #1a0833; cursor:pointer; background:linear-gradient(180deg,#ffb3e6,#ff2fa8 51%,#ff7fd0); box-shadow:0 0 0 2px #fff, 5px 5px 0 rgba(0,0,0,.45); }
#playAgain:active { transform:translate(3px,3px); }
.vburst { position:absolute; inset:0; pointer-events:none;
  background-image: radial-gradient(3px 3px at 20% 30%, #fff, transparent), radial-gradient(3px 3px at 80% 25%, #ffd0ef, transparent),
    radial-gradient(3px 3px at 35% 70%, #fff, transparent), radial-gradient(3px 3px at 65% 65%, #fff0fb, transparent),
    radial-gradient(3px 3px at 50% 15%, #fff, transparent); animation:twinkle .8s steps(2) infinite alternate; }
#foot { position:absolute; z-index:13; left:0; right:0; bottom:3px; text-align:center; font-family:'Comic Neue', cursive; font-size:9px; color:rgba(255,224,251,.85); display:none; }
#victory.show ~ #foot { display:block; }
</style>

<div id="cabinet">
  <div id="hud">
    <div class="bar-wrap left">
      <div class="bar-top"><div class="portrait" id="portraitW"></div><div class="pname">TEAM WOMEN</div></div>
      <div class="bar"><div class="lag lag-w" id="lagW"></div><div class="fill fill-w" id="fillW"></div></div>
    </div>
    <div class="round-box"><div class="round-label">ROUND</div><div class="round-num" id="roundNum">1</div><div class="score-mini" id="scoreMini">SCORE 0</div></div>
    <div class="bar-wrap right">
      <div class="bar-top"><div class="portrait" id="portraitM"></div><div class="pname">TEAM MEN</div></div>
      <div class="bar"><div class="lag lag-m" id="lagM"></div><div class="fill fill-m" id="fillM"></div></div>
    </div>
  </div>

  <div id="prompt"><span class="prompt-label">W O R D</span><span class="prompt-word" id="word">&nbsp;</span></div>

  <div id="stage">
    <div class="floor"></div><div class="stage-glow"></div>
    <div class="vs-badge">VS</div>
    <div class="fighter" id="heroine"></div>
    <div class="fighter" id="triathlete"></div>
    <div id="projectile"></div><div id="impact"></div><div id="combo"></div>
    <div id="reasonPop"></div><div id="alert"></div>
  </div>

  <button id="btnAppeal">appeal this ruling</button>
  <div id="denied">APPEAL DENIED</div>

  <div id="controls">
    <button class="choice" id="btnWomen">FOR<br>WOMEN</button>
    <button class="choice" id="btnMen">FOR<br>MEN</button>
  </div>

  <div id="marquee"><span id="marqueeText"></span></div>

  <div id="announce"><div class="txt" id="announceTxt"></div></div>
  <div id="victory">
    <div class="vburst"></div>
    <div class="vsvg" id="victorySvg"></div>
    <div class="vtitle" id="victoryTitle"></div>
    <div class="vsub" id="victorySub"></div>
    <button id="playAgain">&#9733; PLAY AGAIN &#9733;</button>
  </div>
  <div id="foot">Powered by the International Institute of That&rsquo;s Not For You&trade;</div>
  <div id="crt"></div>
</div>

<script>
const RULINGS = __RULINGS_JSON__;
const BOOKS = ["Invisible Women", "The Second Sex", "Men Explain Things To Me"];
const MARQUEE = "\u2665 welcome 2 the institute \u2665 best viewed in 800\u00d7600 \u2665 sign my guestbook \u2665 yo perreo sola \u2665 un verano sin informaci\u00f3n \u2665 \uD83D\uDC30 conejo approved \uD83D\uDC30 \u2665 no boys allowed (jk\u2026 unless?) \u2665 ur visitor #000127 \u2665 dale \u2665 made with luv + glitter \u2665 ";

/* ===== PIXEL-ART CHARACTERS (bold blocks + hard outlines so they survive downscaling) ===== */
const OUT = '#1a0833';

function heroineStance() {
  return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 320">
  <ellipse cx="100" cy="310" rx="60" ry="10" fill="rgba(8,0,24,.5)"/>
  <!-- fairy wings (Winx) -->
  <path d="M70 150 Q22 120 26 178 Q40 206 78 188 Z" fill="#ff9fe0" stroke="${OUT}" stroke-width="4" opacity=".9"/>
  <path d="M130 150 Q178 120 174 178 Q160 206 122 188 Z" fill="#c98bff" stroke="${OUT}" stroke-width="4" opacity=".9"/>
  <!-- HUGE Bratz/Winx hair behind -->
  <path d="M52 70 Q18 150 44 250 Q60 300 84 300 L84 120 Z" fill="#5a3320" stroke="${OUT}" stroke-width="4"/>
  <path d="M148 70 Q182 150 156 250 Q140 300 116 300 L116 120 Z" fill="#5a3320" stroke="${OUT}" stroke-width="4"/>
  <!-- legs -->
  <rect x="84" y="206" width="14" height="58" fill="#f7d3b0" stroke="${OUT}" stroke-width="4"/>
  <rect x="102" y="206" width="14" height="58" fill="#f7d3b0" stroke="${OUT}" stroke-width="4"/>
  <!-- chunky platform boots -->
  <rect x="78" y="256" width="24" height="42" fill="#e0249a" stroke="${OUT}" stroke-width="4"/>
  <rect x="98" y="256" width="24" height="42" fill="#e0249a" stroke="${OUT}" stroke-width="4"/>
  <rect x="74" y="288" width="32" height="14" fill="#fff" stroke="${OUT}" stroke-width="4"/>
  <rect x="94" y="288" width="32" height="14" fill="#fff" stroke="${OUT}" stroke-width="4"/>
  <!-- mini skirt + exaggerated hips -->
  <path d="M70 176 Q100 166 130 176 L138 214 Q100 230 62 214 Z" fill="#ff2fa8" stroke="${OUT}" stroke-width="4"/>
  <!-- tiny torso / crop top -->
  <path d="M80 132 Q100 124 120 132 L116 176 Q100 184 84 176 Z" fill="#9b3cff" stroke="${OUT}" stroke-width="4"/>
  <rect x="90" y="146" width="4" height="4" fill="#fff"/><rect x="104" y="156" width="4" height="4" fill="#fff"/>
  <!-- belt star -->
  <path d="M100 176 l4 8 9 1 -6 6 1.5 9 -8.5-4.5 -8.5 4.5 1.5-9 -6-6 9-1z" fill="#ffe14f" stroke="${OUT}" stroke-width="2"/>
  <!-- back arm guard -->
  <path d="M120 138 Q150 130 150 100" stroke="#f7d3b0" stroke-width="15" fill="none" stroke-linecap="round"/>
  <path d="M120 138 Q150 130 150 100" stroke="${OUT}" stroke-width="4" fill="none" stroke-linecap="round" opacity=".25"/>
  <!-- front fist forward -->
  <path d="M80 142 Q48 150 38 178" stroke="#f7d3b0" stroke-width="15" fill="none" stroke-linecap="round"/>
  <circle cx="36" cy="180" r="13" fill="#f7d3b0" stroke="${OUT}" stroke-width="4"/>
  <!-- BIG doll head -->
  <rect x="92" y="116" width="16" height="14" fill="#f7d3b0"/>
  <circle cx="100" cy="86" r="34" fill="#f9d8b8" stroke="${OUT}" stroke-width="4"/>
  <!-- voluminous fringe -->
  <path d="M64 86 Q60 40 100 38 Q140 40 136 86 Q120 60 100 60 Q80 60 64 86 Z" fill="#6b3d24" stroke="${OUT}" stroke-width="4"/>
  <!-- lilac eyeshadow -->
  <path d="M78 78 Q88 68 99 76 Z" fill="#c98bff"/><path d="M101 76 Q112 68 122 78 Z" fill="#c98bff"/>
  <!-- HUGE brown almond eyes -->
  <ellipse cx="87" cy="86" rx="11" ry="14" fill="#fff" stroke="${OUT}" stroke-width="3"/>
  <ellipse cx="113" cy="86" rx="11" ry="14" fill="#fff" stroke="${OUT}" stroke-width="3"/>
  <circle cx="87" cy="88" r="7.5" fill="#7a4a24"/><circle cx="113" cy="88" r="7.5" fill="#7a4a24"/>
  <circle cx="87" cy="88" r="3.5" fill="#2a1607"/><circle cx="113" cy="88" r="3.5" fill="#2a1607"/>
  <rect x="89" y="83" width="4" height="4" fill="#fff"/><rect x="115" y="83" width="4" height="4" fill="#fff"/>
  <!-- dramatic lashes -->
  <path d="M75 76 l-7 -5 M77 73 l-7 -3 M79 71 l-6 -1" stroke="${OUT}" stroke-width="2.6" stroke-linecap="round"/>
  <path d="M125 76 l7 -5 M123 73 l7 -3 M121 71 l6 -1" stroke="${OUT}" stroke-width="2.6" stroke-linecap="round"/>
  <!-- blush + big glossy lips -->
  <rect x="74" y="98" width="9" height="6" fill="#ffb3d9"/><rect x="117" y="98" width="9" height="6" fill="#ffb3d9"/>
  <path d="M88 104 Q100 116 112 104 Q100 110 88 104 Z" fill="#e0249a" stroke="${OUT}" stroke-width="2"/>
  <rect x="96" y="105" width="8" height="2" fill="#fff" opacity=".8"/>
  <!-- sparkles -->
  <path d="M150 58 l3 7 7 3 -7 3 -3 7 -3-7 -7-3 7-3z" fill="#fff"/>
  <path d="M40 110 l2 6 6 2 -6 2 -2 6 -2-6 -6-2 6-2z" fill="#fff"/>
  </svg>`;
}

function heroineVictory() {
  return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 320">
  <ellipse cx="100" cy="310" rx="58" ry="9" fill="rgba(8,0,24,.45)"/>
  <path d="M64 140 Q12 100 18 168 Q34 202 80 182 Z" fill="#ff9fe0" stroke="${OUT}" stroke-width="4"/>
  <path d="M136 140 Q188 100 182 168 Q166 202 120 182 Z" fill="#c98bff" stroke="${OUT}" stroke-width="4"/>
  <path d="M52 70 Q14 160 44 256 Q60 300 84 298 L84 120 Z" fill="#5a3320" stroke="${OUT}" stroke-width="4"/>
  <path d="M148 70 Q186 160 156 256 Q140 300 116 298 L116 120 Z" fill="#5a3320" stroke="${OUT}" stroke-width="4"/>
  <rect x="84" y="210" width="14" height="54" fill="#f7d3b0" stroke="${OUT}" stroke-width="4"/>
  <rect x="102" y="210" width="14" height="54" fill="#f7d3b0" stroke="${OUT}" stroke-width="4"/>
  <rect x="78" y="256" width="24" height="42" fill="#e0249a" stroke="${OUT}" stroke-width="4"/>
  <rect x="98" y="256" width="24" height="42" fill="#e0249a" stroke="${OUT}" stroke-width="4"/>
  <rect x="74" y="288" width="32" height="14" fill="#fff" stroke="${OUT}" stroke-width="4"/>
  <rect x="94" y="288" width="32" height="14" fill="#fff" stroke="${OUT}" stroke-width="4"/>
  <path d="M70 176 Q100 166 130 176 L138 214 Q100 230 62 214 Z" fill="#ff2fa8" stroke="${OUT}" stroke-width="4"/>
  <path d="M80 132 Q100 124 120 132 L116 176 Q100 184 84 176 Z" fill="#9b3cff" stroke="${OUT}" stroke-width="4"/>
  <path d="M100 176 l4 8 9 1 -6 6 1.5 9 -8.5-4.5 -8.5 4.5 1.5-9 -6-6 9-1z" fill="#ffe14f" stroke="${OUT}" stroke-width="2"/>
  <!-- both arms thrown up -->
  <path d="M82 138 Q52 110 58 66" stroke="#f7d3b0" stroke-width="15" fill="none" stroke-linecap="round"/>
  <path d="M118 138 Q148 110 142 66" stroke="#f7d3b0" stroke-width="15" fill="none" stroke-linecap="round"/>
  <circle cx="58" cy="62" r="12" fill="#f7d3b0" stroke="${OUT}" stroke-width="4"/>
  <circle cx="142" cy="62" r="12" fill="#f7d3b0" stroke="${OUT}" stroke-width="4"/>
  <rect x="92" y="116" width="16" height="14" fill="#f7d3b0"/>
  <circle cx="100" cy="86" r="34" fill="#f9d8b8" stroke="${OUT}" stroke-width="4"/>
  <path d="M64 86 Q60 40 100 38 Q140 40 136 86 Q120 60 100 60 Q80 60 64 86 Z" fill="#6b3d24" stroke="${OUT}" stroke-width="4"/>
  <path d="M78 78 Q88 68 99 76 Z" fill="#c98bff"/><path d="M101 76 Q112 68 122 78 Z" fill="#c98bff"/>
  <ellipse cx="87" cy="86" rx="11" ry="14" fill="#fff" stroke="${OUT}" stroke-width="3"/>
  <ellipse cx="113" cy="86" rx="11" ry="14" fill="#fff" stroke="${OUT}" stroke-width="3"/>
  <circle cx="87" cy="88" r="7.5" fill="#7a4a24"/><circle cx="113" cy="88" r="7.5" fill="#7a4a24"/>
  <circle cx="87" cy="88" r="3.5" fill="#2a1607"/><circle cx="113" cy="88" r="3.5" fill="#2a1607"/>
  <rect x="89" y="83" width="4" height="4" fill="#fff"/><rect x="115" y="83" width="4" height="4" fill="#fff"/>
  <path d="M88 104 Q100 116 112 104 Q100 110 88 104 Z" fill="#e0249a" stroke="${OUT}" stroke-width="2"/>
  <path d="M40 44 l3 9 9 3 -9 3 -3 9 -3-9 -9-3 9-3z" fill="#fff"/>
  <path d="M160 60 l3 9 9 3 -9 3 -3 9 -3-9 -9-3 9-3z" fill="#ffd0ef"/>
  </svg>`;
}

function triathleteStance() {
  return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 320">
  <ellipse cx="100" cy="310" rx="54" ry="9" fill="rgba(8,0,24,.5)"/>
  <rect x="84" y="200" width="16" height="62" fill="#f2c9a6" stroke="${OUT}" stroke-width="4"/>
  <rect x="102" y="200" width="16" height="62" fill="#f2c9a6" stroke="${OUT}" stroke-width="4"/>
  <rect x="78" y="258" width="26" height="16" fill="#16c0a8" stroke="${OUT}" stroke-width="4"/>
  <rect x="98" y="258" width="26" height="16" fill="#16c0a8" stroke="${OUT}" stroke-width="4"/>
  <path d="M76 118 Q100 110 124 118 L128 204 Q100 216 72 204 Z" fill="#27406b" stroke="${OUT}" stroke-width="4"/>
  <rect x="76" y="118" width="14" height="86" fill="#16c0a8"/>
  <rect x="96" y="140" width="26" height="20" fill="#fff" stroke="${OUT}" stroke-width="3"/>
  <text x="109" y="156" font-size="13" fill="#16243f" text-anchor="middle" font-family="monospace">07</text>
  <path d="M80 126 Q50 122 44 96" stroke="#f2c9a6" stroke-width="14" fill="none" stroke-linecap="round"/>
  <circle cx="43" cy="92" r="11" fill="#f2c9a6" stroke="${OUT}" stroke-width="4"/>
  <path d="M122 126 Q152 124 154 100" stroke="#f2c9a6" stroke-width="14" fill="none" stroke-linecap="round"/>
  <circle cx="155" cy="96" r="11" fill="#f2c9a6" stroke="${OUT}" stroke-width="4"/>
  <rect x="148" y="100" width="12" height="10" fill="#0b1626" stroke="${OUT}" stroke-width="3"/>
  <rect x="92" y="100" width="16" height="14" fill="#f2c9a6"/>
  <circle cx="100" cy="84" r="28" fill="#f5d2ad" stroke="${OUT}" stroke-width="4"/>
  <!-- chunky curly dark hair -->
  <g fill="#2a1a10" stroke="${OUT}" stroke-width="3">
    <circle cx="78" cy="62" r="13"/><circle cx="96" cy="54" r="14"/><circle cx="116" cy="58" r="13"/><circle cx="126" cy="74" r="9"/><circle cx="74" cy="78" r="9"/><circle cx="106" cy="48" r="10"/>
  </g>
  <ellipse cx="90" cy="84" rx="6.5" ry="7.5" fill="#fff" stroke="${OUT}" stroke-width="2.5"/>
  <ellipse cx="110" cy="84" rx="6.5" ry="7.5" fill="#fff" stroke="${OUT}" stroke-width="2.5"/>
  <circle cx="90" cy="85" r="3.8" fill="#1f9e54"/><circle cx="110" cy="85" r="3.8" fill="#1f9e54"/>
  <circle cx="90" cy="85" r="1.8" fill="#0a2e18"/><circle cx="110" cy="85" r="1.8" fill="#0a2e18"/>
  <rect x="88" y="82" width="3" height="3" fill="#fff"/><rect x="108" y="82" width="3" height="3" fill="#fff"/>
  <path d="M82 72 Q90 64 99 71" stroke="#2a1a10" stroke-width="3" fill="none" stroke-linecap="round"/>
  <path d="M103 73 Q110 69 119 73" stroke="#2a1a10" stroke-width="3" fill="none" stroke-linecap="round"/>
  <path d="M92 98 Q100 101 108 98" stroke="#9c5a32" stroke-width="2.5" fill="none" stroke-linecap="round"/>
  <text x="138" y="62" font-size="18" fill="#ffd0ef" font-family="monospace">?</text>
  </svg>`;
}

function triathleteVictory(book) {
  return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 320">
  <ellipse cx="100" cy="300" rx="68" ry="11" fill="rgba(8,0,24,.45)"/>
  <ellipse cx="100" cy="278" rx="58" ry="14" fill="#7b2ff7" stroke="${OUT}" stroke-width="3"/>
  <path d="M52 250 Q60 234 86 240 L92 270 L48 270 Z" fill="#27406b" stroke="${OUT}" stroke-width="4"/>
  <path d="M148 250 Q140 234 114 240 L108 270 L152 270 Z" fill="#27406b" stroke="${OUT}" stroke-width="4"/>
  <circle cx="50" cy="262" r="11" fill="#f2c9a6" stroke="${OUT}" stroke-width="4"/>
  <circle cx="150" cy="262" r="11" fill="#f2c9a6" stroke="${OUT}" stroke-width="4"/>
  <path d="M74 168 Q100 160 126 168 L122 246 Q100 256 78 246 Z" fill="#27406b" stroke="${OUT}" stroke-width="4"/>
  <rect x="74" y="168" width="14" height="78" fill="#16c0a8"/>
  <path d="M82 184 Q70 206 88 216" stroke="#f2c9a6" stroke-width="13" fill="none" stroke-linecap="round"/>
  <path d="M118 184 Q130 206 112 216" stroke="#f2c9a6" stroke-width="13" fill="none" stroke-linecap="round"/>
  <path d="M70 200 L100 195 L130 200 L130 226 L100 224 L70 226 Z" fill="#fff" stroke="${OUT}" stroke-width="4"/>
  <line x1="100" y1="195" x2="100" y2="224" stroke="${OUT}" stroke-width="3"/>
  <rect x="92" y="148" width="16" height="14" fill="#f2c9a6"/>
  <circle cx="100" cy="132" r="27" fill="#f5d2ad" stroke="${OUT}" stroke-width="4"/>
  <g fill="#2a1a10" stroke="${OUT}" stroke-width="3">
    <circle cx="80" cy="114" r="12"/><circle cx="97" cy="106" r="13"/><circle cx="115" cy="110" r="12"/><circle cx="124" cy="124" r="8"/><circle cx="76" cy="126" r="8"/>
  </g>
  <path d="M88 132 q6 -5 12 0" stroke="#1f9e54" stroke-width="3" fill="none"/>
  <path d="M100 132 q6 -5 12 0" stroke="#1f9e54" stroke-width="3" fill="none"/>
  <path d="M92 146 q8 4 16 0" stroke="#9c5a32" stroke-width="2.5" fill="none" stroke-linecap="round"/>
  <path d="M134 116 l2 6 6 2 -6 2 -2 6 -2-6 -6-2 6-2z" fill="#ff6fc0"/>
  <rect x="20" y="284" width="160" height="28" fill="#fff0fb" stroke="${OUT}" stroke-width="4"/>
  <text x="100" y="302" font-size="12" fill="#9b3cff" text-anchor="middle" font-family="monospace">"${book}"</text>
  </svg>`;
}

function miniHeroine() { return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 40 40">
  <circle cx="20" cy="22" r="16" fill="#f9d8b8"/><path d="M4 22 Q2 3 20 2 Q38 3 36 22 Q28 11 20 11 Q12 11 4 22Z" fill="#5a3320"/>
  <ellipse cx="13" cy="22" rx="4" ry="5" fill="#fff"/><ellipse cx="27" cy="22" rx="4" ry="5" fill="#fff"/>
  <circle cx="13" cy="23" r="2.6" fill="#7a4a24"/><circle cx="27" cy="23" r="2.6" fill="#7a4a24"/>
  <path d="M15 31 q5 4 10 0" stroke="#e0249a" stroke-width="2.5" fill="none"/></svg>`; }
function miniTri() { return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 40 40">
  <circle cx="20" cy="23" r="15" fill="#f5d2ad"/><g fill="#2a1a10"><circle cx="10" cy="12" r="7"/><circle cx="20" cy="8" r="8"/><circle cx="30" cy="12" r="7"/><circle cx="33" cy="20" r="4"/><circle cx="7" cy="20" r="4"/></g>
  <circle cx="14" cy="23" r="2.6" fill="#1f9e54"/><circle cx="26" cy="23" r="2.6" fill="#1f9e54"/>
  <path d="M16 31 q4 2 8 0" stroke="#9c5a32" stroke-width="2" fill="none"/></svg>`; }

/* ===== pixelation: draw SVG into a tiny canvas, CSS upscales nearest-neighbor ===== */
function setSprite(el, svg, lowW, lowH) {
  try {
    const cv = document.createElement('canvas');
    cv.width = lowW; cv.height = lowH;
    const ctx = cv.getContext('2d'); ctx.imageSmoothingEnabled = false;
    const img = new Image();
    img.onload = function(){ try { ctx.clearRect(0,0,lowW,lowH); ctx.drawImage(img,0,0,lowW,lowH); } catch(e){ el.innerHTML = svg; } };
    img.onerror = function(){ el.innerHTML = svg; };
    img.src = 'data:image/svg+xml;charset=utf-8,' + encodeURIComponent(svg);
    el.innerHTML = ''; el.appendChild(cv);
  } catch(e) { el.innerHTML = svg; }
}

/* ===== state ===== */
const MAXHP = 100;
let st = {};
function freshState(){ st = { womenHP:MAXHP, menHP:MAXHP, round:1, combo:0, best:0, score:0, busy:false, current:null, lastThing:null, over:false }; }

const $ = id => document.getElementById(id);
const elWord=$('word'), elRound=$('roundNum'), elScore=$('scoreMini');
const elFillW=$('fillW'), elLagW=$('lagW'), elFillM=$('fillM'), elLagM=$('lagM');
const elHeroine=$('heroine'), elTri=$('triathlete'), elStage=$('stage');
const elProj=$('projectile'), elImpact=$('impact'), elCombo=$('combo');
const elReason=$('reasonPop'), elAlert=$('alert'), elAnn=$('announce'), elAnnTxt=$('announceTxt');
const elVic=$('victory'), elBtnW=$('btnWomen'), elBtnM=$('btnMen'), elAppeal=$('btnAppeal'), elDenied=$('denied');

function correctSide(v){ if(v==='FOR WOMEN'||v==='NOT FOR MEN')return'WOMEN'; if(v==='FOR MEN')return'MEN'; return'CLASSIFIED'; }
function vclass(v){ return v==='FOR WOMEN'?'v-women':v==='NOT FOR MEN'?'v-notmen':v==='FOR MEN'?'v-men':'v-classified'; }
function rand(a){ return a[Math.floor(Math.random()*a.length)]; }

function setBars(){ const w=Math.max(0,st.womenHP), m=Math.max(0,st.menHP);
  elFillW.style.width=w+'%'; elLagW.style.width=w+'%'; elFillM.style.width=m+'%'; elLagM.style.width=m+'%'; }
function damageBar(side, amt){ if(side==='men'){ st.menHP=Math.max(0,st.menHP-amt); elFillM.style.width=st.menHP+'%'; elLagM.style.width=st.menHP+'%'; }
  else { st.womenHP=Math.max(0,st.womenHP-amt); elFillW.style.width=st.womenHP+'%'; elLagW.style.width=st.womenHP+'%'; } }

function floatText(big, dmg, cls){ const f=document.createElement('div'); f.className='floater '+(cls||'');
  f.innerHTML=`<span class="big">${big}</span>`+(dmg!=null?`<span class="dmg">-${dmg}</span>`:''); f.style.left=(cls==='miss'?'18%':'66%');
  elStage.appendChild(f); setTimeout(()=>f.remove(),2000); }
function showReason(v, reason){ elReason.innerHTML=`<span class="verdict-chip ${vclass(v)}">${v}</span><div class="reason-text">&ldquo;${reason}&rdquo;</div>`; elReason.classList.add('show'); }
function hideReason(){ elReason.classList.remove('show'); }
function announce(text, cb){ elAnnTxt.textContent=text; elAnn.classList.remove('show'); void elAnn.offsetWidth; elAnn.classList.add('show'); setTimeout(()=>{ elAnn.classList.remove('show'); if(cb)cb(); },1000); }

function showAppeal(){ elAppeal.classList.add('show'); }
function hideAppeal(){ elAppeal.classList.remove('show'); elDenied.classList.remove('show'); }

function nextRound(){ if(st.over)return; hideReason(); hideAppeal(); st.busy=false; elBtnW.disabled=false; elBtnM.disabled=false; pickWord(); }

function pickWord(){ let pool=RULINGS;
  if(Math.random()<0.12){ const cls=RULINGS.filter(r=>r.verdict==='CLASSIFIED'); if(cls.length)pool=cls; }
  let c=rand(pool), t=0; while(c.thing===st.lastThing && t<25){ c=rand(pool); t++; }
  st.current=c; st.lastThing=c.thing; elWord.textContent=c.thing.toUpperCase(); elRound.textContent=st.round; elScore.textContent='SCORE '+st.score; }

function launchProjectile(dir, label, onImpact){ const w=elStage.clientWidth; elProj.textContent=label;
  elProj.style.setProperty('--travel', Math.round(w*0.5)+'px'); elProj.classList.remove('fly','flyBack'); void elProj.offsetWidth;
  if(dir==='toMen'){ elProj.style.left='24%'; elProj.style.right=''; elProj.classList.add('fly'); }
  else { elProj.style.left=''; elProj.style.right='24%'; elProj.classList.add('flyBack'); }
  const h=()=>{ elProj.style.opacity=0; elProj.removeEventListener('animationend',h); onImpact(); }; elProj.addEventListener('animationend',h); }
function impactAt(side){ elImpact.style.setProperty('--ix', side==='men'?'78%':'22%'); elImpact.style.setProperty('--iy','46%');
  elImpact.classList.remove('boom'); void elImpact.offsetWidth; elImpact.classList.add('boom');
  elStage.classList.remove('shake'); void elStage.offsetWidth; elStage.classList.add('shake'); }

const REVEAL_MS = 3200, CLASSIFIED_MS = 3500;

function doCorrect(){ st.combo+=1; st.best=Math.max(st.best,st.combo); const crit=st.combo>=3;
  let dmg=15+Math.min(st.combo,6)*3+(crit?9:0); st.score+=10*st.combo;
  const v=st.current.verdict, reason=st.current.reason, label=st.current.thing.toUpperCase();
  elHeroine.classList.add('lungeL'); setTimeout(()=>elHeroine.classList.remove('lungeL'),500);
  launchProjectile('toMen', label, ()=>{ impactAt('men'); elTri.classList.add('hitR','flash'); setTimeout(()=>elTri.classList.remove('hitR','flash'),520);
    damageBar('men',dmg); const tag=crit?'CRITICAL HIT':(v==='FOR WOMEN'?'SPIRIT DAMAGE':'RULING LANDS'); floatText(tag,dmg,crit?'crit':'');
    if(st.combo>1){ elCombo.textContent='\u2605 COMBO x'+st.combo+' \u2605'; elCombo.classList.remove('show'); void elCombo.offsetWidth; elCombo.classList.add('show'); }
    showReason(v,reason); showAppeal(); setBars();
    if(st.menHP<=0){ koSequence('WOMEN'); } else { st.round+=1; setTimeout(nextRound,REVEAL_MS); } }); }

function doWrong(){ st.combo=0; const dmg=20; const v=st.current.verdict, reason=st.current.reason;
  elTri.classList.add('lungeR'); setTimeout(()=>elTri.classList.remove('lungeR'),500);
  launchProjectile('toWomen','WRONG',()=>{ impactAt('women'); elHeroine.classList.add('hitL','flash'); setTimeout(()=>elHeroine.classList.remove('hitL','flash'),520);
    damageBar('women',dmg); floatText('NOT QUITE',dmg,'miss'); showReason(v,reason); showAppeal(); setBars();
    if(st.womenHP<=0){ koSequence('MEN'); } else { st.round+=1; setTimeout(nextRound,REVEAL_MS); } }); }

function doClassified(){ const v=st.current.verdict, reason=st.current.reason;
  elAlert.classList.remove('on'); void elAlert.offsetWidth; elAlert.classList.add('on');
  elStage.classList.remove('shake'); void elStage.offsetWidth; elStage.classList.add('shake');
  floatText('\u26A0 CLASSIFIED \u26A0', null, 'crit'); showReason(v,reason); showAppeal();
  st.score+=1; elScore.textContent='SCORE '+st.score; st.round+=1; setTimeout(nextRound,CLASSIFIED_MS); }

function onGuess(side){ if(st.busy||st.over||!st.current)return; st.busy=true; elBtnW.disabled=true; elBtnM.disabled=true;
  const cs=correctSide(st.current.verdict); if(cs==='CLASSIFIED')doClassified(); else if(side===cs)doCorrect(); else doWrong(); }

function koSequence(winner){ st.over=true; st.busy=true; elBtnW.disabled=true; elBtnM.disabled=true; hideAppeal(); setBars(); announce('K.O.!', ()=>showVictory(winner)); }
function showVictory(winner){ if(winner==='WOMEN'){ setSprite($('victorySvg'), heroineVictory(), 96, 154);
    $('victoryTitle').innerHTML='FLAWLESS,<br>OBVIOUSLY'; $('victorySub').textContent='Team Women takes the ruling. It was always going to be for women.'; }
  else { const book=rand(BOOKS); setSprite($('victorySvg'), triathleteVictory(book), 96, 154);
    $('victoryTitle').innerHTML='TEAM MEN WINS'; $('victorySub').innerHTML='He sits down, opens &ldquo;'+book+',&rdquo; and begins, quietly, to grow. We are proud of him.'; }
  elVic.classList.add('show'); }

function start(){ setSprite($('portraitW'), miniHeroine(), 20, 20); setSprite($('portraitM'), miniTri(), 20, 20);
  freshState(); setSprite(elHeroine, heroineStance(), 60, 96); setSprite(elTri, triathleteStance(), 60, 96);
  elVic.classList.remove('show'); hideReason(); hideAppeal(); $('marqueeText').textContent=MARQUEE+MARQUEE; setBars(); pickWord(); announce('ROUND 1  FIGHT!'); }

elBtnW.addEventListener('click', ()=>onGuess('WOMEN'));
elBtnM.addEventListener('click', ()=>onGuess('MEN'));
elAppeal.addEventListener('click', ()=>{ elDenied.classList.remove('show'); void elDenied.offsetWidth; elDenied.classList.add('show'); });
$('playAgain').addEventListener('click', start);
start();
</script>
"""


# ---------------------------------------------------------------------------
# Render: inject the rulings as JSON, embed the self-contained arcade screen.
# ---------------------------------------------------------------------------
GAME_HTML = GAME_TEMPLATE.replace("__RULINGS_JSON__", json.dumps(ALL_RULINGS))

try:
    components.html(GAME_HTML, height=716, scrolling=False)
except Exception:
    import html as _html
    _frame = ('<iframe style="width:100%;height:716px;border:none;" srcdoc="'
              + _html.escape(GAME_HTML, quote=True) + '"></iframe>')
    st.html(_frame, unsafe_allow_javascript=True)


# ---------------------------------------------------------------------------
# HOW TO RUN LOCALLY
#   1. pip install streamlit
#   2. streamlit run app.py
#   3. Opens in your browser (usually http://localhost:8501).
#
# HOW TO PLAY
#   - A WORD appears above the arena. Hit FOR WOMEN or FOR MEN.
#   - "NOT FOR MEN" verdicts count as the WOMEN side.
#   - Correct guesses make the heroine attack; the ruling flies across the
#     screen, the triathlete is hit, Team Men's health drops, combos build.
#   - Wrong guesses cost Team Women health. Rare CLASSIFIED = red alert.
#   - Tap "appeal this ruling" during a reveal for the verdict.
#   - Knock a team to zero HP for the victory screen.
# ---------------------------------------------------------------------------
