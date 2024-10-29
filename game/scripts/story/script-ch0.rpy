label ch0_main:
    $ style.say_window = style.window
    $ nb = "namebox"
    stop music fadeout 2.0
    call showintro(intro_t) from _call_showintro_6
    scene bg house
    with dissolve_scene_full
    $ restore_all_characters()
    
    return

label ch0_end:
    

    stop music fadeout 1
    scene black with dissolve_scene_full
    play music ghostmenu
    $ akira = "???"
    ha "Seems like your boyfriend has joined that club you despise."
    its "Well, how infuriating."
    ina "Seems like {i}we'll{/i} need to up our game a bit if we want to take over the school."
    ak "We sure will.  I hope your plan works, boss."
    kiri "Oh, don't worry.{w=1}  It will."
    return