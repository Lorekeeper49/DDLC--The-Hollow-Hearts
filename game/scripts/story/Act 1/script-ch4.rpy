label act1_ch4_main:
    stop music fadeout 2.0
    play music confdep
    scene bg park_01
    with dissolve_scene_full
    call showlocation("Kamiyama Park","October 2, 2023",5*60+0+0/60.0,"bg park_01") from _call_showlocation_15
    $ style.say_window = style.window
    $ nb = "namebox"
    "Sayori and I woke up early and couldn't get back to sleep so we decided to practice archery by literally firing on each other while going through the arrows since we don't have actual targets."
    show sayori turned neut cm zorder 2 at t11
    "Sayori aims the bow at me and draws an arrow."
    "I go into ghost mode."
    play sound deadmantrans
    $ renpy.music.play(audio.deadamb, channel="ambience", fadein=0.5)
    show veins with blink
    t "Fire!"
    "She releases the arrow."
    "HEADSHOT!"
    t "Nice!{nw}"
    play sound deadmantransout
    hide veins with blink
    $ renpy.music.stop(channel="ambience", fadeout=0.5)
    extend "  You've gotten really good at this!"
    s happ om rup "Thanks!"
    show sayori neut
    "She puts away her bow and changes the subject."
    s rdown "You remember prelife?"
    t "How could I forget when we were at war with that storm for the entire century that we were in there!"
    s worr rup "You know, I'm worried about her."
    "What?"
    s "Apparently, the war didn't start deliberately."
    s rdown "She lost control."
    t "Who are you talking about?"
    s rup "I wouldn't want that to happen to her again."
    show sayori cm
    t "Okay, Sayori, could you not play the pronoun game for 5 seconds!?"
    "For God's sake, this is why I try to avoid the pronoun game!"
    s om "I have to."
    s dist rdown "I don't... know her name..."
    t "..."
    "I decide not to press further."
    t "Well, I'm out of arrows, wanna head to school early?"
    s neut rup "Sure."
    scene bg school_day with wipeleft_scene
   
    return

label act1_ch4_end:
    
    "Where am I?"
    "Why am I here?"
    ha "I talked with him."
    show hanato day casual neut ce rhip zorder 2 at t11
    t "Huh?"
    ha oe om "I talked with Kirinani."
    ha ce rup "I don't know how he did it."
    ha oe rdown "But he's a copycat."
    t "But... he was born a-"
    ha rhip lhip "I know, it doesn't make sense!"
    ha dist ce rdown ldown "And I work with him?"
    ha oe "But, I don't like how things are anymore."
    ha neut rhip "After hearing your story, and finding out why he's so mad with you..."
    ha dist rup "I don't know if I can trust him anymore."
    ha ce rdown "Especially with whatever he could possibly be planning to do with breaker."
    show hanato cm
    t "B-Breaker?!"
    ha curi oe "You know what that is?"
    t "A special substance originally made to voluntarily remove someone's attribute so they can safely switch to another one."
    t "However, at some point during the manufactoring process, only 3 out of the 5 tests scheduled were processed, the others were cancelled because something went horribly wrong with each test."
    t "Turns out that the substance not only removes the attribute, but it also destroys the frontal lobe to the point where the person ends up suffering for the rest of their life."
    t "You don't wanna know the details, but it's pretty horrible..."
    ha om "Jesus!  Now I know why he wants it."
    show hanato cm
    t "Actually, I just remembered..."
    t "He was one of the test subjects..."
    ha rhip om "So... he's not himself..."
    t "Yeah... and he never will be again..."
    ha rdown ce "Good fuck!"
    ha laug lup "And that officially marks the first time I've sweared."
    ha neut rhip "But, I'm really not liking this anymore..."
    ha ldown "So, from this point onward, I am now spying on my own family...\nNever thought I'd say that."
    ha lup "Since I know you can lucid dream, I'm allowing you to come here at any time.  Just be aware that my family may be here at the same time as you, so pick your times carefully."
    ha ldown rdown "I'll let you off now while I look for backup on this."
    t "Okay."
    "Things just got a whole lot harder..."
    return