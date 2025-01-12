define CT = Character(None, window_xalign=1.0, window_yalign=1.0, window_background = None, what_color="#ffffff")
define q = Character("???", color = "#f0f8ff")
define e = Character("<[ATHENA]>", color="#f74747", image= "athena")
define mc = Character("<[McName]>", color="#ffffff", image= "mc")
define n = Character("<[NULL]>", color="#4380f3", image= "null")
define i = Character("<[ITHACA]>", color="#f4f009", image= "ithaca")
define tv = Character("<TV>", color="#000000")


image static:        
    "static.webp"
    0.9
    Null ()
    0.05
    "static.webp"
    0.01
    Null ()
    0.05  
    "static.webp"
    0.03
    Null ()
    0.05
    "static.webp"

image gnomes:
    "clip/1.png"
    0.1
    "clip/2.png"
    0.1
    "clip/3.png"
    0.1
    "clip/4.png"
    0.1
    "clip/5.png"
    0.1
    "clip/6.png"
    3.0


#cursor
define config.mouse = {}
define config.mouse['default'] = [("gui/cursor.png", 0, 0)]

#window dialogue always shown as default
define config.window = "show"

#choices
default wallet = False
default mirror = False
default phone = False
default sus1 = False

image lobby:
    "lobby.webp"
    pos (0.5, 0.80)

define dissolve = Dissolve(1.0)

label start:
    window hide
    scene black
    pause 3.0
    show lobby with fade
    pause 1.0

    $ ITHACA = "?????"
    i default "Now that we have all introduced ourselves and clarified our alibis~ \n{w=1}Would our little impostor care to raise their hand?"
    i "Have pity on us and make this a fast one."

    i crazed "I'm not above torturing it out of you." with vpunch
    "The atmosphere in the lobby was grim, suffice to say."
    "The redhaired stopped dead in her tracks and froze."

    $ ATHENA = "?????"
    e default "..."
    "The boy next to you sank deeper into his seat with a quiet sigh."

    $ NULL = "?????"
    n annoyed "..."
    "You, on the otherhand, peered silently at the boy lounging arrogantly on the sofa with a leg dangled over the armrest and a glint of schadenfreude in his smirk."
    "When no one responded, he let out a sharp laugh and dropped the knife."
    i default "Oh don't give me that look! It was a joke, lighten up. It's actually a fruits knife. Here, have some apples."
    e "You seem to think this is some laughing matter. \nBut it's quite frankly a matter of life and death."
    "His smirk widened."
    i default "Oh you need not worry. I think I have {i}much{/i} more experience on this font than you."
    i "Actually..."
    i crazed "{i}I feel my blood singing with excitement.{/i}" with vpunch
    "The other girl gave him a look of disgust hearing that."
    e "Whose to say the imposter is not you. You don't seem quite put together."
    i laugh "Haha! Maybe I am."
    e "Well officer, there you have it. Lock him up and call it a day."
    n default "We have two weeks. That's plenty of time."
    e default "...aren't you guys confident..."
    "She folded her arms and glanced at you briefly before looking away."
    "You nimbly reached for a slice of fruit and popped it in your mouth."
    "The fruit was chilled and refreshing. But.. you had to refrain yourself from pulling a face. It was just... sweet."
    "You never ate anything like this before."
    "But that's because you...{w=1}are precisely the imposter they are searching for."

    scene black with fade 
    show logo at center with dissolve
    pause 2.0
    scene black
    CT "An hour ago."
    play music "dark.mp3"
    $ renpy.music.set_volume(.55, 0.0, channel = "music")
    "You find yourself opening your eyes to a strange and unfamiliar place."
    "First off, it was dark. {w=1}Total blackness."
    "The second thing you noticed was--{w=1}what are you {i}wearing?{/i} You are weighed down not only by the blankets but by a heavy frilly dress you didn't remember putting on."
    "You sat up and searched around in the dark for anything, something solid to grip onto and managed to hit a...{w=1}lamp?"
    "You turned it on."
    "The bright warm light made you a little nauseous but you soon realize that was not the problem. {w=1}Everything was blurry."
    "You are confused."
    "Your vision has always been perfect. {w=1}Unless..."
    "You glanced around and spotted a thin pair of glasses on the nightstand."
    "Are these meant for you?"
    menu:
        "Put them on.":
            jump glassesworn

    label glassesworn: 
        "As your eyes adjust, details of the room emerged. This is a reasonably sized suite you are in."
        "The walls were covered with floral prints and the floors were gleaming hardwood, as if the paint and varnish were just recently applied not too long ago. "
        "To the right, a half opened door exposed tiled floors and a bathtub with transparent curtains strewn across gleaming brass hinges."
        "There is a purse and a keycard sitting on the table next to the bathroom."
        "Looking to your left, Something caught your eyes."
        "No wonder it was so dark. {w=1} The drapes...they weren't just pulled shut, they were hammered to the wall with nails. How strange.."
        "A bit further down was another door."
        "You gathered the ends of your dress and walked over with hesitant steps. Strange. Your feet feel unstable, like extremely sore."
        "You twisted the knob...{w=1} to no avail. The door wouldn't budge. {w=1}Could this be an escape room instance?"
        "No. You turned your head slightly and came face to face with your reflection. There was a full body mirror attached to this wall."
        "An unfamiliar face greeted you. {w=1}Your suspicions were correct. This isn't your body. You have assumed someone else's identity."
        "You frowned. So it's not a simple escape room instance. This body...isn't as strong as your original one. In fact, it is very delicate and petite. {w=1}How distasteful."  
        "You should find clues. You walked over to the table where the purse and keycard are located. You picked up the purse and inspected it carefully. {i}Edgar Wells{/i}. {w=0.5} A famous human designer brand?" 
        "You rummaged the purse. Inside there is a little hand mirror, {w=1}a wallet, a handphone...and 'honeydew flavored chapstick'?"
        jump choiceloop

    label choiceloop:

    menu:
        extend ""
        "Inspect the wallet" if not wallet:
            jump walletchoice
        "Inspect the hand mirror" if not mirror:
            jump mirrorchoice
        "Inspect the handphone" if not phone:
            jump phonechoice
        "Finish inspection" if wallet and mirror and phone:
            jump continue_main_story

label walletchoice:
    $ wallet = True
    "Inside the wallet, there was some spare change, an ID, and a receipt.."
    "The name on the ID is smudged..."
    "The receipt is for a purchase of grape flavored throat lozenges."
    jump choiceloop

label mirrorchoice:
    $ mirror = True
    "You see a reflection of yourself. Or. a reflection of the body you are possessing. A very pretty girl. Your skin is remarkably smooth."
    jump choiceloop

label phonechoice:
    $ phone = True
    "Fortunately for you, you easily unlocked the phone through fingerprint verification."
    "October 14, 2034. 7:56... The time and time displayed on the phone should be accurate. You mindlessly checked for any incoming messages. Ah... there's no signal in this place. But you could still see the messages send to this phone since last night.
    The last message recorded was at 11:56 from..."
    "Manager?"
    "Manager: You have been gone for five days. Pick up the phone. Now."
    "How threatening."
    "Just as you were about to scroll up to read the other messages, the television switched on."
    stop music
    jump continue_main_story

label continue_main_story:
    play audio "tv.mp3"
    pause 1.0
    show static at top with dissolve
    play audio "static.mp3"
    pause 2.0
    hide audio
    tv "The start of a wonderful day coincides with the start of a brilliant adventure! Aren't we excited here?!"
    tv "For the uninitiated, welcome to Motel! Or... is it Hotel!...? Whatever! This will be a two week long program where our four contestants navigate the complexity of human relationships, weave through webs of lies, forge friendships of steel and -- {i}oh am I going off script?{/i}"
    tv "Ahem! {w=1}Our contestants are now currently locked up in their respective rooms. The task for them is simple. Within two weeks, they must vote out the imposter among them!"
    tv "Who is this imposter? Is it human? Alien? A supernatural diety from an outer dimension?! Hahahaha! The imposter themselves should know who they are."
    tv "The rules are simple. The imposter must hide until the end of the two weeks period to win the game. The humans must collaborate amongst themselves and vote out the imposter!"
    tv "3/4 votes are needed to eliminate the imposter!"
    tv "Ah, what was that? What will happen if either side fails? Well..."
    tv "That's not something you'll want to be on the receiving end of!"
    tv "To make this game an exiting one, everyone will have a special skill to help them gain an edge."
    tv "Players! Your doors will unlock very soon! Please meet up in the lobby room as soon as possible to meet your fellow contestants!"
    tv "Game starts now!"
    hide static with dissolve
    pause 0.6

    "Interesting..."
    "The door unlocked with a click."
    
label continue2:
    show hallway at top with dissolve
    pause 0.2
    "You stepped out of the room and into a narrow and silent hallway. It was so quiet you swear you can hear a pin drop. {w=1}You see an elevator at the end of the hallway and gradually made your way over."
    scene black with dissolve
    show elevator at top with fade
    "Lobby room... where could that be?"

    menu:
        extend ""
        "Floor 1":
            jump floor1
        "NOFloor 2":
            jump floor2
        "NOFloor 3":
            jump floor3
        "NOFloor 4":
            jump floor4

label floor1:
scene black 
show lobby with dissolve
"The other contestants were already there when you arrived. \nOn their faces were various expressions and some unspeakable emotions."
"They watched you warily as you sat down on the only available seat on the couch next to a white haired boy."
i default "And at last we have a full house. Welcome welcome."
i default "Now that we have all gathered, let's jump straight into business. Name, occupation, and events leading up to last night. I'll begin."
i smile "I'm Ithaca."
$ ITHACA = "ITHACA"
i default "Yes it's a codename. Would you all believe me if I say I'm a hired assassin? See, I wouldn't want to be implicated when we leave this instance and return home."
e default "When we return home...What a bold confident statement."
i smile "Seamless segway into our next player, alright."
$ ATHENA = "ATHENA"
e default "... {w=1.5}\nI'm Athena. Part-time student, full-time dancer. \nI study traditional dance and I have a few performanced documented on national television."
i cutesmile "Are you saying we have a big time celebrity on our hands? \nMy my, I am a big fan."
e default "...\nQuit the buttery talk."
n default "I'm Null. Infrastructure engineer."
$ NULL = "NULL"
"It seems to be another codename."
i default "The type that designs and safeguards digital networks?"
n default "(He shook his head) \nMy work doesn't really focus on that. I work on artifical intelligence. However you're right. That's generally what we do."
"An assassin, a dancer, and an AI infrastructure engineer. That does sound like a well rounded team."
"You finally glanced up and noticed you have quite a few pair of eyes on you."
i smile "Well? Will you do us the honors?"
$ McName = renpy.input(" ", default = " ", length = 12)
$ McName = McName.strip()
mc default "I am [McName]. I work as an..."
menu:
    extend ""
    "Underground idol":
        mc default "I'm an underground idol...{w=1}I do a few shows here and there... Sometimes I'm hired for birthday parties and special events."
        $ show_athena=True
        $ show_null=True
        $ show_ithaca=True
        jump continue3
    "Model":
        mc default "I'm a model for Edgar Wells. It's a...{w=1}luxury brand for accessories."
        e default "...Really..I have never seen you before. I'm a big fan of Edgar Wells too."
        pause 0.5
        $ show_athena=True
        $ show_null=True
        $ show_ithaca=True
        $ athena_sus+=5
        mc default "{i}...{/i}"
        mc default "I just joined the company last week..."
        i laugh "A bit jumping the gun here, aren't we?"
        jump continue3
label continue3:
i smile "Assuming everyone is who they say they are... can anyone confidently dispel any doubts about their identity? {w=1}\n"



n "I suppose there is something that is verifiable. {w=1}\nThe hotel check-in records."
i shocked "Can we access that without a password?"
e default "Maybe they have it noted down somewhere?"
i poker "That's definitely possible."
n annoyed "In a game instance like this, there should be many routes for us to exploit. Even if there's no password, that's still ok. I can log in as an administrator and force run it."
i poker "..."
mc "..."
e default "Alright. System rebooting."
"She scooted back and allowed Null to take reins. \nNull leaned forward with one hand on the mouse and the other shoved inside his pockets."
"You realized he was taller than you thought. 183cm? It is because of his lanky frame that had you thinking he was around 175."
n default "Ah. {w=1}\nI'm in."
mc default "...That was fast."
"Is it really that simple...? \nIf he really pulls up the check in logs, then your lies about your identity will easily be exposed."
menu:
    extend ""
    "Speak: Is it a good idea?":
        jump spokeout
    "Say nothing.":
        "You held your tongue. {i}It's a two weeks long instance. This... it hasn't even been an hour! Logically, if the records could be retreived so easily, then that's not worth the investment right? \nSpeaking of it, the television also mentioned everyone will be granted an unique ability..."
        "You noticed Athena narrowed her eyes over Null's shoulders, deeply immersed in whatever he was doing. \nIthaca...{w=.5}Strangely, Ithaca on the otherhand didn't look as interested. {i} Why?{/i}"
        jump continue4

label spokeout:
mc default "What if we are walking into a trap...？"
"Null paused to look at you."
n default "?\nWhat?"
"He stared at you with a confused look."
mc default "We can't confirm anyone's identity right now. And you are the only one who knows how to pull up the records. How do we know... these records are right?"
n default "(He blinked slowly)\nAre you suspecting me of potential foul play?"
mc default "I'm not saying you... I'm saying this is strange. What is we are walking straight into a trap? \nI'm just afraid we will be let around the nose."
n default "..."
$ null_sus+=25
$ athena_sus+=15
n default "Then what do you suggest instead?"
mc default "The game master suggests the existence of special abilities. What if this imposter has the ability to digitally alter records? If so, this investigation is going to be colored by red herrings."
n annoyed "..."
n annoyed "What a strange logic."
"He watched you coolly but you sensed the iciness within his gaze."
$ null_sus+=30
n annoyed "Sorry but...{w=1}I don't agree."
i smile "She bring up a good point actually. \nRight now, we are the only ones who are entirely sure of our identities. How can we be sure if the digital records are not altered in some way or form?"
"Passing by, you caught Ithaca's eyes. He gave you a meaningful look. You weren't certain but there was a certain flare of amusement in his smile."
i smile "For example, how can we prove the veracity of these records? You want to stake our identities on these data logs."
n default "Rather than worrying about hypothetical abilities, shouldn't we use the tools we have? Unless..."
n annoyed "Someone has a reason to avoid verification."
e default "..You two are really suspicious right now, you know?"
i cutesmile "Really? I'm just highlighting something very important."
n annoyed "If your records are inaccurate, say it."
$ sus1 = True
jump continue4

label continue4:
"There was a brief silence in the room when time also held its piece."
n annoyed "..."
n annoyed "There's nothing. It's been wiped clean."
e default "...ugh."
i poker "..."
"...Whew. \nThat was a close call."
e default "Could the imposter have deleted them...?"
n default "Possibly. But I suspect it may be part of the instance design."
if sus1:
    n annoyed "(He glanced at you meaningfully.) \nIf it was the imposter who deleted them, they wouldn't have been so worried about the datalog."
    mc default "..."
    menu:
        extend ""
        "You are defaming an innocent person...":
            mc default "...Don't give me that look."
            n default ".."
        "You are jumping to conclusions.":
            mc default ".. Don't irrationally pin suspicion on someone right off the bat."
            n default "(He looked away.)"
            $ null_sus-=5
else:
    jump continue5

label continue5:
    e default "...Back to square one, huh."
    i default "Speaking of it, is this everyone's first instance?"
    n default "Yes."
    e default "....Second one actually."
    "You have been to many instances in the past. But what should you tell them?"
    menu:
        extend ""
        "1. This is my first instance.":
            mc default "This is my first instance as well."
            if sus1:
                $ null_sus+=5
                $ athena_sus+=5
            i default "So we have a veteran among us."
        "2. Not my first.":
            mc default "This is not my first instance either."
            i default "So we have some veterans among us."
    
    i default "This is also my first instance. \nI've always wondered when it'll be my time, to be mysteriously whisked away into a space blot and forced to compete in a mass casualty event to survive." 
    i crazed "This is much tamer than I thought."
    e default "...Don't bank on it. In these instances, you don't know when the sudden switch will be."
    i default "Why don't you tell us a bit about your last instance?"
    e default "..."
    e default "I don't really mind but...to be honest, I forgot most of it. It was a bit like coming out from a dream... I guess that's why I'm calmer than you'd expect. \nAfter all, I already experienced it once and..."
    scene black with dissolve
    pause 1.0
    e default "It was a dark fairy tale."
    show gnomes at top with dissolve
    e default "In that instance, we were the gnomes tasked with preventing Snow White from falling into the wicked queen's hands."
    show 7 at top with dissolve
    i default "That's it? All I hear on the news everyday is how inexorbitant amount of people died after disappearing into an instance. Isn't there that recent one? \nIt was a complete wipe out."
    e default "The news always pick the most sensational story to tell."
    i default "Unfortunately."
    e default "But no, that is not all. No matter how hard we tried, at the end, Snow White bit into the queen's apple. After that...you guys know the story right?"
    show prince at top with dissolve 
    n default "You guys need to find the prince."
    e default "That's right. But...there was something wrong with that instance because the prince disappeared."
    i shocked "Disappeared?"
    e default "That's right."
    i shocked "Then shouldn't you guys have failed that instance? There's no way to rescue the princess now right?"
    e default "... The thing is... afterwards, the wicked queen also disappeared. The instance shut down on it's own. It's like the whole realm collapsed. We players all returned home without any casualties."
    n annoyed "That is strange."
    e default "That's why... a lot of my memories from that time are foggy. It's been two years..."
    "Athena closes her eyes, as if trying to remember the events of that time. But after a while, she shook her head and sighed."
    e default "I can't remember how any of the NPCs looked like..."
    n annoyed "..."
    n annoyed "Isn't it strange?"
    e default "Huh?"
    n annoyed "In instances, there are usually specific tasks and missions with clear routes. Although there are many ways to solve an instance, there are usually clearly set rules which give the players a clue on how to proceed."
    n annoyed "But so far, our task has been ambiguous. First of all, what is an 'imposter' and what kind of creature are they?"
    e default "Isn't it someone who deceives others using a fake identity?"
    n default "But nothing is defined so far. It's true that we don't know the extent of their abilities."
    if sus1:
        "You felt the weight of Null's eyes on you."

    n annoyed "And something has been bothering me so far."
    n annoyed "The record logs are wiped out, which means the game won't leave behind any physical traces of the imposter's identity. It might be actively helping the imposter win by deleting all these traces. Furthermore, there are no NPCs. The only sources we have are each other."
    i laugh "Hahahaha! Insidious isn't it? The game is designed for us to trust each other and rely on each other's words to defeat it. Yet one of us here is a liar..."
    i default "Now that we have all introduced ourselves and clarified our alibis~ \n{w=1}Would our little impostor care to raise their hand?"
    i frontsmirk "Have pity on us and make this a fast one."
    i frontsmirk "Otherwise..."
    i crazed "I'm not above torturing it out of you." with vpunch
    "Ithaca suddenly whips out a pocket knife. The edge of it gleamed in the light, revealing its razor sharp edges. He points it at you guys with a maniacal little grin."
    e default "..."
    n annoyed "..."
    mc default "..."
    i laugh "Hahahah! It was a joke! Lighten up guys! This is a fruit knife I got from the kitchen. There are some sliced apples, want some?"
    "Ithaca stood up and walked towards the back where he appeared a few seconds later with a plate of diced fruits."
    i smile "I'll see what else I can whip up for breakfast."
    e default "...Do we have time to chill like this?"
    n default "We have two weeks after all."
    scene black with dissolve
    











    




    










    