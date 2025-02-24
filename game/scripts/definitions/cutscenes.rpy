label playcutscene(vid, *, back="black", starttransition=False, endtransition=False):
    play movie ("mod_assets/cutscenes/" + vid + ".webm")
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