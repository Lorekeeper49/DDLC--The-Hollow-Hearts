label nstory(bgreturn="bg club_day"):
    scene black with dissolve_scene
    $ window_style = ""
    $ nb = "namebox"
    $ nextscene = "nstory_ch" + str(chapter)
    $ char_perspective = "Natsuki"
    $ aoruguri = "ルナ煽るぐり\n{size=15}Luna Aoruguri{/size}"
    call expression nextscene 
    $ char_perspective = "Taiyen"
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
    call showlocation("Luna Mansion\n{size=25}ルナの邸宅{/size}","August 1, 2018\n{size=15}2015年8月1日{/size}",23*60+59+57/60.0,"bg mansion")
    show tetsuo towards zorder 2 at t11
    $ pause(1.0)
    hide tetsuo towards
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
    y neut "We'll see ourselves out."
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
    a rdown om "Just that wind broken the windows as that's been a common problem for us."
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
    ""

    return

label nstory_ch3:
    #call showlocation("???","Monday, March 1, 2018",21,59,57)
    "Brought down...{w=1}\nBeaten...{w=1}\nKilled..."
    "All because they fell in love with a boy..."
    "Because our father believes that love drove his wife to the grave!"
    "!!!"
    "Dammit!  Right now, I'm in torture!"
    "Captivator" "Where is he!?"
    n "I'd talk if you didn't tape my mouth shut, morons!"
    "{w=1}They facepalm."
    "Slightly surprised they heard that."
    "They remove the tape and I begin talking."
    n "If you mean the boy that entered my room the other day, then he left before I got a chance to ask his identity."
    n "He's probably off whereever he usually hides."
    "They're gonna kill me, this is not nearly enough information for them."
    n "By the way, my father kills his children if they even {i}sound{/i} like they're in love with someone so you may want to be careful with you if you want me alive."

    return

label nstory_ch4:
    call showlocation("???","Monday, August 1, 2018",23,59,57)

    return

label nstory_ch5:
    call showlocation("???","Monday, August 1, 2018",23,59,57)

    return