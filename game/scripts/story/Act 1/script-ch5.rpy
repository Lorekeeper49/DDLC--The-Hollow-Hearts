label act1_ch5_main:
    stop music fadeout 2.0
    scene bg bedroom
    with dissolve_scene_full
    play music t2
    call showlocation("Taiyen's Room\n{size=25}隊円の部屋{/size}","October 3, 2023\n{size=15}2023年10月3日{/size}",6*60+0+0/60.0,"bg bedroom") from _call_showlocation_16
    $ style.say_window = style.window
    $ nb = "namebox"
    show yuri turned anno rup om zorder 2 at t11
    "Routine Therapy."
    y ce "*Sigh* No good."
    t "What's wrong?"
    y oe "My pay's been dropping lately, I don't think I'm taking enough notes."
    t "You're doing fine."
    t "Haven't you been taking more notes now that I'm part of the literature club?"
    y laug "I've forgotten to bring my notebook on several occasions."
    t "That's a surprise."
    y happ "No one's perfect, Taiyen."
   
    return