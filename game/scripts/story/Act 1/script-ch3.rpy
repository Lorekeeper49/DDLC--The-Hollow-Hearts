label act1_ch3_main:
    stop music fadeout 2.0
    play ambience forest
    scene bg tree
    with dissolve_scene_full
    $ style.say_window = style.window
    $ nb = "namebox"
    call showlocation("Converse Park\n{size=25}コンバースパーク{/size}","October 1, 2023\n{size=15}2023年10月1日{/size}",415.2,"bg tree")
    t "A little windy today..."
    "I know school starts in at 7:15 but I actually get a late start due to how my classes are on Tuesdays."
    "So, I'm here for something I do once a week."
    scene bg wilderness with wipeleft
    "I take a seat on one side of the tree in the middle and stare out into the wilderness."
    "And when the clock hits exactly 7:00, the person I expected comes by away from my vision and sits at the opposite end of the tree."
    a "Good morning."
    t "Good morning."
    a "Anything new going on lately?"
    t "I joined a club."
    a "Which one?"
    t "The Literature Club."
    a "Oh!  Didn't take you to actually join a club like that."
    t "You're talking to a famous future author who's already written a few successful pieces, who do you think I am?"
    "We both laugh at that expense."
    "After a bit, she calms down."
    a "Out of curiousity, who's the president?"
    t "Murikou Monika."
    a "Wh...  I'm sorry?"
    t "Murikou Monika.  What?  Do you know her?"
    a "Yes, but..."
    a "I thought she was dead!"
    t "To be honest, she doesn't know how she's alive either."
    t "At least that's what she said when she transferred."
    a "So, she already told you what happened?"
    t "No, she's telling me the full story now."
    a "I see..."
    a "..."
    "Everything falls silent."
    t "..."
    "There's something I want to ask her..."
    "It's about who she is."
    "But I'm not sure if she's okay with that..."
    menu:
        t "(Umm...)"

        "Ask her.":
            $ persistent.choices_made.append("Hidden Girl Revealed")
            call introaoruguri
        "Don't ask.":
            $ persistent.choices_made.append("Hidden Girl Kept Secret")
            "No."
            pass
    $ renpy.save_persistent()
    a om "Well, I should get going."
    a "See you around."
    t "You too."
    hide aoruguri
    "She's gone..."
    t "*Sigh*"
    "Time's almost 8, I should get to school soon."
    stop ambience fadeout 1.0
    call deadfast("bg school_day") from _call_deadfast
    play music t8
    $ style.say_window = style.window_fake
    $ nb = "namebox_fake"
    call showlocation("Sakura Academy\n{size=25}桜学園高校{/size}","October 1, 2023\n{size=15}2023年10月1日{/size}",479.95,"bg school_day")


    
    return

label introaoruguri:
    t "Hey, changing the subject here; can I ask you something?"
    a "Sure."
    t "So, we've sort of known each other for quite a while, right?"
    a "Just not names or what we look like."
    t "Yes, I'd like to change that."
    a "Eh?"
    "She seems surprised!"
    a "Geuss I should've expected that."
    a "I'll agree to this, but just know; I'm a little shy when it comes to things like this."
    a "So I'll try to go at your pace, but I may be slow."
    t "Then let's start by taking a look at each other."
    "I say as I stand up and begin to turn around."
    a "Okay..."
    scene bg tree with wiperight
    "She stands up, slowly."
    show aoruguri turned dist zorder 2 at t11
    "..."
    a md "{cps=5}Uh...{nw}{/cps}"
    show aoruguri ea
    extend "  Hi..."
    show aoruguri ma
    "I'll admit, she does look cute but I'm not one to pay attention to looks, I only use looks to recognize someone or something familiar."
    t "Hi..."
    t "Here, I'll start.  I'm Sakura Taiyen, and my higher generation runs the school I go to.{w=1}\n(Why did I never tell that to you before?)"
    a md "I-I'm Luna Aoruguri... and there's currently nothing special about me."
    $ aoruguri = "ルナ煽るぐり\n{size=15}Luna Aoruguri{/size}"
    a "So you're... Sakura-san."
    show aoruguri ma
    t "I think we're past using family names to address each other, Aoruguri."
    a md "R-right... Taiyen..."
    show aoruguri ma
    "She's so nervous..."
    "But don't worry, I know what to do in these situations.\nAnd that is to ease her into the situation."
    t "Look I understand why you might've hidden yourself from everyone around you."
    t "But, I'm sure that if you just try to introduce yourself to more people, like you're doing with me, then I'm sure people will warm up to you for who you are."
    t "Though who am I to talk?  I'm the exact opposite of shy."
    $ layeredimage_ref("aoruguri")
    show aoruguri crossed
    a dist om "I never would've guessed."
    show aoruguri cm
    "She said that sarcastically."
    a neut "I'll try to take what you said into consideration..."
    t "Good."
    return