label ch0_main:
    $ style.say_window = style.window
    $ nb = "namebox"
    stop music fadeout 2.0
    play music confdep
    scene bg tlivingroom
    with dissolve_scene_full
    $ restore_all_characters()
    $ pla = "???"
    $ aoruguri = "Luna Aoruguri"
    general "IT'S YOUR FAULT."
    "Shut up."
    general "IT'S YOUR FAULT AND YOU KNOW IT."
    "My parents are dead and all you can is try and humiliate me?"
    general "..."
    "That's what I thought!"
    play sound door
    scene bg house with wipeleft_scene
    call showlocation("Sakura Home","September 28, 2023",7*60+59+57/60.0,"bg house")
    t "*Sigh*"
    show yuri turned casual curi rup zorder 2 at t11
    y om "Taiyen?"
    t "Hey Yuri-chan..."
    call showintro(intro_y)
    y "You doing alright?"
    t "Take a guess..."
    y worr ce rdown "My guess is no..."
    t "You're correct..."
    y e1a "Wanna talk about it?"
    t "Well, they're shouting at me again..."
    "My parents were murdered a month ago and ever since then, I've been shouted at by voices telling me it's all my fault."
    y rup "Think you're ever going to get used to it?"
    t "You tell me..."
    show yuri cm
    "She says nothing."
    t "You wanna know what's not helping?"
    t "The fact that the murderer looked a lot like ONE."
    y dist lup om "You've said this before..."
    y sad "If what you say is true, then I don't know how to help you..."
    t "It's fine..."
    t "You being here is enough, my friend."
    y ma "..."
    "Yuri-chan is training to be a therapist, so I'm glad she's here to try and help me through this."
    $ layeredimage_ref("yuri")
    show yuri turned casual worr rup
    y om "Here, maybe I can help take your mind off things."
    y rdown "Follow me."
    scene bg street1 with wipeleft_scene
    show yuri turned casual happ rup zorder 2 at t11
    t "Yuri-chan, where are you taking me?"
    y om "Just keep going."
    show yuri cm
    t "You realize I can run super fast, right?  Just send me the location and I'd be there in seconds."
    y om rdown "I don't wanna ruin the surprise, though."
    show yuri cm
    t "Need I remind you that I am not your boyfriend?"
    y rup om "You don't need to be."
    stop music fadeout 1.0
    scene bg park_01 with wipeleft_scene
    y "We're here."
    t "And where is-{nw}"
    $ style.say_window = style.window_fake
    $ nb = "namebox_fake"
    play music t2
    show sayori turned casual happ rup lup ce om zorder 2 at t11
    s "Ah!  Yuri-chan!  Brought a friend?"
    t "Sayori?"
    s oe "Ah!  Taiyen!"
    call showintro(intro_s)
    t "What are you doing here?  This isn't a livestream, is it?"
    s ldown "Sort of is, sort of isn't."
    s "See the camera?"
    show yuri turned casual pani rup lup om zorder 2 at l21
    show sayori at t22
    y "Wait, Sayori!  We're doing that now?"
    s lup "Of course!  Gotta tell my fans about all my friends!"
    y shy casual "But, I haven't had time to ready myself yet!"
    t "How can you be a therapist when you're this shy about showing yourself to people?"
    y "That's not..."
    s rdown ldown "Come on, Yuri-chan!"
    show sayori cry cm rup at t11
    s "Don't you wanna take care of people like me?"
    "How does she change emotion so fast like that?"
    kmind "Because yes."
    "?"
    show sayori at lhide
    show yuri at lhide
    hide yuri
    hide sayori
    show kotonoha turned casual happ lchest zorder 2 at r11
    k om "Hiya Tai-kun!"
    t "Koto-chan?  You're here too?"
    call showintro(intro_k)
    show kotonoha cm
    t "Did the Midnight Club get some new recruits?  What's happening here?"
    k ldown rhip om "Well first of all, no.  Just thought I'd join a club from my actual school."
    t "And that club is...?"
    show kotonoha at t11
    hide kotonoha
    show monika forward casual happ lpoint rhip zorder 2 at t11 
    m om "The Literature Club!"
    m ldown "Hello there, Student Council President!"
    t "Murikou-san?"
    m lpoint sedu "Ah ah!  If you're gonna be participating in club activites, you gotta call everyone by their first name."
    m "Especially the president."
    call showintro(intro_m)
    show monika cm
    t "Right, sorry."
    t "Monika-chan, right?"
    m nerv om ldown "Not sure about that honorific, but sure!"
    t "Alright."
    show monika happ cm
    t "So, I haven't had time to approve clubs yet so I don't know which members are in which club."
    m lpoint om "Well, everyone you see here is a member of the literature club."
    m "We have our president, Murikou Monika, me,"
    hide monika
    show sayori turned casual happ rup zorder 2 at t11
    m "our vice president, Shinamonpan Sayori,"
    hide sayori
    show yuri turned casual happ rup zorder 2 at t11
    m "our club secretary, Yandere Yuri,"
    hide yuri
    show kotonoha turned casual happ rhip zorder 2 at t11
    m "our newest member, Sakura Kotonoha,"
    hide kotonoha
    m "and our tsundere type member, Luna Natsuki...\nwho is late today because she's having trouble gathering the essentials."
    show monika forward casual happ lpoint rhip zorder 2 at t11 
    t "Alright, well I guess I should introduce myself."
    t "You probably already know this, but I am Sakura Taiyen, the Student Council President and the son of the school's founder."
    m ldown om "Well hello there Taiyen, your sister has told us all about you."
    t "I'm sure she did, we are really close twins after all."
    show sayori turned casual laug rup zorder 2 at l21 
    show monika at t22
    s om "'Really close' is an understatement."
    show sayori at t22
    hide sayori
    hide monika
    show natsuki turned casual nerv om zorder 2 at t11
    n "Hey guys!  I'm here!  Sorry that took so long!"
    m "Ah, there she is!"
    show yuri turned casual worr ce om rup lup zorder 2 at l21
    show natsuki at t22
    y "Natsuki, you really gotta work on getting these priorities straight."
    n angr rhip "Hey, we had a ton of plans for today and I had a lot of things to grab so it was hard to keep track of them!"
    call showintro(intro_n)
    show yuri at lhide
    hide yuri
    show natsuki at t11
    n happ "Now if you'll excuse me, let's get this party started!"
    stop music fadeout 1.0
    $ style.say_window = style.window
    $ nb = "namebox"
    scene bg park_01 with dissolve_scene_full
    play music confdep
    "Everyone's having so much fun together..."
    "I wish I could have fun like that..."
    "I just..."
    "I can't!"
    "I'm such a coward!"
    a "..."
    stop music fadeout 1.0
    $ style.say_window = style.window_fake
    $ nb = "namebox_fake"
    scene bg park_01 with dissolve_scene_full
    play music t8
    show natsuki turned casual happ rhip lhip zorder 2 at t11
    n om "Alright newbie!  Let's see what you're here for!"
    t "I wouldn't call myself a newbie.  Yuri-chan practically dragged me here so I don't really know if I want to join yet."
    n ldown "Oh, come on!"
    n sedu "Don't you wanna join a club full of incredibly cute girls?"
    t "Wha- Hey!  I am the Student Council President, you know I'm better than that!"
    n cm "Sure."
    show natsuki at t22
    show kotonoha turned casual laug lup om zorder 2 at l21
    k "Hey, Natsuki?  Maybe don't tease my twin brother."
    show kotonoha cm at t21
    n lsur "Oh."
    n flus "Yeah, sorry about that.  Didn't realize who I was talking to."
    t "It's fine.  I can take it.  My parents used to tease me every two seconds."
    hide kotonoha
    hide natsuki
    "Sayori has started livestreaming now and everyone seems to be handling it nicely."
    show yuri shy casual ce zorder 2 at t11
    "I worry about Yuri-chan though.  She's not used to being shown to hundreds of people."
    show yuri happ oe
    "But it seems like she's holding strong."
    hide yuri
    show monika forward casual happ rpoint rhip zorder 2 at t11
    m om "Hey, Sayori!  Move that camera over here, I wanna tell you're fans what we're about to do."
    hide monika
    show sayori turned casual happ rup zorder 2 at t11
    s om "Okay!"
    hide sayori
    "Glad everyone's having fun!"
    "I might actually join this!"
    t "Hm?"
    $ style.say_window = style.window
    $ nb = "namebox"
    scene bg park_01 with wipeleft_scene
    a "..."
    "That was close."
    "Why does that boy sound so familiar?"
    a "Hm."
    "I should move somewhere else."
    $ style.say_window = style.window_fake
    $ nb = "namebox_fake"
    scene bg park_01 with wipeleft_scene
    t "What was..."
    show kotonoha turned casual curi om lup zorder 2 at t11
    k "Something wrong Tai-kun?"
    t "Oh, no.  Just thought someone else was watching us."
    k rhip ldown cm e1c "..."
    hide kotonoha
    show monika forward casual happ lpoint rhip zorder 2 at t11
    m om "Okay, everyone!  Let's start the first activity!"
    m ldown "Since we have a couple new members here, let's play 20 Questions and learn about them!"
    "Hardly literature related, but I'll allow it."
    hide monika
    show kotonoha turned casual happ zorder 2 at t11
    "Koto-chan takes the stage."
    hide kotonoha
    show yuri turned casual happ rup zorder 2 at t11
    y om "Taiyen, you count too."
    show yuri cm
    t "Huh?  But I haven't made any-"
    y om rdown "You made the decision to be here."
    show yuri cm
    "She has a point."
    t "Fine."
    hide yuri 
    show kotonoha turned casual happ zorder 2 at t11
    "I join my sister on the stage."
    "...That doesn't exist."
    kmind rhip anno "Just pretend it's there."
    hide kotonoha
    show monika forward casual happ lpoint rhip zorder 2 at t11
    m om "The rules are simple;"
    m ldown "You both will get 10 questions each, you get to choose who asks each question, but you will not be able to choose the same person twice consecutively."
    m lpoint "However, I will be asking the first question this time just to give everyone time to think of their questions."
    m "I will be asking you both this question, so that will leave 9 for each of you."
    show monika zorder 2 at t41
    show sayori turned casual happ rup zorder 2 at t42
    show natsuki turned casual happ rhip zorder 2 at t43
    show yuri turned casual happ rup zorder 2 at t44
    m "So!  First, a literature question:"
    m ldown "In your opinion (assuming you have written something), what's the best thing you've written?"
    $ last_chosen = "monika"
    $ koto_chosen = "monika"
    $ choice_list = ["monika", "sayori", "natsuki", "yuri", "chat"]

    show monika forward casual happ rhip zorder 2 at t41
    show sayori turned casual happ rup zorder 2 at t42
    show natsuki turned casual happ rhip zorder 2 at t43
    show yuri turned casual happ rup zorder 2 at t44
    m om lpoint "Alright, now you can choose."
    m ldown "And to make things more interesting, let's allow Sayori's chat ask questions as well."
    m lpoint "And since you can't choose the same person twice, I'm not in the first selection."
    menu:
        m ldown "So, who will you choose?"
        
        "Monika" if last_chosen != "monika":
            $ last_chosen = "monika"
            "Ignore this, this option never happens, it's just to make copying the menu easier."
        "Sayori" if last_chosen != "sayori":
            $ last_chosen = "sayori"
        
        "Natsuki" if last_chosen != "natsuki":
            $ last_chosen = "natsuki"
        
        "Yuri" if last_chosen != "yuri":
            $ last_chosen = "yuri"
        
        "Sayori's chat" if last_chosen != "chat":
            $ last_chosen = "chat"

    hide yuri
    hide sayori
    hide monika
    hide natsuki
    show kotonoha turned casual happ lup zorder 2 at t11
    $ koto_chosen = renpy.random.choice([person_chosen for person_chosen in choice_list if person_chosen not in [koto_chosen]])
    if koto_chosen == "monika":
        k om "I'll choose Monika."
        "Ignore this, this option never happens, it's just to make copying the menu easier."
    if koto_chosen == "sayori":
        k om "I'll choose Sayori."

    if koto_chosen == "natsuki":
        k om "I'll choose Natsuki."

    if koto_chosen == "yuri":
        k om "I'll choose Yuri."
    
    if koto_chosen == "chat":
        k om "I'll choose Sayori's chat."

    show monika forward casual happ rhip zorder 2 at t41
    show sayori turned casual happ rup zorder 2 at t42
    show natsuki turned casual happ rhip zorder 2 at t43
    show yuri turned casual happ rup zorder 2 at t44
    menu:
        "Next Question."
        
        "Monika" if last_chosen != "monika":
            $ last_chosen = "monika"
        
        "Sayori" if last_chosen != "sayori":
            $ last_chosen = "sayori"
        
        "Natsuki" if last_chosen != "natsuki":
            $ last_chosen = "natsuki"
        
        "Yuri" if last_chosen != "yuri":
            $ last_chosen = "yuri"

        "Sayori's chat" if last_chosen != "chat":
            $ last_chosen = "chat"

    hide yuri
    hide sayori
    hide monika
    hide natsuki
    show kotonoha turned casual happ lup zorder 2 at t11
    $ koto_chosen = renpy.random.choice([person_chosen for person_chosen in choice_list if person_chosen not in [koto_chosen]])
    if koto_chosen == "monika":
        k om "I'll choose Monika."
        
    if koto_chosen == "sayori":
        k om "I'll choose Sayori."

    if koto_chosen == "natsuki":
        k om "I'll choose Natsuki."

    if koto_chosen == "yuri":
        k om "I'll choose Yuri."
    
    if koto_chosen == "chat":
        k om "I'll choose Sayori's chat."

    show monika forward casual happ rhip zorder 2 at t41
    show sayori turned casual happ rup zorder 2 at t42
    show natsuki turned casual happ rhip zorder 2 at t43
    show yuri turned casual happ rup zorder 2 at t44
    menu:
        "Next Question."
        
        "Monika" if last_chosen != "monika":
            $ last_chosen = "monika"
        
        "Sayori" if last_chosen != "sayori":
            $ last_chosen = "sayori"
        
        "Natsuki" if last_chosen != "natsuki":
            $ last_chosen = "natsuki"
        
        "Yuri" if last_chosen != "yuri":
            $ last_chosen = "yuri"

        "Sayori's chat" if last_chosen != "chat":
            $ last_chosen = "chat"

    hide yuri
    hide sayori
    hide monika
    hide natsuki
    show kotonoha turned casual happ lup zorder 2 at t11
    $ koto_chosen = renpy.random.choice([person_chosen for person_chosen in choice_list if person_chosen not in [koto_chosen]])
    if koto_chosen == "monika":
        k om "I'll choose Monika."
        
    if koto_chosen == "sayori":
        k om "I'll choose Sayori."

    if koto_chosen == "natsuki":
        k om "I'll choose Natsuki."

    if koto_chosen == "yuri":
        k om "I'll choose Yuri."
    
    if koto_chosen == "chat":
        k om "I'll choose Sayori's chat."

    show monika forward casual happ rhip zorder 2 at t41
    show sayori turned casual happ rup zorder 2 at t42
    show natsuki turned casual happ rhip zorder 2 at t43
    show yuri turned casual happ rup zorder 2 at t44
    menu:
        "Next Question."
        
        "Monika" if last_chosen != "monika":
            $ last_chosen = "monika"
        
        "Sayori" if last_chosen != "sayori":
            $ last_chosen = "sayori"
        
        "Natsuki" if last_chosen != "natsuki":
            $ last_chosen = "natsuki"
        
        "Yuri" if last_chosen != "yuri":
            $ last_chosen = "yuri"

        "Sayori's chat" if last_chosen != "chat":
            $ last_chosen = "chat"

    hide yuri
    hide sayori
    hide monika
    hide natsuki
    show kotonoha turned casual happ lup zorder 2 at t11
    $ koto_chosen = renpy.random.choice([person_chosen for person_chosen in choice_list if person_chosen not in [koto_chosen]])
    if koto_chosen == "monika":
        k om "I'll choose Monika."
        
    if koto_chosen == "sayori":
        k om "I'll choose Sayori."

    if koto_chosen == "natsuki":
        k om "I'll choose Natsuki."

    if koto_chosen == "yuri":
        k om "I'll choose Yuri."
    
    if koto_chosen == "chat":
        k om "I'll choose Sayori's chat."

    show monika forward casual happ rhip zorder 2 at t41
    show sayori turned casual happ rup zorder 2 at t42
    show natsuki turned casual happ rhip zorder 2 at t43
    show yuri turned casual happ rup zorder 2 at t44
    menu:
        "Next Question."
        
        "Monika" if last_chosen != "monika":
            $ last_chosen = "monika"
        
        "Sayori" if last_chosen != "sayori":
            $ last_chosen = "sayori"
        
        "Natsuki" if last_chosen != "natsuki":
            $ last_chosen = "natsuki"
        
        "Yuri" if last_chosen != "yuri":
            $ last_chosen = "yuri"

        "Sayori's chat" if last_chosen != "chat":
            $ last_chosen = "chat"
            
    hide yuri
    hide sayori
    hide monika
    hide natsuki
    show kotonoha turned casual happ lup zorder 2 at t11
    $ koto_chosen = renpy.random.choice([person_chosen for person_chosen in choice_list if person_chosen not in [koto_chosen]])
    if koto_chosen == "monika":
        k om "I'll choose Monika."
        
    if koto_chosen == "sayori":
        k om "I'll choose Sayori."

    if koto_chosen == "natsuki":
        k om "I'll choose Natsuki."

    if koto_chosen == "yuri":
        k om "I'll choose Yuri."
    
    if koto_chosen == "chat":
        k om "I'll choose Sayori's chat."

    show monika forward casual happ rhip zorder 2 at t41
    show sayori turned casual happ rup zorder 2 at t42
    show natsuki turned casual happ rhip zorder 2 at t43
    show yuri turned casual happ rup zorder 2 at t44
    menu:
        "Next Question."
        
        "Monika" if last_chosen != "monika":
            $ last_chosen = "monika"
        
        "Sayori" if last_chosen != "sayori":
            $ last_chosen = "sayori"
        
        "Natsuki" if last_chosen != "natsuki":
            $ last_chosen = "natsuki"
        
        "Yuri" if last_chosen != "yuri":
            $ last_chosen = "yuri"

        "Sayori's chat" if last_chosen != "chat":
            $ last_chosen = "chat"

    hide yuri
    hide sayori
    hide monika
    hide natsuki
    show kotonoha turned casual happ lup zorder 2 at t11
    $ koto_chosen = renpy.random.choice([person_chosen for person_chosen in choice_list if person_chosen not in [koto_chosen]])
    if koto_chosen == "monika":
        k om "I'll choose Monika."
        
    if koto_chosen == "sayori":
        k om "I'll choose Sayori."

    if koto_chosen == "natsuki":
        k om "I'll choose Natsuki."

    if koto_chosen == "yuri":
        k om "I'll choose Yuri."
    
    if koto_chosen == "chat":
        k om "I'll choose Sayori's chat."

    show monika forward casual happ rhip zorder 2 at t41
    show sayori turned casual happ rup zorder 2 at t42
    show natsuki turned casual happ rhip zorder 2 at t43
    show yuri turned casual happ rup zorder 2 at t44
    menu:
        "Next Question."
        
        "Monika" if last_chosen != "monika":
            $ last_chosen = "monika"
        
        "Sayori" if last_chosen != "sayori":
            $ last_chosen = "sayori"
        
        "Natsuki" if last_chosen != "natsuki":
            $ last_chosen = "natsuki"
        
        "Yuri" if last_chosen != "yuri":
            $ last_chosen = "yuri"

        "Sayori's chat" if last_chosen != "chat":
            $ last_chosen = "chat"

    hide yuri
    hide sayori
    hide monika
    hide natsuki
    show kotonoha turned casual happ lup zorder 2 at t11
    $ koto_chosen = renpy.random.choice([person_chosen for person_chosen in choice_list if person_chosen not in [koto_chosen]])
    if koto_chosen == "monika":
        k om "I'll choose Monika."
        
    if koto_chosen == "sayori":
        k om "I'll choose Sayori."

    if koto_chosen == "natsuki":
        k om "I'll choose Natsuki."

    if koto_chosen == "yuri":
        k om "I'll choose Yuri."
    
    if koto_chosen == "chat":
        k om "I'll choose Sayori's chat."

    show monika forward casual happ rhip zorder 2 at t41
    show sayori turned casual happ rup zorder 2 at t42
    show natsuki turned casual happ rhip zorder 2 at t43
    show yuri turned casual happ rup zorder 2 at t44
    menu:
        "Next Question."
        
        "Monika" if last_chosen != "monika":
            $ last_chosen = "monika"
        
        "Sayori" if last_chosen != "sayori":
            $ last_chosen = "sayori"
        
        "Natsuki" if last_chosen != "natsuki":
            $ last_chosen = "natsuki"
        
        "Yuri" if last_chosen != "yuri":
            $ last_chosen = "yuri"

        "Sayori's chat" if last_chosen != "chat":
            $ last_chosen = "chat"

    hide yuri
    hide sayori
    hide monika
    hide natsuki
    show kotonoha turned casual happ lup zorder 2 at t11
    $ koto_chosen = renpy.random.choice([person_chosen for person_chosen in choice_list if person_chosen not in [koto_chosen]])
    if koto_chosen == "monika":
        k om "I'll choose Monika."
        
    if koto_chosen == "sayori":
        k om "I'll choose Sayori."

    if koto_chosen == "natsuki":
        k om "I'll choose Natsuki."

    if koto_chosen == "yuri":
        k om "I'll choose Yuri."
    
    if koto_chosen == "chat":
        k om "I'll choose Sayori's chat."

    show monika forward casual happ rhip zorder 2 at t41
    show sayori turned casual happ rup zorder 2 at t42
    show natsuki turned casual happ rhip zorder 2 at t43
    show yuri turned casual happ rup zorder 2 at t44
    menu:
        t "Lastly..."
        
        "Monika" if last_chosen != "monika":
            $ last_chosen = "monika"
            m om "Alright!"
            m lpoint "I'm sure everyone's wondering this."
            m ldown "Are you joining the literature club?"
            show monika cm
        "Sayori" if last_chosen != "sayori":
            $ last_chosen = "sayori"
            s om "Alright!"
            s "I'm sure everyone's wondering this."
            s lup "Are you joining the literature club?"
            show sayori cm
        "Natsuki" if last_chosen != "natsuki":
            $ last_chosen = "natsuki"
            n om "Well new guy, I would like to know if you are joining the literature club."
            show natsuki cm
        "Yuri" if last_chosen != "yuri":
            $ last_chosen = "yuri"
            y om "Well my humble patient, I would like to know if you are joining the literature club."
            show yuri cm
        "Sayori's chat" if last_chosen != "chat":
            $ last_chosen = "chat"
            s "They would like to know if you're joining the literature club."
            show sayori cm
    t "Well, this club seems to be a lot of fun, even with only four members."
    show yuri at f44
    show sayori at f42
    t "Not to mention, some of my closest friends are here."
    show yuri at t44
    show sayori at t42
    t "So, final verdict:"
    t "I'm joining the literature club."
    hide yuri
    hide sayori
    hide monika
    hide natsuki
    show kotonoha turned casual happ lup rhip zorder 2 at t11
    k om "Before anyone asks, I am too."
    k ldown "Though I believe that still counts towards the quota."
    m "Yes it does."
    k rdown "Alright!"
    hide kotonoha
    "With the question quota met, we step down from the non-existent stage."
    stop music fadeout 1.0
    $ style.say_window = style.window
    $ nb = "namebox"
    scene bg park_01 with dissolve_scene_full
    play music confdep
    "I'm starting to wonder if I should really be here."
    "Everyone's so social here."
    "But me..."
    "I don't fit in."
    "I just don't fit in!"
    "I'm an observer from afar, not a socialist within reach."
    a "Damnit!"
    stop music fadeout 1.0
    $ style.say_window = style.window_fake
    $ nb = "namebox_fake"
    scene bg park_01 with dissolve_scene_full
    show monika forward casual happ lpoint rhip zorder 2 at t11
    play music t5
    m om "Okay, everyone!  We have one more activity planned for today, and it's a literature one!"
    m ldown "We do this every year, Let's all write a poem and show it to each other!"
    hide monika
    "With that, everyone goes off to write their poems seperately."
    "I'm actually not good at poems, but I might as well try while I can."
    scene bg park_01 with wipeleft_scene
    show monika forward casual happ lpoint rhip zorder 5 at t11
    m om "Alright!  If everyone has written their poems, then we can start sharing."
    show monika cm
    t "Can I go first?  I'm not good at poetry and I want to set a baseline for everybody."
    show kotonoha turned casual happ zorder 1 at t41
    show yuri turned casual happ zorder 2 at t44
    show sayori turned casual happ zorder 3 at t21
    show natsuki turned casual happ zorder 4 at t22
    m ldown om "Sure!"
    show monika cm
    call showpoem(poem_t, False)
    t "I think it speaks for itself."

    call showpoem(poem_k, False)

    call showpoem(poem_m)

    call showpoem(poem_y)

    call showpoem(poem_n)

    call showpoem(poem_s)

    stop music fadeout 1.0
    $ style.say_window = style.window
    $ nb = "namebox"
    scene bg park_01 with dissolve_scene_full
    play music confdep
    "I'm heading back, I can't do this anymore!"
    "Everyone's having too much fun."
    "I can't have any fun."
    "*Sigh*"
    a "I should never have come here..."
    stop music fadeout 1.0
    $ style.say_window = style.window_fake
    $ nb = "namebox_fake"
    scene bg park_01 with dissolve_scene_full
    play music t3
    show monika forward casual happ rhip zorder 2 at t11
    m om "Okay, everyone!  We are running out of time here, so let's decide on what we should write for this year."
    m lpoint "As some of you may know, this is a literature club.  And in this literature club, we are tasked to write about one topic for each year."
    m ldown "Last year, we agreed on drawing from a hat to decide on the topic."
    m rdown "So..."
    "She grabs the hat she mentioned."
    m "We still got a lot of suggestions in here."
    m lpoint "The topic of this year is..."
    show monika cm
    stop music fadeout 3.0
    $ pause(3.0)
    show monika dist
    $ pause(1.0)
    m ce ldown rhip om "*Sigh*\nOh boy..."
    m oe lpoint "'Write about a true experience, past or present, that has made a significant impact on your life.  Preferably, a dramatically long experience.'\n*Sigh*"
    m neut "Does anyone want to reroll?"
    hide monika
    show kotonoha turned casual dist zorder 2 at t41
    show sayori turned casual dist rup zorder 2 at t42
    show natsuki turned casual dist rhip zorder 2 at t43
    show yuri turned casual dist rup zorder 2 at t44
    "..."
    t "I don't."
    y neut om "Me neither."
    show yuri cm
    n om rdown "I kinda do, but...  I know I shouldn't."
    show natsuki cm
    k worr n1 lup om "The problem with this topic is: it goes into subjects that can be really personal for the author."
    k ldown rhip e1d "But if everyone's in agreement, then I have nothing to say."
    show kotonoha cm
    t "Sayori?  Are you in on this?"
    s rdown ce "..."
    s neut oe om "I'll do it."
    hide kotonoha
    hide sayori
    hide natsuki
    hide yuri
    show monika forward casual dist rhip zorder 2 at t11
    m om "Seems like we have a majority..."
    m ce rdown "..."
    m neut oe "Honestly, I'm scared to write mine."
    m dist rhip "But I'm in a similar situation to Natsuki; I {i}should{/i} do this."
    m neut lpoint "Alright.  Let's come back on Monday with the first chapters of our stories complete."
    everyone "Got it."
    stop music fadeout 1.0
    scene black with dissolve_scene_full
    $ style.say_window = style.window
    $ nb = "namebox"
    play music ghostmenu
    $ akira = "Voice 4"
    $ hanato = "Voice 1"
    $ kirinani = "Voice 5"
    $ itsomi = "Voice 2"
    $ inari = "Voice 3"
    ha "Seems like your boyfriend has joined that club you despise."
    its "Well, how infuriating."
    ina "Seems like {i}we'll{/i} need to up our game a bit if we want to take over the school."
    ak "We sure will.  I hope your plan works, boss."
    kiri "Oh, don't worry.{w=1}  It will."
    return