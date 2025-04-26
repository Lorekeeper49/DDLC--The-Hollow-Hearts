label nstory(bgreturn="bg club_day"):
    scene black with dissolve_scene
    $ window_style = ""
    $ nb = "namebox"
    $ nextscene = "nstory_ch" + str(chapter)
    $ char_perspective = "Natsuki"
    $ aoruguri = "ルナ煽るぐり\n{size=15}Luna Aoruguri{/size}"
    call expression nextscene 
    $ char_perspective = "Taiyen"
    stop ambience fadeout 2.0
    stop music fadeout 2.0
    stop sound fadeout 2.0
    scene black with dissolve_scene
    $ window_style = "fake"
    $ nb = "namebox_fake"
    scene expression bgreturn with dissolve_scene_half
    return

label nstory_ch2:
    play ambience creepy
    scene bg bad_bedroom with dissolve_scene_half
    call showlocation("Luna Mansion\n{size=25}ルナの邸宅{/size}","June 21, 2018\n{size=15}2018年6月21日{/size}",23*60+59+57/60.0,"bg mansion")
    show tetsuo towards zorder 2 at t11
    $ pause(1.0)
    hide tetsuo
    $ pause(1.0)
    n "..."
    n "Sis!  How are you doing?"
    a "Not great."
    a "That fucking father ass prick doesn't know what's good for himself!"
    "Where the hell does she learn this language?"
    a "We're still keeping the no sleep thing secret, right?"
    n "Yeah, not a word from me."
    play sound fall2
    with Shake((0, 0, 0, 0), 0.1, dist=50)
    $ pla = "二人共\n{size=15}Both{/size}"
    general "Aah!"
    a "Jesus Christ!"
    tet "WHAT THE HELL WAS THAT?!"
    n "FINDING OUT!"
    "I get out of bed."
    show yuri turned casual worr rup om zorder 2 at t22
    show lilly casual norm a1c2 zorder 2 at t21
    y "You okay?  I didn't get your strings, did I?"
    lil c3 "No, you're fine Sis."
    show lilly a1
    y rdown ce "Thank goodness!  I thought I went too hard this time!"
    n "..."
    y neut oe "We'll see ourselves out."
    hide yuri
    hide lilly
    n "Wait!"
    a "Nat, What are you doing!?"
    n "They can help us!"
    a "Just fix the window.  We can figure that out in a bit.  I'll handle the report."
    "I oblige."
    "..."
    "Oh, they must've heard me."
    "I can see them on the outside of the window."
    n "Alright, the windows done!"
    show aoruguri turned casual neut rhip om zorder 2 at t11
    a "Perfect timing, I just finished the report."
    show aoruguri cm
    n "What'd you tell him?"
    a rdown om "Just that wind broke the window as that's been a common problem for us."
    show aoruguri cm
    n "Don't remind me!"
    n "I'm not sure why he insists on having us live in this house."
    a cross om "Mansion."
    show aoruguri cm
    n "A mansion is a type of house."
    hide aoruguri
    show lilly casual norm c2e zorder 2 at t21
    show yuri turned casual zorder 2 at t22
    lil "Ca-can we come in?"
    show lilly a1
    y worr om "You can do this, Lilly.  Just don't think like what you are, even if you wanna be it."
    "I'm not gonna ask."
    n "You can come in, just be quiet."
    show yuri neut cm
    "They slowly walk through the window and put their feet on the floor."
    y om "What's wrong?"
    show yuri cm
    n "Our father."
    n "Just look at my sister over here."
    n "Her face may not be covered in blood, but she is in serious distress."
    lil c2e "God, that sounds like hell."
    show lilly a2e
    n "You haven't even heard the half of it."
    a "I want him fucking dead."
    n "Seriously, where do you learn this language?"
    "She doesn't answer."
    n "Anyway, I don't know what she's been through, but it's pretty bad."
    show lilly at lhide
    show yuri at lhide
    hide lilly
    hide yuri
    show aoruguri cross casual neut om zorder 2 at r11
    a "Here, let me just tell you the details."
    return

label nstory_ch3:
    play ambience creepy
    scene bg bad_bedroom with dissolve_scene_half
    $ char_perspective = "Aoruguri"
    call showlocation("Luna Mansion\n{size=25}ルナの邸宅{/size}","June 21, 2018\n{size=15}2018年6月21日{/size}",23*60+59+57/60.0,"bg mansion")
    a "What he does is painful!"
    a "Guy's a fucking sadist!"
    show tetsuo towards zorder 2 at t11
    a "He forces us to hurt so many people for his own gain..."
    a "All to build the world his brother envisions."
    a "A world that they control."
    hide tetsuo
    a "And worst of all..."
    a "We're not the only ones being used."
    show wraith_black zorder 2 at t11
    a "There's someone else in this home."
    a "I don't know who they are but..."
    a "I got this strong feeling that they're being used for some crazy deed."
    a "Especially after our brother ran away."
    a "I don't know what he found out, but it's probably pretty bad."
    hide wraith_black
    a "And the screaming..."
    a "The blood curdling fucking screaming!"
    a "It's from our mother..."
    a "And it's nightmare inducing!"
    a "He hates us!"
    show mari forward sad zorder 2 at t11
    a "And our mother can't fight back!"
    a "At this point, I wouldn't surprised if he forced us to watch him rape her."
    hide mari
    n "What the fuck?"
    a "Exactly."
    a "This old man is fucked up."
    a "And we need him dead."
    show lilly casual norm a2e zorder 2 at t21
    show yuri turned casual zorder 2 at t22
    a "Think you could help us?"
    lil c3 "I'm not sure if we can-{nw}"
    y angr rup om "Yes!"
    lil c3e "Sis!"
    y anno "I don't what I'm doing but I'm doing it."
    show lilly a2e
    y angr "We're in a similar position and we don't want anyone to suffer like we have."
    y rdown "What plans do you have?"
    show yuri cm
    a "None at the moment."
    y om "That's fine."
    y rup "We'll figure something out."
    y lup "Together!"
    y ldown "We'll help you out.  We promise."
    return

label nstory_ch4:
    play ambience creepy
    scene bg bad_bedroom with dissolve_scene_half
    call showlocation("Luna Mansion\n{size=25}ルナの邸宅{/size}","July 5, 2018\n{size=15}2018年7月5日{/size}",23*60+59+57/60.0,"bg mansion")
    show yuri turned casual zorder 2 at t11
    y om "Hello."
    n "Where have you been?"
    y curi "Sorry?"
    y rup "I don't think I've...{nw}"
    y angr "Don't mind her." with blink
    n "Okay?"
    show yuri cm
    "What the?"
    "Does she have a split personality?"
    n "Whatever.  Listen, my sister's downstairs, getting her regularly scheduled beat up."
    "God, my jokes are terrible..."
    ""

    return

label nstory_ch5:
    play ambience creepy
    scene bg dark_bathroom with dissolve_scene_half
    a "Go!  Get out of here!"
    n "What?!  I'm not leaving you!"
    tet "Get me the fuck out of here this instant!"
    a "GO!!!"
    n "...!"
    y "Natsuki..."
    y "Trust her."
    n "..."
    n "Okay..."
    stop ambience fadeout 1.0
    scene bg mansion with wipeleft
    $ pause(1.0)
    play sound thunder2
    scene bg club_day 
    show natsuki turned dist rhip lhip zorder 2 at t11
    with Fade(0.1, 5.0, 3.0, color="#fff")
    $ char_perspective = "Taiyen"
    n om "I never saw her again after that..."
    n ldown "I thought she was dead..."
    n cm "..."
    n om "I need a minute..."
    hide natsuki
    "She walks to the back of the room."
    "We give her time to recover."
    return