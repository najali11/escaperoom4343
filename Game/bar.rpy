init python: 

    #This controls when the love-points floater appears. 
    show_ithaca=False
    show_null=False
    show_athena=False

    ## ------------ Love Points Floater ----------------------

    def stats_overlay():               
        
        # --- Ithaca's suspicion bar -------
        if show_ithaca:
            ui.frame(
                xalign = 0.05, #centered
                ypos = 500,) #400 px Down from the Top
            
            ui.vbox(xalign = 0.5)
            ui.text ("Ithaca's Suspicion: %d" %ithaca_sus, 
                xalign = 0.0)
            ui.bar(max_sus, ithaca_sus, 
                style="my_bar")
            
            ui.close()
            
        # --- null's suspicion bar -------   
        if show_null:
            ui.frame(
                xalign = 0.05,
                ypos = 400,) 
            
            ui.vbox()
            ui.text ("Null's Suspicion: %d" %null_sus, 
                xalign = 0.0)
            ui.bar(max_sus, null_sus, 
                style="my_bar")
            
            ui.close()
            
        # --- Athena's sus Bar -------   
        if show_athena:
            ui.frame(
                xalign = 0.05,
                ypos = 600,) 
            
            ui.vbox()
            ui.text ("Athena's Suspicion: %d" %athena_sus, 
                xalign = 0.0)
            ui.bar(max_sus, athena_sus, 
                style="my_bar")
            
            ui.close()
           
    config.overlay_functions.append(stats_overlay)

init -2 python:
    ithaca_sus=25
    max_sus = 150

    null_sus=25
    max_sus = 150

    athena_sus =25
    max_sus = 150
    
init -5 python:
    #custom bar
    style.my_bar = Style(style.default)
    style.my_bar.xalign = 0.5
    style.my_bar.xmaximum = 315 # bar width
    style.my_bar.ymaximum = 30 # bar height
    style.my_bar.left_gutter = 5
    style.my_bar.right_gutter = 5
    
    # I have all my User Interface graphics stored in one file called ui. 
    # To access them in my code, I put ui/ in front of all images in that file. 
    
    style.my_bar.left_bar = Frame("ui/bar_full.png", 0, 0)
    style.my_bar.right_bar = Frame("ui/bar_empty.png", 0, 0)
    style.my_bar.hover_left_bar = Frame("ui/bar_hover.png", 0, 0)
    
    style.my_bar.thumb = "ui/thumb.png"
    style.my_bar.thumb_shadow = None
    style.my_bar.thumb_offset = 5

