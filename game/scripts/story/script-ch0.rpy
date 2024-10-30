label ch0_main:
    $ style.say_window = style.window
    $ nb = "namebox"
    stop music fadeout 2.0
    call showintro(intro_t) from _call_showintro_6
    play music confdep
    scene bg tlivingroom
    with dissolve_scene_full
    $ restore_all_characters()
    $ pla = "???"
    general "IT'S YOUR FAULT."
    "Shut up."
    general "IT'S YOUR FAULT AND YOU KNOW IT."
    "My parents are dead and all you can is try and humiliate me?"
    general "..."
    "That's what I thought!"
    scene bg house with wipeleft_scene
    call showlocation("Sakura Home","September 28, 2023",7*60+59+57/60.0,"bg house")
    t "*Sigh*"
    show yuri turned casual worr rup zorder 2 at t11
    y om "Taiyen?"
    t "Hey Yuri-chan..."
    call showintro(intro_y)
    y "You doing alright?"
    t "Take a guess..."
    y ce rdown "My guess is no..."
    t "You're correct..."
    y oe "Wanna talk about it?"
    t "Well, they're shouting at me again..."
    "My parents were murdered a month ago and ever since then, I've been shouted at by voices telling me it's all my fault."
    y rup "Think you're ever going to get used to it?"
    t "You tell me..."
    show yuri cm
    "She says nothing."
    t "You wanna know what's not helping?"
    t "The fact that the murderer looked a lot like ONE."
    y dist lup om "You've said this before..."
    y worr "If what you say is true, then I don't know how to help you..."
    t "It's fine..."
    t "You being here is enough, my friend."
    y ma "..."
    "Yuri-chan is training to be a therapist, so I'm glad she's here to try and help me through this."
    $ layeredimage_ref("yuri")
    show yuri turned casual worr rup
    y om "Here, maybe I can help take your mind off things."
    y rdown "Follow me."
    
    return

label ch0_end:
    

    stop music fadeout 1
    scene black with dissolve_scene_full
    play music ghostmenu
    $ akira = "???"
    ha "Seems like your boyfriend has joined that club you despise."
    its "Well, how infuriating."
    ina "Seems like {i}we'll{/i} need to up our game a bit if we want to take over the school."
    ak "We sure will.  I hope your plan works, boss."
    kiri "Oh, don't worry.{w=1}  It will."
    return