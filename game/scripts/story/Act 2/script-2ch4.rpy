#Name: A Past Regained
label act2_ch4_main:
    if not known:
        jump act2_ch4_alt
    stop music fadeout 2.0
    play ambience mansion
    scene bg mansion
    with dissolve_scene_full
    call showlocation("Wraith Mansion","October 11, 2023",21*60+14+57/60.0,"bg mansion") from _call_showlocation_43
    k "We're here."
    "Welp, here we go..."
    a "Everyone got their flashlights?"
    "Everyone shows their flashlights."
    a "Good."
    "*Deep breath*"
    "I've seen this place before, but I've never been inside."
    a "Here goes nothing."
    "We all walk inside."
    scene bg foyer
    show screen flashlight 
    with wipeleft_scene
    "...{w=1}Huh?"
    show kotonoha turned casual curi om zorder 2 at t11
    k "Something wrong?"
    a "No?  Just thought... this place looked familiar..."
    show tina turned curi om zorder 2 at l21
    show kotonoha at t22
    ti "Huh?  I thought the Kamiyama family was the only one that lived here."
    show tina at t21
    a "So that's why you wanted to come here!"
    "Do these people seriously not question any plans?"
    ti neut "Yeah, this won't tell us where he is...  But this may give us a hint as to why he's doing everything's he's doing."
    k rhip anno "Alright, Aoruguri, let's see how you are with arrangements!"
    hide tina
    hide kotonoha
    a "Alright.  Since this is a big place, we'll split up!"
    show kotonoha turned casual anno rhip zorder 2 at t22
    show akira 4ad zorder 2 at t21
    a "Kotonoha and Akira will take this floor,"
    hide akira
    hide kotonoha
    show mari forward angr zorder 2 at t22
    show tina turned suit cross anno zorder 2 at t21
    a "Mari and Tina will search upstairs,"
    hide tina
    hide mari
    show lilly casual norm se zorder 2 at t11
    a "and Lilly and I will head to the basement."
    hide lilly
    show tina turned suit cross anno om zorder 2 at t11
    ti "The basement's been blocked for God knows how long, good luck finding it."
    show tina cm
    a "I'm sure we'll find it easily."
    hide tina
    scene bg dark_dining
    show screen flashlight 
    with wipeleft_scene
    "..."
    "Why does this place look so...?"
    lil "Behind you!"
    play sound "sfx/giggle.ogg"
    show screen wraith_tut
    "Stay calm!  Gotta hold my flashlight on it's face!"
    "Whew."
    show lilly casual c2e zorder 2 at t11
    lil "Are you okay?"
    a "Yeah, thanks."
    a "Why aren't you using your true form?"
    lil c2c2 "Normally I would, but then I wouldn't be able to use my flashlight, the only thing that works on these."
    a "Oh."
    "Not sure how that works, but I don't know how dolls work, I've never had one in my life."
    "I didn't even know one could be alive!"
    a "Well anyway, come on.  I found the basement back here."
    scene bg first_room
    show screen flashlight 
    with wipeleft_scene
    "Well, here we go."
    call explore("first_room") from _call_explore_2
    call act2_ch4_common
    return

label act2_ch4_alt:
    stop music fadeout 2.0
    #play ambience mansion
    scene bg foyer
    show dark zorder 10
    with dissolve_scene_full
    call showlocation("Wraith Mansion","October 11, 2023",21*60+14+57/60.0,"bg mansion")
    a "..."
    "I honestly have no idea what I'm doing here."
    "This is stupid!  This is reckless!"
    "I should get out of here while I can!"
    "Yet why does this place look so..." 
    "...familiar?"
    play sound "sfx/giggle.ogg"
    $ pause(1.0)
    a "Eh?"
    "That might've been my imagination..."
    "I didn't bring a flashlight, I'm a fucking idiot."
    play sound footsteps
    a "!!!"
    a "Oh, I am so dead."
    scene bg dark_dining
    show dark zorder 10 
    with wipeleft_scene
    "I hate this!"
    "This place is so barren!"
    "And there's decade old blood everywhere!"
    "The fuck happened here?  Whose is this?"
    $ pla = "???"
    general "YOURS."
    a "!!!"
    "..."
    a "It's fine."
    a "Everything's fine."
    a "This isn't terrifying at all."
    "Oh, who am I kidding?  You know it's bad if I'm this scared!"
    general "YOU DON'T HAVE TO REASSURE YOURSELF..."
    general "WE WON'T HURT YOU!"
    a "Yeah, right."
    scene bg top_kitchen
    show dark zorder 10 
    with wipeleft_scene
    "I don't know how I haven't been attacked yet."
    "With every step I take, I regret this more."
    a "Damnit, just kill me already!"
    general "NOW THAT WOULDN'T BE VERY LOVING OF US, WOULD IT?"
    "I don't trust them in the slightest."
    "I check the drawers and cabinets."
    "..."
    a "Ugh!  There's nothing in these!"
    general "YOU'LL FIND SOMETHING IN YOUR RO-"
    a "Fuck off!  I'm leaving!"
    "I should've never gone in here in the first place"
    scene bg bedroom1
    show dark zorder 10 
    with wipeleft_scene
    a "Huh?!"
    a "This isn't the foyer!"
    a "Did I take a wrong turn?"
    a "Oh God!"
    scene bg bad_bedroom
    show dark zorder 10 
    with wipeleft_scene
    "I'm so lost..."
    "This room has the least amount of blood."
    general "OUR ROOM."
    play sound "sfx/giggle.ogg"
    show wraith_black zorder 2 at t11
    a "!!!"
    a "I don't have a...{nw}"
    play sound jumpscare
    show wraith_black zorder 1000 at face
    $ pause(0.25)
    scene black with None
    stop sound fadeout 3.0
    $ pause(3.0)
    call act2_ch4_common
    return

label act2_ch4_common:
    stop music fadeout 2.0
    play ambience mansion fadein 1.0
    a "{cps=3}...?{/cps}"
    scene bg final_room
    with dissolve_scene_full
    call showlocation("???","October 11, 2023",23*60+59+57/60.0,"bg final_room")
    a "Huh?  Where am I?"
    "Why is there blood?"
    a "Hey, what the fuck?"
    "I immediately try the door."
    a "*Struggling* Hey!  Let me out!  *Bangs door*"
    "..."
    a "No answer."
    "Why do I even try?  That never works..."
    $ pla = "???"
    general "YOU KNOW THIS PLACE."
    a "Who's there?"
    "My memory's all fuzzy."
    general "YOU DON'T KNOW US."
    a "What?"
    general "WE KNOW YOU."
    a "Cut the bullshit!"
    a "Tell me who you are!"
    stop ambience
    show wraith_black at t11
    show wraith_black1 at t21
    show wraith_black2 at t22
    show wraith_black3 at t41
    show wraith_black4 at t44
    general "YOUR SISTER."
    a "Huh?"
    $ pause(0.5)
    show wraith_black1 at t11
    show wraith_black2 at t11
    show wraith_black3 at t11
    show wraith_black4 at t11
    with None
    hide wraith_black 
    hide wraith_black1
    hide wraith_black2
    hide wraith_black3
    hide wraith_black4
    show engeki turned sweater rchest zorder 2 at t11
    with blink
    show engeki mb
    general "Hello."
    general "It's me."
    en "Engeki."
    show engeki ma
    a "Engeki?"
    call showintro(intro_en)
    "I swear, my family gets the weirdest names.  And I'm no exception."
    a "Are you merged with the wraiths?"
    en ec mf bb "Kind of..."
    en ea ba "I didn't think it would happen."
    en "But it allowed me escape."
    en rdown "It's a common misconception that all wraiths are evil."
    show engeki mj
    "Guess that's why they didn't kill me."
    en lchest mb "Actually, most wraiths will do no harm to you."
    show engeki ma
    a "Then where did the misconception come from?"
    en ec me ldown bb "People can have the weirdest gossip sometimes..."
    a "Don't get me started."
    en ea mh rchest ba "Yeah, I'd rather get your memory back."
    a "My memory?"
    en mb "Come with me to the bathroom."
    en mh bb "I hope you're not squeamish..."
    a "Sis, I have an iron stomach."
    en me ba ee "'Sis'?"
    a "You said you're my sister, right?"
    en mh "Well yeah, but..."
    en mf "I didn't expect to be called 'Sis' so soon!"
    a "Honestly, I just wanted to see how it would feel."
    en mb ea "And?"
    show engeki ma
    a "It felt nice... to know I have family that cares for me."
    show engeki lchest
    "She smiles."
    en ldown rdown mh "We shouldn't waste any more time."
    scene bg dark_bathroom 
    show darkred
    with wipeleft
    a "Jesus fucking Christ!"
    "So much blood!"
    en "Don't worry, he's dead."
    "Evidently."
    "What the fuck happened?"
    show tetsuo towards ce zorder 2 at t11
    "He's just..."
    a "!!!"
    show tetsuo oe at face
    play music jumpscare
    $ pause(0.1)
    hide tetsuo
    play ambience hb
    show veins zorder 10 at heartbeat
    a "Ah!"
    en "Are you-"
    a "I'm fine!"
    play sound static
    scene noise with None
    $ pause(0.25)
    stop sound
    scene bg room
    show darkred
    show veins zorder 10 at heartbeat
    show tetsuo towards zorder 2 at t11
    with None
    $ pause(1.0)
    play sound static
    scene noise with None
    $ pause(0.25)
    stop sound
    scene bg dark_kitchen
    show darkred
    show veins zorder 10 at heartbeat
    show tetsuo towards zorder 2 at t11
    with None
    $ pause(0.5)
    play sound "sfx/slap.ogg"
    hide tetsuo
    $ pause(0.5)
    play sound static
    scene noise with None
    $ pause(0.25)
    stop sound
    scene bg bedroom1
    show darkred zorder 9
    show veins zorder 10 at heartbeat
    play sound fall
    $ pause(1.0)
    show tetsuo towards cross zorder 2 at t11
    with None
    $ pause(1.0)
    play sound static
    scene noise with None
    $ pause(0.25)
    stop sound
    scene bg hall2
    show darkred zorder 9
    show veins zorder 10 at heartbeat
    play sound fall2
    $ pause(1.0)
    show tetsuo towards cross zorder 2 at t11
    with None
    $ pause(1.0)
    play sound static
    scene noise with None
    $ pause(0.25)
    stop sound
    scene bg dark_bathroom
    show darkred zorder 9
    show veins zorder 10 at heartbeat
    show tetsuo towards zorder 2 at t11
    with None
    $ pause(0.5)
    show testuo shoc
    play sound static
    show noise zorder 12 with None
    $ pause(0.1)
    stop sound
    hide noise
    $ pause(0.1)
    play sound static
    show noise zorder 12 with None
    $ pause(0.1)
    stop sound
    hide noise
    $ pause(0.1)
    play sound static
    show noise zorder 12 with None
    $ pause(0.1)
    stop sound
    hide noise
    $ pause(0.1)
    play sound static
    show noise zorder 12 with None
    $ pause(0.1)
    stop sound
    hide noise
    $ pause(0.1)
    play sound static
    show noise zorder 12 with None
    $ pause(0.25)
    stop sound
    hide noise
    $ pause(0.25)
    play sound static
    scene noise with None
    $ pause(1.0)
    stop sound
    stop ambience
    stop music
    scene bg dark_bathroom
    show vignette zorder 10
    show engeki turned sweater rchest mi zorder 2 at t11
    play music confdep
    hide vignette with Dissolve(3.0)
    a "I'm okay... I'm okay..."
    a "I remember everything."
    en mh "Are you sure?"
    show engeki mi
    a "Yes."
    en mf ec rdown "I thought that would be more difficult."
    a "Maybe it was that easy because I've been seeing visions of these memories for a few months now."
    en ea "I think I started those."
    a "Not surprised."
    en mi lchest rchest "..."
    a "Sorry, can I... step outside?  I don't think I wanna look at this anymore."
    en "*Nod*"
    scene bg foyer with wipeleft_scene
    "As I realize a decision I want to make, I stop at the door."
    show engeki turned sweater mi rchest bb zorder 2 at t11
    a "Sis..."
    a "I have an enemy outside that I am looking for, I know he survived what I did to him."
    a "Once I step out this door, I won't be coming back for a long time, I may never come back at all."
    a "Do you want to come with me?"
    en eb mh lchest "I'm sorry, I can't..."
    a "What's stopping you?"
    en ed "They are..."
    en eb "They are afraid of what's out there..."
    en ldown "It's why I've stayed here for many years."
    show engeki mi
    a "..."
    menu:
        "Encourage them.":
            $ en_out = True
            $ persistent.choices_made.append("Engeki Left")
            a "No..."
            a "That's not what's stopping you."
            a "They're not scared of the outside..."
            a "They're scared of themselves."
            en ee mh "Huh?"
            a "They're scared of what they'll do to the outside."
            en ba rdown "What do you..."
            a "It's okay.  I was the same once."
            a "But think about this: our mother's out there!"
            en ea "Our mother?"
            a "Yeah!"
            a "And I'm sure she's dying to see you again!"
            en eb mb rchest "I can't believe it!"
            en "Our mother..."
            en ej mj lchest "*Sniff*"
            "I give her a minute."
            en eb mb ldown "I'm fine, I'm okay."
            en rdown "Let's go."
            show engeki ma
            "We step out the door."
        "Understand them.":
            $ en_out = False
            $ persistent.choices_made.append("Engeki Stayed")
            a "I understand."
            a "Guess that's it then..."
            a "*Sigh*"
            "..."
            en mh "Will you-"
            a "I'll come back, I promise I'll come back."
            en ec mf "Okay..."
            show engeki mi
            a "Until then, See you later."
            show engeki ei
            "I step out the door."
    stop ambience fadeout 1.0
    if known:
        call act2_ch4_main_end
    else:
        call act2_ch4_alt_end
    return

label act2_ch4_main_end:
    scene bg mansion with wipeleft_scene
    "We're out!"
    show kotonoha turned casual curi om zorder 2 at t11
    "..."
    a "!!!"
    "My other memory fades back."
    a "Hey, guys!  I made it!"
    k surp cm "!!!"
    k om "Hey guys, she's back!"
    hide kotonoha
    ti "Thank God!"
    "Akira and Tina are way in the back."
    show mari forward happ zorder 2 at t11
    ma om "Aoruguri!"
    a "Mom!"
    show mari cm at face
    "..."
    show mari oe at t11
    ma om "I'm glad you're okay, you have no idea how worried I was!"
    show mari cm
    a "I can imagine."
    if en_out:
        a "My sister is here too."
        show mari curi at t21
        show engeki turned sweater rchest eb at r22
        en mb "Mother!"
        show engeki 
        ma "Engeki?"
        ma happ om "Oh my God!"
        ma tears "I knew it, you're alive!"
        en mb "I'm sorry!  I've been gone too long!"
        show engeki ma
        ma "Engeki..."
        show mari cm at t22
        show engeki ej at t33
        "..."
        hide engeki
    else:
        "I choose not to mention Engeki."
    hide mari
    a "Where's Lilly?"
    show lilly casual doll a0 zorder 2 at t11
    a "!!!"
    "On the ground?"
    a "Lilly!"
    "She's not okay, she's barely stable!"
    k "Don't worry about that, that's just a doll!  We gotta-"
    a "No, you don't understand!  This {i}is{/i} her!"
    k "What?"
    a "We gotta..."
    a "Wait a second."
    "They can see her?"
    a "Did something happen while I was-{nw}"
    hide lilly
    play sound "sfx/monikapound.ogg"
    with Shake((0, 0, 0, 0), 0.1, dist=50)
    a "FUCK!"
    a "What happened?"
    ma "Everyone okay?  What was that?"
    a "A-"
    scene black with dissolve
    a "*Exasperated gasp*"
    a "..."
    "He's back..."
    a "Guys..."
    a "Take care of Lilly."
    k "What are you...?"
    return

label act2_ch4_alt_end:
    scene bg mansion with wipeleft_scene
    "Well..."
    "It's time to-{nw}"
    play sound "sfx/monikapound.ogg"
    with Shake((0, 0, 0, 0), 0.1, dist=50)
    a "FUCK!"
    a "What happened?"
    a "A-"
    scene black with dissolve
    a "*Exasperated gasp*"
    a "..."
    "He's back..."
    return