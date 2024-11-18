label act1_ch3_main:
    stop music fadeout 2.0
    play ambience forest
    scene bg tree
    with dissolve_scene_full
    $ style.say_window = style.window
    $ nb = "namebox"
    call showlocation("Converse Park","October 1, 2023",415.2,"bg tree") from _call_showlocation_8
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

        "[change]Ask her.":
            $ persistent.choices_made.append("Hidden Girl Revealed")
            call introaoruguri from _call_introaoruguri #correct choice
        "[change]Don't ask.":
            $ persistent.choices_made.append("Hidden Girl Kept Secret")
            "No."
            pass
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
    call showlocation("Sakura Academy","October 1, 2023",479.95,"bg school_day") from _call_showlocation_9
    
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
    $ aoruguri = "Luna Aoruguri"
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

label act1_ch3_end:
    show monika forward happ rhip om zorder 2 at t11 
    m "And last is Cherry Blossom Kotonoha!"
    hide monika
    show kotonoha turned happ rhip om zorder 2 at t11
    k "Alright!  Time to talk about ghosts!"
    call kstory(False, "bg schoolriverday") from _call_kstory_1
    show kotonoha turned worr om zorder 2 at t11
    k "Is everyone okay?"
    t "I think so..."
    hide kotonoha
    t "What the hell was that?"
    show yuri turned lsur om lup rup zorder 2 at t11
    y "That looked like..."
    hide yuri
    show lilly c3e zorder 2 at t11
    lil "Are you guys okay?  I'm sorry!  I didn't mean to scare you like that!"
    "..."
    $ pla = "???"
    general "Lilly!"
    "Sounds like she's in trouble."
    show yuri 2r zorder 2 at r22
    show lilly at t21
    y "Father, I'll handle her!"
    show yuri at t22
    kmind "I know what this is.  Tai-kun, everyone else knows what to do here, just follow their lead."
    hide yuri
    hide lilly
    "Got it."
    "I won't ask questions, not until it's safe to."
    scene bg schoolbasement with wipeleft_scene
    call showlocation("Sakura Academy Basement","October 1, 2023",60*16+29+57/60.0,"bg schoolbasement") from _call_showlocation_14
    show monika forward neut zorder 2 at t11
    t "So, what exactly is going on here?"
    m rhip om "Well, ever since she was born, the Yandere parents have been trying to keep Lilly away from people for some unknown reason."
    m lpoint "Let me tell you everything we know;"
    call showintro(intro_lil) from _call_showintro_2
    t "Ah, I see."
    "Sounds like she's had a tough life..."
    hide monika
    "On another note: this asylum we built the school on top of is like a fricking maze!  It's near impossible to navgiate, much less find someone."
    t "Ah, there they are!"
    show yuri turned worr om rup zorder 2 at t22
    show lilly zorder 2 at t21
    y "Lilly, you're not making a lot of sense here, what do you mean you're anyting but human?"
    show yuri cm
    lil a1c2 "It would be a lot easier to explain if you could see anything..."
    y ce om rdown "*Sigh* I don't get it, I don't get it at all."
    show yuri cm
    lil "At this point, I don't think anyone ever will..."
    "Sounds like asking questions won't lead anywhere."
    hide yuri
    hide lilly
    hamind "I didn't see shit!  What the hell is everyone talking about?"
    "Well your father {i}is{/i} an illusionist."
    hamind "Not the...  Wait a second, what?"
    hamind "He's not an..."
    "Isn't he known to lie?"
    show kotonoha turned curi om rhip zorder 2 at t11
    k "Are you talking to someone in there?"
    menu(mouse=240, time=5, force=1):
        "Yes":
            $ persistent.choices_made.append("Hanato Ratted Out")
            $ secrets = True
            t "Hanato broke in."
            hamind "No!"
            k ce "Shit."
            hamind "You shouldn't have done that!"
            "You panicking?"
            hamind "..."
            "That's what I thought!"
            k neut oe "We'll talk later!"
        "No":
            $ secrets = False
            t "No, I'm not."
            "Damnit!"
            k rdown "I won't press.  Especially since you talk to yourself all the time."
    hide kotonoha
    show lilly a2e zorder 2 at t11
    lil "Hey, are you guys okay?"
    t "Yeah, don't worry, we've jumped out of a fifth story window before."
    lil eb "(You're not the only one.)"
    "Even high schoolers go through that much danger..."
    hide lilly
    show yuri turned dist rup om zorder 2 at t11
    y "Guys, I should tell you somehting."
    y neut "I've been writing my story in secret, especially since it's real."
    y dist "And for the next chapter..."
    y ce rdown "I'm gonna be telling you what made my father so... messed up."
    show yuri cm
    t "How the hell are you getting away with it?"
    y rup lup oe om "Luck?"
    y ldown rdown "Honestly, I don't know how he hasn't caught on yet."
    y ce "I'm so obvious..."
    y oe "*Sigh* (Fuck this is annoying...)"
    hide yuri
    show natsuki turned dist om rhip zorder 2 at t11
    n "Honestly, I could repeat everything Yuri just said, with a few differences..."
    n neut "The main one being that I...{w=1}{nw}"
    show natsuki ce
    extend " ran away from my family..."
    "Does everyone have problems?"
    hide natsuki
    t "That reminds me..."
    show sayori turned zorder 2 at t11
    t "Sayori, your story sounded excruciatingly familiar, why?"
    s rup om "It's us... pre-life."
    t "I thought you didn't wanna relive that anymore."
    s rdown "I did, but then I saw someone whom I thought was dead."
    s "I'll explain things later, when the situation's less tense."
    s rup "For now, let's tend to Yuri-chan's sister."
    s "We can call it a day when we know she's fine."
    return