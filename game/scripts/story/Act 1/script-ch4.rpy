label act1_ch4_main:
    stop music fadeout 2.0
    play music confdep
    scene bg park_01
    with dissolve_scene_full
    call showlocation("Kamiyama Park\n{size=25}神山のパーク{/size}","October 2, 2023\n{size=15}2023年10月2日{/size}",5*60+0+0/60.0,"bg park_01")
    $ window_style = ""
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

    if known:
        # Talk to Natsuki about Aoruguri
    else:
        # Ask Lilly why we were able to see her true form


    
    return