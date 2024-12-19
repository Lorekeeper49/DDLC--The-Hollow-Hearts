label act1_ch2_main:
    stop music fadeout 2.0
    scene bg residential_day
    with dissolve_scene_full
    play music t2
    call showlocation("Residential Street\n{size=25}住宅街{/size}","September 30, 2023\n{size=15}2023年9月30日{/size}",405.2, "bg residential") from _call_showlocation_4
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

    stop music fadeout 1
    scene black with dissolve_scene_full
    play music ghostmenu
    kiri "Hanato-kun, are you sure about this?"
    "Hanato?"
    ha "Of course I am, father!  I {i}want{/i} Taiyen-kun to hear us this time."
    "I think I know these people."
    kiri "Alright, he's all yours."
    "His voice sounds horribly familiar."
    ha "Oh, don't worry about that."
    "*Sigh*"
    "Why are you making me listen to making me listen to you on purpose this time, Hanato?"
    ha "*Creepy giggle* Oh, nothing."
    ha "I just want you to know that you're being watched..."
    "Not just watched, but also stalked."
    ha "By Itsomi, sure."
    ha "But also by me!"
    ha "Now that I have entered your daydream, I know your every move from this point forward."
    ha "So, you better think hard about your choices {i}before{/i} you make them..."
    ha "because once you do-"
    "-there's no going back and you guys can easily ruin my day."
    ha "Or worse.  *Creepy giggle*"
    ha "That's your message."
    ha "I'll be talking to you while you're awake now."
    ha "Be ready."
    ha "*Creepy giggle*"
    call showintro(intro_ha) from _call_showintro
    return