screen notify(message):
    zorder 100

    text message at _notify_transform

    # This controls how long it takes between when the screen is
    # first shown, and when it begins hiding.
    timer 3.25 action Hide('notify')

transform _notify_transform:
    # These control the position.
    xalign .02 yalign .015

    # These control the actions on show and hide.
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0

style appeal_text:
    font "mod_assets/fonts/AlexBrush-Regular.ttf"
    size 75
    color gui.text_color
    outlines [(2, "#000000aa", 0, 0)]
    xcenter 1150
    ycenter 100
    xoffset -100
    text_align 1.0
    line_spacing 0.1

style add_text:
    font "mod_assets/fonts/AlexBrush-Regular.ttf"
    size 75
    color "#00ff00"
    outlines [(2, "#000000aa", 0, 0)]
    xcenter 1230
    ycenter 50
    text_align 1.0

style sub_text:
    font "mod_assets/fonts/AlexBrush-Regular.ttf"
    size 75
    color "#ff0000"
    outlines [(2, "#000000aa", 0, 0)]
    xcenter 1230
    ycenter 50
    text_align 1.0
image appeal_show:
    "mod_assets/appeal.png"
    xcenter 640

image appeal_text = ParameterizedText(style="appeal_text")

image add_text = ParameterizedText(style="add_text")
image sub_text = ParameterizedText(style="sub_text")

transform appeal_transform:
    alpha 0
    xoffset 30
    on show:
        easeout .5 yoffset 0 zoom 1.00 alpha 1.00 xoffset 0
    on replace:
        alpha 1
        yoffset 0
        zoom 1
    on hide:
        easein .5 yoffset 0 zoom 1.00 alpha 0.00 xoffset 30

transform appealin:
    alpha 0
    on show:
        easeout .25 yoffset 0 zoom 1.00 alpha 1.00 xoffset 0
        easeout 1 yoffset -30 alpha 0
    on hide:
        easein .5 yoffset 0 zoom 1.00 alpha 0.00 xoffset 30   

transform appealde:
    alpha 0
    on show:
        easeout .25 yoffset 0 zoom 1.00 alpha 1.00 xoffset 0
        easeout 1 yoffset 30 alpha 0
    on hide:
        easein .5 yoffset 0 zoom 1.00 alpha 0.00 xoffset 30

label addappeal(char="",app=0,eal=0,unlock=False):
    show appeal_show zorder 100 at appeal_transform
    show appeal_text ("[char]:" + str(eal) + "\nNormal") as atext zorder 100 at appeal_transform
    pause(1)
    if app > 0:
        show add_text ("+" + str(app)) as numtext zorder 100 at appealin
        show appeal_text ("[char]:" + str(eal+app) + "\nNormal") as atext zorder 100 at appeal_transform
        pause(1)
    elif app < 0:
        show sub_text (str(app)) as numtext zorder 100 at appealde
        show appeal_text ("[char]:" + str(eal+app) + "\nNormal") as atext zorder 100 at appeal_transform
        pause(1)
    hide atext
    hide numtext
    if unlock:
        show appeal_text "Path Unlocked" as atext zorder 100 at appeal_transform
        pause(1)
        hide atext
    hide appeal_show
    return

label addstoryappeal(char="",app=0,eal=0,unlock=False):
    show appeal_show zorder 100 at appeal_transform
    show appeal_text ("[char]:" + str(eal) + "\nStory") as atext zorder 100 at appeal_transform
    pause(1)
    if app > 0:
        show add_text ("+" + str(app)) as numtext zorder 100 at appealin
        show appeal_text ("[char]:" + str(eal+app) + "\nStory") as atext zorder 100 at appeal_transform
        pause(1)
    elif app < 0:
        show sub_text (str(app)) as numtext zorder 100 at appealde
        show appeal_text ("[char]:" + str(eal+app) + "\nStory") as atext zorder 100 at appeal_transform
        pause(1)
    hide atext
    hide numtext
    if unlock:
        show appeal_text "Path Unlocked" as atext zorder 100 at appeal_transform
        pause(1)
        hide atext
    hide appeal_show
    return

label addtrust(char="",app=0,eal=0,unlock=False):
    show appeal_show zorder 100 at appeal_transform
    show appeal_text ("[char]:" + str(eal) + "\nTrust") as atext zorder 100 at appeal_transform
    pause(1)
    if app > 0:
        show add_text ("+" + str(app)) as numtext zorder 100 at appealin
        show appeal_text ("[char]:" + str(eal+app) + "\nTrust") as atext zorder 100 at appeal_transform
        pause(1)
    elif app < 0:
        show sub_text (str(app)) as numtext zorder 100 at appealde
        show appeal_text ("[char]:" + str(eal+app) + "\nTrust") as atext zorder 100 at appeal_transform
        pause(1)
    hide atext
    hide numtext
    if unlock:
        show appeal_text "Path Unlocked" as atext zorder 100 at appeal_transform
        pause(1)
        hide atext
    hide appeal_show
    return