label act1_ch6_main:
    stop music fadeout 2.0
    scene bg bedroom
    with dissolve_scene_full
    play music t2
    $ style.say_window = style.window
    $ nb = "namebox"
    call showlocation("Taiyen's Room","October 4, 2023",6*60+0+0/60.0,"bg bedroom")
    
    achieve act1fin
    return