define CT = Character(None, window_xalign=1.0, window_yalign=1.0, window_background = None, what_color="#ffffff")
define q = Character("???", color = "#f0f8ff")
define E = Character("<Ericia>", image= "ericia")
define mc = Character("<[McName]>", image= "mc")

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

    show scene2 behind rain at truecenter with dissolve
    show rain at truecenter 
    
    play music "rain.wav"
    pause 6.0
    scene black with dissolve
    pause 3.0

    #sets rain to 85% of full value
    $ renpy.music.set_volume(.85, 0.0, channel = "music")
    play audio "clock.mp3"
    scene black
    pause 2.0
    show clock at truecenter with dissolve
    pause 5.0
    scene black with fade
    play audio "clock.mp3"
    show clock1 at truecenter with fade
    pause 2.0
    stop audio
    scene black with dissolve
    play audio "knock.wav"
    $ renpy.music.set_volume(.75, 0.0, channel = "music")
    "There was a knock at the door."
    $ renpy.music.set_volume(.65, 0.0, channel = "music")
    q "Hello? {w=0.4}{nw}"
    q "I'm the new tenant of room 103. {w=0.7}{nw}"
    q "The lady at the front told me somebody already arrived last night. {w=0.9}{nw}"
    window auto
    $ renpy.music.set_volume(.55, 0.0, channel = "music")
    "You make your way over from the windowsill and opened the door."
    $ renpy.music.set_volume(.35, 0.0, channel = "music")

    #door opening sound, but can be for door closing too?
    play audio "door.mp3"
    scene black
    pause 2.0
    "A young woman, looking around the same age as you, appeared before your eyes."
    "She extends her hand." 
    show handnail at truecenter with fade 
    "You take notice of the fact that her nails are painted bright red."
    hide handnail with fade
    "A sudden strange smell wafts into your nose for a moment."
    "You wrinkle your nose and took a more quiet sniff."
    "Perhaps it was a figment of your imagination."

    E default "I'm Ericia."
    E "You are...?"

    $ McName = renpy.input(" ", default = " ", length = 12)
    $ McName = McName.strip()

    "You are [McName], you tell her, before giving her a firm handshake."
    E default "Pleased to make your acquaintance, [McName]."  
    "Ericia's smile is faint, almost imperceptible, but her eyes remain sharp, scrutinizing you."
    E default "We'll need to rely on each other in the coming days. Trust is... essential."
    "She whips her head around the hall suspiciously, before lowering her voice to a tiny decibel."
    E default "Have you met the other tenants yet?"
    "You shake your head."
    mc default "I thought I should wait until someone else arrived to do that."
    "Ericia nods slowly, her expression unreadable."
    E default "You are right. Caution can be a virtue here."
    "She checks her watch and frowns."
    E default "11:39... It's getting late." 
    E "Let's reconvene in the morning. We have much to discuss."
    "You nod in agreement."
    mc "Goodnight."
    E "Rest well."

    play audio "door.mp3"
    $ renpy.music.set_volume(.25, 0.0, channel = "music")
    pause 3.0
    "You stared coldly at the door for a brief moment before retrieving a slip of paper from your pocket."
    scene black 
    $ renpy.music.set_volume(.15, 0.0, channel = "music")
    pause 2.0
    $ renpy.music.set_volume(.05, 0.0, channel = "music")
    play music "dark.mp3"
    $ renpy.music.set_volume(.55, 0.0, channel = "music")
    show hint at truecenter with dissolve
    pause 8.0
    window hide
    CT "Within seven days, find the nonhuman within the group of players..."
    $ renpy.music.set_volume(.75, 0.0, channel = "music")
    CT "And kill them..."
    pause 2.0

    menu:
        "Flip paper":
            show hintflip at truecenter 
            $ renpy.music.set_volume(.75, 0.0, channel = "music")
            pause 8.0
    
    scene black with dissolve
    jump recall

    return


label recall:
    scene black with fade
    CT "You appeared at the motel entrance last night at 11:30."
    CT "When you arrived, you were greeted by a lady in blue at the front desk who handed you the keys to your room."
    CT "The lobby was dimly lit by the emanating warm glows from a lightbulb by the lobby desk."
    CT "In fact, you noticed a strange smell of chlorine water the moment you stepped into the place."
    CT "But at that time, you made no inquiries about it."
    CT "Your key was to room 101, in the floor directly above the lobby."
    CT "The room immediately adjacent to the stairs where you came up from was room 114."
    CT "Walking to your room, the floors constantly creaked and howled."
    CT "This motel seems to be poorly maintained."
    CT "You noticed light emanating from the door gaps of room 107 and 109."
    CT "These rooms are occupied, you mentally noted."
    CT "As for the other rooms, you weren't too sure. You did not hear any noise from them. But that may just speak to the soundproofness of these rooms."
    CT "101. You reached your room."
    show room1 at top with dissolve
    mc default "..."
    "It was a comfortable looking room."
    "You had taken a glance at the clock on the wall."
    "11:47."
    "From your pocket, you unravelled a slip of paper."

    

    play audio "door.mp3"

    scene black with dissolve
    





