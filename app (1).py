# -*- coding: utf-8 -*-
import json
import streamlit as st
import streamlit.components.v1 as components

# ---------------------------------------------------------------------------
# THAT'S NOT FOR YOU  -  ARCADE FIGHTING EDITION (bilingual EN / AR-ES cut)
# A ridiculous magical-girl fighting game whose sole purpose is to determine
# whether random objects are FOR WOMEN or FOR MEN. Now with a "learning
# Spanish" toggle (neutral Rioplatense) so Alex can study while he loses.
# Runs entirely client-side; fighters are chunky upscaled pixel sprites.
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

RULINGS = [{'k': 'NM', 'en': ['Seatbelts', 'Thought you were a good driver?'], 'es': ['Cinturones de seguridad', '¿Te creías buen conductor?']}, {'k': 'NM', 'en': ['Glasses', 'What do men need to see so badly?'], 'es': ['Anteojos', '¿Qué necesitan ver los hombres con tanta urgencia?']}, {'k': 'W', 'en': ['Coconut water', "It's spiritual."], 'es': ['Agua de coco', 'Es espiritual.']}, {'k': 'M', 'en': ['Cockroaches', 'Self-explanatory.'], 'es': ['Cucarachas', 'Se explica solo.']}, {'k': 'W', 'en': ['Leisure time', 'Why would men rest? tired from lying??'], 'es': ['Tiempo libre', '¿Por qué descansarían los hombres? ¿cansados de mentir??']}, {'k': 'M', 'en': ['Dried grass', 'You can have this'], 'es': ['Pasto seco', 'Te lo podés quedar']}, {'k': 'NM', 'en': ['Hydration', 'What exactly were you planning to do today?'], 'es': ['Hidratación', '¿Qué tenías pensado hacer hoy, exactamente?']}, {'k': 'M', 'en': ['Cargo shorts', 'Yes please hide.'], 'es': ['Bermudas cargo', 'Sí, por favor, escondete.']}, {'k': 'W', 'en': ['Astrology', 'We invented the stars.'], 'es': ['Astrología', 'Nosotras inventamos las estrellas.']}, {'k': 'NM', 'en': ['Ladders', 'Who said you could go up?'], 'es': ['Escaleras', '¿Quién dijo que podías subir?']}, {'k': 'M', 'en': ['Grilling', 'A controlled little fire to feel in charge of.'], 'es': ['El asado', 'Un fueguito controlado para sentirse al mando.']}, {'k': 'W', 'en': ['Crying', 'An advanced emotional technology.'], 'es': ['Llorar', 'Una tecnología emocional avanzada.']}, {'k': 'NM', 'en': ['Opinions', 'Did anyone ask?'], 'es': ['Las opiniones', '¿Alguien preguntó?']}, {'k': 'M', 'en': ['Fantasy football', 'A spreadsheet that loves them back.'], 'es': ['El fantasy football', 'Una planilla que sí los quiere.']}, {'k': 'W', 'en': ['Naps', 'We earned them.'], 'es': ['Las siestas', 'Nos las ganamos.']}, {'k': 'NM', 'en': ['Maps', 'Thought you knew the way?'], 'es': ['Los mapas', '¿Creías que sabías el camino?']}, {'k': 'W', 'en': ['Sourdough starters', 'A pet you can eat.'], 'es': ['La masa madre', 'Una mascota que te podés comer.']}, {'k': 'M', 'en': ['Lawnmowers', 'A loud Saturday companion.'], 'es': ['Las cortadoras de pasto', 'Una ruidosa compañía de sábado.']}, {'k': 'NM', 'en': ['The aux cord', 'Are you sure you should be in charge of the vibe?'], 'es': ['El cable auxiliar', '¿Seguro que vos tenés que manejar la música?']}, {'k': 'W', 'en': ['Moonlight', "She's one of us."], 'es': ['La luz de la luna', 'Es una de las nuestras.']}, {'k': 'M', 'en': ['Protein powder', 'Sand for the soul.'], 'es': ['La proteína en polvo', 'Arena para el alma.']}, {'k': 'NM', 'en': ['Thermostats', 'Who told you you were cold?'], 'es': ['Los termostatos', '¿Quién te dijo que tenías frío?']}, {'k': 'NM', 'en': ['Reverse parking', 'Confident, are we?'], 'es': ['Estacionar marcha atrás', 'Confiados, ¿no?']}, {'k': 'M', 'en': ['Power tools', "Personally that's ok with me."], 'es': ['Las herramientas eléctricas', 'Personalmente, eso lo banco.']}, {'k': 'NM', 'en': ['The remote control', 'And who appointed you?'], 'es': ['El control remoto', '¿Y quién te nombró a vos?']}, {'k': 'NM', 'en': ['Directions', 'Lost again?'], 'es': ['Las direcciones', '¿Perdido de nuevo?']}, {'k': 'W', 'en': ['Journaling', "But I'll let you have this one alex."], 'es': ['Escribir un diario', 'Pero esta te la dejo, alex.']}, {'k': 'W', 'en': ['Group chats', 'The real government.'], 'es': ['Los grupos de chat', 'El verdadero gobierno.']}, {'k': 'NM', 'en': ['Loud sneezing', 'Was that necessary?'], 'es': ['Estornudar fuerte', '¿Hacía falta?']}, {'k': 'W', 'en': ['Brunch', 'A holy meal.'], 'es': ['El brunch', 'Una comida sagrada.']}, {'k': 'M', 'en': ['Riding lawnmowers', "I guess it's ok if you drive that."], 'es': ['Las cortadoras con asiento', 'Bueno, si manejás eso, pase.']}, {'k': 'NM', 'en': ['Calendars', "You forgot, didn't you?"], 'es': ['Los calendarios', 'Te olvidaste, ¿no?']}, {'k': 'M', 'en': ['Lint', 'Pocket confetti.'], 'es': ['La pelusa', 'Confeti de bolsillo.']}, {'k': 'NM', 'en': ['Standing too close', 'Why so near?'], 'es': ['Pararse muy cerca', '¿Por qué tan cerca?']}, {'k': 'M', 'en': ['Energy drinks', 'Caffeinated optimism.'], 'es': ['Las bebidas energéticas', 'Optimismo con cafeína.']}, {'k': 'NM', 'en': ['Whistling', 'Who taught you that?'], 'es': ['Silbar', '¿Quién te enseñó eso?']}, {'k': 'W', 'en': ['Flowers', "Nature's compliments."], 'es': ['Las flores', 'Los cumplidos de la naturaleza.']}, {'k': 'M', 'en': ['Folding chairs', 'You can sit I guess.'], 'es': ['Las sillas plegables', 'Te podés sentar, supongo.']}, {'k': 'NM', 'en': ['The last word', 'Are you finished?'], 'es': ['La última palabra', '¿Terminaste?']}, {'k': 'NM', 'en': ['Mansplaining', 'Did we ask you to elaborate?'], 'es': ['El mansplaining', '¿Te pedimos que explicaras?']}, {'k': 'NM', 'en': ['The thermostat (again)', 'Cold? Already?'], 'es': ['El termostato (otra vez)', '¿Frío? ¿Ya?']}, {'k': 'W', 'en': ['Lavender', 'She calms only us.'], 'es': ['La lavanda', 'Solo a nosotras nos calma.']}, {'k': 'M', 'en': ['Toolboxes', 'Like a jewelry box but you buy it for yourself.'], 'es': ['Las cajas de herramientas', 'Como un joyero, pero te lo comprás vos.']}, {'k': 'W', 'en': ['Stargazing', 'Returning home, basically.'], 'es': ['Mirar las estrellas', 'Básicamente, volver a casa.']}, {'k': 'NM', 'en': ['Loud opinions on coffee', 'Is this a TED talk?'], 'es': ['Opinar fuerte sobre el café', '¿Esto es una charla TED?']}, {'k': 'W', 'en': ['Bubble baths', 'Ritual cleansing.'], 'es': ['Los baños de espuma', 'Limpieza ritual.']}, {'k': 'M', 'en': ['Gravel', 'Decorative crunch.'], 'es': ['La grava', 'Crujido decorativo.']}, {'k': 'NM', 'en': ['Eye contact while parking', 'Nervous?'], 'es': ['Mirar a los ojos al estacionar', '¿Nervioso?']}, {'k': 'M', 'en': ['Antlers on the wall', 'Like hanging a diploma for less smart creatures.'], 'es': ['Astas en la pared', 'Como colgar un diploma para criaturas menos inteligentes.']}, {'k': 'NM', 'en': ["The phrase 'well actually'", 'Actually what?'], 'es': ['La frase «en realidad»', '¿En realidad qué?']}, {'k': 'W', 'en': ['Peonies', 'They bloom on command for us.'], 'es': ['Las peonías', 'Florecen cuando se lo pedimos.']}, {'k': 'NM', 'en': ['The fast lane', 'Somewhere to be?'], 'es': ['El carril rápido', '¿Tenés algún lado adonde ir?']}, {'k': 'W', 'en': ['Matcha', 'Green meditation.'], 'es': ['El matcha', 'Meditación verde.']}, {'k': 'W', 'en': ['Wide-leg trousers', 'Architecture.'], 'es': ['Los pantalones anchos', 'Arquitectura.']}, {'k': 'M', 'en': ['Bottle openers shaped like fish', 'A personality, allegedly.'], 'es': ['Los destapadores con forma de pez', 'Una personalidad, supuestamente.']}, {'k': 'NM', 'en': ["The phrase 'trust me'", 'Why would we?'], 'es': ['La frase «confiá en mí»', '¿Por qué lo haríamos?']}, {'k': 'W', 'en': ['Fairy lights', 'Captured stars.'], 'es': ['Las lucecitas', 'Estrellas capturadas.']}, {'k': 'NM', 'en': ['Heated debates at parties', 'Is this fun for you?'], 'es': ['Los debates acalorados en fiestas', '¿Esto te divierte?']}, {'k': 'W', 'en': ['Champagne', 'Bubbles of victory.'], 'es': ['El champán', 'Burbujas de victoria.']}, {'k': 'NM', 'en': ['The phone at dinner', 'Something more important than our date, Alex?'], 'es': ['El celular en la cena', '¿Algo más importante que nuestra cita, Alex?']}, {'k': 'W', 'en': ['Pearls', "The ocean's apology."], 'es': ['Las perlas', 'La disculpa del océano.']}, {'k': 'M', 'en': ['Camo print', 'HIDE PLEASE HIDE.'], 'es': ['El estampado militar', 'ESCONDETE POR FAVOR ESCONDETE.']}, {'k': 'NM', 'en': ['Unsolicited feedback', 'Did a request go out?'], 'es': ['Las críticas no pedidas', '¿Salió algún pedido?']}, {'k': 'W', 'en': ['Croissants', "I don't need to explain this."], 'es': ['Las medialunas', 'No necesito explicar esto.']}, {'k': 'M', 'en': ['Screws and stuff', 'No notes. None.'], 'es': ['Tornillos y esas cosas', 'Sin comentarios. Ninguno.']}, {'k': 'NM', 'en': ['The thermostat (one more time)', 'Still cold?'], 'es': ['El termostato (una vez más)', '¿Seguís con frío?']}, {'k': 'NM', 'en': ['The middle armrest', 'Both of them?'], 'es': ['El apoyabrazos del medio', '¿Los dos?']}, {'k': 'NM', 'en': ["The phrase 'calm down'", 'Excuse me?'], 'es': ['La frase «calmate»', '¿Perdón?']}, {'k': 'W', 'en': ['Linen', 'Effortless on purpose.'], 'es': ['El lino', 'Descuidado a propósito.']}, {'k': 'M', 'en': ['Fishing hats', 'A hobby worn proudly.'], 'es': ['Los sombreros de pesca', 'Un hobby usado con orgullo.']}, {'k': 'NM', 'en': ['Cutting in line', 'Were you raised in a barn?'], 'es': ['Colarse en la fila', '¿Te criaron en un establo?']}, {'k': 'W', 'en': ['Cherry blossoms', 'They time their bloom for us.'], 'es': ['Los cerezos en flor', 'Florecen en su momento para nosotras.']}, {'k': 'NM', 'en': ['Explaining the movie', 'We watched it too?'], 'es': ['Explicar la película', '¿La vimos las dos también?']}, {'k': 'NM', 'en': ['Reclining the seat fully', 'Comfortable back there?'], 'es': ['Reclinar todo el asiento', '¿Cómodo ahí atrás?']}, {'k': 'W', 'en': ['Moon phases', 'We keep the schedule.'], 'es': ['Las fases de la luna', 'Nosotras llevamos la agenda.']}, {'k': 'M', 'en': ['Toothpick chewing', 'I hope you poke the roof of your mouth.'], 'es': ['Masticar escarbadientes', 'Ojalá te pinches el paladar.']}, {'k': 'NM', 'en': ['The last slice', 'Were you going to ask?'], 'es': ['La última porción', '¿Ibas a preguntar?']}, {'k': 'W', 'en': ['Silk pillowcases', 'We deserve a soft landing.'], 'es': ['Las fundas de seda', 'Merecemos un aterrizaje suave.']}, {'k': 'W', 'en': ['Benito', 'or.. womann?? this woman.'], 'es': ['Benito', '¿o... mujerr?? esta mujer.']}, {'k': 'W', 'en': ['Bad Bunny', 'Ours. You may listen quietly.'], 'es': ['Bad Bunny', 'Nuestro. Podés escuchar calladito.']}, {'k': 'W', 'en': ['Un Verano Sin Ti', 'Required reading.'], 'es': ['Un Verano Sin Ti', 'Lectura obligatoria.']}, {'k': 'NM', 'en': ['Conejo Malo', 'Did he ever once mention you?'], 'es': ['Conejo Malo', '¿Alguna vez te nombró?']}, {'k': 'W', 'en': ['Perreo', 'A feminine science.'], 'es': ['Perreo', 'Una ciencia femenina.']}]

ROASTS = {
    # Alex gets these ONLY when he guesses correctly: positive reinforcement, but still insulting.
    'right': [
        "Good job, Harley Quinn.",
        "Good go! Your prize is a beach trip to Bolivia.",
        "Even a broken clock is right twice a day, I guess.",
        "Good job! I'll pay for half of your croissant.",
        "Fine, I'll marry into a fart family, I guess.",
        "I'll give it to you because you're cute.",
        "Nice! I'll pay for half of your croissant.",
        "Mazel tov. Bare minimum achieved.",
        "Bless him. He tried, and somehow succeeded.",
        "Swims, bikes, runs, occasionally reads the room.",
        "A child psychologist identifying categories? Groundbreaking.",
        "All that cardio finally moved blood to the brain.",
        "The watch-reading paid off. Character development.",
        "Carb-loaded for one correct answer. Inspiring.",
        "North London's finest privately educated gentleman has located one fact.",
        "Fine. That was correct. Don't make it your whole personality.",
        "He painted his nails and got an answer right. Feminism advances.",
        "Look at him learning. Slowly. But learning.",
        "Correct. I am being very generous about this.",
        "You may sit at the women's table for three minutes.",
        "One point for Alex, several concerns remain.",
        "Correct, unfortunately for my argument."
    ],
    # Alex gets these ONLY when he guesses incorrectly: discouraging / insulting messages.
    'wrong': [
        "Better luck next time, Harley.",
        "North London's finest schools and still gets it wrong.",
        "North London's finest privately educated gentleman... and still wrong.",
        "A child psychologist who can't read the room.",
        "A child psychologist who can't read a room.",
        "Shouldn't an NHS guy know this?",
        "Wow, didn't know a triathlete would get this one wrong.",
        "Flat feet, smooth brain!",
        "Worse than getting hit by a bus.",
        "All that cardio and still wrong.",
        "A triathlon first-place trophy won't help you here, babe.",
        "Reads a watch all day, can't read a room.",
        "Swims, bikes, runs, loses.",
        "Carb-loaded for absolutely nothing.",
        "Bless him. He tried.",
        "The performative era is over, sweetie.",
        "Bolivia would have guessed better.",
        "He painted his nails for moments like this.",
        "Not the privately educated frontal lobe failing us.",
        "Incorrect. Battersea is reviewing your visa.",
        "This is why the Institute was founded.",
        "A strong body and yet the answer escaped.",
        "The room was available to be read. You declined.",
        "Emotionally available, categorically unavailable.",
        "He trained for three sports and none of them was thinking.",
        "That answer was hit by a bus.",
        "Wrong, but with confidence. Dangerous combination.",
        "A historic defeat for men with Garmin watches."
    ]
}

STRINGS = {
    'en': {
        'teamW': 'MARTA',
        'teamM': 'ALEX',
        'wordLabel': 'WHO IS THIS FOR?',
        'btnW': 'FOR<br>WOMEN',
        'btnM': 'FOR<br>MEN',
        'appeal': 'appeal this ruling',
        'playAgain': 'PLAY AGAIN',
        'denied': 'APPEAL DENIED',
        'score': 'ALEX SCORE',
        'combo': 'COMBO',
        'fight': 'FIGHT!',
        'roundWord': 'ROUND',
        'ko': 'K.O.!',
        'vW': 'FOR WOMEN',
        'vNM': 'NOT FOR MEN',
        'vM': 'FOR MEN',
        'vC': 'CLASSIFIED',
        'hitW': 'MARTA DAMAGE',
        'hitM': 'ALEX DAMAGE',
        'correctWord': 'CORRECT',
        'wrongWord': 'WRONG',
        'critTags': ['CRITICAL HIT', 'HE FELT THAT', 'DEVASTATING', 'TKO ENERGY'],
        'rightTags': ['CORRECT, UNFORTUNATELY', 'FINE, YES', 'HE GOT ONE', 'ACCIDENTALLY RIGHT'],
        'wrongTags': ['WRONG, BABE', 'DID YOU LISTEN?', 'EMBARRASSING', 'THAT WAS A CHOICE'],
        'vicWTitle': 'FLAWLESS,<br>OBVIOUSLY',
        'vicWSub': 'Marta wins. It was never close. Alex may now sit quietly and reflect.',
        'vicMTitle': 'ALEX WINS',
        'vicMSub': 'He sits down, opens “[book],” and finally, finally starts listening. We are cautiously proud of him.',
        'books': ['Invisible Women', 'The Second Sex', 'How to Understand Women'],
        'marquee': '♥ welcome 2 the institute ♥ no boys allowed (we said what we said) ♥ yo perreo sola ♥ tití me preguntó ♥ un verano sin ti ♥ 🐰 el conejo is ours 🐰 ♥ battersea is the new bolivia ♥ 69 reasons why I should be your girlfriend already ♥ ur visitor #000127 ♥ cry about it ♥ dale ♥ made with luv + spite ♥',
        'footer': 'Powered by the International Institute of That’s Not For You™'
    }
}

GAME_DATA = json.dumps({"rulings": RULINGS, "roasts": ROASTS, "str": STRINGS}, ensure_ascii=False)

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
.prompt-label { font-size:13px; color:#ffd0ef; letter-spacing:3px; }
.prompt-word { display:block; font-size:38px; color:#fff; line-height:1.4; margin-top:6px;
  text-shadow:0 0 10px #ff2fa8, 3px 3px 0 #c1147f, 4px 4px 0 #1a0833; word-break:break-word; }
@media (max-width:560px){ .prompt-word{ font-size:28px; } }

/* ===== STAGE ===== */
#topbar { position:relative; z-index:6; display:flex; align-items:center; justify-content:space-between; padding:8px 12px 0; }
#topbar .title { font-family:'Press Start 2P',monospace; font-size:10px; color:#fff; letter-spacing:1px; text-shadow:2px 2px 0 #1a0833, 0 0 8px #ff2fa8; }
#stage { position:absolute; left:0; right:0; top:178px; bottom:112px; z-index:4; overflow:hidden; }
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
#reasonPop { position:absolute; z-index:9; left:50%; bottom:20%; transform:translateX(-50%) translateY(16px); width:94%;
  text-align:center; opacity:0; transition:all .25s steps(3); }
#reasonPop.show { opacity:1; transform:translateX(-50%) translateY(0); }
.rpanel { display:inline-block; max-width:94%; padding:12px 16px; background:rgba(13,4,32,.88);
  border:3px solid #1a0833; box-shadow:0 0 0 3px #ff8fdf, 5px 5px 0 rgba(0,0,0,.5); }
.verdict-chip { display:inline-block; font-size:26px; padding:10px 22px; border:3px solid #1a0833; margin-bottom:10px; box-shadow:3px 3px 0 rgba(0,0,0,.4); }
.v-women { background:#ffd0ef; color:#c1147f; } .v-notmen { background:#e3d2ff; color:#7b2ff7; }
.v-men { background:#d6ecff; color:#1846a8; } .v-classified { background:#ffe14f; color:#8a2c00; }
.reason-text { font-family:'Comic Neue', cursive; font-style:italic; font-weight:700; font-size:42px; color:#fff;
  text-shadow:3px 3px 0 #1a0833; line-height:1.3; }
@media (max-width:560px){ .reason-text{ font-size:30px; } .verdict-chip{ font-size:22px; } .taunt{ font-size:18px; } }
.taunt { font-family:'Comic Neue', cursive; font-weight:700; font-size:24px; color:#ff8fdf; margin-top:12px;
  text-shadow:2px 2px 0 #1a0833; }
.feedback-text { font-family:'Comic Neue', cursive; font-style:italic; font-weight:700; font-size:46px; color:#fff;
  text-shadow:3px 3px 0 #1a0833, 0 0 12px #ff2fa8; line-height:1.15; padding:8px 4px; }
.feedback-sub { font-family:'Press Start 2P', monospace; font-size:13px; color:#ffe14f; margin-bottom:10px; text-shadow:2px 2px 0 #1a0833; }
@media (max-width:560px){ .feedback-text{ font-size:34px; } }

#alert { position:absolute; inset:0; z-index:8; pointer-events:none; opacity:0; }
#alert.on { animation:alertFlash .35s steps(2) 6; }
@keyframes alertFlash { 0%{opacity:0; box-shadow:inset 0 0 0 0 #ff2d2d;} 50%{opacity:1; box-shadow:inset 0 0 90px 20px rgba(255,45,45,.75);} 100%{opacity:0;} }

/* ===== APPEAL ===== */
#btnAppeal { position:absolute; z-index:10; left:50%; bottom:120px; transform:translateX(-50%);
  font-family:'Comic Neue', cursive; font-weight:700; font-size:16px; color:#1a0833; cursor:pointer;
  background:linear-gradient(180deg,#fff,#ffd0ef 60%,#ffb3e6); border:3px solid #1a0833;
  padding:9px 18px; box-shadow:0 0 0 2px #fff, 4px 4px 0 rgba(0,0,0,.4); display:none; }
#btnAppeal.show { display:block; animation:appealBob .6s steps(2) infinite alternate; }
#btnAppeal:active { transform:translateX(-50%) translateY(3px); }
@keyframes appealBob { from{box-shadow:0 0 0 2px #fff,4px 4px 0 rgba(0,0,0,.4);} to{box-shadow:0 0 0 2px #ff2fa8,4px 4px 0 rgba(0,0,0,.4);} }
#denied { position:absolute; z-index:13; left:50%; top:42%; transform:translate(-50%,-50%) rotate(-16deg) scale(0);
  font-family:'Press Start 2P', monospace; font-size:30px; color:#ff2d2d; border:5px solid #ff2d2d; padding:12px 18px;
  text-shadow:2px 2px 0 #1a0833; box-shadow:0 0 0 3px #1a0833; pointer-events:none; }
#denied.show { animation:stamp 1.6s steps(3) forwards; }
@keyframes stamp { 0%{transform:translate(-50%,-50%) rotate(-16deg) scale(2.4); opacity:0;} 18%{transform:translate(-50%,-50%) rotate(-16deg) scale(1); opacity:1;} 78%{opacity:1;} 100%{opacity:0;} }

/* ===== CONTROLS ===== */
#controls { position:absolute; left:0; right:0; bottom:36px; z-index:7; display:flex; gap:10px; padding:0 12px; }
.choice { flex:1; font-family:'Press Start 2P', monospace; font-size:15px; color:#fff; padding:16px 8px;
  border:3px solid #1a0833; cursor:pointer; line-height:1.5; transition:transform .05s; box-shadow:0 0 0 2px #fff, 5px 5px 0 rgba(0,0,0,.45); }
.choice:active { transform:translate(3px,3px); box-shadow:0 0 0 2px #fff, 2px 2px 0 rgba(0,0,0,.45); }
.choice:disabled { filter:grayscale(.55) brightness(.75); cursor:default; }
#btnWomen { background:linear-gradient(180deg,#ffb3e6 0%,#ff2fa8 51%,#ff7fd0 100%); }
#btnMen { background:linear-gradient(180deg,#a9d4ff 0%,#1f63e0 51%,#7fb0ff 100%); }
#btnWomen:hover, #btnMen:hover { filter:brightness(1.08); }

/* ===== REGGAETON TICKER ===== */
#marquee { position:absolute; left:0; right:0; bottom:0; z-index:7; height:30px; overflow:hidden; white-space:nowrap;
  background:#0d0420; border-top:3px solid #ff8fdf; }
#marquee span { display:inline-block; padding-left:100%; animation:scroll 24s linear infinite;
  font-family:'Comic Neue', cursive; font-weight:700; color:#ffd0ef; font-size:18px; line-height:30px; }
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
  <div id="topbar"><div class="title" id="title">THAT'S NOT FOR YOU</div></div>
  <div id="hud">
    <div class="bar-wrap left">
      <div class="bar-top"><div class="portrait" id="portraitW"></div><div class="pname" id="pnameW">TEAM WOMEN</div></div>
      <div class="bar"><div class="lag lag-w" id="lagW"></div><div class="fill fill-w" id="fillW"></div></div>
    </div>
    <div class="round-box"><div class="round-label" id="roundLabel">ROUND</div><div class="round-num" id="roundNum">1</div><div class="score-mini" id="scoreMini">SCORE 0</div></div>
    <div class="bar-wrap right">
      <div class="bar-top"><div class="portrait" id="portraitM"></div><div class="pname" id="pnameM">TEAM MEN</div></div>
      <div class="bar"><div class="lag lag-m" id="lagM"></div><div class="fill fill-m" id="fillM"></div></div>
    </div>
  </div>

  <div id="prompt"><span class="prompt-label" id="wordLabel">W O R D</span><span class="prompt-word" id="word">&nbsp;</span></div>

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
const DATA = __GAMEDATA__;
const lang='en';
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

const MAXHP=100; let st={};
function freshState(){ st={womenHP:MAXHP,menHP:MAXHP,round:1,combo:0,best:0,score:0,busy:false,current:null,lastT:null,over:false,messageText:'',revealActive:false,winner:null,book:null}; }
const $=id=>document.getElementById(id);
const elWord=$('word'), elRound=$('roundNum'), elScore=$('scoreMini');
const elFillW=$('fillW'), elLagW=$('lagW'), elFillM=$('fillM'), elLagM=$('lagM');
const elHeroine=$('heroine'), elTri=$('triathlete'), elStage=$('stage');
const elProj=$('projectile'), elImpact=$('impact'), elCombo=$('combo');
const elReason=$('reasonPop'), elAlert=$('alert'), elAnn=$('announce'), elAnnTxt=$('announceTxt');
const elVic=$('victory'), elBtnW=$('btnWomen'), elBtnM=$('btnMen'), elAppeal=$('btnAppeal'), elDenied=$('denied');

function L(){ return DATA.str[lang]; }
function rand(a){ return a[Math.floor(Math.random()*a.length)]; }
function randIdx(a){ return Math.floor(Math.random()*a.length); }
function correctSide(k){ return (k==='W'||k==='NM')?'WOMEN':(k==='M'?'MEN':'CLASSIFIED'); }
function damageSideFor(k){ return (k==='W'||k==='NM')?'men':(k==='M'?'women':null); }
function vclass(k){ return k==='W'?'v-women':k==='NM'?'v-notmen':k==='M'?'v-men':'v-classified'; }
function vlabel(k){ const s=L(); return k==='W'?s.vW:k==='NM'?s.vNM:k==='M'?s.vM:s.vC; }
const FEEDBACK_MS=4000, VERDICT_MS=5000, CLASSIFIED_MS=6500;

function setBars(){ const w=Math.max(0,st.womenHP), m=Math.max(0,st.menHP);
  elFillW.style.width=w+'%'; elLagW.style.width=w+'%'; elFillM.style.width=m+'%'; elLagM.style.width=m+'%'; }
function damageBar(side, amt){ if(side==='men'){ st.menHP=Math.max(0,st.menHP-amt); elFillM.style.width=st.menHP+'%'; elLagM.style.width=st.menHP+'%'; }
  else { st.womenHP=Math.max(0,st.womenHP-amt); elFillW.style.width=st.womenHP+'%'; elLagW.style.width=st.womenHP+'%'; } }
function floatText(big, dmg, cls, side){ const f=document.createElement('div'); f.className='floater '+(cls||'');
  f.innerHTML='<span class="big">'+big+'</span>'+(dmg!=null?'<span class="dmg">-'+dmg+'</span>':''); f.style.left=(side==='women'?'18%':'66%');
  elStage.appendChild(f); setTimeout(function(){f.remove();},2200); }

function showFeedback(){
  const verdict = st.lastCorrect ? L().correctWord : L().wrongWord;
  const chipClass = st.lastCorrect ? 'v-women' : 'v-men';
  elReason.innerHTML='<div class="rpanel"><div class="feedback-sub">'+verdict+'</div><div class="feedback-text">'+st.messageText+'</div></div>';
  elReason.classList.add('show');
}

function showReason(){
  if(!st.current) return;
  const k=st.current.k;
  const word=st.current.en[0].toUpperCase();
  const reason=st.current.en[1];
  elReason.innerHTML='<div class="rpanel"><span class="verdict-chip '+vclass(k)+'">'+word+' is '+vlabel(k)+'</span><div class="reason-text">because “'+reason+'”</div></div>';
  elReason.classList.add('show');
}
function hideReason(){ elReason.classList.remove('show'); st.revealActive=false; }
function announce(text, cb){ elAnnTxt.textContent=text; elAnn.classList.remove('show'); void elAnn.offsetWidth; elAnn.classList.add('show'); setTimeout(function(){ elAnn.classList.remove('show'); if(cb)cb(); },1000); }
function showAppeal(){ elAppeal.classList.add('show'); }
function hideAppeal(){ elAppeal.classList.remove('show'); elDenied.classList.remove('show'); }

function nextRound(){ if(st.over)return; hideReason(); hideAppeal(); st.busy=false; elBtnW.disabled=false; elBtnM.disabled=false; pickWord(); }
function pickWord(){ let pool=DATA.rulings;
  if(Math.random()<0.12){ const c=DATA.rulings.filter(function(r){return r.k==='C';}); if(c.length)pool=c; }
  let c=rand(pool),tr=0; while(c.en[0]===st.lastT && tr<25){ c=rand(pool); tr++; }
  st.current=c; st.lastT=c.en[0]; elWord.textContent=c.en[0].toUpperCase(); elRound.textContent=st.round; elScore.textContent=L().score+' '+st.score; }

function launchProjectile(dir, label, onImpact){ const w=elStage.clientWidth; elProj.textContent=label;
  elProj.style.setProperty('--travel', Math.round(w*0.5)+'px'); elProj.classList.remove('fly','flyBack'); void elProj.offsetWidth;
  if(dir==='toMen'){ elProj.style.left='24%'; elProj.style.right=''; elProj.classList.add('fly'); }
  else { elProj.style.left=''; elProj.style.right='24%'; elProj.classList.add('flyBack'); }
  const handler=function(){ elProj.style.opacity=0; elProj.removeEventListener('animationend',handler); onImpact(); }; elProj.addEventListener('animationend',handler); }
function impactAt(side){ elImpact.style.setProperty('--ix', side==='men'?'78%':'22%'); elImpact.style.setProperty('--iy','46%');
  elImpact.classList.remove('boom'); void elImpact.offsetWidth; elImpact.classList.add('boom');
  elStage.classList.remove('shake'); void elStage.offsetWidth; elStage.classList.add('shake'); }


function playRulingAnimation(targetSide, label, dmg, floatLabel, floatClass, afterImpact){
  const toMen = targetSide === 'men';
  if(toMen){
    elHeroine.classList.add('lungeL'); setTimeout(function(){elHeroine.classList.remove('lungeL');},500);
    launchProjectile('toMen', label, function(){
      impactAt('men'); elTri.classList.add('hitR','flash'); setTimeout(function(){elTri.classList.remove('hitR','flash');},520);
      damageBar('men', dmg); floatText(floatLabel, dmg, floatClass, 'men'); setBars(); afterImpact();
    });
  } else {
    elTri.classList.add('lungeR'); setTimeout(function(){elTri.classList.remove('lungeR');},500);
    launchProjectile('toWomen', label, function(){
      impactAt('women'); elHeroine.classList.add('hitL','flash'); setTimeout(function(){elHeroine.classList.remove('hitL','flash');},520);
      damageBar('women', dmg); floatText(floatLabel, dmg, floatClass, 'women'); setBars(); afterImpact();
    });
  }
}

function resolveGuess(isCorrect){
  const k=st.current.k, target=damageSideFor(k), label=st.current.en[0].toUpperCase();
  if(!target){ doClassified(); return; }

  st.lastCorrect = isCorrect;
  if(isCorrect){
    st.combo++; st.best=Math.max(st.best,st.combo); st.score+=10*st.combo;
    st.messageText=rand(DATA.roasts.right);
  } else {
    st.combo=0; st.score=Math.max(0, st.score-5);
    st.messageText=rand(DATA.roasts.wrong);
  }

  const crit=isCorrect && st.combo>=3;
  const dmg=(isCorrect ? 15+Math.min(st.combo,6)*3+(crit?9:0) : 20);
  const floatLabel=isCorrect ? (crit?rand(L().critTags):rand(L().rightTags)) : rand(L().wrongTags);
  const floatClass=isCorrect ? (crit?'crit':'') : 'miss';

  playRulingAnimation(target, label, dmg, floatLabel, floatClass, function(){
    if(isCorrect && st.combo>1){ elCombo.textContent='★ '+L().combo+' x'+st.combo+' ★'; elCombo.classList.remove('show'); void elCombo.offsetWidth; elCombo.classList.add('show'); }
    elScore.textContent=L().score+' '+st.score;

    // First: Alex sees a clear praise-roast or insult for 4 seconds.
    st.revealActive=true;
    showFeedback();

    setTimeout(function(){
      // Second: the actual ruling appears for 5 seconds.
      showReason();
      setTimeout(function(){
        if(st.menHP<=0){ koSequence('WOMEN'); }
        else if(st.womenHP<=0){ koSequence('MEN'); }
        else { st.round++; nextRound(); }
      }, VERDICT_MS);
    }, FEEDBACK_MS);
  });
}


function doClassified(){ st.tauntShown=false; elAlert.classList.remove('on'); void elAlert.offsetWidth; elAlert.classList.add('on');
  elStage.classList.remove('shake'); void elStage.offsetWidth; elStage.classList.add('shake');
  floatText('\u26A0 '+L().vC+' \u26A0', null, 'crit', 'men'); st.revealActive=true; showReason(); showAppeal();
  st.score++; elScore.textContent=L().score+' '+st.score; st.round++; setTimeout(nextRound,CLASSIFIED_MS); }

function onGuess(side){ if(st.busy||st.over||!st.current)return; st.busy=true; elBtnW.disabled=true; elBtnM.disabled=true;
  const cs=correctSide(st.current.k); if(cs==='CLASSIFIED')doClassified(); else resolveGuess(side===cs); }

function koSequence(winner){ st.over=true; st.busy=true; elBtnW.disabled=true; elBtnM.disabled=true; hideAppeal(); setBars(); announce(L().ko, function(){showVictory(winner);}); }
function showVictory(winner){ st.winner=winner; const s=L();
  if(winner==='WOMEN'){ setSprite($('victorySvg'), heroineVictory(), 96, 154); $('victoryTitle').innerHTML=s.vicWTitle; $('victorySub').innerHTML=s.vicWSub; }
  else { st.book=rand(s.books); setSprite($('victorySvg'), triathleteVictory(st.book), 96, 154); $('victoryTitle').innerHTML=s.vicMTitle; $('victorySub').innerHTML=s.vicMSub.replace('[book]', st.book); }
  elVic.classList.add('show'); }

function applyLang(){ const s=L();
  $('pnameW').textContent=s.teamW; $('pnameM').textContent=s.teamM; $('wordLabel').textContent=s.wordLabel;
  elBtnW.innerHTML=s.btnW; elBtnM.innerHTML=s.btnM; elAppeal.textContent=s.appeal;
  $('playAgain').innerHTML='★ '+s.playAgain+' ★'; elDenied.textContent=s.denied;
  $('foot').innerHTML=s.footer; $('marqueeText').textContent=s.marquee+'   '+s.marquee;
  if(st.current){ elWord.textContent=st.current.en[0].toUpperCase(); }
  elScore.textContent=s.score+' '+st.score;
  if(st.revealActive){ showReason(); }
  if(elVic.classList.contains('show') && st.winner){ if(st.winner==='WOMEN'){ $('victoryTitle').innerHTML=s.vicWTitle; $('victorySub').innerHTML=s.vicWSub; } else { $('victoryTitle').innerHTML=s.vicMTitle; $('victorySub').innerHTML=s.vicMSub.replace('[book]', st.book||s.books[0]); } } }

function start(){ setSprite($('portraitW'), miniHeroine(), 20, 20); setSprite($('portraitM'), miniTri(), 20, 20);
  freshState(); elBtnW.disabled=false; elBtnM.disabled=false;
  setSprite(elHeroine, heroineStance(), 60, 96); setSprite(elTri, triathleteStance(), 60, 96);
  elVic.classList.remove('show'); hideReason(); hideAppeal(); applyLang(); setBars(); pickWord();
  const s=L(); announce(s.roundWord+' 1  '+s.fight); }

elBtnW.addEventListener('click', function(){ onGuess('WOMEN'); });
elBtnM.addEventListener('click', function(){ onGuess('MEN'); });
elAppeal.addEventListener('click', function(){ elDenied.classList.remove('show'); void elDenied.offsetWidth; elDenied.classList.add('show'); });
$('playAgain').addEventListener('click', start);
start();

</script>
"""

GAME_HTML = GAME_TEMPLATE.replace("__GAMEDATA__", GAME_DATA)

try:
    components.html(GAME_HTML, height=716, scrolling=False)
except Exception:
    import html as _html
    _frame = ('<iframe style="width:100%;height:716px;border:none;" srcdoc="'
              + _html.escape(GAME_HTML, quote=True) + '"></iframe>')
    st.html(_frame, unsafe_allow_javascript=True)

# ---------------------------------------------------------------------------
# HOW TO RUN LOCALLY:  pip install streamlit   then   streamlit run app.py
# ---------------------------------------------------------------------------
