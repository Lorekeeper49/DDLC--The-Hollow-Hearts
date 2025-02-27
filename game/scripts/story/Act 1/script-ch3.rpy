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
            if not "Hidden Girl Revealed" in persistent.choices_made:
                $ persistent.choices_made.append("Hidden Girl Revealed")
            $ known = True
            call introaoruguri
        "Don't ask.":
            if not "Hidden Girl Kept Secret" in persistent.choices_made:
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
    ara mf "{b}You will read them respectfully.{/b}"
    hide vignette
    hide aragaki
    $ renpy.music.set_volume(1.0, delay=0, channel="music")
    "Ignoring his command, I read them reluctantly."
    "A lot of the rules here are the same as we had before, no need for changing those."
    t "'No sexual conduct in the bathrooms'?"
    "Is this a joke?"
    t "I don't think we've ever needed to explicitly spell that out before."
    show kotonoha turned laug rhip lup zorder 2 at t11
    k om "To be fair, I did just have to deal like 3 in a row yesterday."
    t "Seriously?"
    k ldown "Yeah, it was certainly something."
    t "And I thought you were immature."
    k e1b "That is a very low bar."
    t "Okay, but I'm marking this for extra review.  We may need to look at our rates before we explicitly enforce something like this."
    hide kotonoha
    show aragaki turned crossed md zorder 2 at t11
    ara mf "I'll allow it."
    hide aragaki
    show sayori turned doub zorder 2 at t11
    s om "Uh, Taiyen..."
    s nuet rup "Look at the last rule."
    "She has me worried."
    hide sayori
    stop music fadeout 1.0
    t "'No romantic conduct between those of the same...'"
    t "No..."
    show aragaki turned crossed md zorder 2 at t11
    ara mf "Excuse me?"
    t "I said no!  I am not letting your religious ass have influence on this school's rules!"
    show aragaki mj
    t "I don't know if you know about this, but some of my best friends are either gay or pansexual, I don't know about bisexual but let me tell you, I support them all the way through."
    ara not_crossed md "You know what the law says-{nw}"
    t "Fucking screw the law!  Do you think really that my parents ever cared about the law?"
    show aragaki eb mj
    t "We've all spoken about this!  They need to pass legal gay marriage or SO HELP ME!"
    play sound beat
    show vignette zorder 1 with BumpTransition
    ara bd mf "{b}You will-{/b}{nw}"
    hide vignette
    t "NO I WILL NOT!"
    show aragaki mj
    t "I hate to be the one to break it to you, but you have NEVER been able to control your family and you never WILL be able to!"
    ara md "I am trying to make this school more normal!  PLEASE!"
    show aragaki mj
    menu:
        "Deny this rule":
            t "NO!  We are NOT doing this!"
            t "I'm sorry but you need to stop clinging to normality!  It doesn't mean anything anymore!"
        "Submit this rule":
            t "FINE!"
            achieve hate
            t "But I'm marking this, we can't add it now!"
            t "Not when there are pansexuals currently in this school."
            "I make a subtle gesture to Sayori which he doesn't notice."
    t "Your other rules are fine."
    "After what I just read, I'm surprised there isn't anyrthing about transgender or non-binary."
    "However if there were, I would have a few choice words to say to him."
    t "You can place in the ones I haven't marked."
    "I hand him my marked up paper."
    hide aragaki
    "Because I've got better things to do than be here, I leave to go somewhere else less infuriating."
    scene bg schoolriverday with wipeleft_scene
    play ambience river fadein 1.0
    play ambience2 forest fadein 1.0
    call showlocation("Sakura River\n{size=25}桜川{/size}","October 1, 2023\n{size=15}2023年10月1日{/size}",11*60+29+57/60.0, "bg schoolriverday")
    t "*Sigh*"
    show natsuki turned neut rhip zorder 2 at t11
    n om "Hey dude."
    show natsuki cm
    t "Hey..."
    n cross om "Sayori already told me the details, you needn't say anything."
    show natsuki cm
    t "..."
    n dist "..."
    n turned rhip neut om "You know?  I'm lesbian."
    t "The tsundere too, huh?"
    n lhip happ "What'd you expect?  A heterosexual?"
    show natsuki cm
    t "I didn't expect anything to be honest."
    n laug "..."
    show natsuki dist
    "She looks across the river."
    n ldown om "Sister?"
    n rdown "Are you alive out there?"
    if known:
        show natsuki cm
        "My cue."
        t "Hey, has Sayori told you about what I do every Tuesday yet?"
        n rhip happ om "Outing with a woman, right?"
        show natsuki cm
        t "A secluded one, more like."
        t "She actually properly introduced herself today."
        show natsuki dist
        t "My request."
        "She's not interested right now."
        t "It's someone you've been looking for."
        n curi "Huh?"
        "That got her."
        n cross om "I'm listening"
        show natsuki cm
        t "Kinda cute, black hair, blue eyes, short stature..."
        t "A storm..."
        t "Name: Luna Aoruguri."
        n turned lsur "!!!"
        n om "Ao...ru..."
        n rhip "You're kidding!"
        t "I am dead serious.  It's the only name she said."
        n cross "And you're sure she wasn't lying?"
        t "With how nervous she was, I don't think she even {i}could{/i} lie."
        n "..."
        show natsuki doub cm
        "She seems doubtful."
        n turned neut "Where does she attend?"
        n rhip "I wanna see this for myself."
        t "She... never told me."
        n dist "..."
        t "But next week, I'll talk to her."
        t "Come with me then."
        t "That is if you can make it."
        show natsuki ce
        "She considers it."
        n cross happ om "Oh, what the hell?  I can skip class, this is my little sister were talking about here."
        show natsuki cm
        t "Teh, I trust you on that."
        t "Just make sure you can catch up."
        t "I'll cover for you."
        n om "Thanks."
        show natsuki cm
        "She smiles."
        n neut "Speaking of siblings..."
    else:
        t "Out of curiousity, how did you find out?"
        n rhip curi om "Huh?"
        t "That you're a lesbian?"
        n neut "Oh."
        n laug "That's a bit of an embarrassing topic."
        show natuski cm
        t "It's fine, you don't have to say anything."
        n om "Well, if you'll allow me..."
        show natsuki ce cm
        "She clears her throat."
        n cross neut oe om "I'm in love with a certain someone..."
        n doub "With purple hair."
        t "Yuri-chan?"
        t "My training therapist?"
        n turned rhip laug "If she's your therapist, why are you using that honorific?"
        t "I don't know."
        t "Just force of habit at this point."
        n cross lhip "Well anyway..."

    n neut rhip lhip om "You know, I still can't believe it."
    n lsur ldown "Yuri's sister is a doll?"
    n laug "What...?"
    t "It's surely a lot to process..."
    t "The real question is how she is so... human?"
    t "She can get sick, take needle shots..."
    t "Heck, she's even got blood."
    n rdown "She must've been one hell of a science experiment."
    t "I'm telling her you said that."
    n pani "Uh!  Don't!  Please don't!  Seriously!"


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