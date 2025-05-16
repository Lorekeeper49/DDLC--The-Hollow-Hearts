label act3_path13:
    $ window_style = ""
    $ nb = "namebox"
    stop music fadeout 2.0
    $ char_perspective = "Taiyen"
    $ chapter = 1
    call chapter_trans("人形\n{size=35}The Doll{/size}")
    scene bg bedroom with dissolve_scene_full
    menu:
        "Oh, you're back?"

        "Yep, and I'm controlling someone else too.":
            pass
        "I'm in her as well.":
            pass
    menu:
        "As in?"

        "Luna Aoruguri.":
            "Oh!"
        "Your girlfriend.":
            "I..."
            "Okay, you and I both know that she is not my girlfriend."
            "But anyway..."
    "Good to know that you can control multiple people."
    menu:
        "I should tell you how this works.":
            pass
        "You should tell her about me.":
            pass
    "Not now."
    "A lot's going on right now, and someone's at the door."
    scene black with wipeleft_scene
    $ char_perspective = "Aoruguri"
    a "Who am I?"
    a "What have I done?"
    a "Who have I killed?"
    a "What..."
    a "..."
    scene bg entrance with wipeleft_scene
    $ char_perspective = "Taiyen"
    show yuri turned casual zorder 2 at t11
    t "Yuri-chan?"
    t "Is this about the murderer?"
    y "Yes."
    menu:
        "Tell her.":
            t "..."
        "Say nothing.":
            t "..."
            "I think she'll find out anyway."
    t "I think you should see something..."
    scene black with wipeleft
    $ char_perspective = "Aoruguri"
    t "Aoruguri?  Are you okay?"
    a "..."
    "He's outside the door."
    a "No...  I'm not."
    t "If it helps, I can-{nw}"
    a "I killed your sister in a state of no control!  Do you expect me to be okay!?"
    t "I don't, I just..."
    t "The sister of someone else you killed is outside the door."
    t "I recommend you listen to what she has to say."
    "Without a word, I comply."
    with wipeleft_scene
    $ char_perspective = "Taiyen"
    show yuri turned casual rup zorder 2 at t11
    y om "Should it be me or her?"
    "Iru's talking."
    menu:
        "I'll let you be the judge."

        "Yuri":
            t "Her."
            ""
        "Iru":
            t "You."
            ""



    menu:
        "How do we rebuild Lilly?"

        "Use Yuri's father.":
            ""
        "Have Yuri try.":
            ""
        "Have Aoruguri try":
            ""
        "Have Taiyen try":
            ""
    return