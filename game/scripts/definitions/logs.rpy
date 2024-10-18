init python:
    class Log:
        def __init__(self, title="", text=""):
            self.title = title
            self.text = text
    
    log1 = Log(
        title = "Log 1", 
        text = """\
    """
    )

    

transform paper_in:
    truecenter
    alpha 0
    linear 1.0 alpha 1

transform paper_out:
    alpha 1
    linear 1.0 alpha 0

screen log(currentlog):
    style_prefix "log"
    viewport id "vp":
        child_size (710, None)
        mousewheel True
        draggable True
        has vbox
        null height 40
        text "[currentlog.title]\n\n[currentlog.text]" style "monika_text"
        null height 100
    vbar value YScrollValue(viewport="vp") style "log_vbar"



style log_vbox:
    xalign 0.5
style log_viewport:
    xanchor 0
    xsize 720
    xpos 280
style log_vbar is vscrollbar:
    xpos 1000
    yalign 0.5

    ysize 700

style log_text:
    font "mod_assets/fonts/Unitblock-mLAwm.ttf"
    size 34
    color "#ffffff"
    outlines []
    text_align 0.5

label playlog(currentlog=None, logaudio=None, bgreturn=""):
    scene black with dissolve_scene
    if currentlog == None or logaudio == None:
        return
    play sound logaudio
    window hide
    $ renpy.game.preferences.afm_enable = False
    show screen log(currentlog)
    with Dissolve(1)
    $ pause()
    hide screen log
    with Dissolve(.5)
    window auto
    scene expression bgreturn with dissolve_scene
    return
