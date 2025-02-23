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
            $ known = True
            call introaoruguri
        "Don't ask.":
            $ persistent.choices_made.append("Hidden Girl Kept Secret")
            $ known = False
            "No."
            pass
    $ renpy.save_persistent()
    a om "Well, I should get going."
    a "See you around."
    t "You too."
    hide aoruguri
    "She's gone..."
    t "*Sigh*"
    if known:
        t "I need to talk with Natsuki..."
    stop ambience fadeout 1.0
    call deadfast("bg school_day")
    play music t8
    $ style.say_window = style.window_fake
    $ nb = "namebox_fake"
    call showlocation("Sakura Academy\n{size=25}桜学園高校{/size}","October 1, 2023\n{size=15}2023年10月1日{/size}",479.95,"bg school_day")
    "As I walk toward the front door, I notice the intercom is on."
    k "And as the student council president comes from his weekly outing with a woman..."
    "Since when did Koto-chan become the anouncer?"
    k "I'd like to mention that our new principle is setting up some new rules.  The student council will be discussing those with him pronto."
    "It's rare that we get new rules."
    "Guess I know what's going on today."
    scene bg security_building with wipeleft_scene
    "At our luxurious security building..."
    show sayori turned happ zorder 2 at t11
    t "Oh, hello Sayori.  Looking to join?"
    s om "Of course!"
    s rup "I already took care of the papers."
    show sayori cm
    t "Look at you getting things done!"
    show sayori ce
    t "I'll look at the papers and go over them.  You can use this as a trial meeting.  And let's just say..."
    show sayori oe rdown
    t "This is not out of bias but... I think your chances are pretty high."
    hide sayori
    show aragaki turned crossed md zorder 2 at t11
    ara mf "Alright, everyone, here's the new rules I thought of."
    call showintro(intro_ara)
    show aragaki md
    "Aragaki..."
    "Who did you dictate to get you in this position?"
    play sound beat
    $ renpy.music.set_volume(0.0, delay=0, channel="music")
    show vignette zorder 1 with BumpTransition
    ara mg "{b}You will read them respectfully.{/b}"
    hide vignette
    hide aragaki
    $ renpy.music.set_volume(1.0, delay=0, channel="music")
    "Ignoring his command, I read them reluctantly."
    #TODO: add a section where Taiyen reads a rule against uncommon sexuality and is greatly against it



    call tstory
    show monika turned dist rhip zorder 2 at t21
    show natsuki turned dist rhip zorder 2 at t22
    n om "So that's why you looked familiar..."
    t "You recognized me?"
    n cross neut "Didn't bother to mention it because I didn't think it was important."
    t "Makes sense."
    n turned rhip "Anyway, I'll go next."
    hide monika
    show natsuki at t11
    "Natsuki and I swap places."
    n cross om "This is where my father really started to break and become worse than he already was."
    call nstory
    
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
    show aoruguri cross
    a dist om "I never would've guessed."
    show aoruguri cm
    "She said that sarcastically."
    a neut om "I'll try to take what you said into consideration..."
    show aoruguri cm
    t "Good."
    return