init python:
    import datetime
    menu_trans_time = 1
    splash_messages = [
    "ENDINGS FOUND: " + str(persistent.endings) + "/14\nPLAYTHROUGHS: " + str(persistent.playthrough),
    "Try to save them all\nbefore it's too late.",
    "They all have their own problems.\nHELP THEM!",
    "You persue 1,\nthe rest die.",
    "This game is not suitable for children\nor those who are easily disturbed",
    "If even 1 dies,\nRESET.",
    "Make one wrong choice,\nand it's over!",
    "This is {b}not{/b} an easy mod."
    ]

image splash_warning = ParameterizedText(style="splash_text", xalign=0.5, yalign=0.5)

image menu_bg:
    topleft
    "mod_assets/gui/menu_bg.png"
    menu_bg_loop

image game_menu_bg:
    topleft
    "mod_assets/gui/menu_bg.png"
    menu_bg_loop

image menu_fade:
    "black"
    menu_fadeout

image menu_art_y:
    subpixel True
    im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/o.png")
    xcenter 500
    ycenter 250
    zoom 0.25

image menu_art_n:
    subpixel True
    im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2tf.png")
    xcenter 840
    ycenter 340
    zoom 0.25

image menu_art_s:
    subpixel True
    im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/k.png")
    xcenter 700
    ycenter 200
    zoom 0.25

image menu_art_m:
    subpixel True
    im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/q.png")
    xcenter 610
    ycenter 100
    zoom 0.25

image menu_art_k:
    subpixel True
    im.Composite((960, 960), (0, 0), "mod_assets/characters/kotonoha/1.png", (0, 0), "mod_assets/characters/kotonoha/o.png")
    xcenter 640
    ycenter 600
    zoom 0.25

image menu_art_a:
    subpixel True
    "mod_assets/MPT/aoruguri/example.png"
    xcenter 800
    ycenter 600
    zoom 0.25


image menu_nav:
    "mod_assets/gui/main_menu.png"

image menu_logo:
    "mod_assets/logo.png"
    subpixel True
    xcenter 640
    ycenter 360
    zoom 0.6
    parallel:
        0.5
        easein 0.05 zoom 0.65
        easeout 0.05 zoom 0.6 
        0.2
        easein 0.05 zoom 0.65
        easeout 0.05 zoom 0.6
        0.5
        repeat
    parallel:
        ease 3.0 rotate 15
        0.1
        ease 3.0 rotate -15
        repeat


transform menu_bg_loop:
    subpixel True
    topleft
    parallel:
        xoffset 0 yoffset 0
        linear 3.0 xoffset -100 yoffset -100
        repeat

transform menu_nav_move:
    subpixel True
    xoffset -500
    time 1.5
    easein_quint 1 xoffset 0

transform menu_fadeout:
    easeout 0.75 alpha 0


image intro:
    truecenter
    "black"
    0.5
    "mod_assets/gui/splash.png" with Dissolve(0.5, alpha=True)
    2.5
    "black" with Dissolve(0.5, alpha=True)
    0.5

image warning:
    truecenter
    "black"
    "splash_warning" with Dissolve(0.5, alpha=True)
    2.5
    "black" with Dissolve(0.5, alpha=True)
    0.5

image tos = "bg/warning.png"
image tos2 = "bg/warning2.png"


label splashscreen:

    python:
        process_list = []
        currentuser = ""
        if renpy.windows:
            try:
                process_list = subprocess.check_output("wmic process get Description", shell=True).lower().replace("\r", "").replace(" ", "").split("\n")
            except:
                pass
            try:
                for name in ('LOGNAME', 'USER', 'LNAME', 'USERNAME'):
                    user = os.environ.get(name)
                    if user:
                        currentuser = user
            except:
                pass


    python:
        firstrun = ""
        try:
            firstrun = renpy.file("firstrun").read(1)
        except:
            with open(config.basedir + "/game/firstrun", "wb") as f:
                pass
    if not firstrun:
        if persistent.first_run and (config.version == persistent.oldversion or persistent.autoload == "postcredits_loop"):
            $ quick_menu = False
            scene black
            menu:
                "A previous save file has been found. Would you like to delete your save data and start over?"
                "Yes, delete my existing data.":
                    "Deleting save data...{nw}"
                    python:
                        delete_all_saves()
                        renpy.loadsave.location.unlink_persistent()
                        renpy.persistent.should_save_persistent = False
                        renpy.utter_restart()
                "No, continue where I left off.":
                    $ restore_relevant_characters()

        python:
            if not firstrun:
                try:
                    with open(config.basedir + "/game/firstrun", "w") as f:
                        f.write("1")
                except:
                    renpy.jump("readonly")

    if config.version != persistent.oldversion:
        $ restore_relevant_characters()
        $ persistent.oldversion = config.version
        $ renpy.save_persistent()

    if not persistent.first_run:
        python:
            restore_all_characters()
        $ quick_menu = False
        scene black
        pause 0.5
        scene tos
        with Dissolve(1.0)
        pause 1.0
        "Disclaimer."
        "This is a Doki Doki Literature Club fan mod that is not affiliated with Team Salvato."
        "It is designed to be played only after the official game has been completed."
        "You can download Doki Doki Literature Club at: {a=https://ddlc.moe}http://ddlc.moe{/a}"
        "Also:"
        "This mod contains disturbing dialogue and visuals, violence, suggestive dialogue and visuals, and other things that may affect certain people."
        "If you have any issues with these factors, it is recommended that you either stop playing or take the necessary precautions before you continue."
        menu:
            "By clicking the button above, you agree that you are aware of these factors and wish to proceed with this in mind."
            "I agree.":
                pass
        "Real quick:"
        "This is the first time I've ever written a story with multiple paths so you are free to let me know of anything I probably could've done better."
        "I also no little to nothing about Japanese culture so I apologize for any inconsisties with that."
        "Now, with all of that said."
        $ persistent.first_run = True
        scene tos2
        with Dissolve(1.5)
        "Thank you for playing DDLC: The Hollow Hearts."
        "I, and the team that helped me out, hope you enjoy this mod."
        pause 1.0
        scene black
        if not config.developer:
            $ startnow = True

    $ basedir = config.basedir.replace('\\', '/')


    $ config.allow_skipping = False


    show black
    $ config.main_menu_music = audio.t1
    if not startnow:
        $ renpy.music.play(config.main_menu_music)
    $ starttime = datetime.datetime.now()
    show intro with Dissolve(0.5, alpha=True)
    $ pause(3.0 - (datetime.datetime.now() - starttime).total_seconds())
    hide intro with Dissolve(max(0, 3.5 - (datetime.datetime.now() - starttime).total_seconds()), alpha=True)
    $ splash_message = renpy.random.choice(splash_messages)
    show splash_warning "[splash_message]" with Dissolve(max(0, 4.0 - (datetime.datetime.now() - starttime).total_seconds()), alpha=True)
    $ pause(6.0 - (datetime.datetime.now() - starttime).total_seconds())
    hide splash_warning with Dissolve(max(0, 6.5 - (datetime.datetime.now() - starttime).total_seconds()), alpha=True)
    $ pause(6.5 - (datetime.datetime.now() - starttime).total_seconds())
    $ config.allow_skipping = True
    if startnow:
        $ startnow = False
        jump autoload
    return

label after_load:
    if persistent.playthrough == 0:
        $ restore_all_characters()
    $ config.allow_skipping = allow_skipping
    $ _dismiss_pause = config.developer
    $ persistent.ghost_menu = False
    $ style.say_dialogue = style.normal
    if persistent.playthrough == 0 and not persistent.first_load and not config.developer:
        $ persistent.first_load = True
        call screen dialog("Hint: You can use the \"Skip\" button to\nfast-forward through text you've already read.", ok_action=Return())
    return None



label autoload:
    python:

        if "_old_game_menu_screen" in globals():
            _game_menu_screen = _old_game_menu_screen
            del _old_game_menu_screen
        if "_old_history" in globals():
            _history = _old_history
            del _old_history
        renpy.block_rollback()


        renpy.context()._menu = False
        renpy.context()._main_menu = False
        main_menu = False
        _in_replay = None


    if renpy.get_return_stack():
        $ renpy.pop_call()
    
    $ quick_menu = True
    $ style.say_dialogue = style.normal
    $ allow_skipping = True
    $ config.allow_skipping = True
    $ af_enabled = True
    "This mod starts immediately when you first open it without going to the title screen, so it is recommended that you set you're options now."
    jump start

label before_main_menu:
    $ config.main_menu_music = audio.t1
    return

label readonly:
    scene black
    "The game cannot be run because you are trying to run it from a read-only location."
    "Please copy the DDLC application to your desktop or other accessible location and try again."
    $ renpy.quit()
    return