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
    hamind "Hellooo!"
    "Was wondering when you'd wake up."
    hamind "I like the sound of your irratation."
    "Good, cause it's all you'll hear from me."
    play sound bell
    scene bg class_day with wipeleft_scene
    $ pla = "Junior Third Year"
    "The more I look at this school, the more I realize just how weird it is compared to other Japanese schools!"
    "We've got the class numbers in reverse order, years on all different floors, and to top it off..."
    "If and when you get through all 3 years, you have the option to take a 4th year (which I took by the way) in case you want extra education before college."
    "How we managed to get away with the first 2 things I mentioned, I have no idea.  Though it seems Sakura Academy being a private academy allowed for the 3rd thing to go through."
    "My family's strange..."
    "And they say that's a good thing."
    "Anyway, what's important here is the class representative election."
    t "And the class 1-A representative is..."
    general "You.  Like always."
    t "Actually no, Junior; you're it."
    t "I got downed by 1 vote!"
    "They are shocked."
    general "Wow, this is not what I expected.  I'm sorry, Senpai."
    t "It's fine.  In fact, I wanted this to happen, I needed a break from the amount work I did in the last 3 years being class rep."
    general "Uh..{w=1}I'm not gonna regret this, am I?"
    menu(mouse=240):
        "Yes":
            t "Ye{w=0.5}ah, no."
        "No":
            t "No."
    hamind "Dammit!"
    t "Don't worry."
    "Yeah, I can resist that, thank you!"
    hamind "Clearly!"
    "After that triumphant showing, I notice that I nothing left to do, so I head outside the room to see if I can help out in the halls since classes never really do much teaching on this day."
    stop music fadeout 0.5
    scene bg corridor with wipeleft
    $ pause(0.5)
    show itsomi angr zorder 2 at r11
    $ pause(1)
    show itsomi happ at lhide
    $ pause(1)
    hide itsomi
    hamind "Itsomi?"
    "What's wrong with her?"
    hamind "She's know to get easily infuriated..."
    "I'll check on her."
    hamind "Dude, she's your enemy!"
    "So are you."
    "I go over to where she went."
    $ itsomi = "Kamiyama Itsomi"
    scene bg locker_day with wipeleft
    t "Hey, are you okay?"
    show itsomi zorder 2 at t11
    its "Heh, I thought you hated me."
    t "I thought you were convinced otherwise."
    its "I knew you didn't like me!"
    t "Wha-?  Have you been attempting to seduce me this entire time?!"
    its "Shut up.  I'm not in love with you."
    t "Coulda fooled me."
    "I say that sarcastically."
    its "Anyway, I'm leaving early.\nI went through the process already."
    its "(This is not my year.)"
    t "Why?"
    its "My entire class hates me."
    t "Hey, I still handle the class transfer papers."
    t "My office is on the roof, we can talk about this there."
    its "Wow um..."
    t "Hey!  My parents wanted me to do work here while being a student and I can't take the floor 5 offices so we were kinda out of options there!"
    its "I know it's just...  That's your office?"
    its "Wow, you must have millions to have something as luxurious as THAT."
    t "That's what happens when you have a family that runs a popular private school."
    its "Anyway, that's done in the morning, correct?"
    t "Actually, you can do it at any time, even right now!"  
    its "Then I'll do that."
    t "You'll need to wait until tomorrow for it to fanalize."
    its "That's fine."
    t "Then take my hand."
    "She does so."
    call deadfast("bg roofoffice") from _call_deadfast_1
    call showlocation("Taiyen's office","Tuesday, October 1, 2023",630.27,"bg roofoffice") from _call_showlocation_10
    "Never thought I'd be walking with Itsomi willingly."
    "Before, I said I'd rather die before I even got close to this."
    "But, when she's not being like I know her, all fake loving act that no one buys, she's actually quite nice."
    "Also no, I don't know if I trust her yet, I'm just doing what I'd normally do for a student in her situation."
    call showintro(intro_its) from _call_showintro_1
    show itsomi zorder 2 at t11
    t "So, any specific class you want?"
    its "Just one that doesn't have students that hate me."
    t "Here then, I'll give you this."
    "I look on my PC and find the class I'm looking for;"
    "Class 3-C."
    hamind "Excuse me?"
    its "Isn't that my sister's class?"
    t "Yes."
    its "Why?  Don't you hate me enough to not put us together?" (multiple=2)
    hamind "Why? Don't you hate her enough to not put us together?" (multiple=2)
    t "You want something else?"
    t "Besides, unless you're fine with a different order, this is the only class with the exact same schedule as your previous class."
    its "It's not that."
    its "I just..."
    its "Wow, you are nice."
    t "I could say the same about you, Itsomi!"
    its "Why does my brother hate you again?"
    its "I'm still not sure if I'm okay with the things he did..."
    "The hell's that implying?"
    hamind "You don't wanna know."
    "I geuss I don't."
    "I give Itsomi the papers to sign."
    t "Wait, I just realized."
    its "What?"
    $ hint = "This wasn't intentional, I swear!"
    t "Your name, it's a pun, isn't it?"
    t "It's-so-me?  Itsomi!"
    its "Tehaha, about time you realize!"
    "God, how did it take so long?"
    $ hint = ""
    "After our laughing fit, we go back on subject."
    t "Anyway, you okay with this?"
    "She takes the paper."
    its "Of course!"
    "She signs the paper."
    "I smack a button and literally the only vent on this roof opens."
    t "Then do the honors!"
    "She then does literally the only thing this vent was created for and sends the paper down it and to the office."
    "Then vent then closes automatically."
    its "Well, I best be off!"
    t "Can you endure through the rest of the day or do you need to step out?"
    its "I think I can take it."
    t "Ok."
    t "Stay safe out there!"
    its "You too!"
    hide itsomi
    "She leaves."
    "Wow, I thought Itsomi was horrible but when you actually get to know her..."
    "She's friendly."
    "Anyway, lunch break's about to start, I should head to the river."
    play sound bell
    scene bg schoolriverday with wipeleft_scene
    play music t8 
    call showlocation("Sakura Academy River","October 1, 2023",719.95,"bg schoolriverday") from _call_showlocation_11
    t "{rb}Arigatou gozaimasu!{/rb}{rt}Thank you very much!{/rt}"
    "So glad I suggested that cafe belts be set up around the school!"
    "..."
    "Hanato?"
    "Weird, I wonder why she's not talking."
    "Oh... well, at least that will make small talk with Natsuki easier."
    "Or... "
    show sayori turned happ zorder 4 at t21
    show natsuki turned happ zorder 3 at t22
    show yuri turned happ zorder 2 at t44
    show kotonoha turned happ zorder 1 at t41
    show monika forward happ zorder 5 at t11
    extend "the entire club!"
    "Well, I wasn't expecting this!\nGuessing Natsuki told them about where I eat."
    show natsuki lhip rhip at t11
    hide sayori
    hide monika
    hide kotonoha
    hide yuri
    n "Heya Taiyen!"
    n "Thought I'd invite the club to come see ya!  We got plans that need discussing!"
    t "Club time is 2 hours long, you really needed another hour for this?"
    show monika forward happ lpoint at t11
    show monika at t22
    show natsuki at t21
    m om "Well, you'll see."
    show monika cm at t11
    hide natsuki
    "She presses a button which turns the bench I'm currently sitting on into a circular seat as everyone sits down."
    t "(No one ever uses this mode!)"
    m rhip om "So!  We need to talk festival."
    m ldown "Our chapters are quite long this time so it's best to do this sooner rather than later."
    t "Right that's this month!{w=1}\n(Probably should've asked 'her' about that...)"
    m curi "I heard that."
    show monika rdown
    extend "\nWho do you mean?"
    t "Someone I don't actually know, she goes to Kamiyama and is a storm."
    m lsur "You know Aoruguri?!"
    "Huh?!"
    show natsuki turned lsur om at r22
    n "Wait, What?!{nw=0.5}"
    show kotonoha turned curi om at l41
    k "Who?!{nw}"
    show yuri turned lsur rup lup at r44
    y "Huh?!{nw}"
    show sayori turned lsur at l21
    s "Who?!{nw=1}"
    t "Ok everybody, slow down!"
    show sayori at lhide
    show kotonoha at lhide
    show natsuki at rhide
    show yuri at rhide
    hide sayori
    hide kotonoha
    hide natsuki
    hide yuri
    "Sheesh!  Didn't think she was that popular!"
    $ aoruguri = "Luna Aoruguri"
    t "Monika-chan, how do you know her?"
    m neut "You'll find out in my book..."
    m lpoint "but since everybody seems to know this, I'll just say it;"
    m rhip "she's the one who started the fire."
    t "She never told me she did that!"
    t "(Man, I really need to do my homework.)"
    m ldown rdown "No kidding."
    m rhip happ "But that's a topic for later!"
    m lpoint "Let's get back to the festival topic!"
    t "Yes, let's."
    scene bg class_day with wipeleft_scene
    call showlocation("About 50 Minutes Later","October 1, 2023",779.95,"time") from _call_showlocation_12
    "Back to class, I'm remembering what we discussed during lunch."
    "Well- trying to.\nHanato's making this real difficult."
    hamind "Hehehe!"
    "I believe we talked about presenting stories during the festival."
    "Which isn't a problem but there is also something else that seems important that Hanato is probably preventing me from remembering."
    "Welp, I'll ask Koto-chan later."
    "Can't block photographic memory."
    scene bg club_day with wipeleft_scene
    call showlocation("The Literature Club","October 1, 2023",916.0,"bg club_day") from _call_showlocation_13
    t "CLUBTIME!!!"
    hamind "Ow!  You're louder than me!"
    "Heh heh."
    show natsuki turned rhip anno om zorder 2 at t11
    n "Did you have to do that?"
    show natsuki cm
    t "What?  I do that every assembly."
    n lhip om "Yeah, {i}assemblies!{/i} those are fine!  It's a big room."
    n "Clubtime however?"
    hamind "Ough, she's scary."
    show natsuki cm at t22
    show monika forward lpoint rhip om ce zorder 3 at l21
    m "Now now, Natsuki.  I'm sure he knows his volume checks out, that wasn't nearly loud enough to go through the walls."
    m happ ldown oe "Besides, this just means that he likes it here."
    show monika cm
    t "Thanks Monika-chan."
    hide monika
    hide natsuki
    "Screaming like that is one of the few reasons why I'm glad the walls are soundproof in each classroom."
    "And don't worry, cries for help are still heard and alerted for thanks to the security cameras."
    "Anyway, Let's get this club started!"
    show monika forward happ lpoint rhip om zorder 2 at t11
    play music t5
    m "Alright!  Since each of our chapters are very long this time, we're gonna start with reading our writings!"
    show monika cm
    show kotonoha turned dist rhip ce om zorder 1 at t41
    k "I volunteer to go last, what happened last night was a fucking nightmare..."
    hide kotonoha
    t "I'll go second to last."
    m om ldown "Any other volunteers?"
    show monika cm
    "No one answers."
    m om lpoint "Then it's to the randomizer!"
    $ order = random_list(["ch3_mon", "ch3_nat", "ch3_yur", "ch3_sayo"])
    m ldown "First is..."
    call expression order[0] from _call_expression
    show monika forward happ rhip om zorder 2 at t11 
    m "Next is..."
    call expression order[1] from _call_expression_1
    show monika forward happ rhip om zorder 2 at t11 
    m "Next is..."
    call expression order[2] from _call_expression_2
    show monika forward happ rhip om zorder 2 at t11 
    m "Next is..."
    call expression order[3] from _call_expression_3
    show monika forward happ rhip om zorder 2 at t11 
    m "Next is Imfamous Book Writing Taiyen-senpai!"
    show kotonoha turned happ zorder 1 at t41
    show natsuki turned happ rhip zorder 3 at t22
    show monika cm zorder 5 at t11
    show yuri turned happ zorder 2 at t44
    show sayori turned happ zorder 4 at t21
    t "Okay!"
    t "Small warning, this chapter may seem all over the place at first, but don't worry, it'll make sense."
    t "Enjoy."
    return

label ch3_mon:
    m "The Inspirational and Beautiful Monika, me!"

    return

label ch3_nat:
    m "Ever Cheerful Natsuki!"

    return

label ch3_yur:
    m "Shy but Gracious Yuri!"

    return

label ch3_sayo:
    m "Cinnamon Bun Sayori!"

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
    "I step down from the pedestal."
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
    "Well your brother {i}is{/i} an illusionist."
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