default persistent.cutscenes_watched = []

label playcutscene(vid, *, back="black", starttransition=None, endtransition=None):
    $ _show_skip_prompt = False
    play movie ("mod_assets/cutscenes/" + vid + "/movie.webm")
    play sound ("mod_assets/cutscenes/" + vid + "/sound.ogg")
    play music ("mod_assets/cutscenes/" + vid + "/music.ogg")
    play ambience ("mod_assets/cutscenes/" + vid + "/ambience.ogg")
    play cutscene_voice ("voicelines/" + persistent.voice_lang + "/cutscenes/" + vid + ".ogg")
    scene black
    show movie 
    with starttransition
    if vid in persistent.cutscenes_watched:
        show screen skipper onlayer textbox
    else:
        $ persistent.cutscenes_watched.append(vid)
    $ can_cont = False
    call expression (vid + "_subtitle")
    $ can_cont = True
    stop movie 
    scene expression back with endtransition
    $ _show_skip_prompt = False
    hide screen skipper onlayer textbox
    return

# - cutscenes
image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0, loop=False)

screen skipper:
    if _show_skip_prompt:
        text _("PRESS ENTER TO SKIP") at skip_prompt_dissolve:
            size 20
            color "#ccc"
            align (1.0, 1.0)
            offset (-20, -20)
            font "mod_assets/fonts/FOT-RodinNTLG Pro EB.otf"
        timer 5.0 action SetVariable("_show_skip_prompt", False)

    key "K_RETURN" action If(_show_skip_prompt, Return(), SetVariable("_show_skip_prompt", True))
    key "K_SPACE" action If(_show_skip_prompt, Return(), SetVariable("_show_skip_prompt", True))
    key "mouseup_1" action If(_show_skip_prompt, Return(), SetVariable("_show_skip_prompt", True))

label test_subtitle:
    $ pause(260)

    return