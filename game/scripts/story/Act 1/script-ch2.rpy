label act1_ch2_main:
    stop music fadeout 2.0
    scene bg bedroom
    with dissolve_scene_full
    call showlocation("Taiyen's Room\n{size=25}隊円の部屋{/size}","September 30, 2023\n{size=15}2023年9月30日{/size}",405.2, "bg bedroom")
    $ style.say_window = style.window
    $ nb = "namebox"
    show monika forward nuet rhip zorder 2 at t11
    "Routine checkup."
    m om "Any progress?"
    t "No."
    show monika dist cm
    "I'm the only one who knows about her unidentified attribute."
    show monika neut
    t "Your power is still beyond even my comprehension."
    t "I don't get it."
    t "I really don't."
    t "It seems to be similar to copycat in that you have abilities similar to others."
    t "But on the other hand, it also seems to be an entirely new power that we haven't discovered yet."
    m curi "So, what are you thinking?"
    t "Hmm..."
    t "Now that I've joined your literature club, I may be able to gather more data based on how you act in there."
    t "I'll bring my notebook to see what I can jot down."
    m neut "We're still keeping this secret, right?"
    t "Per your request."
    m rdown "Thank you."
    hide monika
    "She leaves."
    "I should head to school."
    scene bg residential_day with wipeleft_scene
    $ style.say_window = style.window_fake
    $ nb = "namebox_fake"
    play music t2
    call showlocation("Residential Street\n{size=25}住宅街{/size}","September 30, 2023\n{size=15}2023年9月30日{/size}",6*60+59+57/60.0, "bg residential_day")
    show lilly norm de zorder 2 at t31
    show sayori turned happ rup zorder 2 at t32
    show yuri turned happ zorder 2 at t33
    s om "Hey, Taiyen!  Over here!"
    "And this is why Monika can't leave my house normally."
    show sayori cm
    t "Hey everyone!  Nice to see ya!"
    t "How are you all doing?"
    y rup om "We're all doing just fine."
    show yuri cm
    t "Good!"
    s om "Koko-tan went on ahead."
    show sayori cm
    t "Figured.  She always does that."
    t "Lilly!  Glad to see you have recovered nicely."
    lil ee "Thank you!"
    show lilly de
    y om "The flu doesn't get her that easily!"
    y dist lup "(How does she even get sick?)"
    show sayori curi
    t "Sorry?"
    y curi "Huh?"
    y "Oh!{w=1}{nw}"
    show yuri happ ldown rdown
    extend "  Nothing."
    show yuri cm
    t "Okay."
    "Could've sworn she said something."
    s happ om "Let's not worry about that right now and get to school!"
    t "Yeah!"
    scene bg class_day with wipeleft_scene
    call showlocation("Class 3-A\n{size=25}3年A組{/size}","September 30, 2023\n{size=15}2023年9月30日{/size}",7*60+29+57/60.0, "bg class_day")
    show lilly norm de zorder 2 at t31
    show sayori turned happ rup zorder 2 at t32
    show yuri turned happ rup zorder 2 at t33
    t "Gotta say, I find it interesting but also fun that all 4 of us are in the same class."
    lil ee "Yeah, we got kinda lucky."
    hide lilly
    hide sayori
    hide yuri
    "We all take our seats."
    show yuri turned happ zorder 2 at t11
    "Yuri-chan's got seat 5-5 in the back corner."
    show yuri at t22
    show lilly norm de zorder 2 at l21
    "Lilly has seat 4-5, in front of her sister."
    show lilly at t21
    hide lilly
    hide yuri
    show sayori turned happ zorder 2 at t11
    "Sayori's got seat 2-3, right behind me."
    hide sayori
    "And I have seat 1-3 at the front of the class."
    $ pla = "先生\n{size=15}Teacher{/size}"
    general "Alright class!  Let's begin!"
    scene bg schoolriverday with dissolve_scene_full

    
    return