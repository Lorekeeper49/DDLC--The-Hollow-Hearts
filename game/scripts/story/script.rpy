label start:
    $ anticheat = persistent.anticheat

    $ devmode = False

    $ chapter = 0


    $ _dismiss_pause = config.developer

    $ quick_menu = True
    $ style.say_dialogue = style.normal
    $ allow_skipping = True
    $ config.allow_skipping = True
    $ af_enabled = True

    stop music fadeout 2.0
    scene black with dissolve_scene_full
    window hide
    show menu_logo as show_logo zorder 10000 at center_zoom(0.5, 1.0, 5.0) with Dissolve(2.0)
    $ pause(1.0)
    hide show_logo with Dissolve(2.0)

    window hide

    $ act = 0

    $ chapter = 0
    show location_text "プロローグ\n{size=35}Prologue{/size}\nクラブオーダー\n{size=35}Club Order{/size}" zorder 10000 at center_zoom(0.5, 1.0, 6.0) with Dissolve(2.0)
    $ pause(1.0)
    hide location_text with Dissolve(2.0)
    call ch0_main

    achieve newfriends
    scene black with dissolve_scene_full
    $ kirinani = "???"
    ak "The test has been completed."
    ak "Huh?  Looks like he and his sister might be able to hear us.  I will need to fix that."
    ak "*Pencil scratching*"
    ak "Hey Boss, do you mind if we keep them on the man?"
    kiri "Not at all."
    kiri "It is my intention that the man follows us from now on."
    ak "Understood."
    ak "(Taiyen, hang in there.)"
    return

label act1:
    $ act = 1
    call act_trans
    $ chapter = 1
    call chapter_trans("ブレイカー\n{size=35}Breaker{/size}")
    call act1_ch1_main 

    $ chapter = 2
    call chapter_trans("プリカーサーズ\n{size=35}The Precursors{/size}")
    call act1_ch2_main 

    $ chapter = 3
    call chapter_trans("悪い事\n{size=35}The Wrong Thing{/size}")
    call act1_ch3_main 

    $ chapter = 4
    call chapter_trans("過去\n{size=35}The Past{/size}")
    call act1_ch4_main 

    $ chapter = 5
    call chapter_trans("彼女は何処にでもいる\n{size=35}The One That's Everywhere{/size}")
    call act1_ch5_main 

    $ chapter = 6
    call chapter_trans("敵\n{size=35}The Enemy{/size}")
    call act1_ch6_main

    scene black with dissolve_scene_full
    achieve act1fin
    $ kirinani = "???"
    kiri "The man found out."
    kiri "Move the CONTROLLER to the girl, they can have fun with her for a while."
    return

label act2:
    $ known = True
    $ act = 2
    call act_trans
    $ chapter = 1
    call chapter_trans("夜に活動するクラブ\n{size=35}A Club That Works at Night{/size}")
    call act2_ch1_main

    $ chapter = 2
    call chapter_trans("闇の発見\n{size=35}Dark Discoveries{/size}")
    call act2_ch2_main
    
    $ chapter = 3
    call chapter_trans("アフターマス\n{size=35}The Aftermath{/size}")
    call act2_ch3_main

    $ chapter = 4
    call chapter_trans("取り戻した過去\n{size=35}A Past Regained{/size}")
    call act2_ch4_main
    call showintro(intro_kiri)

    $ chapter = 5
    call chapter_trans("スタート\n{size=35}It Begins{/size}")
    call act2_ch5_main

    jump act2_end

label act2_alt:
    $ known = False
    $ act = 2
    call act_trans
    $ chapter = 1
    call chapter_trans("夜に活動するクラブ\n{size=35}A Club That Works at Night{/size}")
    call act2_ch1_main

    $ chapter = 2
    call chapter_trans("闇の発見\n{size=35}Dark Discoveries{/size}")
    call act2_ch2_alt
    
    $ chapter = 3
    call chapter_trans("アフターマス\n{size=35}The Aftermath{/size}")
    call act2_ch3_alt

    $ chapter = 4
    call chapter_trans("取り戻した過去\n{size=35}A Past Regained{/size}")
    call act2_ch4_alt
    call showintro(intro_kiri)

    $ chapter = 5
    call chapter_trans("スタート\n{size=35}It Begins{/size}")
    call act2_ch5_alt
    
    jump act2_end

label act2_end:
    scene black with dissolve_scene_full
    achieve act2fin
    "As the scene from the school unfolds, you realize you've lost all control of the situation."
    "The computer screen glows in front of you as you wait for a chance to regain control."
    "The girl hasn't figured you out yet like the man has so you're in the clear."
    "But you really wish you had listened to the man's orders."
    "Now your boss is wreaking havoc at his school."
    "But then, you had a tought..."
    "What if you could control both of them at the same time?"
    "The computer's control module uses USB dongles to tell it which person to control."
    "So if you could the one for the man..."
    "Aspired by this thought and knowing full well that no one is watching you, you quickly make your way to the storage where the dongles are held."
    "You easily find the one you're looking for within a small box.  It is convenient that these are labeled."
    "You quickly return back to the computer, eager to see if this will work."
    "With the one for the girl still in, you insert the other dongle and..."
    return 

label dev:
    stop music fadeout 2.0
    scene black
    with dissolve_scene_full
    "DEVELOPER MODE ACTIVE"
    label dev_loop:
        $ quick_menu = True
        $ style.say_dialogue = style.normal
        $ allow_skipping = True
        $ config.allow_skipping = True
        $ af_enabled = True
        $ entirestory = False
        $ chapter = 0
        $ clubtell = False
        $ onlytell = False
        $ donttell = False
        $ class5a = False
        $ dontknow = False
        $ locationlie = False
        $ cute = False
        $ tellfans = False
        $ dontfans = False
        $ known = False
        $ act = 1
        $ aoruguri = "隠れた少女\n{size=15}Hidden Girl{/size}"
        $ window_style = ""
        $ nb = "namebox"
    label dev_start2: 
        menu:
            "SELECT AN ACT:"

            "ACT 1":
                $ act = 1
                call act_trans
                $ char_perspective = "Taiyen"
                menu:
                    "SELECT A CHAPTER:"

                    "CHAPTER 1":
                        "BEGINNING CHAPTER 1"
                        $ chapter = 1
                        call chapter_trans("ブレイカー\n{size=35}Breaker{/size}")
                        call act1_ch1_main
                    "CHAPTER 2":
                        $ chapter = 2
                        "BEGINNING CHAPTER 2"
                        $ hanato = "神山華翔\n{size=15}Kamiyama Hanato"
                        call chapter_trans("プリカーサーズ\n{size=35}The Precursors{/size}")
                        call act1_ch2_main
                    "CHAPTER 3":
                        $ chapter = 3
                        "BEGINNING CHAPTER 3"
                        $ hanato = "神山華翔\n{size=15}Kamiyama Hanato"
                        call chapter_trans("秘密のベアリング\n{size=35}Bearing Secrets{/size}")
                        call act1_ch3_main
                    "CHAPTER 4":
                        $ chapter = 4
                        "BEGINNING CHAPTER 4"
                        $ hanato = "神山華翔\n{size=15}Kamiyama Hanato"
                        call chapter_trans("過去\n{size=35}The Past{/size}")
                        call act1_ch4_main
                    "CHAPTER 5":
                        $ chapter = 5
                        "BEGINNING CHAPTER 5"
                        $ hanato = "神山華翔\n{size=15}Kamiyama Hanato"
                        call chapter_trans("彼女は何処にでもいる\n{size=35}The One That's Everywhere{/size}")
                        call act1_ch5_main
                    "CHAPTER 6":
                        $ chapter = 6
                        "BEGINNING CHAPTER 6"
                        $ hanato = "神山華翔\n{size=15}Kamiyama Hanato"
                        call chapter_trans("敵\n{size=35}The Enemy{/size}")
                        call act1_ch6_main
                    "BACK":
                        jump dev_loop
            "ACT 2":
                $ act = 2
                $ hanato = "神山華翔\n{size=15}Kamiyama Hanato"
                $ aoruguri = "ルナ煽るぐり\n{size=15}Luna Aoruguri"
                $ char_perspective = "Aoruguri"
                call act_trans
                menu:
                    "WHICH PATH?"

                    "NORMAL":
                        $ known = True
                    "ALTERNATE":
                        $ known = False
                menu:
                    "SELECT A CHAPTER:"

                    "CHAPTER 1":
                        "BEGINNING CHAPTER 1"
                        $ chapter = 1
                        call chapter_trans("夜に活動するクラブ\n{size=35}A Club That Works at Night")
                        call act2_ch1_main
                    "CHAPTER 2":
                        $ chapter = 2
                        "BEGINNING CHAPTER 2"
                        call chapter_trans("闇の発見\n{size=35}Dark Discoveries{/size}")
                        if known:    
                            call act2_ch2_main
                        else:
                            call act2_ch2_alt
                    "CHAPTER 3":
                        $ chapter = 3
                        "BEGINNING CHAPTER 3"
                        call chapter_trans("アフターマス\n{size=35}The Aftermath{/size}")
                        if known:    
                            call act2_ch3_main
                        else:
                            call act2_ch3_alt
                    "CHAPTER 4":
                        $ chapter = 4
                        "BEGINNING CHAPTER 4"
                        call chapter_trans("取り戻した過去\n{size=35}A Past Regained{/size}")
                        if known:    
                            call act2_ch4_main
                        else:
                            call act2_ch4_alt
                    "CHAPTER 5":
                        $ chapter = 5
                        "BEGINNING CHAPTER 5"
                        call chapter_trans("スタート\n{size=35}It Begins{/size}")
                        if known:    
                            call act2_ch5_main
                        else:
                            call act2_ch5_alt
                    "BACK":
                        jump dev_loop
        jump dev_loop