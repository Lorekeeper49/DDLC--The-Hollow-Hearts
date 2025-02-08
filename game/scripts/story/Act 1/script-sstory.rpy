label sstory(bgreturn="bg club_day"):
    if renpy.music.is_playing(channel="music_swap"):
        $ previouschan = "music_swap"
        stop music_swap fadeout 2.0
    else:
        $ previouschan = "music"
        stop music fadeout 2.0
    scene black with dissolve_scene
    $ style.say_window = style.window
    $ nb = "namebox"
    $ nextscene = "sstory_ch" + str(chapter)
    call expression nextscene from _call_expression_7
    stop music fadeout 2.0
    scene black with dissolve_scene
    $ style.say_window = style.window_fake
    $ nb = "namebox_fake"
    $ audio.t5s = "<from 0 loop 4.444>bgm/5_sayori.ogg"
    $ renpy.music.play(audio.t5s, channel=previouschan, fadein=2.0)
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