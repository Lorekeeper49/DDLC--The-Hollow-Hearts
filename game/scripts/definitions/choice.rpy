init -1 style choice_button is button
init -1 style choice_button_text is button_text
init -1 style choice_text is text

init -1 style choice_button is default:
    hover_sound gui.hover_sound
    activate_sound gui.activate_sound

init -1 style choice_button_text is default:
    font "mod_assets/fonts/NotoSerifJP-Regular.otf"
    color "#fff"
    hover_color "#000"
    size 35
    outlines [(1, "#585858", 0, 0), (1, "#585858", 1, 1)]

init -1 style choice_text is default:
    font "mod_assets/fonts/NotoSerifJP-Regular.otf"
    color "#fff"
    outlines [(1, "#585858", 0, 0), (1, "#585858", 1, 1)]

default choice_impact = False
init -501 screen choice(items,title="",time=None,force=0):
    if choice_impact:
        on "show" action [Show("dummy_dark"), SetVariable("selected_choice", 0), SetVariable("choice_selected", False), Show("impact_item", None, items[selected_choice], _transform=impact_center, _tag="selected_item"), Show("impact_item", None, items[(selected_choice+1) % len(items)], _transform=impact_right, _tag="next_item"), Show("impact_item", None, items[selected_choice-1], _transform=impact_left, _tag="prev_item"), SetVariable("choice_selected", False), Show("impacted_choice", Fade(0.1, 0, 0.5, color="#fff"), items, title)]
        if choice_selected:
            timer 5.0 action [SetVariable("choice_selected", False), items[selected_choice].action]
    else:
        use unimpacted_choice(items, time, force)

init -501 screen unimpacted_choice(items,time,force):
    use choice_menu_bg
    fixed at choice_menu_transform:
        viewport id "vp":
            mousewheel True
            draggable True
            has vbox
            null height 40
            xmaximum 300
            style_prefix "choice"
            for i in items:
                if "locked" in i.kwargs:
                    if i.kwargs['locked']:
                        text "???" xpos 150
                    else:
                        text "PATH UNLOCKED" xpos 150
                        textbutton i.caption action i.action xpos 150
                else:
                    textbutton i.caption action i.action xpos 150
    
    if time is not None:
        timer time action items[force].action
        
        add Solid("#585858"):
            at transform:
                subpixel True xysize (50, 200)
                yalign 0.5 xpos 0.05
                linear time yzoom 0.0

init -501 screen choice_menu_bg():

    frame at choice_menu_transform:
        ysize 800
        background "choice_bg"

image choice_bg:
    "mod_assets/gui/choice_bg.png"
    alpha 0.5

init -501 transform choice_menu_transform:
    on show:
        xpos 1280
        ypos 0
        easeout .25 xpos 740
    on hide:
        xpos 740
        easein .25 xpos 1280

define selected_choice = 0
define choice_selected = False
init -501 screen impacted_choice(items,title):
    fixed at impact_transform:
        style_prefix "impact"
        # choice frames from left to right: prev, current, next
        text title xalign 0.5 size 50

        button:
            xalign 1.0
            yalign 0.5
            text ">"
            background "#0008"
            action SetVariable("selected_choice", (selected_choice + 1) % len(items)) # what it's supposed to be:[SetVariable("selected_choice", (selected_choice + 1) % len(items)), Show("selected_item", None, _transform=impact_left, _tag="prev_item"), Show("next_item", None, _transform=impact_center, _tag="selected_item"), Hide("prev_item"), Show("impact_item", None, items[(selected_choice+1) % len(items)], _transform=impact_left, _tag="next_item")]
        button:
            xalign 0.0
            yalign 0.5
            text "<"
            background "#0008"
            action SetVariable("selected_choice", (selected_choice - 1) % len(items)) # what it's supposed to be [SetVariable("selected_choice", (selected_choice - 1) % len(items)), Show("selected_item", None, _transform=impact_right, _tag="next_item"), Show("prev_item", None, _transform=impact_center, _tag="selected_item"), Hide("next_item"), Show("impact_item", None, items[selected_choice-1], _transform=impact_right, _tag="prev_item")]
        button:
            xalign 0.5
            yalign 1.0
            text "SELECT"
            background "#0008"
            action [SetVariable("choice_selected", True), Hide("impacted_choice"), Hide("selected_item"), Hide("next_item"), Hide("prev_item"), Hide("dummy_dark", Dissolve(5))]
        
init -501 transform impact_transform:
    on show:
        zoom 2.0
        easeout .25 zoom 1.0
    on hide:
        alpha 1.0
        easein 5.0 alpha 0.0

init -501 transform impact_center:
    on show:
        xcenter 640 ycenter 360 zoom 2.0
        easeout_quart 1.0 zoom 1.0
    on replace:
        ease_quart 0.1 zoom 1.0 xcenter 640 ycenter 360 alpha 1.0
    on hide:
        easeout_quart 0.1 zoom 1.25
        linear 4.9 zoom 2.0 alpha 0.0

init -501 transform impact_right:
    on show:
        xcenter 1380 ycenter 360 alpha 0.0 zoom 0.5
        easeout_quart 1.0 xpos 1100 alpha 0.5 zoom 0.75
    on replace:
        ease_quart 1.0 zoom 0.75 xcenter 1100 ycenter 360 alpha 0.5
    on hide:
        easein_quart 1.0 zoom 0.5 xpos 1280 alpha 0.0

init -501 transform impact_left:
    yanchor 1.0
    on show:
        zoom 0.5 xpos 0 alpha 0.0 ycenter 360 xpos 1.0
        easeout_quart 1.0 xcenter 260 alpha 0.5 zoom 0.75
    on replace:
        ease_quart 1.0 zoom 0.75 xcenter 260 ycenter 360 alpha 0.5
    on hide:
        easein_quart 1.0 zoom 0.5 xpos 0 alpha 0.0

init -501 screen impact_item(item, *, _transform):
    style_prefix "impact"
    frame at _transform:
        text item.caption size 50

init -501 screen dummy_dark:
    add "dark"