init python:
    class Log:
        def __init__(self, title="", text=""):
            self.title = title
            self.text = text
    
    log1 = Log(
        title = "Log 1", 
        text = """\
    The purpose of these logs is to give information about the Breaker experiment and how exactly it went in the process of production.  The reason why these are physical logs not saved onto my computer is because I don't want this information to be leaked before we can release this for public use.
    The purpose of Breaker is to allow people to remove their current attribute amnd either exchange it for another one, or stay without it and be ordinary, whatever that means.
    Five test subjects have volunteered to take the substance: Kamiyama Kirinani, Luna Dominion, Yandere Lilly, Kusunoki Mari, and Settou Seiei.  We'll supply these logs with tutorials on how to perform the procedure safely.

    Another thing, this is off-topic but important, my son seems to be taking care of a peculiar storm for the time being.  DNA tests reveal she is the daughter of Kusunoki Mari.  That girl never had a good family... 
    Taiyen...
    Please...
    If your hearing this...
    Take care of her daughter.
    """
    )
    log5 = Log(
        title = "Log 5", 
        text = """\
    TESTS ONE AND TWO COMPLETE.  AWAITING RESULTS...
    The tests are going smoothly, that or my son is lying to me.  I always worry about lies, even if they're from my own family...
    That's off-topic.  What's on-topic is that the tests seem to be going off without a hitch.  I'm still waiting on accurate results, but our volunteers might just be in store for a better future, here's hoping.
    TEST THREE is tonight, results should come by then.
    """
    )
    finallog = Log(
        title = "Final Log", 
        text = """\
    The experiment failed, they're completely different people now, I've destroyed them.
    What we failed to realize was that every attribute was tied to the person's personality.  To change one's attribute, you must change their personality.  What we were essentially trying to do without realizing it is allow them to change their attribute without changing their personality.  You can imagine how mcuh of an issue that can become when you attempt to put it into practice.
    Now they are suffering, and it's all because of me!  I know I should do it myself, but I want someone to end their suffering before it escalates for the worse.  I am not a killer, but I know I can't let them live like this!  Damnit!  This is all my fault!
    I just hope... that this won't come back to bite me.
    """
    )

screen log(currentlog):
    style_prefix "log"
    viewport id "vp":
        child_size (710, None)
        mousewheel True
        draggable True
        has vbox
        null height 40
        text "[currentlog.title]\n\n[currentlog.text]"
        null height 100
    frame at duration_transform:
        xsize 1280
        ysize 720
        background Solid("#00f7ff50")
    vbar value YScrollValue(viewport="vp") style "log_vbar"

transform duration_transform:
    ypos -720
    linear renpy.music.get_duration(channel='sound') ypos 0

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

label playlog(currentlog=None, bgreturn=""):
    scene black with dissolve_scene
    if currentlog == None:
        return
    play sound "mod_assets/logs/" + currentlog.title + ".ogg"
    window hide
    $ renpy.game.preferences.afm_enable = False
    show screen log(currentlog) with Dissolve(1)
    $ pause()
    hide screen log with Dissolve(.5)
    window auto
    scene expression bgreturn with dissolve_scene
    return
