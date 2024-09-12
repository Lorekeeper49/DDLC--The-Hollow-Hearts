label nstory(bgreturn="bg club_day"):
    if renpy.music.is_playing(channel="music_swap"):
        $ previouschan = "music_swap"
        stop music_swap fadeout 2.0
    else:
        $ previouschan = "music"
        stop music fadeout 2.0
    scene black with dissolve_scene
    $ style.say_window = style.window
    $ nb = "namebox"
    $ nextscene = "nstory_ch" + str(chapter)
    call expression nextscene from _call_expression_6
    stop music fadeout 2.0
    scene black with dissolve_scene
    $ style.say_window = style.window_fake
    $ nb = "namebox_fake"
    $ renpy.music.play(audio.t5y, channel=previouschan, fadein=2.0)
    scene expression bgreturn with dissolve_scene_half
    return

label nstory_ch3:
    #call showlocation("???","Monday, March 1, 2018",21,59,57)
    "Brought down...{w=1}\nBeaten...{w=1}\nKilled..."
    "All because they fell in love with a boy..."
    "Because our father believes that love drove his wife to the grave!"
    "!!!"
    "Dammit!  Right now, I'm in torture!"
    "Captivator" "Where is he!?"
    n "I'd talk if you didn't tape my mouth shut, morons!"
    "{w=1}They facepalm."
    "Slightly surprised they heard that."
    "They remove the tape and I begin talking."
    n "If you mean the boy that entered my room the other day, then he left before I got a chance to ask his identity."
    n "He's probably off whereever he usually hides."
    "They're gonna kill me, this is not nearly enough information for them."
    n "By the way, my father kills his children if they even {i}sound{/i} like they're in love with someone so you may want to be careful with you if you want me alive."

    return

label nstory_ch4:
    call showlocation("???","Monday, August 1, 2018",23,59,57) from _call_showlocation_26

    return

label nstory_ch5:
    call showlocation("???","Monday, August 1, 2018",23,59,57) from _call_showlocation_27

    return