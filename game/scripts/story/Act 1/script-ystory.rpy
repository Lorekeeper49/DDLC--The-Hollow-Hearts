label ystory(bgreturn="bg club_day"):
    scene black with dissolve_scene
    $ style.say_window = style.window
    $ nb = "namebox"
    $ nextscene = "ystory_ch" + str(chapter)
    call expression nextscene from _call_expression_14
    stop music fadeout 2.0
    scene black with dissolve_scene
    $ style.say_window = style.window_fake
    $ nb = "namebox_fake"
    scene expression bgreturn with dissolve_scene_half
    return

label ystory_ch2:
    scene bg yuriroom_night with dissolve_scene_half
    #call showlocation("?????? House","Monday, August 1, 2020",23,59,57)
    lil "Dad, Stop!  I can't take this!"
    $ pla = "Father"
    general "Fuck you!  Don't you wanna know what pain feels like!?"
    lil "STOOOOOOOPPP!!!"
    "Escaped from the clutches his machine, my sister pins our father to the wall with knives."
    general "YOU LITTLE SHIT!"
    lil "Stay there!"
    lil "Think about what I want for once!"
    
    return

label ystory_ch3:
    call showlocation("???","Monday, August 1, 2020",23,59,57) from _call_showlocation_35

    return

label ystory_ch4:
    call showlocation("???","Monday, August 1, 2020",23,59,57) from _call_showlocation_36

    return

label ystory_ch5:
    call showlocation("???","Monday, August 1, 2020",23,59,57) from _call_showlocation_37

    return