label sstory(bgreturn="bg club_day"):
    scene black with dissolve_scene
    $ window_style = ""
    $ nb = "namebox"
    $ nextscene = "sstory_ch" + str(chapter)
    $ char_perspective = "Sayori"
    call expression nextscene 
    $ char_perspective = "Taiyen"
    stop music fadeout 2.0
    stop sound fadeout 2.0
    scene black with dissolve_scene
    $ window_style = "fake"
    $ nb = "namebox_fake"
    scene expression bgreturn with dissolve_scene_half
    return

label sstory_ch2:
    play music confdep
    scene bg storyshouse_day with dissolve_scene_half
    
    return

label sstory_ch3:
    call showlocation("???","Monday, August 1, 1906",23,59,57) from _call_showlocation_28

    return

label sstory_ch4:
    call showlocation("???","Monday, August 1, 1906",23,59,57) from _call_showlocation_29

    return

label sstory_ch5:
    call showlocation("???","Monday, August 1, 1906",23,59,57) from _call_showlocation_30

    return