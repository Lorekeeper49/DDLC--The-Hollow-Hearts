init -1 style explore_button:
    background "#6464646c"
    hover_background "#ffffff6c"

init -1 style explore_text:
    font "mod_assets/fonts/Unitblock-mLAwm.ttf"
    size 25
    color "#ffffff6c"
    text_align 0.5

init -1 python:
    """
    for all screens: style_prefix "explore"
    button template:
        button xcenter x ycenter y xysize (width, height) action ButtonAction(next_location, dialogue, or save_var)
        text "label" xcenter x ycenter y
    """
    def update_time():
        remaining_sec -= 1
        if remaining_sec <= 0:
            renpy.call(oot)
    def get_length(s):
        return len(s)
    class TrackCursor(renpy.Displayable):
        #class form here: https://lemmasoft.renai.us/forums/viewtopic.php?p=340355&sid=4540fae3b4ed740ce81e66660e093648#p340355
        def __init__(self, child):

            super(TrackCursor, self).__init__()

            self.child = renpy.displayable(child)

            self.x = None
            self.y = None

        def render(self, width, height, st, at):

            rv = renpy.Render(width, height)

            if self.x is not None:
                cr = renpy.render(self.child, width, height, st, at)
                cw, ch = cr.get_size()
                rv.blit(cr, (self.x - cw / 2, self.y - ch / 2))

            return rv

        def event(self, ev, x, y, st):

            if (x != self.x) or (y != self.y):
                self.x = x
                self.y = y
                renpy.redraw(self, 0)

label explore(start, transition=False, limited_time=-1, fail_label=""):
    if start.startswith("deep_forest"):
        scene bg deep_forest
    else:
        scene expression "bg [start]"
    show screen quick_menu
    if transition:
        with wipeleft_scene
    if limited_time > -1:
        $ remaining_sec = limited_time
        $ oot = fail_label
        show screen timer
    $ codes = []
    $ explored = []
    $ renpy.call_screen(start)
    return

label next_location(loc, *, transition=True, t=False, f=False, w=False):
    if loc.startswith("deep_forest"):
        scene bg deep_forest
    else:
        scene expression "bg [loc]"
    if t:
        show screen timer
    if f:
        show screen flashlight
    if transition:
        with Fade(0.25, 0.0, 0.25)
    if w:
        if random_chance(50):
            show screen wraith
    $ renpy.call_screen(loc)
    return

default inventory = []
default explored = []
default party = []
default code = ""
default dial = ""
default prev_loc = ""
default to_input = ""
default codes = []

label dialpad(c, p, s):
    $ code = c
    $ prev_loc = p
    $ dial = ""
    $ to_input = s
    call screen code_input
    return

screen code_input:
    style_prefix "explore"
    add "vignette"
    text "[dial]" xcenter 640 ycenter 140
    button xcenter 750 ycenter 580 xysize (75, 75) action [If(dial == code, AddToSet(codes, to_input)), Call("next_location", prev_loc, False)]
    text "ENTER" xcenter 750 ycenter 580
    button xcenter 530 ycenter 580 xysize (75, 75) action SetVariable("dial", "")
    text "CLEAR" xcenter 530 ycenter 580
    button xcenter 640 ycenter 580 xysize (75, 75) action SetVariable("dial", dial + "0")
    text "0" xcenter 640 ycenter 580
    button xcenter 530 ycenter 470 xysize (75, 75) action SetVariable("dial", dial + "1")
    text "1" xcenter 530 ycenter 470
    button xcenter 640 ycenter 470 xysize (75, 75) action SetVariable("dial", dial + "2")
    text "2" xcenter 640 ycenter 470
    button xcenter 750 ycenter 470 xysize (75, 75) action SetVariable("dial", dial + "3")
    text "3" xcenter 750 ycenter 470
    button xcenter 530 ycenter 360 xysize (75, 75) action SetVariable("dial", dial + "4")
    text "4" xcenter 530 ycenter 360
    button xcenter 640 ycenter 360 xysize (75, 75) action SetVariable("dial", dial + "5")
    text "5" xcenter 640 ycenter 360
    button xcenter 750 ycenter 360 xysize (75, 75) action SetVariable("dial", dial + "6")
    text "6" xcenter 750 ycenter 360
    button xcenter 530 ycenter 250 xysize (75, 75) action SetVariable("dial", dial + "7")
    text "7" xcenter 530 ycenter 250
    button xcenter 640 ycenter 250 xysize (75, 75) action SetVariable("dial", dial + "8")
    text "8" xcenter 640 ycenter 250
    button xcenter 750 ycenter 250 xysize (75, 75) action SetVariable("dial", dial + "9")
    text "9" xcenter 750 ycenter 250
    text "[get_length(code)]-DIGIT CODE" xcenter 640 ycenter 40


screen flashlight:
    zorder 1000
    add TrackCursor("mod_assets/flashlight.png") 

default remaining_sec = -1
default oot = ""
screen timer:
    timer 1.0 repeat True action Function("update_time")