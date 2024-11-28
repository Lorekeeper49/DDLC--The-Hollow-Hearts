init python:
    class Poem:
        def __init__(self, author="", title="", text=""):
            self.author = author
            self.title = title
            self.text = text

    poem_y = Poem(
    author = "yuri",
    title = "Dead Life",
    text = """\
Oh life so tangent,
why did you hurt me so?
why art thou have a pure life
for great myths of old?

I may be broken.
I may be oblivious.
Yandere life.
Yandere way.

Dead life.
Dead wars.
Dead promises.

I just have one question,
why?"""
    )

    poem_n = Poem(
    author = "natsuki",
    title = "Unknown Feelings",
    text = """\
Where is she?
I may be lost but...
she's in the woods.
She is death.
She is forgotten.
She is broken.
She is storming.
She is...
Nothing.
Nothing to help her.
Nothing to lead her.
Nothing to guide her.
She is gone.
And she doesn't know it."""
    )

    poem_s = Poem(
    author = "sayori",
    title = "Before the Past",
    text = """\
Before the past,
what is there?
After the future,
what exists?

Nothing can exist
before the past.
Nothing can exist
after the future.

So what is there?

I know the prefix
before the prefix.
I know the suffix
after the suffix.

Before life
we were none.
Before the past
we were war

After life
we are none.
After the future
we are war.

It's all the same
in an endless cycle."""
    )

    poem_m = Poem(
    author = "monika",
    title = "A Perfect Girl",
    text = """\
A perfect girl is supposed to be stable.
A perfect girl is supposed to be calm.
A perfect girl is supposed to be happy.
A perfect girl is supposed to be pretty.
A perfect girl is supposed to be perfect.

Perfection doesn't exist.

A perfect girl is not stable.
A perfect girl is not calm.
A perfect girl is not happy.
A perfect girl is not pretty.
A perfect girl is not perfect.

Nobody is."""
    )

    poem_k = Poem(
    author = "kotonoha",
    title = "Contradicting Correlation",
    text = """\
What do you get while your asleep?
Nightmares.
What do you get while your awake?
Halluncinations.
They may be different, but they're the same.

What is amazing, but unbelievable?
Myths.
What is amazing and believable?
Legends.
They may be different, but they're the same.

What stays hidden while afar?
Snipers.
What stays hidden while up close?
Spies.
They may be different, but they're the same.

What is at the front of a coin?
Heads.
What is at the back of a coin?
Tails.
They may be different, but they're the same."""
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
        else:
            $ audio.t5b = "<from " + str(currentpos) + " loop 4.444>bgm/5_" + poem.author + ".ogg"
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
