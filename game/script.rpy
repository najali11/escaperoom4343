define CT = Character(None, window_xalign=0.5, window_yalign=0.5, window_background = None, what_color="#ffffff")
define q = Character("???", color = "#f0f8ff")
define E = Character("Ericia", color = "#f0f8ff")
define mc = Character("[McName]")

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
    CT "You make your way over from the windowsill and opened the door."
    $ renpy.music.set_volume(.35, 0.0, channel = "music")

    #door opening sound, but can be for door closing too?
    play audio "door.mp3"
    scene black
    pause 2.0
    CT "A young woman, looking around the same age as you, appeared before your eyes."
    CT "She extends her hand." 
    show handnail at truecenter with fade 
    "You take notice of the fact that her nails are painted bright red."
    hide handnail with fade
    CT "A sudden strange smell wafts into your nose for a moment."
    CT "You wrinkle your nose and took a more quiet sniff."
    CT "Perhaps it was a figment of your imagination."

    E "I'm Ericia."
    E "You are...?"

    $ McName = renpy.input(" ", default = " ", length = 12)
    $ McName = McName.strip()

    CT "You are [McName], you tell her, before giving her a firm handshake."
    E "Pleased to make your acquaintance, [McName]."  
    CT "Ericia's smile is faint, almost imperceptible, but her eyes remain sharp, scrutinizing you."
    E "We'll need to rely on each other in the coming days. Trust is... essential."
    CT "She whips her head around the hall suspicously, before lowering her voice to a tiny decibel."
    E "Have you met the other tenants yet?"
    "You shake your head."
    mc "I thought I should wait until someone else arrived to do that."
    CT "Ericia nods slowly, her expression unreadable."
    E "You are right. Caution can be a virtue here."
    "She checks her watch and frowns."
    E "11:39... It's getting late." 
    E "Let's reconvene in the morning. We have much to discuss."
    "You nod in agreement."
    mc "Goodnight."
    E "Rest well."

    play audio "door.mp3"
    $ renpy.music.set_volume(.25, 0.0, channel = "music")
    pause 3.0
    CT "You stared coldly at the door for a brief moment before retrieving a slip of paper from your pocket."
    scene black 
    $ renpy.music.set_volume(.15, 0.0, channel = "music")
    pause 2.0
    $ renpy.music.set_volume(.05, 0.0, channel = "music")
    play music "dark.mp3"
    $ renpy.music.set_volume(.55, 0.0, channel = "music")
    show hint at truecenter with dissolve
    pause 8.0
    "Within seven days, find the nonhuman within the group of players..."
    $ renpy.music.set_volume(.75, 0.0, channel = "music")
    "And kill them..."
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
    CT ""


