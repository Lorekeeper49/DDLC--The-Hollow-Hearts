init python:
    class Poem:
        def __init__(self, author="", title="", text=""):
            self.author = author
            self.title = title
            self.text = text

    poem_y = Poem(
    author = "yuri",
    title = "",
    text = """\
"""
    )

    poem_n = Poem(
    author = "natsuki",
    title = "",
    text = """\
"""
    )

    poem_s = Poem(
    author = "sayori",
    title = "",
    text = """\
"""
    )

    poem_m = Poem(
    author = "monika",
    title = "",
    text = """\
"""
    )

    poem_k = Poem(
    author = "kotonoha",
    title = "",
    text = """\
"""
    )

    poem_t = Poem(
    author = "taiyen",
    title = "I am Stupid",
    text = """\
I call myself that
all the time.
I am not a that,
it is my prime.

I am not a sage.
I don't know a page.
I'm not in a cage.
Someone got a guage?

I need some help
for a phase.
I've only dealt
with a daze.

My mind goes dead.
I've been sped.
I'm just bread.
I need a head.

I can do stories.
I can't do poems."""
    )

image paper = "images/bg/poem.jpg"


transform paper_in:
    truecenter
    alpha 0
    linear 1.0 alpha 1

transform paper_out:
    alpha 1
    linear 1.0 alpha 0

screen poem(currentpoem, paper="paper"):
    style_prefix "poem"
    vbox:
        add paper
    viewport id "vp":
        child_size (710, None)
        mousewheel True
        draggable True
        has vbox
        null height 40
        if currentpoem.author == "yuri":
            text "[currentpoem.title]\n\n[currentpoem.text]" style "yuri_text"
        elif currentpoem.author == "sayori":
            text "[currentpoem.title]\n\n[currentpoem.text]" style "sayori_text"
        elif currentpoem.author == "natsuki":
            text "[currentpoem.title]\n\n[currentpoem.text]" style "natsuki_text"
        elif currentpoem.author == "monika":
            text "[currentpoem.title]\n\n[currentpoem.text]" style "monika_text"
        elif currentpoem.author == "kotonoha":
            text "[currentpoem.title]\n\n[currentpoem.text]" style "koto_text"
        elif currentpoem.author == "taiyen":
            text "[currentpoem.title]\n\n[currentpoem.text]" style "tai_text"
        null height 100
    vbar value YScrollValue(viewport="vp") style "poem_vbar"



style poem_vbox:
    xalign 0.5
style poem_viewport:
    xanchor 0
    xsize 720
    xpos 280
style poem_vbar is vscrollbar:
    xpos 1000
    yalign 0.5

    ysize 700





style yuri_text:
    font "gui/font/y1.ttf"
    size 32
    color "#000"
    outlines []

style natsuki_text:
    font "gui/font/n1.ttf"
    size 28
    color "#000"
    outlines []
    line_leading 1

style sayori_text:
    font "gui/font/s1.ttf"
    size 34
    color "#000"
    outlines []

style monika_text:
    font "gui/font/m1.ttf"
    size 34
    color "#000"
    outlines []

style koto_text:
    font "mod_assets/fonts/AlexBrush-Regular.ttf"
    size 34
    color "#000"
    outlines []

style tai_text:
    font "mod_assets/fonts/Unitblock-mLAwm.ttf"
    size 34
    color "#000"
    outlines []

label showpoem(poem=None, music=True, track=None, revert_music=True, img=None, where=i11, paper=None):
    if poem == None:
        return
    play sound page_turn
    if music:
        $ currentpos = get_pos()
        if track:
            $ audio.t5b = "<from " + str(currentpos) + " loop 4.444>" + track
        elif renpy.exists("bgm/5_" + poem.author + ".ogg"):
            $ audio.t5b = "<from " + str(currentpos) + " loop 4.444>bgm/5_" + poem.author + ".ogg"
        else:
            $ audio.t5b = "<from " + str(currentpos) + " loop 4.444>bgm/5.ogg"
        stop music fadeout 2.0
        $ renpy.music.play(audio.t5b, channel="music_poem", fadein=2.0, tight=True)
    window hide
    $ renpy.game.preferences.afm_enable = False
    if paper:
        show screen poem(poem, paper=paper)
    else:
        show screen poem(poem)
    if not persistent.first_poem:
        $ persistent.first_poem = True
        $ renpy.save_persistent()
        show expression "gui/poem_dismiss.png" as poem_dismiss:
            xpos 1050 ypos 590
    with Dissolve(1)
    $ pause()
    if img:
        $ renpy.hide(poem.author)
        $ renpy.show(img, at_list=[where])
    hide screen poem
    hide poem_dismiss
    with Dissolve(.5)
    window auto
    if music and revert_music:
        $ currentpos = get_pos(channel="music_poem")
        $ audio.t5c = "<from " + str(currentpos) + " loop 4.444>bgm/5.ogg"
        stop music_poem fadeout 2.0
        $ renpy.music.play(audio.t5c, fadein=2.0)
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
