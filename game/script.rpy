define CT = Character(None, window_xalign=0.5, window_yalign=0.5, window_background = None, what_color="#ffffff")
define q = Character("???", color = "#f0f8ff")
define E = Character("Ericia", color = "#f0f8ff")
define mc = Character("[McName]")

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

    show scenefixed behind rain at truecenter
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
    
    CT "10:13 {w=0.2}{nw}"
    CT "10:1_ {w=0.2}{nw}"
    CT "10:13 {w=0.2}{nw}"
    CT "10:1_ {w=0.2}{nw}"
    CT "10:14 {w=0.2}{nw}"
    stop audio

    play audio "knock.wav"
    $ renpy.music.set_volume(.75, 0.0, channel = "music")
    CT "There was a knock at the door."
    $ renpy.music.set_volume(.65, 0.0, channel = "music")
    q "Hello?"
    q "I'm the new tenant of room 103."
    q "The lady at the front told me somebody already arrived last night."
    window auto
    $ renpy.music.set_volume(.55, 0.0, channel = "music")
    CT "You make your way over from the windowsill and opened the door."
    $ renpy.music.set_volume(.35, 0.0, channel = "music")
    play audio "door.mp3"
    scene black
    pause 2.0
    CT "A young woman, looking the same age as you appeared before your eyes."
    CT "She extends her hand." 

    E "I'm Ericia."
    E "And you are...?"

    $ McName = renpy.input(" ", default = " ", length = 12)
    $ McName = McName.strip()

    mc "I'm [McName]."
    CT "You are [McName], you tell her, before shaking her hand with a firm grip."
    E "Pleased to make your acquaintance, [McName]."  
    CT "Ericia faintly smiles at you, but you can sense the tensed lines under her brows."
    E "We will have to depend on each other for these next few days."
    CT "She looks around the hall suspiciously."
    E "Have you.. visited the other tenants yet?"
    "You shake your head."
    mc "I thought I should wait until everyone arrived to do that."
    CT "Ericia laughs uneasily."
    E "You are right. Better safe than sorry, right?"






    return


