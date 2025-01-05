define CT = Character(None, window_xalign=1.0, window_yalign=1.0, window_background = None, what_color="#ffffff")
define q = Character("???", color = "#f0f8ff")
define e = Character("<[ATHENA]>", color="#f74747", image= "athena")
define mc = Character("<[McName]>", color="#ffffff", image= "mc")
define n = Character("<[NULL]>", color="#4380f3", image= "null")
define i = Character("<[ITHACA]>", color="#f4f009", image= "ithaca")
define tv = Character("<TV>", color="#000000")

#choices
default wallet = False
default mirror = False
default phone = False

image lobby:
    "lobby.jpg"
    pos (0.5, 0.59)

transform fadeout_slowly(timeInSeconds=1.0):
    linear timeInSeconds alpha 0

define dissolve = Dissolve(1.0)

init:
    image rain:
  
        "rain1.png"
        0.2
        "rain3.png"
        0.2
        "rain2.png"
        0.2
        repeat

        
        choice 0.1:   #weight of choice is 0.1
            "lightning.png"
            alpha  0.0
            linear 0.3 alpha  1.0
            linear 0.3 alpha  0.0
            
        choice 0.1:
            "rev_lightning"
            alpha  0.0
            linear 0.3 alpha  1.0
            linear 0.3 alpha  0.0
            
        repeat

label start:
    window hide
    scene black
    pause 3.0
    show lobby with fade
    pause 1.0

    $ ITHACA = "?????"
    i default "Now that we have all introduced ourselves and clarified our alibis~ \n{w=1}Would our little impostor care to raise their hand?"
    i "Have pity on us and make this a fast one."

    i crazed "Otherwise, when I find you, it won't be a happy ending."
    "The atmosphere in the lobby was grim, suffice to say."
    "The redhaired scowled and flipped her hair back with a roll of her eyes."

    $ ATHENA = "?????"
    e default "...as if that will work."
    "The boy next to you sank deeper into his seat with a quiet sigh."

    $ NULL = "?????"
    n annoyed "..."
    "You, on the otherhand, peered silently at the boy lounging arrogantly on the sofa with a leg dangled over the armrest and a glint of schadenfreude in his smirk."
    "When no one responded, he let out a sharp laugh and dropped the knife."
    i default "Oh don't give me that look! It was just a little ice-breaker to get things going."
    e "You seem to think this is some laughing matter. \nBut it's quite frankly a matter of life and death."
    "His smirk widened."
    i default "Oh you need not worry. I think I have {i}much{/i} more experience on this font than you."
    i "Actually..."
    i crazed "{i}I feel my blood singing with excitement.{/i}" with vpunch
    "The other girl gave him a look of disgust hearing that."
    e "Whose to say the alien is not you. You seem quite departed from your humanity."
    i laugh "Haha! Maybe I am."
    e "Well officer, there you have it. Lock him up and call it a day."
    n default "We have two weeks. That's plenty of time."
    e default "...aren't you guys confident..."
    "She folded her arms and glanced at you briefly before scowling away."
    "You nimbly reached for the cup of red tea and brought it to your lips."
    "The drink was hot and refreshing. But.. you had to refrain yourself from pulling a face. It was just... bitter."
    "You never drank anything like this before."
    "But that's because you...{w=1}are precisely the imposter they are searching for."

    scene black with fade 
    pause 2.0
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
        "There is a table next to the bathroom and sitting on it-- a purse and a keycard."
        "Looking to your left, Something caught your eyes."
        "No wonder it was so dark. {w=1} The drapes...they weren't just pulled shut, they were hammered to the wall with nails. How strange.."
        "A bit further down was another door."
        "You gathered the ends of your dress and walked over with hesitant steps. Strange. Your feet feel unstable, like extremely sore."
        "You twisted the knob...{w=1} to no avail. The door wouldn't budge. {w=1}Could this be an escape room instance?"
        "No. You turned your head slightly and came face to face with your reflection. There was a full body mirror attached to this wall."
        "An unfamiliar face greeted you. {w=1}Your suspicions were correct. This isn't your body. You have assumed someone else's identity."
        "You frowned. So it's not a simple escape room instance. This body...isn't as strong as your original one. In fact, it is very delicate and petite. {w=1}How distasteful."  
        "You should find clues. You walked over to the table where the purse and keycard are located. You picked up the purse and inspected it carefully. {i}Edgar's Well{/i}. {w=0.5} A famous human designer brand?" 
        "You rummaged the purse. Inside there is a little hand mirror, {w=1}a wallet, a handphone...and 'honeydew flavored chapstick'?"
        jump choiceloop

    label choiceloop:

    menu:
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
    "Manager: You have been gone for five days young lady. Pick up the phone. Now."
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
    tv "Contestants! Your doors will unlock very soon! Please meet up in the lobby room as soon as possible to meet your fellow contestants!"
    tv "Game starts now!"
    hide static with dissolve
    pause 0.6

    "Interesting..."
    "The door unlocked with a click."
    
label continue2:
    "You stepped out of the room and into a narrow and silent hallway. It was so quiet you swear you can hear a pindrop. {w=1}You see that an elevator at the end of the hallway and gradually made your way over."
    scene black with dissolve
    show elevator with fade
    "Lobby room... where could that be?"

    menu:
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
i default "Now that we have all gathered, let's jump straight into business. Let's introduce ourselves. I'll begin."
i default "I'm Ithaca."
$ ITHACA = "ITHACA"
i default "Yes it's a codename. Would you all believe me if I say I'm a hired assassin? See, I wouldn't want to be implicated when we leave this instance and return home."
e default "When we return home...What a bold confident statement."
i laugh "Seamless segway into our next player, alright."
$ ATHENA = "ATHENA"
e default "... {w=1.5}\nI'm Athena. Part-time student, full-time dancer. \nI study traditional dance and I've done a few shows for central television."
i laugh "Are you saying we have a big time celebrity on our hands? \nMy my, I am a big fan."
e default "...\nQuit the buttery talk."
n default "I'm Null. Infrastructure engineer."
$ NULL = "NULL"
"It seems to be another codename."
i default "The type that designs and safeguards digital networks?"
n default "(He shook his head) My work doesn't really focus on that. I work on artifical intelligence. \nHowever you're right. That's generally what we do."
"An assassin, a dancer, and an AI infrastructure engineer. That deos sound like a well rounded team."
"You glanced up and noticed everyone staring at you."
i default "Well? Would you do us the honors?"
$ McName = renpy.input(" ", default = " ", length = 12)
$ McName = McName.strip()
mc default "I am [McName]. I work as an..."
menu:
    "Underground idol":
        mc default "I'm an underground idol...{w=1}I do a few shows here and there... Sometimes I'm hired for birthday parties and special events."
        jump continue3
    "Model":
        mc default "I'm a model for Edgar's Well. It's a...{w=1}luxury brand for accessories."
        e default "...No way. I've never seen your magazine covers before."
        mc default "{i}Shit.{/i}"
        mc default "I just joined the company last week... My first shoot was yesterday morning actually..."
        i laugh "A bit jumping the gun here, aren't we?"
        jump continue3
label continue3:
i default "Assuming everyone is who they say they are... can anyone confidently dispel any doubts about their identity? {w=1}\n"



n "There is something that is verifiable. {w=1}\nThe hotel check-in records."









    