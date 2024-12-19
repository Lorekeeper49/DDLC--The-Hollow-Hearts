label act1_ch6_main:
    stop music fadeout 2.0
    scene bg bedroom
    with dissolve_scene_full
    play music t2
    $ style.say_window = style.window
    $ nb = "namebox"
    call showlocation("Taiyen's Room\n{size=25}隊円の部屋{/size}","October 4, 2023\n{size=15}2023年10月4日{/size}",6*60+0+0/60.0,"bg bedroom")
    
    achieve act1fin
    return