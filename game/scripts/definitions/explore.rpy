init -501 style explore_button:
    background "#6464646c"
    hover_background "#ffffff6c"

init -501 style explore_text:
    font "mod_assets/fonts/FOT-RodinNTLG Pro EB.otf"
    size 25
    color "#ffffff6c"
    text_align 0.5

image explore_text = ParameterizedText(style="explore_text")

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
    # Only use this when adding items to the inventory, it makes sure the items are in the same place for each list so the inventory view can work correctly
    def add_to_inv(EN_name, JP_name, desc, chara=None):
        if chara is None:
            chara = char_perspective
        inventory[chara].append({"EN_name": EN_name, "JP_name": JP_name, "desc": desc})
    def remove_from_inv(item, chara=None):
        if chara is None:
            chara = char_perspective
        try:
            i = find_in_inv(item, chara)
            del inventory[chara][i]
        except: pass
    def clear_inv(chara=None):
        if chara is None:
            chara = char_perspective
        inventory[chara].clear()
    def item_in_inv(item, chara=None):
        return find_in_inv(item, chara) != -1
    def find_in_inv(item, chara=None):
        if chara is None:
            chara = char_perspective
        for i in range(len(inventory[chara])):
            if item == inventory[chara][i]["EN_name"] or item == inventory[chara][i]["JP_name"] or item == inventory[chara][i]["desc"]:
                return i
        return -1
    class TrackCursor(renpy.Displayable):
        #class from here: https://lemmasoft.renai.us/forums/viewtopic.php?p=340355&sid=4540fae3b4ed740ce81e66660e093648#p340355
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

label explore(start, *args, transition=None, return_label=None, limited_time=-1, fail_label="", **kwargs):
    if start.startswith("deep_forest"):
        scene bg deep_forest
    else:
        scene expression "bg [start]"
    show screen quick_menu onlayer textbox
    with transition
    if limited_time > -1:
        $ remaining_sec = limited_time
        $ oot = fail_label
        show screen timer
    $ codes = []
    $ explored = []
    $ renpy.call_screen(start, *args, **kwargs)
    hide screen quick_menu onlayer textbox
    return return_label

default jumpnum = 0
label next_location(loc, *args, transition=Fade(0.25, 0.0, 0.25), j=False, f=False, hide_f=False, w=False, **kwargs):
    if loc.startswith("deep_forest"):
        scene bg deep_forest
    else:
        scene expression "bg [loc]"
    if j:
        if random_chance(10):
            $ renpy.music.play(audio.jumpscare, channel="jump" + str(jumpnum), loop=True)
            show bg factory onlayer forebackground with Fade(0.1, 0.0, 0.1, color="#fff")
            $ pause(0.05)
            hide bg factory onlayer forebackground
            with Fade(0.1, 0.0, 0.1, color="#fff")
            $ remaining_sec -= 300
            $ jumpnum += 1
    if f:
        show flashlight onlayer foreground
    if hide_f:
        hide flashlight onlayer foreground
    with transition
    if w:
        $ wraith_beaten = False
        if random_chance(50):
            play sound "sfx/giggle.ogg"
            show screen wraith
    $ renpy.call_screen(loc, *args, **kwargs)
    return

default inventory = {
    "Taiyen": [],
    "Aoruguri": [],
    "Monika": [],
    "Sayori": [],
    "Natsuki": [],
    "Yuri": [],
    "Kotonoha": [],
    "Lilly": []
    }
default char_perspective = ""
default explored = []
default party = []
default code = ""
default dial = ""
default prev_loc = ""
default to_input = ""
default codes = []

label call_inventory(*correct_items, correct_action=None, incorrect_action=None):
    call screen inventory_view(Return())
    if used_item in correct_items:
        call screen explore_item(correct_action)
    else:
        call screen explore_item(incorrect_action)
    return

screen explore_item(item_action):
    timer 0.1 action item_action

label dialpad(c, p, s, limit_input=False, show_code_length=True):
    $ code = c
    $ prev_loc = p
    $ dial = ""
    $ to_input = s
    call screen code_input(limit_input, show_code_length)
    return

screen code_input(limit_input=False, show_code_length=True):
    style_prefix "explore"
    add "vignette"
    text "[dial]" xcenter 640 ycenter 140
    button xcenter 750 ycenter 580 xysize (100, 100) action [If(dial == code, AddToSet(codes, to_input)), Call("next_location", prev_loc, transition=False)]
    text "入力\nENTER" xcenter 750 ycenter 580
    button xcenter 530 ycenter 580 xysize (100, 100) action SetVariable("dial", "")
    text "クリア\nCLEAR" xcenter 530 ycenter 580
    button xcenter 640 ycenter 580 xysize (100, 100) action [SetVariable("dial", dial + "0"), If(limit_input, If(len(dial) >= len(code), [If(dial == code, AddToSet(codes, to_input)), Call("next_location", prev_loc, transition=False)]))]
    text "0" xcenter 640 ycenter 580
    button xcenter 530 ycenter 470 xysize (100, 100) action [SetVariable("dial", dial + "1"), If(limit_input, If(len(dial) >= len(code), [If(dial == code, AddToSet(codes, to_input)), Call("next_location", prev_loc, transition=False)]))]
    text "1" xcenter 530 ycenter 470
    button xcenter 640 ycenter 470 xysize (100, 100) action [SetVariable("dial", dial + "2"), If(limit_input, If(len(dial) >= len(code), [If(dial == code, AddToSet(codes, to_input)), Call("next_location", prev_loc, transition=False)]))]
    text "2" xcenter 640 ycenter 470
    button xcenter 750 ycenter 470 xysize (100, 100) action [SetVariable("dial", dial + "3"), If(limit_input, If(len(dial) >= len(code), [If(dial == code, AddToSet(codes, to_input)), Call("next_location", prev_loc, transition=False)]))]
    text "3" xcenter 750 ycenter 470
    button xcenter 530 ycenter 360 xysize (100, 100) action [SetVariable("dial", dial + "4"), If(limit_input, If(len(dial) >= len(code), [If(dial == code, AddToSet(codes, to_input)), Call("next_location", prev_loc, transition=False)]))]
    text "4" xcenter 530 ycenter 360
    button xcenter 640 ycenter 360 xysize (100, 100) action [SetVariable("dial", dial + "5"), If(limit_input, If(len(dial) >= len(code), [If(dial == code, AddToSet(codes, to_input)), Call("next_location", prev_loc, transition=False)]))]
    text "5" xcenter 640 ycenter 360
    button xcenter 750 ycenter 360 xysize (100, 100) action [SetVariable("dial", dial + "6"), If(limit_input, If(len(dial) >= len(code), [If(dial == code, AddToSet(codes, to_input)), Call("next_location", prev_loc, transition=False)]))]
    text "6" xcenter 750 ycenter 360
    button xcenter 530 ycenter 250 xysize (100, 100) action [SetVariable("dial", dial + "7"), If(limit_input, If(len(dial) >= len(code), [If(dial == code, AddToSet(codes, to_input)), Call("next_location", prev_loc, transition=False)]))]
    text "7" xcenter 530 ycenter 250
    button xcenter 640 ycenter 250 xysize (100, 100) action [SetVariable("dial", dial + "8"), If(limit_input, If(len(dial) >= len(code), [If(dial == code, AddToSet(codes, to_input)), Call("next_location", prev_loc, transition=False)]))]
    text "8" xcenter 640 ycenter 250
    button xcenter 750 ycenter 250 xysize (100, 100) action [SetVariable("dial", dial + "9"), If(limit_input, If(len(dial) >= len(code), [If(dial == code, AddToSet(codes, to_input)), Call("next_location", prev_loc, transition=False)]))]
    text "9" xcenter 750 ycenter 250
    if show_code_length:
        text "[len(code)]桁コード\n[len(code)]-DIGIT CODE" xcenter 640 ycenter 40

image flashlight:
    TrackCursor("mod_assets/flashlight.png") 

default remaining_sec = -1
default oot = ""
screen timer:
    timer 1.0 repeat True action If(remaining_sec <= 0, [Hide("timer"), Call(oot)], SetVariable("remaining_sec", remaining_sec-1))