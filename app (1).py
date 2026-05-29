import random
import streamlit as st

# ---------------------------------------------------------------------------
# THAT'S NOT FOR YOU  -  ARCADE EDITION
# A forgotten arcade machine that exists solely to determine whether random
# objects are FOR WOMEN or FOR MEN.
# Official rulings from the International Institute of That's Not For You(TM)
# ---------------------------------------------------------------------------

st.set_page_config(page_title="THAT'S NOT FOR YOU", page_icon="✨", layout="centered")

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
# RARE CLASSIFIED EVENTS  -  additive only (the existing RULINGS are untouched).
# These trigger the flashing red-alert special animation.
# ---------------------------------------------------------------------------
CLASSIFIED_SPECIALS = [
    {"thing": "Penguins", "verdict": "CLASSIFIED", "reason": "Ongoing investigation."},
    {"thing": "Helicopters", "verdict": "CLASSIFIED", "reason": "Files sealed by the Institute."},
    {"thing": "The number 7", "verdict": "CLASSIFIED", "reason": "We don't talk about it."},
    {"thing": "Geese", "verdict": "CLASSIFIED", "reason": "Pending tribunal."},
    {"thing": "Mondays", "verdict": "CLASSIFIED", "reason": "Above your clearance level."},
]

# Books the gentleman reads in his victory scene (affectionate, not mean).
FEMINIST_READS = ["Invisible Women", "The Second Sex", "Men Explain Things To Me"]


# ---------------------------------------------------------------------------
# Game logic helpers
# ---------------------------------------------------------------------------
def correct_side(verdict):
    """Which giant button is the 'right' answer for a verdict."""
    if verdict in ("FOR WOMEN", "NOT FOR MEN"):
        return "WOMEN"
    if verdict == "FOR MEN":
        return "MEN"
    return "CLASSIFIED"


def new_round():
    """Pick a fresh word, never the one shown immediately before."""
    last = st.session_state.get("current")
    last_thing = last["thing"] if last else None

    # ~12% of the time, a rare CLASSIFIED alarm event.
    if random.random() < 0.12:
        pool = CLASSIFIED_SPECIALS
    else:
        pool = RULINGS

    choice = random.choice(pool)
    if last_thing is not None:
        tries = 0
        while choice["thing"] == last_thing and tries < 20:
            choice = random.choice(pool)
            tries += 1

    st.session_state.current = choice
    st.session_state.phase = "guess"
    st.session_state.result = None
    st.session_state.last_guess = None
    st.session_state.hit_side = None
    st.session_state.gained = 0
    st.session_state.appealed = False
    st.session_state.book = random.choice(FEMINIST_READS)


def reset_game():
    st.session_state.women_hp = 100
    st.session_state.men_hp = 100
    st.session_state.score = 0
    st.session_state.combo = 0
    st.session_state.best_combo = 0
    st.session_state.round = 1
    st.session_state.winner = None
    new_round()


def apply_guess(side):
    """Resolve the player's guess. Player fights on Team Women: correct guesses
    hit Team Men; wrong guesses cost Team Women health."""
    cur = st.session_state.current
    cside = correct_side(cur["verdict"])

    if cside == "CLASSIFIED":
        # Rare alarm event: no damage, small consolation point.
        st.session_state.result = "CLASSIFIED"
        st.session_state.gained = 1
        st.session_state.score += 1
        st.session_state.hit_side = None
    elif side == cside:
        st.session_state.result = "CORRECT"
        st.session_state.combo += 1
        st.session_state.best_combo = max(st.session_state.best_combo, st.session_state.combo)
        dmg = 12 + min(st.session_state.combo, 6) * 4          # combo hits harder
        st.session_state.men_hp = max(0, st.session_state.men_hp - dmg)
        st.session_state.gained = 10 * st.session_state.combo   # combo scoring
        st.session_state.score += st.session_state.gained
        st.session_state.hit_side = "men"
    else:
        st.session_state.result = "WRONG"
        st.session_state.combo = 0
        st.session_state.women_hp = max(0, st.session_state.women_hp - 18)
        st.session_state.gained = 0
        st.session_state.hit_side = "women"

    # Check for a knockout.
    if st.session_state.men_hp <= 0:
        st.session_state.winner = "WOMEN"
        st.session_state.phase = "victory"
    elif st.session_state.women_hp <= 0:
        st.session_state.winner = "MEN"
        st.session_state.phase = "victory"
    else:
        st.session_state.phase = "reveal"


# ---------------------------------------------------------------------------
# Session state bootstrap
# ---------------------------------------------------------------------------
if "phase" not in st.session_state:
    reset_game()


# ===========================================================================
# CHARACTER ART  (inline SVG - no copyrighted images, just Y2K vibes)
# ===========================================================================
def heroine_svg(pose="idle"):
    """Team Women heroine: brunette, huge round eyes, platform boots,
    sparkly outfit. Winx / Bratz / Totally Spies energy. Fully fictional."""
    arms = (
        # victory: both arms thrown up, magical-girl pose
        '<path d="M40 96 Q18 70 26 44" stroke="#f2c9a6" stroke-width="9" fill="none" stroke-linecap="round"/>'
        '<path d="M80 96 Q102 70 94 44" stroke="#f2c9a6" stroke-width="9" fill="none" stroke-linecap="round"/>'
        if pose == "victory" else
        # idle: hand on hip, other hand out, confident
        '<path d="M40 98 Q22 108 30 126" stroke="#f2c9a6" stroke-width="9" fill="none" stroke-linecap="round"/>'
        '<path d="M82 98 Q104 100 100 84" stroke="#f2c9a6" stroke-width="9" fill="none" stroke-linecap="round"/>'
    )
    sparkle_extra = (
        '<g fill="#fff">'
        '<path d="M60 6 l3 7 7 3 -7 3 -3 7 -3-7 -7-3 7-3z"/>'
        '<path d="M16 30 l2 5 5 2 -5 2 -2 5 -2-5 -5-2 5-2z"/>'
        '<path d="M104 30 l2 5 5 2 -5 2 -2 5 -2-5 -5-2 5-2z"/>'
        '</g>' if pose == "victory" else ''
    )
    return f'''
<svg viewBox="0 0 120 230" xmlns="http://www.w3.org/2000/svg" class="char-svg">
  {sparkle_extra}
  <!-- long brunette hair (back) -->
  <path d="M30 52 Q20 120 34 170 L46 168 Q40 110 46 60 Z" fill="#5a3320"/>
  <path d="M90 52 Q100 120 86 170 L74 168 Q80 110 74 60 Z" fill="#5a3320"/>
  <!-- legs -->
  <rect x="50" y="150" width="8" height="40" rx="4" fill="#f2c9a6"/>
  <rect x="63" y="150" width="8" height="40" rx="4" fill="#f2c9a6"/>
  <!-- chunky platform boots -->
  <rect x="44" y="186" width="18" height="26" rx="5" fill="#d23c9b"/>
  <rect x="60" y="186" width="18" height="26" rx="5" fill="#d23c9b"/>
  <rect x="42" y="206" width="22" height="10" rx="4" fill="#fff"/>
  <rect x="58" y="206" width="22" height="10" rx="4" fill="#fff"/>
  <!-- sparkly dress -->
  <path d="M42 96 Q60 86 78 96 L86 152 Q60 162 34 152 Z" fill="url(#dress)"/>
  <circle cx="52" cy="120" r="2" fill="#fff"/><circle cx="66" cy="132" r="2" fill="#fff"/>
  <circle cx="60" cy="110" r="2" fill="#fff"/><circle cx="72" cy="124" r="2" fill="#fff"/>
  {arms}
  <!-- neck + head -->
  <rect x="55" y="78" width="10" height="12" fill="#f2c9a6"/>
  <circle cx="60" cy="62" r="22" fill="#f7d3b0"/>
  <!-- hair front + fringe -->
  <path d="M38 60 Q36 34 60 32 Q84 34 82 60 Q74 48 60 48 Q46 48 38 60 Z" fill="#6b3d24"/>
  <!-- huge round eyes -->
  <ellipse cx="51" cy="62" rx="7" ry="9" fill="#fff"/>
  <ellipse cx="69" cy="62" rx="7" ry="9" fill="#fff"/>
  <circle cx="51" cy="63" r="4.5" fill="#7b2ff7"/>
  <circle cx="69" cy="63" r="4.5" fill="#7b2ff7"/>
  <circle cx="52.5" cy="61" r="1.6" fill="#fff"/>
  <circle cx="70.5" cy="61" r="1.6" fill="#fff"/>
  <!-- lashes -->
  <path d="M44 58 q4 -3 8 -1" stroke="#3a2014" stroke-width="1.5" fill="none"/>
  <path d="M62 57 q4 -2 9 1" stroke="#3a2014" stroke-width="1.5" fill="none"/>
  <!-- blush + glossy smile -->
  <circle cx="46" cy="70" r="3" fill="#ffb3d9" opacity="0.8"/>
  <circle cx="74" cy="70" r="3" fill="#ffb3d9" opacity="0.8"/>
  <path d="M54 73 q6 6 12 0" stroke="#d6248f" stroke-width="2.5" fill="none" stroke-linecap="round"/>
  <defs>
    <linearGradient id="dress" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#ff79d2"/><stop offset="1" stop-color="#9b5cff"/>
    </linearGradient>
  </defs>
</svg>'''


def triathlete_svg(pose="idle"):
    """Team Men: curly hair, green eyes, triathlon suit, slightly confused but
    determined. Victory = sits down and reads feminist literature. Fully fictional."""
    if pose == "victory":
        book = st.session_state.get("book", FEMINIST_READS[0])
        return f'''
<svg viewBox="0 0 120 230" xmlns="http://www.w3.org/2000/svg" class="char-svg">
  <!-- seated, content, reading -->
  <rect x="30" y="150" width="64" height="14" rx="6" fill="#7a8aa0"/>            <!-- bench -->
  <rect x="40" y="120" width="40" height="34" rx="10" fill="#21314a"/>          <!-- tri-suit torso -->
  <!-- folded legs -->
  <rect x="40" y="150" width="40" height="9" rx="4" fill="#21314a"/>
  <rect x="34" y="156" width="14" height="9" rx="4" fill="#f2c9a6"/>
  <rect x="72" y="156" width="14" height="9" rx="4" fill="#f2c9a6"/>
  <!-- arms holding book -->
  <path d="M44 128 Q40 140 50 142" stroke="#f2c9a6" stroke-width="8" fill="none" stroke-linecap="round"/>
  <path d="M76 128 Q80 140 70 142" stroke="#f2c9a6" stroke-width="8" fill="none" stroke-linecap="round"/>
  <!-- the book -->
  <rect x="44" y="128" width="32" height="22" rx="2" fill="#ffffff" stroke="#d6248f" stroke-width="2"/>
  <line x1="60" y1="129" x2="60" y2="149" stroke="#ffb3d9" stroke-width="1.5"/>
  <!-- head -->
  <rect x="55" y="104" width="10" height="12" fill="#f2c9a6"/>
  <circle cx="60" cy="92" r="20" fill="#f7d3b0"/>
  <!-- curly hair -->
  <g fill="#3a2414">
    <circle cx="46" cy="78" r="9"/><circle cx="58" cy="72" r="10"/>
    <circle cx="72" cy="78" r="9"/><circle cx="78" cy="88" r="7"/>
    <circle cx="42" cy="88" r="7"/>
  </g>
  <!-- green eyes, calm, content -->
  <path d="M50 92 q4 -3 8 0" stroke="#1f7a3d" stroke-width="2.5" fill="none"/>
  <path d="M62 92 q4 -3 8 0" stroke="#1f7a3d" stroke-width="2.5" fill="none"/>
  <path d="M52 100 q8 4 16 0" stroke="#7a4a2a" stroke-width="2" fill="none" stroke-linecap="round"/>
  <!-- little reading hearts -->
  <text x="86" y="96" font-size="11" fill="#ff6fc0">&#9825;</text>
  <text x="92" y="84" font-size="8" fill="#ff9fd8">&#9825;</text>
  <!-- book title banner -->
  <rect x="14" y="200" width="92" height="22" rx="6" fill="#fff0fb" stroke="#ff8fdf" stroke-width="2"/>
  <text x="60" y="215" font-size="9" fill="#9b59d0" text-anchor="middle" font-family="Comic Sans MS, cursive">"{book}"</text>
</svg>'''
    # idle fighting stance
    return '''
<svg viewBox="0 0 120 230" xmlns="http://www.w3.org/2000/svg" class="char-svg">
  <!-- legs -->
  <rect x="50" y="150" width="9" height="40" rx="4" fill="#f2c9a6"/>
  <rect x="63" y="150" width="9" height="40" rx="4" fill="#f2c9a6"/>
  <!-- running shoes -->
  <rect x="44" y="186" width="20" height="12" rx="5" fill="#16c0a8"/>
  <rect x="60" y="186" width="20" height="12" rx="5" fill="#16c0a8"/>
  <!-- tri-suit torso -->
  <path d="M42 96 Q60 90 78 96 L82 152 Q60 158 38 152 Z" fill="#21314a"/>
  <path d="M42 96 L38 152 Q49 156 50 152 L52 96 Z" fill="#16c0a8" opacity="0.85"/>  <!-- stripe -->
  <circle cx="68" cy="112" r="7" fill="#fff"/>
  <text x="68" y="116" font-size="9" fill="#21314a" text-anchor="middle" font-family="Arial">7</text>
  <!-- arms, raised but unsure -->
  <path d="M44 100 Q26 96 30 78" stroke="#f2c9a6" stroke-width="9" fill="none" stroke-linecap="round"/>
  <path d="M80 100 Q98 104 96 120" stroke="#f2c9a6" stroke-width="9" fill="none" stroke-linecap="round"/>
  <!-- neck + head -->
  <rect x="55" y="80" width="10" height="12" fill="#f2c9a6"/>
  <circle cx="60" cy="66" r="20" fill="#f7d3b0"/>
  <!-- curly hair -->
  <g fill="#3a2414">
    <circle cx="46" cy="52" r="9"/><circle cx="58" cy="46" r="10"/>
    <circle cx="72" cy="52" r="9"/><circle cx="78" cy="62" r="7"/>
    <circle cx="42" cy="62" r="7"/>
  </g>
  <!-- green eyes, one brow up = confused but determined -->
  <ellipse cx="53" cy="66" rx="4.5" ry="5.5" fill="#fff"/>
  <ellipse cx="68" cy="66" rx="4.5" ry="5.5" fill="#fff"/>
  <circle cx="53" cy="67" r="2.6" fill="#1f7a3d"/>
  <circle cx="68" cy="67" r="2.6" fill="#1f7a3d"/>
  <path d="M47 58 q5 -4 10 -1" stroke="#3a2414" stroke-width="2" fill="none"/>   <!-- raised brow -->
  <path d="M62 59 q5 -1 10 1" stroke="#3a2414" stroke-width="2" fill="none"/>
  <path d="M54 76 q6 2 12 0" stroke="#7a4a2a" stroke-width="2" fill="none" stroke-linecap="round"/>
  <text x="92" y="58" font-size="12" fill="#7a8aa0" font-family="Arial">?</text>
</svg>'''


# ===========================================================================
# CSS  -  Y2K arcade, built on the original pink/lilac/glossy aesthetic
# ===========================================================================
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Comic+Neue:wght@400;700&family=Press+Start+2P&display=swap');

    .stApp {
        background:
            radial-gradient(circle at 18% 12%, #ffffff 0%, transparent 38%),
            radial-gradient(circle at 82% 88%, #ffffff 0%, transparent 38%),
            linear-gradient(135deg, #ffd6f5 0%, #e7d6ff 50%, #ffe9fb 100%);
        background-attachment: fixed;
    }
    #MainMenu, header, footer {visibility: hidden;}
    .block-container { max-width: 760px; padding-top: 1.4rem; }

    /* floating background hearts + stars */
    .bg-deco { position: fixed; inset: 0; pointer-events: none; z-index: 0; overflow: hidden; }
    .bg-deco span {
        position: absolute; font-size: 20px; opacity: 0.55;
        animation: floaty 7s ease-in-out infinite;
    }
    @keyframes floaty { 0%,100% { transform: translateY(0) rotate(0); }
                        50% { transform: translateY(-16px) rotate(12deg); } }

    .tnfy-sparkles { text-align:center; font-size:18px; letter-spacing:6px;
                     color:#ff8fdf; margin: 2px 0 4px; }
    .tnfy-title {
        font-family:'Press Start 2P', monospace; font-size:24px; line-height:1.5;
        text-align:center; color:#ff4fb0;
        text-shadow: 2px 2px 0 #fff, 3px 3px 0 #c98bff, 4px 4px 6px rgba(123,47,247,.4);
        letter-spacing:1px; margin-bottom:4px;
    }
    .tnfy-subtitle { font-family:'Comic Neue', cursive; text-align:center; font-size:14px;
                     color:#9b59d0; font-style:italic; margin-bottom:10px; }

    /* the arcade cabinet frame */
    .cabinet {
        position: relative; z-index: 1;
        background: linear-gradient(180deg,#fff 0%,#fff0fb 100%);
        border: 4px solid #ff8fdf; border-radius: 22px; padding: 14px;
        box-shadow: 0 0 0 4px #fff, 0 0 0 8px #d9b8ff,
                    inset 0 0 24px rgba(255,143,223,.25),
                    0 12px 30px rgba(180,100,220,.35);
    }

    /* HUD: health bars + names */
    .hud { display:flex; justify-content:space-between; gap:10px; margin-bottom:6px; }
    .hud-side { flex:1; }
    .hud-name { font-family:'Press Start 2P', monospace; font-size:9px; margin-bottom:4px; }
    .hud-name.l { color:#d6248f; text-align:left; }
    .hud-name.r { color:#2f72f7; text-align:right; }
    .hpbar { height:16px; border:3px solid #fff; border-radius:10px; background:#3a2a40;
             box-shadow:0 2px 0 rgba(0,0,0,.15); overflow:hidden; }
    .hpfill { height:100%; transition:width .4s ease; }
    .hp-w { background:linear-gradient(90deg,#ff5fc0,#ffd0ef); }
    .hp-m { background:linear-gradient(270deg,#2f72f7,#bfe0ff); margin-left:auto; }

    .scorebar { display:flex; justify-content:center; gap:14px; flex-wrap:wrap;
                font-family:'Press Start 2P', monospace; font-size:9px; color:#7b2ff7;
                margin:8px 0 2px; }
    .scorebar b { color:#d6248f; }
    .combo-pop { font-family:'Press Start 2P', monospace; font-size:13px; color:#ff2fa8;
                 text-align:center; text-shadow:1px 1px 0 #fff;
                 animation: pop .4s ease; }
    @keyframes pop { 0%{transform:scale(0);} 70%{transform:scale(1.3);} 100%{transform:scale(1);} }

    .round-banner { text-align:center; font-family:'Press Start 2P', monospace; font-size:12px;
                    color:#9b59d0; margin:6px 0 2px; letter-spacing:1px; }

    /* battlefield: heroine | arena | triathlete */
    .battlefield { display:flex; align-items:flex-end; justify-content:space-between; gap:6px;
                   margin:6px 0; }
    .fighter { width:26%; }
    .char-svg { width:100%; height:auto; max-height:230px; filter: drop-shadow(0 6px 6px rgba(123,47,247,.25)); }
    @keyframes shake { 0%,100%{transform:translateX(0);} 20%{transform:translateX(-7px) rotate(-3deg);}
                       40%{transform:translateX(7px) rotate(3deg);} 60%{transform:translateX(-5px);}
                       80%{transform:translateX(5px);} }
    .hit { animation: shake .45s ease; }
    @keyframes win-bounce { 0%,100%{transform:translateY(0) scale(1);} 50%{transform:translateY(-12px) scale(1.06);} }
    .winpose { animation: win-bounce 1s ease-in-out infinite; }

    /* center arena card */
    .arena {
        flex:1; min-height:200px; display:flex; flex-direction:column; justify-content:center;
        background: radial-gradient(circle at 50% 25%, #fff 0%, #ffe9fb 70%);
        border:4px solid #ff8fdf; border-radius:18px; padding:14px 10px; text-align:center;
        box-shadow: inset 0 0 18px rgba(255,143,223,.4), 0 0 0 3px #fff;
        position:relative;
    }
    .arena::before { content:"VS"; position:absolute; top:-12px; left:50%; transform:translateX(-50%);
        background:#7b2ff7; color:#fff; font-family:'Press Start 2P',monospace; font-size:9px;
        padding:4px 8px; border-radius:8px; box-shadow:0 2px 0 #4a1a9a; }
    .arena-word { font-family:'Press Start 2P', monospace; font-size:18px; color:#7b2ff7;
                  line-height:1.5; word-break:break-word; margin:6px 0; }
    .arena-prompt { font-family:'Comic Neue', cursive; font-size:14px; color:#9b59d0; font-style:italic; }
    .arena-verdict { display:inline-block; font-family:'Comic Neue', cursive; font-weight:700;
                     font-size:19px; padding:6px 16px; border-radius:999px; margin:8px 0 4px;
                     border:3px solid #fff; box-shadow:0 3px 0 rgba(0,0,0,.08); }
    .v-women{background:#ffd0ef;color:#d6248f;} .v-notmen{background:#e3d2ff;color:#7b2ff7;}
    .v-men{background:#d6ecff;color:#2f72f7;} .v-classified{background:#fff3c4;color:#b8860b;}
    .arena-reason { font-family:'Comic Neue', cursive; font-size:15px; font-style:italic; color:#6a4a8a; }
    .result-badge { font-family:'Press Start 2P', monospace; font-size:16px; margin-top:10px; }
    .r-correct{color:#2faa6a; text-shadow:1px 1px 0 #fff;}
    .r-wrong{color:#e23c6a; text-shadow:1px 1px 0 #fff;}

    /* CLASSIFIED red alert */
    .alert .arena { animation: alarm .5s steps(2) infinite; border-color:#ff2d2d; }
    @keyframes alarm { 0%{box-shadow:inset 0 0 24px rgba(255,0,0,.6),0 0 0 4px #ff2d2d;}
                       100%{box-shadow:inset 0 0 24px rgba(255,180,0,.6),0 0 0 4px #ffb400;} }
    .alert-text { font-family:'Press Start 2P', monospace; font-size:13px; color:#ff2d2d;
                  animation: blink .4s steps(2) infinite; }
    @keyframes blink { 50%{opacity:.2;} }

    /* glossy buttons (original look) */
    div.stButton > button {
        font-family:'Comic Neue', cursive; font-weight:700; font-size:17px; color:#fff !important;
        background: linear-gradient(180deg,#ffa6e6 0%,#ff5fc0 50%,#ff2fa8 51%,#ff7fd4 100%);
        border:3px solid #fff; border-radius:999px; padding:10px 16px; width:100%;
        box-shadow: inset 0 2px 4px rgba(255,255,255,.8), 0 5px 0 #c12f8f, 0 8px 14px rgba(193,47,143,.4);
        transition: transform .05s ease;
    }
    div.stButton > button:hover { filter:brightness(1.05); color:#fff !important; }
    div.stButton > button:active { transform:translateY(4px);
        box-shadow: inset 0 2px 4px rgba(255,255,255,.8), 0 1px 0 #c12f8f; }

    /* the two GIANT arcade choice buttons */
    .st-key-btn_women button {
        font-family:'Press Start 2P', monospace !important; font-size:15px !important;
        padding:22px 10px !important; line-height:1.6 !important;
        background: linear-gradient(180deg,#ffb3e6 0%,#ff4fb8 50%,#e0249a 51%,#ff7fd0 100%) !important;
        box-shadow: inset 0 2px 5px rgba(255,255,255,.85), 0 7px 0 #a81f7f, 0 10px 18px rgba(168,31,127,.45) !important;
    }
    .st-key-btn_men button {
        font-family:'Press Start 2P', monospace !important; font-size:15px !important;
        padding:22px 10px !important; line-height:1.6 !important;
        background: linear-gradient(180deg,#a9d4ff 0%,#3f8bff 50%,#1f63e0 51%,#7fb0ff 100%) !important;
        box-shadow: inset 0 2px 5px rgba(255,255,255,.85), 0 7px 0 #1846a8, 0 10px 18px rgba(24,70,168,.45) !important;
    }
    .st-key-btn_men button:active, .st-key-btn_women button:active { transform:translateY(5px) !important; }

    .appeal-note { text-align:center; font-family:'Comic Neue', cursive; font-weight:700;
                   font-size:15px; color:#d6248f; background:#fff0fb; border:2px dashed #ff8fdf;
                   border-radius:12px; padding:7px; margin-top:8px; }

    /* scrolling reggaeton / Y2K marquee */
    .marquee { overflow:hidden; white-space:nowrap; margin-top:12px; border-top:2px dotted #ff8fdf;
               border-bottom:2px dotted #ff8fdf; padding:5px 0; }
    .marquee span { display:inline-block; padding-left:100%; animation: scroll 18s linear infinite;
        font-family:'Comic Neue', cursive; color:#9b59d0; font-size:13px; }
    @keyframes scroll { to { transform: translateX(-100%); } }

    .tnfy-footer { text-align:center; font-family:'Comic Neue', cursive; font-size:12px;
                   color:#9b59d0; margin-top:14px; opacity:.9; }
    </style>
    """,
    unsafe_allow_html=True,
)

# floating background hearts + stars
st.markdown(
    '<div class="bg-deco">'
    '<span style="left:6%;top:18%;color:#ff8fdf;">&#9825;</span>'
    '<span style="left:90%;top:24%;color:#c98bff;animation-delay:1s;">&#10022;</span>'
    '<span style="left:12%;top:70%;color:#ffb3e6;animation-delay:2s;">&#10038;</span>'
    '<span style="left:84%;top:74%;color:#ff8fdf;animation-delay:.6s;">&#9825;</span>'
    '<span style="left:48%;top:8%;color:#c98bff;animation-delay:1.4s;">&#10022;</span>'
    '<span style="left:70%;top:50%;color:#ffb3e6;animation-delay:2.4s;">&#10038;</span>'
    '</div>',
    unsafe_allow_html=True,
)

# ---------------------------------------------------------------------------
# Header
# ---------------------------------------------------------------------------
st.markdown('<div class="tnfy-sparkles">&#10022; &#9733; &#9825; &#9733; &#10022;</div>', unsafe_allow_html=True)
st.markdown('<div class="tnfy-title">THAT\'S NOT FOR YOU</div>', unsafe_allow_html=True)
st.markdown('<div class="tnfy-subtitle">official rulings from the international institute &#8226; arcade edition</div>', unsafe_allow_html=True)

# ---------------------------------------------------------------------------
# Build the cabinet HTML (HUD + battlefield + arena)
# ---------------------------------------------------------------------------
S = st.session_state
phase = S.phase
cur = S.current
is_classified_now = (phase in ("reveal", "guess")) and S.get("result") == "CLASSIFIED"

VCLASS = {"FOR WOMEN": "v-women", "NOT FOR MEN": "v-notmen", "FOR MEN": "v-men", "CLASSIFIED": "v-classified"}

# fighter poses
women_pose = "victory" if (phase == "victory" and S.winner == "WOMEN") else "idle"
men_pose = "victory" if (phase == "victory" and S.winner == "MEN") else "idle"
women_cls = "fighter"
men_cls = "fighter"
if phase == "victory" and S.winner == "WOMEN":
    women_cls += " winpose"
if phase == "victory" and S.winner == "MEN":
    men_cls += " winpose"
if S.get("hit_side") == "women":
    women_cls += " hit"
if S.get("hit_side") == "men":
    men_cls += " hit"

# arena center content per phase
if phase == "guess":
    arena_inner = (
        f'<div class="arena-word">{cur["thing"].upper()}</div>'
        f'<div class="arena-prompt">FOR WOMEN&hellip; or FOR MEN?</div>'
    )
elif phase == "reveal":
    if S.result == "CLASSIFIED":
        arena_inner = (
            f'<div class="alert-text">&#9888; CLASSIFIED &#9888;</div>'
            f'<div class="arena-word">{cur["thing"].upper()}</div>'
            f'<div class="arena-verdict v-classified">CLASSIFIED</div>'
            f'<div class="arena-reason">&ldquo;{cur["reason"]}&rdquo;</div>'
            f'<div class="result-badge" style="color:#b8860b;">FILE SEALED</div>'
        )
    else:
        badge = ('<div class="result-badge r-correct">CORRECT! +%d</div>' % S.gained
                 if S.result == "CORRECT"
                 else '<div class="result-badge r-wrong">WRONG!</div>')
        arena_inner = (
            f'<div class="arena-word">{cur["thing"].upper()}</div>'
            f'<div class="arena-verdict {VCLASS.get(cur["verdict"],"v-classified")}">{cur["verdict"]}</div>'
            f'<div class="arena-reason">&ldquo;{cur["reason"]}&rdquo;</div>'
            f'{badge}'
        )
else:  # victory
    if S.winner == "WOMEN":
        arena_inner = (
            '<div class="result-badge r-correct">FLAWLESS,</div>'
            '<div class="result-badge r-correct">OBVIOUSLY</div>'
            '<div class="arena-prompt">Team Women takes the ruling. &#10022;</div>'
        )
    else:
        book = S.get("book", FEMINIST_READS[0])
        arena_inner = (
            '<div class="result-badge" style="color:#2f72f7;">TEAM MEN WINS</div>'
            f'<div class="arena-prompt">He sits down and opens<br>&ldquo;{book}&rdquo;. Growth. &#9825;</div>'
        )

alert_wrap = "alert" if (phase == "reveal" and S.result == "CLASSIFIED") else ""

# combo popup
combo_html = ""
if phase == "reveal" and S.result == "CORRECT" and S.combo > 1:
    combo_html = f'<div class="combo-pop">&#9733; COMBO x{S.combo}! &#9733;</div>'

cabinet_html = f'''
<div class="cabinet {alert_wrap}">
  <div class="hud">
    <div class="hud-side">
      <div class="hud-name l">&#9825; TEAM WOMEN</div>
      <div class="hpbar"><div class="hpfill hp-w" style="width:{S.women_hp}%;"></div></div>
    </div>
    <div class="hud-side">
      <div class="hud-name r">TEAM MEN &#9889;</div>
      <div class="hpbar"><div class="hpfill hp-m" style="width:{S.men_hp}%;"></div></div>
    </div>
  </div>
  <div class="round-banner">ROUND {S.round} &#8226; FIGHT!</div>
  {combo_html}
  <div class="battlefield">
    <div class="{women_cls}">{heroine_svg(women_pose)}</div>
    <div class="arena">{arena_inner}</div>
    <div class="{men_cls}">{triathlete_svg(men_pose)}</div>
  </div>
  <div class="scorebar">
    <span>SCORE <b>{S.score}</b></span>
    <span>COMBO <b>x{S.combo}</b></span>
    <span>BEST <b>x{S.best_combo}</b></span>
  </div>
  <div class="marquee"><span>&#9825; un verano sin datos &#9733; perreo hasta que el Instituto cierre &#9825; dial-up loading&hellip; please wait &#10022; baby one more ruling &#9733; reggaeton clearance: granted &#9825; sparkle.gif &#9825; under construction since 2004 &#10022;</span></div>
</div>
'''
st.markdown(cabinet_html, unsafe_allow_html=True)

# NOTE: CLASSIFIED events trigger the flashing red-alert visual (see the
# `.alert` CSS above) - the siren is rendered as flashing colour + blinking
# text so the app stays portable across all Streamlit versions.

# ---------------------------------------------------------------------------
# Interactive controls (Streamlit buttons) per phase
# ---------------------------------------------------------------------------
if phase == "guess":
    c1, c2 = st.columns(2)
    with c1:
        if st.button("FOR\nWOMEN", key="btn_women"):
            apply_guess("WOMEN")
            st.rerun()
    with c2:
        if st.button("FOR\nMEN", key="btn_men"):
            apply_guess("MEN")
            st.rerun()

elif phase == "reveal":
    if st.button("&#9654; NEXT ROUND", key="next"):
        S.round += 1
        new_round()
        st.rerun()
    # the beloved appeal easter egg, preserved from the original
    if st.button("appeal this ruling", key="appeal"):
        S.appealed = True
    if S.appealed:
        st.markdown('<div class="appeal-note">Appeal denied. &#10022;</div>', unsafe_allow_html=True)

else:  # victory
    if st.button("&#9733; PLAY AGAIN &#9733;", key="again"):
        reset_game()
        st.rerun()

# ---------------------------------------------------------------------------
# Footer
# ---------------------------------------------------------------------------
st.markdown(
    '<div class="tnfy-footer">Powered by the International Institute '
    'of That\'s Not For You&trade;</div>',
    unsafe_allow_html=True,
)


# ---------------------------------------------------------------------------
# HOW TO RUN LOCALLY
# ---------------------------------------------------------------------------
# 1. Install the dependency:
#       pip install streamlit
#
# 2. From the folder containing this file, run:
#       streamlit run app.py
#
# 3. Streamlit will open the app in your browser (usually http://localhost:8501).
#
# HOW TO PLAY
#   - A word appears in the arena. Hit FOR WOMEN or FOR MEN.
#   - "NOT FOR MEN" verdicts count as the WOMEN side.
#   - Correct guesses damage Team Men and build your combo (combos hit harder).
#   - Wrong guesses cost Team Women health.
#   - Rare CLASSIFIED alarms are freebies - no damage, just chaos.
#   - Knock a team's health to zero to trigger the victory animation.
# ---------------------------------------------------------------------------
