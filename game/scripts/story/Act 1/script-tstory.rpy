label tstory(bgreturn="bg club_day"):
    scene black with dissolve_scene
    $ style.say_window = style.window
    $ nb = "namebox"
    $ nextscene = "tstory_ch" + str(chapter)
    call expression nextscene 
    stop music fadeout 2.0
    stop sound fadeout 2.0
    scene black with dissolve_scene
    $ style.say_window = style.window_fake
    $ nb = "namebox_fake"
    scene expression bgreturn with dissolve_scene_half
    return

label tstory_ch2:
    scene bg factory with dissolve_scene_half
    call showlocation("Palace Factories Inc.","September 29, 2015",20*60+4+57/60.0,"bg factory") from _call_showlocation_31
    $ pla = "Worker"
    t "Oi!  Stop slacking off!  Get back to work!"
    general "You're not the boss of me!"
    t "Hey, don't make me report that attitude to your real boss, who is out sick for the week."
    t "So, like it or not, I'm your boss for this week!"
    t "And I don't know about you, but I personally wouldn't want to be fired by my substitute boss!"
    "God, do these guys ever learn?"
    "I may sound strict, but this is how the actual boss is with slacking workers."
    
    return

label tstory_ch3:
    scene bg factory with dissolve_scene_half
    call showlocation("Palace Factories Inc.","October 1, 2015",20*60+4+57/60.0,"bg factory") from _call_showlocation_32
    t "So... this is who I'm taking care of for the rest of the week."
    "NAME: [[UNKNOWN]"
    "ATTRIBUTE: STORM"
    "APPEARANCE: BLACK HAIR, BLUE EYES, SHORT STATURE"

    return

label tstory_ch4:
    scene bg factory with dissolve_scene_half
    call showlocation("Palace Factories Inc.","October 1, 2015",20*60+4+57/60.0,"bg factory") from _call_showlocation_33

    return

label tstory_ch5:
    scene bg factory with dissolve_scene_half
    call showlocation("Palace Factories Inc.","October 2, 2015",20*60+4+57/60.0,"bg factory") from _call_showlocation_34
    s "It is done."
    t "Thank you."
    "The experiment went horribly wrong!"
    "Their personalities completely changed to ones they hate."
    "Things they used to like but now hate."
    "Not only that, their attributes changed too!"
    "ONE's now a copycat,"
    "TWO's now a rampant image,"
    "And THREE's now an ordinary girl."
    t "Dammit!  I didn't know this would happen!"

    return