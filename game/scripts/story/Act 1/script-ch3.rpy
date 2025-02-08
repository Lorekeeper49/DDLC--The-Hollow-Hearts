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
    "The situation might be the same with Hanato, she doesn't seem to have woken up yet."
    "At least I believe that's a limitation to her powers."
    "I don't know..."
    "Either way, I'm here for something I do once a week on Tuesdays like these."
    scene bg wilderness with wipeleft
    "I take a seat on one side of the tree in the middle and stare out into the wilderness."
    "And when the clock hits exactly 7:00, the person I expected comes by away from my vision and sits at the opposite end of the tree."
    a "Ohayou gozaimasu."
    t "Ohayou gozaimasu."
    a "Anything new going on lately?"
    t "Got a mind intruder."
    a "Ugh, hate those..."
    t "Tell me about it..."
    t "But besides that, there are many things that I don't have enough information to properly talk about yet."
    a "You said that last time too...{w=1} {i}before{/i} you went on vacation for a month."
    t "It's different things this time..."
    t "And about those other things, I'm finally getting some information for those!"
    t "So I'll let you in on them!"
    a "Do talk."
    t "So, Akira-kun seemed to be acting strange for a while and I just got reminded about that school you used to go to known as Kanzen Academy."
    a "Did you really need to remind me?"
    t "Yes, because I need you to confirm something for me; who was the principal?"
    a "Kamiyama?"
    t "Yes, but do you know his given name?"
    a "Kiri...{w=1}nani?"
    t "(I knew it.)"
    t "I'm friends with the enemy, just great."
    a "Oh, I'm sorry!"
    t "Not your fault."
    a "Don't tell your friends that you know...  No telling how that's gonna end."
    t "I wasn't gonna..."
    t "But that's pretty much everything."
    a "Well, on my side, nothing new's been going on, surprisingly."
    t "Yeah, usually you {i}do{/i} have something new."
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
    "Time's almost 8, I should get to school before Hanato wakes up."
    stop ambience fadeout 1.0
    call deadfast("bg school_day") from _call_deadfast
    play music t8
    $ style.say_window = style.window_fake
    $ nb = "namebox_fake"
    call showlocation("Sakura Academy\n{size=25}桜学園高校{/size}","October 1, 2023\n{size=15}2023年10月1日{/size}",479.95,"bg school_day")


    
    return

label introaoruguri:
    t "Can I ask you something?"
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
    t "Here, I'll start, I'm Sakura Taiyen, and my higher generation runs the school I go to.{w=1}\n(Why did I never tell that to you before?)"
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