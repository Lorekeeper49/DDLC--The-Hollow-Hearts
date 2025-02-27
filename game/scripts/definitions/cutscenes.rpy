label playcutscene(vid, *, back="black", starttransition=False, endtransition=False):
    play movie ("mod_assets/cutscenes/" + vid + "/movie.webm")
    play sound ("mod_assets/cutscenes/" + vid + "/sound.ogg")
    play music ("mod_assets/cutscenes/" + vid + "/music.ogg")
    play ambience ("mod_assets/cutscenes/" + vid + "/ambience.ogg")
    play cutscene_voice ("voicelines/" + persistent.voice_lang + "/cutscenes/" + vid + ".ogg")
    scene movie
    if starttransition:
        with wipeleft_scene
    $ can_cont = False
    call expression (vid + "_subtitle")
    $ can_cont = True
    scene expression back
    stop movie
    if endtransition:
        with wipeleft_scene
    return

# - cutscenes
image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0, loop=False)