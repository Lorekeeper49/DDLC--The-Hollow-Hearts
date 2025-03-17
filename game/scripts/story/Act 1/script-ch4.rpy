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

        
        
    show lilly norm a1e zorder 2 at t11
    t "Lilly, can we talk?"
    lil c2 "Uh."
    show lilly c2e
    extend "  Sure, what's up?"
    show lilly a1e
    t "Outside.  Let's go outside for this."
    "I sound serious but I don't mean to."
    scene bg schoolriverday with wipeleft_scene
    play ambience river fadein 1.0
    play ambience2 forest fadein 1.0
    call showlocation("Sakura River\n{size=25}桜川{/size}","October 2, 2023\n{size=15}2023年10月1日{/size}",11*60+29+57/60.0, "bg schoolriverday")
    show lilly norm c2e zorder 2 at t32
    show natsuki turned neut rhip zorder 2 at t31
    show yuri turned neut zorder 2 at t33
    lil "So, what's up?"
    show lilly a1e
    "Natsuki's here too, just to give us another set of eyes."
    t "Can you like... transform here?"
    show natsuki lsur
    show yuri curi
    lil c1e "Uh, what?"
    t "I wanna check something..."
    lil c2e "Okay..."
    n rdown om "Oh no..."
    play music jumpscare
    stop ambience
    stop ambience2
    show vignette zorder 1 with BumpTransition
    show natsuki s_scream at h31
    show yuri nerv
    show lilly doll a0
    $ pause(0.5)
    n "*Screams in terror*{w=0.5}{nw}"
    t "Natsuki!  Natsuki!  Calm down!"
    "I hold Natsuki by the shoulders, making sure she doesn't run away from the terror that is in front of her."
    "In front of me too."
    "Jesus Christ, is this what she truly looks like?"
    show lilly a0 with Fade(0.0, 0.05, 0.0)
    $ pause(0.05)
    show lilly with Fade(0.0, 0.05, 0.0)
    $ pause(0.05)
    show lilly with Fade(0.0, 0.05, 0.0)
    $ pause(0.05)
    show lilly with Fade(0.0, 0.05, 0.0)
    $ pause(0.05)
    stop music
    hide vignette 
    show natsuki pani
    with Fade(0.0, 1.0, 0.0)
    $ pause(1.0)
    play ambience river fadein 1.0
    play ambience2 forest fadein 1.0
    t "I knew it!"
    show yuri lsur 
    lil w3e "Wait, you saw me?!"
    y vsur om rup "Are you serious?"
    show natsuki nerv rhip
    "Natsuki and I both nod our heads."
    lil w3 "...What?"
    y lup "I saw nothing."
    "Then what was your reaction earlier?"
    n om "Now I understand why you two like horror so much."
    "How is that relevent in any way?"
    lil w3e "But that doesn't make any sense!"
    lil w3 "How did you..."
    lil w3e "No.  How did {i}either{/i} of you see my true form?!"
    lil w3e2b "I left this life so long ago!"
    lil doll a3 "He forced me to be alone!"
    hide natsuki
    hide yuri
    lil "He created me just to be some crazy science experiment, never to go outside!"
    lil a4 "I just wanted to talk with people!"
    show vignette zorder 1 with dissolve
    lil "I just wanted to make friends!"
    show darkred zorder 1 with dissolve
    lil "Not be human!"
    show lilly a2
    "She's crying blood!"
    lil a4 "This is what I want you to see me as!"
    hide darkred with dissolve
    lil "Not that!"


    
    return