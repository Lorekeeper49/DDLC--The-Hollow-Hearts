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
    t "Not to mention, you're literally writing about it."
    s worr rup "You know, I'm worried about her."
    t "Huh?"
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
    stop music fadeout 1.0
    scene bg school_day with wipeleft_scene
    $ window_style = "fake"
    $ nb = "namebox_fake"

        
        
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
    hide natsuki
    show natsuki turned pani om zorder 2 at t31
    show lilly norm a1e
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
    stop ambience
    stop ambience2
    play music static
    $ renpy.music.set_volume(0.25, delay=0, channel="music")
    lil doll c0 "He forced me to be alone!"
    hide natsuki
    hide yuri
    lil "He created me just to be some crazy science experiment, never to go outside!"
    lil d0 "I just wanted to talk with people!"
    $ renpy.music.set_volume(0.50, delay=0, channel="music")
    show vignette zorder 1
    lil "I just wanted to make friends!"
    $ renpy.music.set_volume(0.75, delay=0, channel="music")
    show darkred zorder 1
    lil "Not be human!"
    show lilly b0
    "She's crying blood!"
    lil d0 "This is what I want you to see me as!"
    $ renpy.music.set_volume(1.0, delay=0, channel="music")
    hide darkred
    lil "Not that!"
    show lilly b0
    "I feel bad."
    "But..."
    "I finally understand why she was the way she was back then."
    stop music fadeout 1.0
    scene black with dissolve_scene
    "Back then, when I first met Lilly..."
    "I was the one who came to her."
    "But... she wouldn't talk to me..."
    # Transition to scene of Lilly and Taiyen's first meeting
    

    scene black with dissolve_scene
    "As I retell this story, I realize that I am not just talking to myself."
    show dark zorder 3
    show hanato night zorder 2 at t11
    "In fact, I can see her right now, hiding in the darkness of my mind."
    "I know her, and she is impolitely listening."
    "But she is not my concern."
    hide dark
    hide hanato
    "There's someone else here."
    "You."
    "The one... looking at a screen."
    "..."
    "Look, I don't know if you're some sort of spark..."
    "An onlooker watching from a camera..."
    "Or some person trying to control me like some video game character..."
    if achievement.has("hate"):
        "Probably that one because it seems you've already made me do something I would never do!"
    "But there's something you need to know regardless."
    "You've probably seen these people already in your time."
    "And I can tell that you've probably done some..."
    "Rather intimate things to a few of them."
    "The girls mainly."
    "I'm not assuming your gender, I wouldn't care if you were female or other, I'm just throwing that out there."
    "But...  I'm here to tell you that things... may not be the same here..."
    "If you've caught on already, then great!  I didn't need to say that."
    "But... if you are someone who is controlling me..."
    "The choices you will be given..."
    "And possibly {i}have{/i} been given..."
    "The things you can make me do..."
    "And possibly someone else..."
    "Most if not all of them will matter."
    "And some of them... could lead to outcomes you don't want."
    "That I... don't want."
    "So I ask you to make every choice with extreme care."
    "I can't stop you."
    "Nor do I know how."
    "I'm not even gonna try to tell everyone about you because you might be able just stop me from doing so."
    "So I hope you can keep everyone in check and alive."
    "I don't care how much you hate any of them."
    "Make sure they are all alive."
    "I want a good ending out of this."
    "You've already made one decision that has changed the course of someone else's entire future."
    "So I hope this will all be worth it in the end."
    "I can do things without your control as well, as you've seen."
    "I won't give you many options yet, I actually want to learn how to do things against your judgement."
    "But as more time goes on and I know I can trust you more and more..."
    "I'll be more than willing to leave things in your hands."
    "I'll know when you are gone."
    "So while you are here, you are to follow these rules."
    menu:
        "Deal?"

        "Yes.":
            "Good."
        "No.":
            "Hmph."
            "Well regardless, you're still going to follow them whether you like it or not."
    "I'll head back to the original topic now."
    "This was your warning, CONTROLLER."
    scene bg schoolriverday with dissolve_scene
    "As I finish my message to you, I give Lilly a much needed hug."


    call kstory
    show kotonoha turned doub lup zorder 2 at t11
    k om "Almost ran into the bastard while escaping, but I did make it out in the end."
    t "So someone sabotaged us?"
    k ldown rhip neut "Yes, but the question is who?"
    show kotonoha cm
    t "I'm more confused as to how."
    k lup om "Let's worry about that later, okay?"
    k ldown "Monika's last, right?"
    show kotonoha at lhide
    hide kotonoha
    show monika forward neut rhip zorder 2 at r11
    m om "Correct."
    call mstory
    show monika forward rhip zorder 2 at t11
    m om "It was at this point that I knew that principal was up to no good."
    m lpoint "And if he is still alive as Kotonoha says..."
    m ldown "Then his plan of control might already be in motion."
    menu:
        "Tell them about me.":
            if not "CONTROLLER Told" in persistent.choices_made:
                $ persistent.choices_made.append("CONTROLLER Told")

        "Say nothing.":
            if not "CONTROLLER Untold" in persistent.choices_made:
                $ persistent.choices_made.append("CONTROLLER Untold")

    
    return