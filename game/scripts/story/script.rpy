label start:
    $ anticheat = persistent.anticheat

    $ devmode = False

    $ chapter = 0


    $ _dismiss_pause = config.developer

    $ m_name = "Girl 3"
    $ n_name = "Girl 2"
    $ y_name = "Girl 1"

    $ quick_menu = True
    $ style.say_dialogue = style.normal
    $ allow_skipping = True
    $ config.allow_skipping = True
    $ af_enabled = True

    if persistent.demo:
        "INFORMATION:"
        "Since this is a demo, everything you see is subject to change.  That said, many things will remain the same, but I will not reveal what those are."
        "If you'd like to support the mod, {a=https://discord.gg/Q3CcJW4Ag2}click here to join the discord server.{/a}"
        "For Dokitubers: Please do not use auto-advance, the mod is meant to be fully voice-acted and the non-voiced lines advance too fast to read as of now, so please don't use it."
        "With all that said, please enjoy the mod!"

    "This mod features a lot of choices that could drastically change the story if you're not careful..."
    menu:
        "Would you like these choices to be marked with an asterisk (*) at the start of each such choice?"

        "Yes":
            pass
        "No":
            $ change = ""
    "Understood."
    "That's all!  So without further ado, let's begin DDLC: The Hollow Hearts!"

    $ act = 0

    $ chapter = 0
    show location_text "Prologue:\nClub Order" zorder 10000 at center_zoom(0.5, 1.0, 6.0) with Dissolve(2.0)
    $ pause(1.0)
    hide location_text with Dissolve(2.0)
    call ch0_main from _call_ch0_main
    call storyresponse_start from _call_storyresponse_start
    call ch0_end from _call_ch0_end

    $ act = 1
    call act_trans
    $ chapter = 1
    call chapter_trans("Breaker")
    call act1_ch1_main from _call_act1_ch1_main

    $ chapter = 2
    call chapter_trans("The Precursors")
    call act1_ch2_main from _call_act1_ch2_main
    call tstory from _call_tstory
    call storyresponse_start from _call_storyresponse_start_1
    call act1_ch2_end from _call_act1_ch2_end

    $ chapter = 3
    call chapter_trans("Bearing Secrets")
    call act1_ch3_main from _call_act1_ch3_main
    call tstory from _call_tstory_1
    call storyresponse_start from _call_storyresponse_start_2
    call act1_ch3_end from _call_act1_ch3_end

    $ chapter = 4
    call chapter_trans("")
    call act1_ch4_main from _call_act1_ch4_main
    call tstory from _call_tstory_2
    call storyresponse_start from _call_storyresponse_start_3
    call act1_ch4_end from _call_act1_ch4_end

    $ chapter = 5
    call chapter_trans("")
    call act1_ch5_main from _call_act1_ch5_main
    call tstory from _call_tstory_3
    call storyresponse_start from _call_storyresponse_start_4
    call act1_ch5_end from _call_act1_ch5_end

    $ chapter = 6
    call chapter_trans("The Enemy")
    call act1_ch6_main

    $ act = 2
    call act_trans
    $ chapter = 1
    call chapter_trans("A Club That Works at Night")
    call act2_ch1_main from _call_act2_ch1_main

    $ chapter = 2
    call chapter_trans("Dark Discoveries")
    call act2_ch2_main from _call_act2_ch2_main
    
    $ chapter = 3
    call chapter_trans("The Aftermath")
    call act2_ch3_main from _call_act2_ch3_main

    $ chapter = 4
    call chapter_trans("A Past Regained")
    call act2_ch4_main from _call_act2_ch4_main
    call showintro(intro_kiri)

    $ chapter = 5
    call chapter_trans("It Begins")
    call act2_ch5_main from _call_act2_ch5_main
    
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
        $ style.say_window = style.window_fake
        $ nb = "namebox_fake"
        $ aoruguri = "Hidden Girl"
    label dev_start2: 
        menu:
            "SELECT AN ACT:"

            "ENTIRE STORY":
                "GOING THROUGH THE ENTIRE STORY FROM START"
                $ entirestory = True
                jump start
            "PROLOGUES":
                menu:
                    "SELECT A PROLOGUE:"
                    
                    "MAIN":
                        "BEGINNING PROLOGUE"
                        $ chapter = 0
                        show location_text "Prologue:\nClub Order" zorder 10000 at center_zoom(0.5, 1.0, 6.0) with Dissolve(2.0)
                        $ pause(1.0)
                        hide location_text with Dissolve(2.0)
                        call ch0_main from _call_ch0_main_1
                        call storyresponse_start from _call_storyresponse_start_5
                        call ch0_end from _call_ch0_end_1
                    "SAYORI":
                        menu:
                            "SELECT A CHAPTER:"

                            "CHAPTER 1":
                                $ chapter = 2
                                "BEGINNING CHAPTER 1"
                            "CHAPTER 2":
                                $ chapter = 3
                                "BEGINNING CHAPTER 2"
                            "CHAPTER 3":
                                $ chapter = 4
                                "BEGINNING CHAPTER 3"
                            "CHAPTER 4":
                                $ chapter = 5
                                "BEGINNING CHAPTER 4"
                            "BACK":
                                jump dev_loop
                        call sstory from _call_sstory_1
                    "MONIKA":
                        menu:
                            "SELECT A CHAPTER:"

                            "CHAPTER 1":
                                $ chapter = 2
                                "BEGINNING CHAPTER 1"
                            "CHAPTER 2":
                                $ chapter = 3
                                "BEGINNING CHAPTER 2"
                            "CHAPTER 3":
                                $ chapter = 4
                                "BEGINNING CHAPTER 3"
                            "CHAPTER 4":
                                $ chapter = 5
                                "BEGINNING CHAPTER 4"
                            "BACK":
                                jump dev_loop
                        call mstory from _call_mstory_1
                    "NATSUKI":
                        menu:
                            "SELECT A CHAPTER:"

                            "CHAPTER 1":
                                $ chapter = 3
                                "BEGINNING CHAPTER 1"
                            "CHAPTER 2":
                                $ chapter = 4
                                "BEGINNING CHAPTER 2"
                            "CHAPTER 3":
                                $ chapter = 5
                                "BEGINNING CHAPTER 3"
                            "BACK":
                                jump dev_loop
                        call nstory from _call_nstory
                    "YURI":
                        menu:
                            "SELECT A CHAPTER:"

                            "CHAPTER 1":
                                $ chapter = 2
                                "BEGINNING CHAPTER 1"
                            "CHAPTER 2":
                                $ chapter = 3
                                "BEGINNING CHAPTER 2"
                            "CHAPTER 3":
                                $ chapter = 4
                                "BEGINNING CHAPTER 3"
                            "CHAPTER 4":
                                $ chapter = 5
                                "BEGINNING CHAPTER 4"
                            "BACK":
                                jump dev_loop
                        call ystory from _call_ystory_1
                    "KOTONOHA":
                        menu:
                            "SELECT A CHAPTER:"

                            "CHAPTER 1":
                                $ chapter = 2
                                "BEGINNING CHAPTER 1"
                            "CHAPTER 2":
                                $ chapter = 3
                                "BEGINNING CHAPTER 2"
                            "CHAPTER 3":
                                $ chapter = 4
                                "BEGINNING CHAPTER 3"
                            "CHAPTER 4":
                                $ chapter = 5
                                "BEGINNING CHAPTER 4"
                            "BACK":
                                jump dev_loop
                        call kstory from _call_kstory_2
                    "TAIYEN":
                        menu:
                            "SELECT A CHAPTER:"

                            "CHAPTER 1":
                                $ chapter = 2
                                "BEGINNING CHAPTER 1"
                            "CHAPTER 2":
                                $ chapter = 3
                                "BEGINNING CHAPTER 2"
                            "CHAPTER 3":
                                $ chapter = 4
                                "BEGINNING CHAPTER 3"
                            "CHAPTER 4":
                                $ chapter = 5
                                "BEGINNING CHAPTER 4"
                            "BACK":
                                jump dev_loop
                        call tstory
                    "BACK":
                        jump dev_loop
            "ACT 1":
                $ act = 1
                call act_trans
                menu:
                    "SELECT A CHAPTER:"

                    "CHAPTER 1":
                        "BEGINNING CHAPTER 1"
                        $ chapter = 1
                        call chapter_trans("Breaker")
                        call act1_ch1_main from _call_act1_ch1_main_1
                    "CHAPTER 2":
                        $ chapter = 2
                        "BEGINNING CHAPTER 2"
                        $ hanato = "Kamiyama Hanato"
                        call chapter_trans("The Precursors")
                        call act1_ch2_main from _call_act1_ch2_main_1
                        call tstory                        
                        call storyresponse_start from _call_storyresponse_start_6
                        call act1_ch2_end from _call_act1_ch2_end_1
                    "CHAPTER 3":
                        $ chapter = 3
                        "BEGINNING CHAPTER 3"
                        $ hanato = "Kamiyama Hanato"
                        call chapter_trans("Bearing Secrets")
                        call act1_ch3_main from _call_act1_ch3_main_1
                        call tstory 
                        call storyresponse_start from _call_storyresponse_start_7
                        call act1_ch3_end from _call_act1_ch3_end_1
                    "CHAPTER 4":
                        $ chapter = 4
                        "BEGINNING CHAPTER 4"
                        $ hanato = "Kamiyama Hanato"
                        call chapter_trans("")
                        call act1_ch4_main from _call_act1_ch4_main_1
                        call tstory 
                        call storyresponse_start from _call_storyresponse_start_8
                        call act1_ch4_end from _call_act1_ch4_end_1
                    "CHAPTER 5":
                        $ chapter = 5
                        "BEGINNING CHAPTER 5"
                        $ hanato = "Kamiyama Hanato"
                        call chapter_trans("")
                        call act1_ch5_main from _call_act1_ch5_main_1
                        call tstory 
                        call storyresponse_start from _call_storyresponse_start_9
                        call act1_ch5_end from _call_act1_ch5_end_1
                    "BACK":
                        jump dev_loop
            "ACT 2":
                $ act = 2
                $ hanato = "Kamiyama Hanato"
                $ style.say_window = style.window
                $ nb = "namebox"
                $ aoruguri = "Luna Aoruguri"
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
                        call chapter_trans("A Club That Works at Night")
                        call act2_ch1_main from _call_act2_ch1_main_1
                    "CHAPTER 2":
                        $ chapter = 2
                        "BEGINNING CHAPTER 2"
                        call chapter_trans("Dark Discoveries")
                        call act2_ch2_main from _call_act2_ch2_main_1
                    "CHAPTER 3":
                        $ chapter = 3
                        "BEGINNING CHAPTER 3"
                        call chapter_trans("The Aftermath")
                        call act2_ch3_main from _call_act2_ch3_main_1
                    "CHAPTER 4":
                        $ chapter = 4
                        "BEGINNING CHAPTER 4"
                        call chapter_trans("A Past Regained")
                        call act2_ch4_main from _call_act2_ch4_main_1
                    "CHAPTER 5":
                        $ chapter = 5
                        "BEGINNING CHAPTER 5"
                        call chapter_trans("It Begins")
                        call act2_ch5_main from _call_act2_ch5_main_1
                    "BACK":
                        jump dev_loop
            "QUIT":
                "RETURNING TO MAIN MENU"
                return
        jump dev_loop


label endgame(pause_length=4.0):
    $ quick_menu = False
    stop music fadeout 2.0
    scene black
    show end
    with dissolve_scene_full
    pause pause_length
    $ quick_menu = True
    return