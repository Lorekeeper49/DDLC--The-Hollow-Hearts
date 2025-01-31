label playcutscene(name, back, *, starttransition=False, endtransition=False):
    $ renpy.play("mod_assets/cutscenes/audio/[name].ogg", channel="cutscene_audio")
    scene expression "mv [name]"
    if starttransition:
        with wipeleft_scene
    $ can_cont = False
    call expression "[name]_subtitle"
    $ can_cont = True
    scene expression back
    if endtransition:
        with wipeleft_scene
    return

# - cutscenes