# Name: A Club That Works at Night
label act2_ch1_main:
    $ style.say_window = style.window
    $ nb = "namebox"
    call showintro(intro_a) from _call_showintro_4
    play music confdep
    scene black with dissolve_scene
    scene bg kamihallday with dissolve_scene 
    $ pause(1)
    play sound lightswitch
    $ pause(0.5)
    scene bg kamihallnight with None
    a "*Smacks wall*\nUgh!  Goddamn it!"
    "Why did I run away!?!?"
    "I spend all this time talking to that... boy, Taiyen, and I still can't talk to others!"
    "I'm a fucking coward."
    "*Sigh*"
    "What time is it?"
    "15:30..."
    "Most of the students have gone home now."
    "I would do the same, but that's the thing!"
    "This school {i}is{/i} my home."
    "I have nowhere to go."
    "Nowhere..."
    ti "Hey, are you okay?"
    show tina turned suit curi zorder 3 at t11
    a "Huh?"
    ti rhip "Hey, I don't mean to startle you."
    a "No, you're fine."
    a "Aren't you the cranky one of that group?"
    ti angr lhip "Hey!  Don't use that on me!"
    a "Okay sorry, Jesus!"
    "Just proving my point."
    show tina anno ldown
    a "I am also sorry for running back there."
    show tina curi
    a "I do that with everyone...\nI'm a bit of a coward."
    show lilly c1e zorder 2 at t21
    lil "So you don't have friends?"
    ti anno rside "Lilly!"
    a "It's fine!"
    show tina neut
    "I don't know how I'm keeping my cool here but I'm not questioning it."
    a "And actually, I have 2 friends.  Kamiyama Akira and Sakura Taiyen."
    a "Wait!  Wasn't he behind you guys back there?"
    show akira 2al zorder 2 at t22
    ak "Someone call for me?"
    a "Speak of the... not-devil."
    ak 4ag "I {i}spy{/i} on the devil, thank you!"
    a "Hence the 'not' part."
    "I know he's joking but I do believe there is some truth behind those words."
    ak 2al "Anyway, I should ask: what are you doing here?  Aren't you normally on the roof at this time?"
    "I guess that would explain why he'd be late if I was there right now."
    a "Yes, but I think you can guess what happened here."
    a "*Sigh*"
    ak "Mm..."
    ak 2ac "I'll handle her, you two should head to clubroom."
    ti rdown "Copy that."
    hide tina
    hide lilly
    show akira zorder 2 at t11
    "They leave and Akira sits next to me."
    ak 1af "So...{w=1}{nw}"
    show akira 1al
    extend " I guess my secret's out."
    ak "Well, one of them."
    "How many secrets do you have?"
    ak 1ab "You know, you could join me if you wanted."
    show akira 1aa
    a "Me with a team of delinquents?"
    if not known:
        jump act2_ch1_alt
    a "I mean, I could do it but..."
    a "I don't even know how to control my abilities correctly.  Not to mention my social problems..."
    ak 4ab "We can teach you."
    show akira 4aa
    a "Do you even have a storm in your ranks?"
    ak 2an "Better; a telegraph!"
    a "A telegraph?"
    "Fuck, okay.  I've been meaning to learn how to use storm for a while so..."
    a "Fuck it, take me there!"
    ak 1ab "Come on then!"
    scene bg kamihallnight with wipeleft_scene
    call showlocation("Kamiyama Academy 3F","October 8, 2023",659.95,"bg kamihallnight") from _call_showlocation_38
    "Why do they always put the night atmosphere on during clubtime?"
    "Like I like the the illusion, but most find it unusual."
    show akira 1ab zorder 2 at t11
    ak "Here we are!"
    "Class 1-C."
    "That was my first-year class."
    scene bg kamiclassnight
    show akira 1ab zorder 2 at t11
    with wipeleft
    ak "Kotonoha?  We have a potential new member!"
    show akira at rhide
    hide akira
    show kotonoha turned casual happ om zorder 2 at l11 
    k "Oh!  Who is it?"
    show kotonoha cm
    "This girl ain't in this school!"
    "Come to think of it, neither is that Lilly girl."
    a "L-Luna Aoruguri."
    k curi om "Oh!"
    k rhip happ "Well this is a surprise!  I didn't think I'd be meeting you in here."
    k rdown lchest "I'm Kotonoha, Sakura Kotonoha.  And please, let's go on a first name basis since you seem to do the same with my brother."
    show kotonoha lup
    "Taiyen's sister!  In the flesh!"
    "Alright, I think I can get along with her."
    k lup om "And I think I can get along with you!"
    k ldown rhip "I'm the telegraph Akira mentioned."
    k "And you're a storm, correct?"
    show kotonoha cm
    a "An untrained one."
    k om ce "Then, we can train you!  Up until midnight."
    a "Until midnight?"
    a "Well, lucky for you, storms don't sleep."
    scene bg kamiclassnight with wipeleft_scene
    call showlocation("Midnight", "October 8, 2023",0.0,"black") from _call_showlocation_39
    "Very glad storms don't get tired because I have been training for 8 hours straight, only stopping to go to the bathroom."
    show kotonoha turned casual anno rhip om zorder 5 at t11
    k "Everyone!  Places at the table!"
    show akira 4ae zorder 4 at t21
    show lilly norm se zorder 1 at t41
    show mari forward anno om zorder 3 at t22
    show tina turned suit cross anno om zorder 2 at t44
    everyone "Right!"
    hide akira
    hide lilly 
    hide mari 
    hide tina
    hide kotonoha
    "Someone's serious!"
    "Does she always do this?"
    show kotonoha turned casual anno rhip om zorder 5 at t11
    k "So!  We need to find Kirinani!"
    "Agh!  Should've known that fire wouldn't kill him."
    k lup "I know he's not home, I tore up that place hours ago."
    show kotonoha cm
    show akira 4ae zorder 4 at r44
    ak "(Quite literally!  That would explain the mess.)"
    ak 1ab "Always thorough!  That's what I like about you, Kotonoha!"
    show akira at rhide
    hide akira
    "...{w=1}\nI'm not even gonna question what that could mean."
    k om "So, we need to figure out where else he may be."
    show kotonoha at rhide
    hide kotonoha
    show tina turned suit anno om zorder 2 at l11
    ti "I might have a suggestion for that."
    ti lpistol "There's an old mansion at the west side of town about 50 blocks from here."
    ti ldown "That place has been abandoned for years but I know some friends that like to hang out around there."
    "Wait!"
    show tina cm
    a "No, not that place!"
    ti om "Yes that place.\nWhat?  Sound like a death wish?"
    show tina cm
    a "Are you crazy!?  That place is swarming with wraiths!"
    ti lpistol om "And?"
    "Oh, don't point a gun at me!  Even if it is a fingergun."
    "They're scaring me."
    show tina at lhide
    hide tina
    show lilly ee zorder 2 at r11
    a "My god, you guys do this all the time?"
    lil "Pretty much."
    show lilly doll c0 with blink
    lil "But it's fun!{w=0.25}{nw}"
    scene bg kamiclassnight
    show lilly doll a0 zorder 2 at t11
    with blink
    $ pause(0.25)
    scene bg kamiclassnight
    show lilly norm f1c2 zorder 2 at t11
    with blink
    "...{w=1}{nw}" with blink
    "..." with blink
    "The fuck?"
    show kotonoha turned casual curi om zorder 1 at l21
    show lilly at t22
    k "You look like you just saw a ghost."
    "Huh?"
    a "You didn't see that just now?"
    k rhip "No?"
    lil c1e "(Wait...)"
    a "I think I'm going crazy."
    lil c3 "(You're... not...)"
    "What?"
    show lilly at rhide
    hide lilly
    show kotonoha anno zorder 2 at t11
    k "Anyway, I think your plan works here unless anyone else has any better plans."
    show kotonoha cm
    "No one answers."
    k om "Then we'll head there at 22:00 tomorrow!"
    show akira 4ae zorder 4 at t21
    show lilly norm se zorder 1 at t41
    show mari forward anno om zorder 3 at t22
    show tina turned cross anno om zorder 2 at t44
    everyone "Right!"
    return

label act2_ch1_alt:
    a "...{w=2}*Inhale*"
    stop music
    a "I'm sorry, I can't..."
    ak 1al "!!!"
    hide akira
    ak "Aoruguri?  Aoruguri!"
    scene bg kamihallnight with wipeleft_scene
    a "*Huff* *Puff*"
    a "Damnit!  WHY!?"
    show mari forward worr zorder 2 at t11
    ma "Aoruguri?"
    a "Mari..."
    a "I'm sorry...  I couldn't do it!"
    ma sad "Aoruguri..."
    scene black with dissolve_scene
    ma "Hey, honey...  It's okay."
    ma "You're okay."
    ma "Here..."
    scene noise with None
    play sound static
    $ pause(0.15)
    stop sound
    show bg office at center_zoom(1.0, 2.0, 5.0)
    ma "Let's head to my office, okay?"
    a "Okay..."
    play ambience clock
    scene bg mari_office with dissolve_scene_full
    call showlocation("Principal's Office", "October 8, 2023",659.95,"bg mari_office")
    call showintro(intro_mari)
    show mari forward worr zorder 2 at t11
    ma "So it was the Midnight Club that offered you to join them."
    a "Yes..."
    ma ea "*Sigh*"
    ma ef "You know, I'm affiliated with that club.  I participate in some of the endeavors they go through."
    a "What?"
    a "Mari, you daredevil!  Do you how many dangerous situations they get themselves into?"
    ma ed "I am not a daredevil, we both know those are more reckless than this club."
    a "I'm not so sure about 'both'."
    ma ef "Well, at least I know."
    ma ea "And the rest of the club..."
    ma ef "Going in circles."
    ma "Look, what I want to get at is that they could use you."
    a "Just because you want me there with you?"
    ma ed "No..."
    ma ec "Here."
    hide mari
    "Mari goes to the computers on the left which show the classroom cameras and focuses the one for 3-B onto the projector."
    "I watch as the members talk about what I just did."
    stop ambience fadeout 1.0
    scene bg kamiclassnight with wipeleft_scene
    
    return