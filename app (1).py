import json
import streamlit as st
import streamlit.components.v1 as components

# ---------------------------------------------------------------------------
# THAT'S NOT FOR YOU  -  ARCADE FIGHTING EDITION
# A ridiculous magical-girl fighting game whose sole purpose is to determine
# whether random objects are FOR WOMEN or FOR MEN.
# Street Fighter, reimagined by a 13-year-old girl in 2004.
#
# The whole match (health, rounds, attacks, animations) runs client-side in a
# single isolated HTML/JS screen, so it actually feels like a game instead of a
# web page that reloads on every click.
# ---------------------------------------------------------------------------

st.set_page_config(page_title="THAT'S NOT FOR YOU", page_icon=":sparkles:", layout="wide")

# strip Streamlit chrome so the cabinet is the whole screen
st.markdown(
    '''<style>
    #MainMenu, header, footer {visibility:hidden;}
    .block-container {padding:0.4rem 0.6rem 0; max-width:960px;}
    .stApp {background: linear-gradient(135deg,#2a0a4d 0%, #4a1480 50%, #2a0a4d 100%);}
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
  position: relative;
  width: 100%;
  max-width: 900px;
  height: 700px;
  margin: 0 auto;
  border-radius: 16px;
  overflow: hidden;
  border: 5px solid #ff8fdf;
  box-shadow: 0 0 0 4px #fff, 0 0 0 9px #7b2ff7, 0 0 40px rgba(123,47,247,.6),
              inset 0 0 60px rgba(58,20,102,.5);
  font-family: 'Press Start 2P', monospace;
  user-select: none;
  background:
    radial-gradient(ellipse at 50% 0%, #ff5fc0 0%, #9b2fd6 38%, #4a1480 75%, #2a0a4d 100%);
}

/* twinkling star field */
#cabinet::before {
  content: "";
  position: absolute; inset: 0; pointer-events: none; opacity: .8;
  background-image:
    radial-gradient(1.5px 1.5px at 12% 18%, #fff, transparent),
    radial-gradient(1.5px 1.5px at 28% 8%, #ffd0ef, transparent),
    radial-gradient(2px 2px at 47% 22%, #fff, transparent),
    radial-gradient(1.5px 1.5px at 68% 10%, #fff0fb, transparent),
    radial-gradient(2px 2px at 82% 26%, #fff, transparent),
    radial-gradient(1.5px 1.5px at 92% 14%, #ffd0ef, transparent),
    radial-gradient(1.5px 1.5px at 58% 6%, #fff, transparent);
  animation: twinkle 2.4s ease-in-out infinite alternate;
}
@keyframes twinkle { from { opacity:.45 } to { opacity:.95 } }

/* ===================== HUD ===================== */
#hud {
  position: relative; z-index: 6;
  display: flex; align-items: flex-start; justify-content: space-between;
  gap: 8px; padding: 10px 12px 4px;
}
.bar-wrap { flex: 1; display: flex; flex-direction: column; }
.bar-top { display: flex; align-items: center; gap: 6px; margin-bottom: 3px; }
.bar-wrap.right .bar-top { flex-direction: row-reverse; }
.portrait { width: 34px; height: 34px; border-radius: 8px; border: 2px solid #fff;
  background: #2a0a4d; overflow: hidden; flex: none; box-shadow: 0 0 8px rgba(255,143,223,.7); }
.portrait svg { width: 100%; height: 100%; }
.pname { font-size: 9px; color: #fff; text-shadow: 1px 1px 0 #7b2ff7; letter-spacing: 1px; }
.bar-wrap.right .pname { margin-left: auto; }

.bar { position: relative; height: 18px; background: #1a0833;
  border: 3px solid #fff; border-radius: 4px; overflow: hidden;
  box-shadow: inset 0 0 6px rgba(0,0,0,.6), 0 2px 0 rgba(0,0,0,.3);
  transform: skewX(-12deg); }
.bar-wrap.right .bar { transform: skewX(12deg); }
.lag, .fill { position: absolute; top: 0; bottom: 0; left: 0; width: 100%; }
.lag { background: #fff; transition: width .55s ease .15s; }
.fill { transition: width .18s ease; }
.fill-w { background: linear-gradient(90deg, #ff9fe0, #ff2fa8 60%, #d6248f); }
.fill-m { background: linear-gradient(90deg, #16c0a8, #2f72f7 60%, #1f63e0); }
.bar-wrap.right .lag, .bar-wrap.right .fill { left: auto; right: 0; }

.round-box { flex: none; width: 78px; text-align: center; padding-top: 2px; }
.round-label { font-size: 8px; color: #ffd0ef; letter-spacing: 2px; }
.round-num { font-size: 20px; color: #fff; text-shadow: 0 0 8px #ff2fa8, 2px 2px 0 #7b2ff7; line-height: 1.4; }
.score-mini { font-size: 7px; color: #ffe9fb; margin-top: 2px; }

/* ===================== WORD PROMPT ===================== */
#prompt {
  position: relative; z-index: 6; text-align: center; margin: 2px 12px 0;
  padding: 7px 6px;
  background: linear-gradient(180deg, rgba(42,10,77,.85), rgba(123,47,247,.55));
  border: 2px solid #ff8fdf; border-radius: 10px;
  box-shadow: 0 0 14px rgba(255,47,168,.5), inset 0 0 10px rgba(255,143,223,.3);
}
.prompt-label { font-size: 8px; color: #ffd0ef; letter-spacing: 4px; }
.prompt-word { display: block; font-size: 18px; color: #fff; line-height: 1.45; margin-top: 5px;
  text-shadow: 0 0 10px #ff2fa8, 2px 2px 0 #d6248f, 3px 3px 0 #7b2ff7; word-break: break-word; }
@media (max-width: 560px) { .prompt-word { font-size: 14px; } }

/* ===================== STAGE ===================== */
#stage {
  position: absolute; left: 0; right: 0;
  top: 122px; bottom: 92px;
  z-index: 4; overflow: hidden;
}
/* glossy perspective floor */
.floor {
  position: absolute; left: -10%; right: -10%; bottom: 0; height: 42%;
  background:
    repeating-linear-gradient(90deg, rgba(255,143,223,.25) 0 2px, transparent 2px 46px),
    linear-gradient(180deg, #6a1fb0 0%, #ff5fc0 100%);
  transform: perspective(380px) rotateX(58deg);
  transform-origin: bottom center;
  box-shadow: 0 -2px 30px rgba(255,47,168,.5);
}
.floor::after {
  content: ""; position: absolute; inset: 0;
  background: repeating-linear-gradient(0deg, rgba(255,255,255,.18) 0 2px, transparent 2px 46px);
}
.stage-glow { position: absolute; left: 50%; bottom: 6%; width: 60%; height: 30%;
  transform: translateX(-50%); border-radius: 50%;
  background: radial-gradient(ellipse, rgba(255,210,239,.5), transparent 70%); pointer-events: none; }

.fighter { position: absolute; bottom: 4%; width: 30%; max-width: 230px; z-index: 5;
  filter: drop-shadow(0 10px 10px rgba(20,0,40,.55)); }
.fighter svg { width: 100%; height: auto; display: block; }
#heroine { left: 3%; transform-origin: bottom center; animation: bobL 2.2s ease-in-out infinite; }
#triathlete { right: 3%; transform-origin: bottom center; animation: bobR 2.2s ease-in-out infinite; }
@keyframes bobL { 0%,100%{ transform: translateY(0) rotate(-1deg);} 50%{ transform: translateY(-6px) rotate(-2deg);} }
@keyframes bobR { 0%,100%{ transform: translateY(0) rotate(1deg);} 50%{ transform: translateY(-5px) rotate(1.5deg);} }

.lungeL { animation: lungeL .5s ease !important; }
@keyframes lungeL { 0%{transform:translateX(0) rotate(-1deg);} 40%{transform:translateX(38px) scale(1.06) rotate(2deg);} 100%{transform:translateX(0) rotate(-1deg);} }
.lungeR { animation: lungeR .5s ease !important; }
@keyframes lungeR { 0%{transform:translateX(0) rotate(1deg);} 40%{transform:translateX(-34px) scale(1.05) rotate(-3deg);} 100%{transform:translateX(0) rotate(1deg);} }

.hitL { animation: hitL .5s ease !important; }
@keyframes hitL { 0%{transform:translateX(0);} 15%{transform:translateX(-16px) rotate(-6deg);} 30%{transform:translateX(10px) rotate(3deg);} 50%{transform:translateX(-8px) rotate(-3deg);} 70%{transform:translateX(5px);} 100%{transform:translateX(0);} }
.hitR { animation: hitR .5s ease !important; }
@keyframes hitR { 0%{transform:translateX(0);} 15%{transform:translateX(18px) rotate(8deg);} 30%{transform:translateX(-10px) rotate(-4deg);} 50%{transform:translateX(9px) rotate(4deg);} 70%{transform:translateX(-5px);} 100%{transform:translateX(0);} }
.fighter.flash svg { animation: flashWhite .4s ease; }
@keyframes flashWhite { 0%,100%{filter:none;} 30%{filter:brightness(3) saturate(.2);} 60%{filter:brightness(1.6);} }

.vs-badge { position: absolute; left: 50%; top: 16%; transform: translateX(-50%);
  font-size: 26px; color: #fff; z-index: 6;
  text-shadow: 0 0 12px #ff2fa8, 3px 3px 0 #7b2ff7, -1px -1px 0 #ff8fdf;
  animation: vspulse 1.6s ease-in-out infinite; }
@keyframes vspulse { 0%,100%{transform:translateX(-50%) scale(1);} 50%{transform:translateX(-50%) scale(1.14);} }

/* projectile = the WORD flying across */
#projectile { position: absolute; z-index: 8; left: 22%; top: 38%;
  font-size: 13px; color: #2a0a4d; padding: 6px 10px; border-radius: 999px;
  background: linear-gradient(180deg,#fff,#ffd0ef); border: 2px solid #ff2fa8;
  box-shadow: 0 0 16px #ff79d2, 0 0 30px #ff2fa8; opacity: 0; pointer-events: none;
  white-space: nowrap; max-width: 56%; overflow: hidden; text-overflow: ellipsis; }
#projectile.fly { animation: fly .52s cubic-bezier(.4,0,.7,1) forwards; }
@keyframes fly {
  0%{ opacity:0; transform: translateX(0) scale(.4) rotate(0); }
  12%{ opacity:1; transform: translateX(20px) scale(1.1) rotate(60deg);}
  100%{ opacity:1; transform: translateX(var(--travel,420px)) scale(.85) rotate(540deg);} }
#projectile.flyBack { animation: flyBack .52s cubic-bezier(.4,0,.7,1) forwards; }
@keyframes flyBack {
  0%{ opacity:0; transform: translateX(0) scale(.4);} 12%{opacity:1;transform:translateX(-16px) scale(1.05);}
  100%{ opacity:1; transform: translateX(calc(var(--travel,420px) * -1)) scale(.85) rotate(-480deg);} }

/* impact flash + screen shake */
#impact { position: absolute; inset: 0; z-index: 7; pointer-events: none; opacity: 0;
  background: radial-gradient(circle at var(--ix,75%) var(--iy,45%), rgba(255,255,255,.95), rgba(255,47,168,.5) 25%, transparent 55%); }
#impact.boom { animation: boom .45s ease; }
@keyframes boom { 0%{opacity:0; transform:scale(.6);} 25%{opacity:1; transform:scale(1.1);} 100%{opacity:0; transform:scale(1.3);} }
.shake { animation: shakeStage .4s ease; }
@keyframes shakeStage { 0%,100%{transform:translate(0,0);} 20%{transform:translate(-6px,3px);} 40%{transform:translate(7px,-3px);} 60%{transform:translate(-5px,2px);} 80%{transform:translate(4px,-2px);} }

/* floating combat text */
.floater { position: absolute; z-index: 9; pointer-events: none; text-align: center;
  left: 60%; top: 30%; transform: translateX(-50%);
  animation: floatUp 1.3s ease forwards; }
.floater .big { font-size: 18px; color: #fff; text-shadow: 0 0 10px #ff2fa8, 2px 2px 0 #d6248f; }
.floater .dmg { display:block; font-size: 22px; margin-top: 2px; color: #ffe14f; text-shadow: 2px 2px 0 #b8460a, 0 0 10px #ffa800; }
.floater.crit .big { color:#fff; text-shadow: 0 0 14px #ff2fa8, 2px 2px 0 #7b2ff7; }
.floater.miss .big { color:#9fd0ff; text-shadow: 2px 2px 0 #1f63e0; }
@keyframes floatUp { 0%{opacity:0; transform:translate(-50%,10px) scale(.5);} 20%{opacity:1; transform:translate(-50%,-6px) scale(1.15);} 70%{opacity:1; transform:translate(-50%,-30px) scale(1);} 100%{opacity:0; transform:translate(-50%,-54px) scale(.9);} }

/* combo badge */
#combo { position: absolute; z-index: 9; left: 50%; top: 6%; transform: translateX(-50%) scale(0);
  font-size: 13px; color: #fff; padding: 6px 12px; border-radius: 999px;
  background: linear-gradient(180deg,#ff79d2,#7b2ff7); border: 2px solid #fff;
  box-shadow: 0 0 16px #ff2fa8; }
#combo.show { animation: comboPop .9s ease; }
@keyframes comboPop { 0%{transform:translateX(-50%) scale(0);} 35%{transform:translateX(-50%) scale(1.3);} 70%{transform:translateX(-50%) scale(1);} 100%{transform:translateX(-50%) scale(1); opacity:0;} }

/* verdict + reason caption */
#reasonPop { position: absolute; z-index: 9; left: 50%; bottom: 8%; transform: translateX(-50%) translateY(16px);
  width: 86%; text-align: center; opacity: 0; transition: all .3s ease; }
#reasonPop.show { opacity: 1; transform: translateX(-50%) translateY(0); }
.verdict-chip { display: inline-block; font-size: 11px; padding: 5px 14px; border-radius: 999px;
  border: 2px solid #fff; margin-bottom: 6px; }
.v-women { background:#ffd0ef; color:#d6248f; } .v-notmen { background:#e3d2ff; color:#7b2ff7; }
.v-men { background:#d6ecff; color:#2f72f7; } .v-classified { background:#fff3c4; color:#b8860b; }
.reason-text { font-family:'Comic Neue', cursive; font-style: italic; font-weight: 700;
  font-size: 15px; color: #fff; text-shadow: 1px 1px 3px #2a0a4d; }

/* red alert (CLASSIFIED) */
#alert { position: absolute; inset: 0; z-index: 8; pointer-events: none; opacity: 0;
  border: 0 solid #ff2d2d; }
#alert.on { animation: alertFlash .4s steps(2) 4; }
@keyframes alertFlash { 0%{opacity:0; box-shadow: inset 0 0 0 0 #ff2d2d;} 50%{opacity:1; box-shadow: inset 0 0 80px 18px rgba(255,45,45,.7);} 100%{opacity:0;} }

/* ===================== CONTROLS ===================== */
#controls { position: absolute; left: 0; right: 0; bottom: 0; z-index: 7;
  display: flex; gap: 10px; padding: 10px 12px 12px; }
.choice { flex: 1; font-family: 'Press Start 2P', monospace; font-size: 14px; color: #fff;
  padding: 16px 8px; border: 3px solid #fff; border-radius: 12px; cursor: pointer; line-height: 1.5;
  transition: transform .06s ease, filter .1s ease; }
.choice:active { transform: translateY(4px); }
.choice:disabled { filter: grayscale(.5) brightness(.8); cursor: default; }
#btnWomen { background: linear-gradient(180deg,#ffb3e6 0%,#ff4fb8 50%,#e0249a 51%,#ff7fd0 100%);
  box-shadow: inset 0 2px 5px rgba(255,255,255,.85), 0 6px 0 #a81f7f, 0 9px 16px rgba(168,31,127,.5); }
#btnMen { background: linear-gradient(180deg,#a9d4ff 0%,#3f8bff 50%,#1f63e0 51%,#7fb0ff 100%);
  box-shadow: inset 0 2px 5px rgba(255,255,255,.85), 0 6px 0 #1846a8, 0 9px 16px rgba(24,70,168,.5); }
#btnWomen:hover, #btnMen:hover { filter: brightness(1.08); }

/* ===================== ANNOUNCER / KO ===================== */
#announce { position: absolute; inset: 0; z-index: 11; display: flex; align-items: center;
  justify-content: center; pointer-events: none; }
#announce .txt { font-size: 40px; color: #fff; opacity: 0;
  text-shadow: 0 0 18px #ff2fa8, 4px 4px 0 #7b2ff7, -2px -2px 0 #ff8fdf; }
#announce.show .txt { animation: slam .9s ease; }
@keyframes slam { 0%{opacity:0; transform: scale(3) rotate(-8deg);} 30%{opacity:1; transform: scale(1) rotate(-4deg);} 80%{opacity:1; transform: scale(1) rotate(-4deg);} 100%{opacity:0; transform: scale(1.1);} }

/* ===================== VICTORY ===================== */
#victory { position: absolute; inset: 0; z-index: 12; display: none; flex-direction: column;
  align-items: center; justify-content: center; text-align: center; padding: 18px;
  background: radial-gradient(ellipse at 50% 30%, rgba(123,47,247,.55), rgba(20,0,40,.92)); }
#victory.show { display: flex; }
#victory .vsvg { width: 46%; max-width: 280px; margin-bottom: 6px; }
#victory .vtitle { font-size: 20px; color: #fff; line-height: 1.6; text-shadow: 0 0 14px #ff2fa8, 3px 3px 0 #7b2ff7; }
#victory .vsub { font-family:'Comic Neue', cursive; font-style: italic; font-weight: 700; font-size: 15px;
  color: #ffd0ef; margin-top: 10px; max-width: 460px; }
#playAgain { margin-top: 16px; font-family:'Press Start 2P', monospace; font-size: 14px; color:#fff;
  padding: 14px 22px; border: 3px solid #fff; border-radius: 12px; cursor: pointer;
  background: linear-gradient(180deg,#ffb3e6,#ff2fa8 51%,#ff7fd0);
  box-shadow: inset 0 2px 5px rgba(255,255,255,.85), 0 6px 0 #a81f7f; }
#playAgain:active { transform: translateY(4px); }
.vburst { position: absolute; inset: 0; pointer-events: none;
  background-image:
    radial-gradient(3px 3px at 20% 30%, #fff, transparent),
    radial-gradient(3px 3px at 80% 25%, #ffd0ef, transparent),
    radial-gradient(2px 2px at 35% 70%, #fff, transparent),
    radial-gradient(3px 3px at 65% 65%, #fff0fb, transparent),
    radial-gradient(2px 2px at 50% 15%, #fff, transparent);
  animation: twinkle 1s ease-in-out infinite alternate; }

#foot { position: absolute; z-index: 13; left: 0; right: 0; bottom: 3px; text-align: center;
  font-family:'Comic Neue', cursive; font-size: 9px; color: rgba(255,224,251,.85); display:none; }
#victory.show ~ #foot { display: block; }
</style>

<div id="cabinet">
  <div id="hud">
    <div class="bar-wrap left">
      <div class="bar-top"><div class="portrait" id="portraitW"></div><div class="pname">TEAM WOMEN</div></div>
      <div class="bar"><div class="lag lag-w" id="lagW"></div><div class="fill fill-w" id="fillW"></div></div>
    </div>
    <div class="round-box">
      <div class="round-label">ROUND</div>
      <div class="round-num" id="roundNum">1</div>
      <div class="score-mini" id="scoreMini">SCORE 0</div>
    </div>
    <div class="bar-wrap right">
      <div class="bar-top"><div class="portrait" id="portraitM"></div><div class="pname">TEAM MEN</div></div>
      <div class="bar"><div class="lag lag-m" id="lagM"></div><div class="fill fill-m" id="fillM"></div></div>
    </div>
  </div>

  <div id="prompt">
    <span class="prompt-label">W O R D</span>
    <span class="prompt-word" id="word">&nbsp;</span>
  </div>

  <div id="stage">
    <div class="floor"></div>
    <div class="stage-glow"></div>
    <div class="vs-badge">VS</div>
    <div class="fighter" id="heroine"></div>
    <div class="fighter" id="triathlete"></div>
    <div id="projectile"></div>
    <div id="impact"></div>
    <div id="combo"></div>
    <div id="reasonPop"></div>
    <div id="alert"></div>
  </div>

  <div id="controls">
    <button class="choice" id="btnWomen">FOR<br>WOMEN</button>
    <button class="choice" id="btnMen">FOR<br>MEN</button>
  </div>

  <div id="announce"><div class="txt" id="announceTxt"></div></div>

  <div id="victory">
    <div class="vburst"></div>
    <div class="vsvg" id="victorySvg"></div>
    <div class="vtitle" id="victoryTitle"></div>
    <div class="vsub" id="victorySub"></div>
    <button id="playAgain">&#9733; PLAY AGAIN &#9733;</button>
  </div>
  <div id="foot">Powered by the International Institute of That&rsquo;s Not For You&trade;</div>
</div>

<script>
// ===== injected by Streamlit =====
const RULINGS = __RULINGS_JSON__;
const BOOKS = ["Invisible Women", "The Second Sex", "Men Explain Things To Me"];

// ---------- character art ----------
function heroineStance() {
  return `<svg viewBox="0 0 200 320" xmlns="http://www.w3.org/2000/svg">
    <defs>
      <linearGradient id="hsuit" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#ff8fe0"/><stop offset=".5" stop-color="#ff2fa8"/><stop offset="1" stop-color="#9b3cff"/></linearGradient>
      <linearGradient id="hhair" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#6b3d24"/><stop offset="1" stop-color="#3a2014"/></linearGradient>
      <radialGradient id="hglow" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#fff" stop-opacity=".9"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></radialGradient>
    </defs>
    <ellipse cx="100" cy="306" rx="64" ry="12" fill="rgba(20,0,40,.45)"/>
    <!-- long hair behind -->
    <path d="M62 96 Q34 180 58 260 L86 252 Q70 170 82 110 Z" fill="url(#hhair)"/>
    <path d="M138 96 Q170 180 150 264 L120 254 Q132 168 120 110 Z" fill="url(#hhair)"/>
    <!-- back leg + platform boot -->
    <path d="M118 196 L150 250 L138 264 L104 212 Z" fill="#f7d3b0"/>
    <rect x="132" y="250" width="34" height="40" rx="10" transform="rotate(20 149 270)" fill="#d23c9b"/>
    <rect x="150" y="276" width="40" height="16" rx="6" fill="#fff"/>
    <!-- front leg + platform boot -->
    <path d="M86 198 L70 256 L92 264 L104 210 Z" fill="#f7d3b0"/>
    <rect x="58" y="252" width="34" height="42" rx="10" fill="#e0249a"/>
    <rect x="48" y="280" width="44" height="16" rx="6" fill="#fff"/>
    <!-- hips / skirt -->
    <path d="M74 168 Q100 156 126 168 L132 210 Q100 224 68 210 Z" fill="url(#hsuit)"/>
    <!-- torso (exaggerated hourglass) -->
    <path d="M78 108 Q100 100 122 108 L118 150 Q126 158 120 172 Q100 182 80 172 Q74 158 82 150 Z" fill="url(#hsuit)"/>
    <circle cx="92" cy="138" r="2.4" fill="#fff"/><circle cx="108" cy="150" r="2.4" fill="#fff"/><circle cx="100" cy="128" r="2.4" fill="#fff"/>
    <!-- belt star -->
    <path d="M100 168 l4 8 9 1 -6.5 6 1.5 9 -8-4.5 -8 4.5 1.5-9 -6.5-6 9-1z" fill="#fff"/>
    <!-- back arm (raised guard) -->
    <path d="M120 116 Q150 110 156 84" stroke="#f7d3b0" stroke-width="13" fill="none" stroke-linecap="round"/>
    <circle cx="156" cy="80" r="10" fill="#f7d3b0"/>
    <!-- front arm (fist forward, ready) -->
    <path d="M80 120 Q52 128 40 150" stroke="#f7d3b0" stroke-width="13" fill="none" stroke-linecap="round"/>
    <circle cx="38" cy="152" r="11" fill="#f7d3b0"/>
    <circle cx="38" cy="152" r="5" fill="url(#hglow)"/>
    <!-- neck + head -->
    <rect x="93" y="92" width="14" height="16" fill="#f7d3b0"/>
    <circle cx="100" cy="74" r="26" fill="#f9d8b8"/>
    <!-- fringe + long front hair -->
    <path d="M73 74 Q70 40 100 38 Q130 40 127 74 Q116 56 100 56 Q84 56 73 74 Z" fill="url(#hhair)"/>
    <path d="M75 70 Q66 130 80 150 L88 146 Q80 110 84 76 Z" fill="url(#hhair)"/>
    <path d="M125 70 Q134 130 120 150 L112 146 Q120 110 116 76 Z" fill="url(#hhair)"/>
    <!-- huge brown eyes + dramatic lashes -->
    <ellipse cx="89" cy="74" rx="9" ry="12" fill="#fff"/>
    <ellipse cx="111" cy="74" rx="9" ry="12" fill="#fff"/>
    <circle cx="89" cy="76" r="6" fill="#7a4a24"/><circle cx="111" cy="76" r="6" fill="#7a4a24"/>
    <circle cx="89" cy="76" r="2.6" fill="#2a1607"/><circle cx="111" cy="76" r="2.6" fill="#2a1607"/>
    <circle cx="91.5" cy="73" r="2" fill="#fff"/><circle cx="113.5" cy="73" r="2" fill="#fff"/>
    <path d="M79 66 Q88 60 99 65" stroke="#1a0d05" stroke-width="2.6" fill="none" stroke-linecap="round"/>
    <path d="M101 65 Q112 60 121 66" stroke="#1a0d05" stroke-width="2.6" fill="none" stroke-linecap="round"/>
    <path d="M80 64 l-6 -4 M82 62 l-6 -2" stroke="#1a0d05" stroke-width="2" stroke-linecap="round"/>
    <path d="M120 64 l6 -4 M118 62 l6 -2" stroke="#1a0d05" stroke-width="2" stroke-linecap="round"/>
    <!-- blush + glossy lips -->
    <ellipse cx="80" cy="86" rx="5" ry="3.4" fill="#ffb3d9" opacity=".8"/>
    <ellipse cx="120" cy="86" rx="5" ry="3.4" fill="#ffb3d9" opacity=".8"/>
    <path d="M92 90 Q100 98 108 90 Q100 94 92 90 Z" fill="#e0249a"/>
    <path d="M93 90 Q100 92 107 90" stroke="#fff" stroke-width="1.4" fill="none" opacity=".7"/>
    <!-- sparkle accents -->
    <path d="M150 50 l2 6 6 2 -6 2 -2 6 -2-6 -6-2 6-2z" fill="#fff"/>
    <path d="M30 120 l2 5 5 2 -5 2 -2 5 -2-5 -5-2 5-2z" fill="#fff"/>
  </svg>`;
}

function heroineVictory() {
  return `<svg viewBox="0 0 200 320" xmlns="http://www.w3.org/2000/svg">
    <defs>
      <linearGradient id="hv1" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#ff8fe0"/><stop offset=".5" stop-color="#ff2fa8"/><stop offset="1" stop-color="#9b3cff"/></linearGradient>
      <linearGradient id="hv2" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#6b3d24"/><stop offset="1" stop-color="#3a2014"/></linearGradient>
    </defs>
    <g style="animation: spinPose 3s ease-in-out infinite;transform-origin:100px 200px">
    <ellipse cx="100" cy="306" rx="60" ry="11" fill="rgba(20,0,40,.4)"/>
    <path d="M64 96 Q30 190 60 270 L88 260 Q70 170 84 110 Z" fill="url(#hv2)"/>
    <path d="M136 96 Q170 190 140 270 L112 260 Q130 170 116 110 Z" fill="url(#hv2)"/>
    <rect x="78" y="244" width="20" height="50" rx="9" fill="#e0249a"/><rect x="102" y="244" width="20" height="50" rx="9" fill="#e0249a"/>
    <rect x="70" y="284" width="34" height="16" rx="6" fill="#fff"/><rect x="96" y="284" width="34" height="16" rx="6" fill="#fff"/>
    <path d="M74 168 Q100 158 126 168 L130 248 Q100 258 70 248 Z" fill="url(#hv1)"/>
    <path d="M80 108 Q100 100 120 108 L116 168 Q100 176 84 168 Z" fill="url(#hv1)"/>
    <path d="M100 168 l4 8 9 1 -6.5 6 1.5 9 -8-4.5 -8 4.5 1.5-9 -6.5-6 9-1z" fill="#fff"/>
    <!-- both arms up, triumphant -->
    <path d="M82 116 Q54 92 60 56" stroke="#f7d3b0" stroke-width="13" fill="none" stroke-linecap="round"/>
    <path d="M118 116 Q146 92 140 56" stroke="#f7d3b0" stroke-width="13" fill="none" stroke-linecap="round"/>
    <circle cx="60" cy="52" r="10" fill="#f7d3b0"/><circle cx="140" cy="52" r="10" fill="#f7d3b0"/>
    <rect x="93" y="92" width="14" height="16" fill="#f7d3b0"/>
    <circle cx="100" cy="74" r="26" fill="#f9d8b8"/>
    <path d="M73 74 Q70 40 100 38 Q130 40 127 74 Q116 56 100 56 Q84 56 73 74 Z" fill="url(#hv2)"/>
    <ellipse cx="89" cy="74" rx="9" ry="12" fill="#fff"/><ellipse cx="111" cy="74" rx="9" ry="12" fill="#fff"/>
    <circle cx="89" cy="76" r="6" fill="#7a4a24"/><circle cx="111" cy="76" r="6" fill="#7a4a24"/>
    <circle cx="89" cy="76" r="2.6" fill="#2a1607"/><circle cx="111" cy="76" r="2.6" fill="#2a1607"/>
    <circle cx="91.5" cy="73" r="2" fill="#fff"/><circle cx="113.5" cy="73" r="2" fill="#fff"/>
    <path d="M79 66 Q88 60 99 65" stroke="#1a0d05" stroke-width="2.6" fill="none"/>
    <path d="M101 65 Q112 60 121 66" stroke="#1a0d05" stroke-width="2.6" fill="none"/>
    <ellipse cx="80" cy="86" rx="5" ry="3.4" fill="#ffb3d9" opacity=".8"/><ellipse cx="120" cy="86" rx="5" ry="3.4" fill="#ffb3d9" opacity=".8"/>
    <path d="M90 88 Q100 100 110 88 Q100 95 90 88 Z" fill="#e0249a"/>
    </g>
    <path d="M40 40 l3 9 9 3 -9 3 -3 9 -3-9 -9-3 9-3z" fill="#fff"><animate attributeName="opacity" values="1;.2;1" dur="1s" repeatCount="indefinite"/></path>
    <path d="M162 60 l3 9 9 3 -9 3 -3 9 -3-9 -9-3 9-3z" fill="#ffd0ef"><animate attributeName="opacity" values=".3;1;.3" dur="1.2s" repeatCount="indefinite"/></path>
    <text x="30" y="150" font-size="20" fill="#fff">&#9825;</text>
    <text x="158" y="150" font-size="16" fill="#ffd0ef">&#9825;</text>
    <style>@keyframes spinPose{0%,100%{transform:rotate(-4deg) scale(1)}50%{transform:rotate(4deg) scale(1.04)}}</style>
  </svg>`;
}

function triathleteStance() {
  return `<svg viewBox="0 0 200 320" xmlns="http://www.w3.org/2000/svg">
    <defs><linearGradient id="trisuit" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#27406b"/><stop offset="1" stop-color="#16243f"/></linearGradient></defs>
    <ellipse cx="100" cy="306" rx="58" ry="11" fill="rgba(20,0,40,.45)"/>
    <!-- legs -->
    <rect x="84" y="196" width="15" height="64" rx="7" fill="#f2c9a6"/>
    <rect x="103" y="196" width="15" height="64" rx="7" fill="#f2c9a6"/>
    <!-- running shoes -->
    <path d="M78 258 q-6 10 4 16 l22 0 0 -16 z" fill="#16c0a8"/>
    <path d="M120 258 q6 10 -4 16 l-22 0 0 -16 z" fill="#16c0a8"/>
    <rect x="80" y="270" width="30" height="6" rx="3" fill="#fff"/><rect x="92" y="270" width="30" height="6" rx="3" fill="#fff"/>
    <!-- tri-suit torso (sleeveless) -->
    <path d="M78 116 Q100 108 122 116 L126 200 Q100 212 74 200 Z" fill="url(#trisuit)"/>
    <path d="M78 116 L74 200 Q84 206 88 200 L90 116 Z" fill="#16c0a8" opacity=".85"/>
    <!-- race bib -->
    <rect x="96" y="138" width="26" height="20" rx="3" fill="#fff"/>
    <text x="109" y="153" font-size="12" fill="#16243f" text-anchor="middle" font-family="Arial">07</text>
    <!-- arms up but unsure -->
    <path d="M80 124 Q52 120 46 96" stroke="#f2c9a6" stroke-width="12" fill="none" stroke-linecap="round"/>
    <circle cx="45" cy="92" r="9" fill="#f2c9a6"/>
    <path d="M120 124 Q150 122 152 100" stroke="#f2c9a6" stroke-width="12" fill="none" stroke-linecap="round"/>
    <circle cx="153" cy="96" r="9" fill="#f2c9a6"/>
    <!-- sport watch -->
    <rect x="146" y="100" width="11" height="9" rx="2" fill="#0b1626"/>
    <!-- neck + head -->
    <rect x="93" y="100" width="14" height="14" fill="#f2c9a6"/>
    <circle cx="100" cy="82" r="24" fill="#f5d2ad"/>
    <!-- curly dark hair -->
    <g fill="#2a1a10">
      <circle cx="80" cy="64" r="12"/><circle cx="96" cy="56" r="13"/><circle cx="114" cy="60" r="12"/>
      <circle cx="124" cy="74" r="9"/><circle cx="74" cy="78" r="9"/><circle cx="104" cy="50" r="10"/>
    </g>
    <!-- green eyes, one brow raised = confused but determined -->
    <ellipse cx="91" cy="82" rx="5.5" ry="6.5" fill="#fff"/><ellipse cx="109" cy="82" rx="5.5" ry="6.5" fill="#fff"/>
    <circle cx="91" cy="83" r="3.4" fill="#1f9e54"/><circle cx="109" cy="83" r="3.4" fill="#1f9e54"/>
    <circle cx="91" cy="83" r="1.6" fill="#0a2e18"/><circle cx="109" cy="83" r="1.6" fill="#0a2e18"/>
    <circle cx="92.4" cy="81" r="1.2" fill="#fff"/><circle cx="110.4" cy="81" r="1.2" fill="#fff"/>
    <path d="M84 72 Q91 66 99 71" stroke="#2a1a10" stroke-width="2.4" fill="none" stroke-linecap="round"/>
    <path d="M102 73 Q109 69 117 73" stroke="#2a1a10" stroke-width="2.4" fill="none" stroke-linecap="round"/>
    <path d="M93 96 Q100 99 107 96" stroke="#9c5a32" stroke-width="2.2" fill="none" stroke-linecap="round"/>
    <text x="138" y="64" font-size="16" fill="#ffd0ef" font-family="Arial">?</text>
  </svg>`;
}

function triathleteVictory(book) {
  return `<svg viewBox="0 0 200 320" xmlns="http://www.w3.org/2000/svg">
    <defs><linearGradient id="tvsuit" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#27406b"/><stop offset="1" stop-color="#16243f"/></linearGradient></defs>
    <ellipse cx="100" cy="300" rx="70" ry="12" fill="rgba(20,0,40,.4)"/>
    <!-- seated cushion -->
    <ellipse cx="100" cy="276" rx="60" ry="16" fill="#7b2ff7" opacity=".6"/>
    <!-- folded legs -->
    <path d="M52 250 Q60 234 86 240 L92 268 L48 268 Z" fill="url(#tvsuit)"/>
    <path d="M148 250 Q140 234 114 240 L108 268 L152 268 Z" fill="url(#tvsuit)"/>
    <circle cx="52" cy="262" r="10" fill="#f2c9a6"/><circle cx="148" cy="262" r="10" fill="#f2c9a6"/>
    <!-- torso -->
    <path d="M76 168 Q100 160 124 168 L120 244 Q100 252 80 244 Z" fill="url(#tvsuit)"/>
    <path d="M76 168 L80 244 Q88 248 90 244 L88 168 Z" fill="#16c0a8" opacity=".8"/>
    <!-- arms holding book -->
    <path d="M82 184 Q70 206 86 214" stroke="#f2c9a6" stroke-width="11" fill="none" stroke-linecap="round"/>
    <path d="M118 184 Q130 206 114 214" stroke="#f2c9a6" stroke-width="11" fill="none" stroke-linecap="round"/>
    <!-- open book -->
    <path d="M72 200 L100 196 L128 200 L128 224 L100 222 L72 224 Z" fill="#fff" stroke="#d6248f" stroke-width="2"/>
    <line x1="100" y1="196" x2="100" y2="222" stroke="#ffb3d9" stroke-width="2"/>
    <line x1="78" y1="206" x2="94" y2="204" stroke="#c9c2cf" stroke-width="1.4"/>
    <line x1="78" y1="212" x2="94" y2="211" stroke="#c9c2cf" stroke-width="1.4"/>
    <line x1="106" y1="204" x2="122" y2="206" stroke="#c9c2cf" stroke-width="1.4"/>
    <line x1="106" y1="211" x2="122" y2="212" stroke="#c9c2cf" stroke-width="1.4"/>
    <!-- head -->
    <rect x="93" y="148" width="14" height="14" fill="#f2c9a6"/>
    <circle cx="100" cy="132" r="23" fill="#f5d2ad"/>
    <g fill="#2a1a10">
      <circle cx="81" cy="115" r="11"/><circle cx="96" cy="108" r="12"/><circle cx="113" cy="112" r="11"/>
      <circle cx="122" cy="124" r="8"/><circle cx="76" cy="128" r="8"/>
    </g>
    <!-- content closed-eyes, calm reading -->
    <path d="M88 132 q5 -4 10 0" stroke="#1f9e54" stroke-width="2.4" fill="none"/>
    <path d="M102 132 q5 -4 10 0" stroke="#1f9e54" stroke-width="2.4" fill="none"/>
    <path d="M92 144 q8 4 16 0" stroke="#9c5a32" stroke-width="2.2" fill="none" stroke-linecap="round"/>
    <text x="132" y="120" font-size="14" fill="#ff6fc0">&#9825;</text>
    <text x="140" y="106" font-size="10" fill="#ff9fd8">&#9825;</text>
    <!-- book title banner -->
    <rect x="24" y="284" width="152" height="26" rx="8" fill="#fff0fb" stroke="#ff8fdf" stroke-width="2"/>
    <text x="100" y="301" font-size="11" fill="#9b59d0" text-anchor="middle" font-family="Comic Sans MS, Comic Neue, cursive">&ldquo;${book}&rdquo;</text>
  </svg>`;
}

function miniPortrait(which) {
  if (which === 'w') {
    return `<svg viewBox="0 0 40 40"><circle cx="20" cy="22" r="16" fill="#f9d8b8"/>
      <path d="M5 22 Q3 4 20 3 Q37 4 35 22 Q28 12 20 12 Q12 12 5 22Z" fill="#3a2014"/>
      <ellipse cx="14" cy="22" rx="3.5" ry="4.5" fill="#fff"/><ellipse cx="26" cy="22" rx="3.5" ry="4.5" fill="#fff"/>
      <circle cx="14" cy="23" r="2.2" fill="#7a4a24"/><circle cx="26" cy="23" r="2.2" fill="#7a4a24"/>
      <path d="M16 31 q4 3 8 0" stroke="#e0249a" stroke-width="2" fill="none"/></svg>`;
  }
  return `<svg viewBox="0 0 40 40"><circle cx="20" cy="23" r="15" fill="#f5d2ad"/>
    <g fill="#2a1a10"><circle cx="11" cy="13" r="6"/><circle cx="20" cy="9" r="7"/><circle cx="29" cy="13" r="6"/><circle cx="32" cy="20" r="4"/><circle cx="8" cy="20" r="4"/></g>
    <circle cx="14" cy="23" r="2.4" fill="#1f9e54"/><circle cx="26" cy="23" r="2.4" fill="#1f9e54"/>
    <path d="M16 31 q4 2 8 0" stroke="#9c5a32" stroke-width="2" fill="none"/></svg>`;
}

// ---------- state ----------
const MAXHP = 100;
let st = {};
function freshState() {
  st = { womenHP: MAXHP, menHP: MAXHP, round: 1, combo: 0, best: 0, score: 0,
         busy: false, current: null, lastThing: null, over: false };
}

// ---------- elements ----------
const $ = id => document.getElementById(id);
const elWord = $('word'), elRound = $('roundNum'), elScore = $('scoreMini');
const elFillW = $('fillW'), elLagW = $('lagW'), elFillM = $('fillM'), elLagM = $('lagM');
const elHeroine = $('heroine'), elTri = $('triathlete'), elStage = $('stage');
const elProj = $('projectile'), elImpact = $('impact'), elCombo = $('combo');
const elReason = $('reasonPop'), elAlert = $('alert'), elAnn = $('announce'), elAnnTxt = $('announceTxt');
const elVic = $('victory'), elBtnW = $('btnWomen'), elBtnM = $('btnMen');

// ---------- helpers ----------
function correctSide(v) {
  if (v === 'FOR WOMEN' || v === 'NOT FOR MEN') return 'WOMEN';
  if (v === 'FOR MEN') return 'MEN';
  return 'CLASSIFIED';
}
function vclass(v){ return v==='FOR WOMEN'?'v-women':v==='NOT FOR MEN'?'v-notmen':v==='FOR MEN'?'v-men':'v-classified'; }
function rand(a){ return a[Math.floor(Math.random()*a.length)]; }

function setBars() {
  const w = Math.max(0, st.womenHP), m = Math.max(0, st.menHP);
  elFillW.style.width = w + '%'; elLagW.style.width = w + '%';
  elFillM.style.width = m + '%'; elLagM.style.width = m + '%';
}
function damageBar(side, amount) {
  if (side === 'men') { st.menHP = Math.max(0, st.menHP - amount); $('fillM').style.width = st.menHP + '%'; $('lagM').style.width = st.menHP + '%'; }
  else { st.womenHP = Math.max(0, st.womenHP - amount); $('fillW').style.width = st.womenHP + '%'; $('lagW').style.width = st.womenHP + '%'; }
}

function floatText(big, dmg, cls) {
  const f = document.createElement('div');
  f.className = 'floater ' + (cls||'');
  f.innerHTML = `<span class="big">${big}</span>` + (dmg!=null?`<span class="dmg">-${dmg}</span>`:'');
  f.style.left = (cls==='miss'?'18%':'66%');
  elStage.appendChild(f);
  setTimeout(()=>f.remove(), 1300);
}

function showReason(v, reason) {
  elReason.innerHTML = `<span class="verdict-chip ${vclass(v)}">${v}</span><div class="reason-text">&ldquo;${reason}&rdquo;</div>`;
  elReason.classList.add('show');
}
function hideReason(){ elReason.classList.remove('show'); }

function announce(text, cb) {
  elAnnTxt.textContent = text; elAnn.classList.remove('show'); void elAnn.offsetWidth;
  elAnn.classList.add('show');
  setTimeout(()=>{ elAnn.classList.remove('show'); if(cb) cb(); }, 900);
}

function nextRound() {
  if (st.over) return;
  hideReason();
  st.busy = false; elBtnW.disabled = false; elBtnM.disabled = false;
  pickWord();
}

function pickWord() {
  let pool = RULINGS;
  // rare CLASSIFIED alarm ~12%
  if (Math.random() < 0.12) {
    const cls = RULINGS.filter(r => r.verdict === 'CLASSIFIED');
    if (cls.length) pool = cls;
  }
  let c = rand(pool), tries = 0;
  while (c.thing === st.lastThing && tries < 25) { c = rand(pool); tries++; }
  st.current = c; st.lastThing = c.thing;
  elWord.textContent = c.thing.toUpperCase();
  elRound.textContent = st.round;
  elScore.textContent = 'SCORE ' + st.score;
}

// ---------- attack sequences ----------
function launchProjectile(dir, label, onImpact) {
  // dir: 'toMen' (heroine -> right) or 'toWomen' (man -> left)
  const stageW = elStage.clientWidth;
  elProj.textContent = label;
  elProj.style.setProperty('--travel', Math.round(stageW * 0.52) + 'px');
  elProj.classList.remove('fly','flyBack'); void elProj.offsetWidth;
  if (dir === 'toMen') { elProj.style.left = '24%'; elProj.style.right=''; elProj.classList.add('fly'); }
  else { elProj.style.left=''; elProj.style.right = '24%'; elProj.classList.add('flyBack'); }
  const handler = () => { elProj.style.opacity = 0; elProj.removeEventListener('animationend', handler); onImpact(); };
  elProj.addEventListener('animationend', handler);
}
function impactAt(side) {
  elImpact.style.setProperty('--ix', side==='men' ? '78%' : '22%');
  elImpact.style.setProperty('--iy', '46%');
  elImpact.classList.remove('boom'); void elImpact.offsetWidth; elImpact.classList.add('boom');
  elStage.classList.remove('shake'); void elStage.offsetWidth; elStage.classList.add('shake');
}

function doCorrect() {
  st.combo += 1; st.best = Math.max(st.best, st.combo);
  const crit = st.combo >= 3;
  let dmg = 15 + Math.min(st.combo, 6) * 3 + (crit ? 9 : 0);   // grows with combo
  st.score += 10 * st.combo;
  const v = st.current.verdict, reason = st.current.reason, label = st.current.thing.toUpperCase();

  elHeroine.classList.add('lungeL');
  setTimeout(()=>elHeroine.classList.remove('lungeL'), 500);

  launchProjectile('toMen', label, () => {
    impactAt('men');
    elTri.classList.add('hitR','flash');
    setTimeout(()=>elTri.classList.remove('hitR','flash'), 520);
    damageBar('men', dmg);
    const tag = crit ? 'CRITICAL HIT' : (v === 'FOR WOMEN' ? 'SPIRIT DAMAGE' : 'RULING LANDS');
    floatText(tag, dmg, crit ? 'crit' : '');
    if (st.combo > 1) { elCombo.textContent = '\u2605 COMBO x' + st.combo + ' \u2605'; elCombo.classList.remove('show'); void elCombo.offsetWidth; elCombo.classList.add('show'); }
    showReason(v, reason);
    setBars();
    if (st.menHP <= 0) { koSequence('WOMEN'); }
    else { st.round += 1; setTimeout(nextRound, 1700); }
  });
}

function doWrong() {
  st.combo = 0;
  const dmg = 20;
  const v = st.current.verdict, reason = st.current.reason;

  elTri.classList.add('lungeR');
  setTimeout(()=>elTri.classList.remove('lungeR'), 500);

  launchProjectile('toWomen', 'WRONG', () => {
    impactAt('women');
    elHeroine.classList.add('hitL','flash');
    setTimeout(()=>elHeroine.classList.remove('hitL','flash'), 520);
    damageBar('women', dmg);
    floatText('NOT QUITE', dmg, 'miss');
    showReason(v, reason);
    setBars();
    if (st.womenHP <= 0) { koSequence('MEN'); }
    else { st.round += 1; setTimeout(nextRound, 1700); }
  });
}

function doClassified() {
  const v = st.current.verdict, reason = st.current.reason;
  elAlert.classList.remove('on'); void elAlert.offsetWidth; elAlert.classList.add('on');
  elStage.classList.remove('shake'); void elStage.offsetWidth; elStage.classList.add('shake');
  floatText('\u26A0 CLASSIFIED \u26A0', null, 'crit');
  showReason(v, reason);
  st.score += 1; elScore.textContent = 'SCORE ' + st.score;
  st.round += 1; setTimeout(nextRound, 1900);
}

function onGuess(side) {
  if (st.busy || st.over || !st.current) return;
  st.busy = true; elBtnW.disabled = true; elBtnM.disabled = true;
  const cs = correctSide(st.current.verdict);
  if (cs === 'CLASSIFIED') doClassified();
  else if (side === cs) doCorrect();
  else doWrong();
}

// ---------- KO / victory ----------
function koSequence(winner) {
  st.over = true; st.busy = true;
  elBtnW.disabled = true; elBtnM.disabled = true;
  setBars();
  announce('K.O.!', () => showVictory(winner));
}

function showVictory(winner) {
  if (winner === 'WOMEN') {
    elHeroine.style.animation = 'none';
    $('victorySvg').innerHTML = heroineVictory();
    $('victoryTitle').innerHTML = 'FLAWLESS,<br>OBVIOUSLY';
    $('victorySub').textContent = 'Team Women takes the ruling. It was always going to be for women.';
  } else {
    const book = rand(BOOKS);
    $('victorySvg').innerHTML = triathleteVictory(book);
    $('victoryTitle').innerHTML = 'TEAM MEN WINS';
    $('victorySub').innerHTML = 'He sits down, opens &ldquo;' + book + ',&rdquo; and begins, quietly, to grow. We are proud of him.';
  }
  elVic.classList.add('show');
}

// ---------- boot ----------
function start() {
  $('portraitW').innerHTML = miniPortrait('w');
  $('portraitM').innerHTML = miniPortrait('m');
  freshState();
  elHeroine.innerHTML = heroineStance();
  elTri.innerHTML = triathleteStance();
  elHeroine.style.animation = ''; elTri.style.animation = '';
  elVic.classList.remove('show');
  hideReason();
  setBars();
  pickWord();
  announce('ROUND 1  FIGHT!');
}

elBtnW.addEventListener('click', () => onGuess('WOMEN'));
elBtnM.addEventListener('click', () => onGuess('MEN'));
$('playAgain').addEventListener('click', start);
start();
</script>
"""


# ---------------------------------------------------------------------------
# Render the game: inject the rulings as JSON, then embed the self-contained
# arcade screen in an isolated iframe.
# ---------------------------------------------------------------------------
GAME_HTML = GAME_TEMPLATE.replace("__RULINGS_JSON__", json.dumps(ALL_RULINGS))

try:
    components.html(GAME_HTML, height=716, scrolling=False)
except Exception:
    # Future-proof fallback: wrap the game in an isolated srcdoc iframe so its
    # CSS/JS can never leak into the host page, even if components.html is gone.
    import html as _html
    _frame = (
        '<iframe style="width:100%;height:716px;border:none;" '
        'srcdoc="' + _html.escape(GAME_HTML, quote=True) + '"></iframe>'
    )
    st.html(_frame, unsafe_allow_javascript=True)


# ---------------------------------------------------------------------------
# HOW TO RUN LOCALLY
# ---------------------------------------------------------------------------
# 1. pip install streamlit
# 2. streamlit run app.py
# 3. Opens in your browser (usually http://localhost:8501).
#
# HOW TO PLAY
#   - A WORD appears above the arena. Hit FOR WOMEN or FOR MEN.
#   - "NOT FOR MEN" verdicts count as the WOMEN side.
#   - Correct guesses make the heroine attack: the ruling flies across the
#     screen, the triathlete gets hit, Team Men's health drops, combos build.
#   - Wrong guesses cost Team Women health.
#   - Rare CLASSIFIED words trigger a flashing red alert (no damage).
#   - Knock a team to zero HP for the victory screen.
# ---------------------------------------------------------------------------
