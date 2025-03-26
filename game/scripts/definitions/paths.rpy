default cute = False
default known = False
default found_breaker = False
default secrets = False
default en_out = False
default followed = False
default persistent.choices_made = []
define extra_selected = []
define selected_path = -1
define path_shown = True

# Choice Filters: used to filter out paths for organization
#   keys: the category names to use for reference and display
#       variable to set: the defined global that changes with the buttons
#       hidden: determines if the category should be hidden if the player hasn't unlocked it
#       buttons: a list of the buttons associated
#           choice name: the name of the filter
#           variable value: the value the category variable is set to, don't use None, that is no filter
#           needed choices: the choices the player has to have made to unlock the filter
#           hidden: determines if the filter should be hidden if the player hasn't unlocked it
default act2_choice_filters = {
    "HIDDEN GIRL": { "variable to set": "hidden_girl", "JP": "隠れた少女", "hidden": False,
        "buttons": [
        {"choice name": "REVEALED", "JP": "ハニカミ", "variable value": "revealed", "needed choices": ["Hidden Girl Revealed"], "hidden": False}, 
        {"choice name": "HIDDEN", "JP": "隠れ", "variable value": "hidden", "needed choices": ["Hidden Girl Kept Secret"], "hidden": False}
        ]
    }
}

# Path Lists: the lists of paths you can take
#   title: The name of the path, the screen looks for "mod_assets/paths/" + title + ".png" for the thumbnail and expects it to be a 1920x1080 image 
#   needed choices: the choices the player has to have made to unlock the path
#   categories: the categories the path is associated with, used for filtering
#       keys: category name
#       value: the value the filter category needs to be to be shown besides None
#   label: the label to call when the player hits play
#   extra options: extra options that the player can select that change the path slightly
#       option name: the name of the option
#       needed choices: the choices the player has to have made to unlock the option
#       hidden: determines if the option should be hidden if the player hasn't unlocked it
#   hidden: determines if the path should be hidden if the player hasn't unlocked it
default act2_path_list = [
    {"title": "The Timid Storm", "JP": "小心嵐", "needed choices": ["Hidden Girl Revealed"], "categories": {"HIDDEN GIRL": "revealed"}, "label": "act2", "extra options": [], "hidden": True},
    {"title": "The Hidden Girl", "JP": "隠れた少女", "needed choices": ["Hidden Girl Kept Secret"], "categories": {"HIDDEN GIRL": "hidden"}, "label": "act2_alt", "extra options": [], "hidden": False}
]

# define your choice filter variables here.  You must use define and not default or there will be an error.
# don't edit these variables in the story or reloading will reset them
define hidden_girl = None
define test_girl = None

transform occasional_flash:
    parallel:
        linear 0.1 alpha 0.5
        5.0
        linear 0.1 alpha 1.0
        repeat

style path_bg_text:
    font "mod_assets/fonts/FOT-RodinNTLG Pro EB.otf"
    color "#fff"
    size 200
    text_align 0.5

default current_text = "CONTROLLER"
default char_list = "t_list"
default t_list = [
    "KILL HIM",
    "HE NEEDS DEATH",
    "CONTROLLER",
    "HELP ME",
    "SAVE THEM",
    "I RUINED HIM"
    ]

screen path_chooser(choice_filters, path_list):
    add "black"
    add "taiyen cross" xcenter 640 ycenter 640 zoom 2.0
    text current_text style "path_bg_text" xcenter 640 ycenter 360
    add "noise" at occasional_flash
    add "dark"
    style_prefix "path"
    frame:
        xysize (640, 720)
        background "#08080880"
    hbox:
        vbox:
            frame:
                text "FILTER CHOICES" xalign 0.1 yalign 0.5 style "path_button_text"
                text "選択肢フィルター" xalign 0.1 yalign 1.1 style "path_kan" 
                background "#20202080"
            viewport:
                mousewheel True
                draggable True
                has vbox
                for category in choice_filters:
                    for filt in choice_filters[category]["buttons"]:
                        $ path_shown = True
                        if choice_filters[category]["hidden"] and not all(item in persistent.choices_made for item in filt["needed choices"]):
                            $ path_shown = False
                            break
                    if path_shown:
                        frame:
                            text category xalign 0.1 yalign 0.5 style "path_button_text"
                            text choice_filters[category]["JP"] xalign 0.1 yalign 1.1 style "path_kan" 
                        for filt in choice_filters[category]["buttons"]:
                            if not filt["hidden"] or all(item in persistent.choices_made for item in filt["needed choices"]):
                                button:
                                    text filt["JP"] xalign 0.1 yalign 1.1 style "path_kan" 
                                    hbox:
                                        yalign 0.5
                                        spacing 10
                                        if globals()[choice_filters[category]["variable to set"]] == filt["variable value"]:
                                            frame xysize (40, 40) background "#fff"
                                        else:
                                            frame xysize (40, 40) background "#000"
                                        if filt["needed choices"] is None or all(item in persistent.choices_made for item in filt["needed choices"]):
                                            text filt["choice name"] style "path_button_text"
                                        else:
                                            text "?" style "path_button_text"
                                    action If(filt["needed choices"] is None or all(item in persistent.choices_made for item in filt["needed choices"]), SetVariable(choice_filters[category]["variable to set"], filt["variable value"]))
                        button:
                            text "フィルターなし" xalign 0.1 yalign 1.1 style "path_kan" 
                            hbox:
                                yalign 0.5
                                spacing 10
                                if globals()[choice_filters[category]["variable to set"]] is None:
                                    frame xysize (40, 40) background "#fff"
                                else:
                                    frame xysize (40, 40) background "#000"
                                text "NO FILTER" style "path_button_text"
                            action SetVariable(choice_filters[category]["variable to set"], None)
                        button:
                            text "全て隠す" xalign 0.1 yalign 1.1 style "path_kan" 
                            hbox:
                                yalign 0.5
                                spacing 10
                                if globals()[choice_filters[category]["variable to set"]] == False:
                                    frame xysize (40, 40) background "#fff"
                                else:
                                    frame xysize (40, 40) background "#000"
                                text "HIDE ALL" style "path_button_text"
                            action SetVariable(choice_filters[category]["variable to set"], False)
    vbox:
        spacing -4
        frame:
            xpos 640
            xsize 500
            text "CHOOSE YOUR PATH" xcenter 250 yalign 0.5 style "path_button_text"
            text "道を選んで下さい" xcenter 250 yalign 1.1 style "path_kan" 
        frame:
            xpos 636
            xysize (500, 640)
            background "#0000"
            viewport:
                mousewheel True
                draggable True
                has vbox
                spacing 10
                for i in range(len(path_list)):
                    for category in path_list[i]["categories"]:
                        $ path_shown = True
                        if (globals()[choice_filters[category]["variable to set"]] is not None and globals()[choice_filters[category]["variable to set"]] != path_list[i]["categories"][category]) or (path_list[i]["hidden"] and not all(item in persistent.choices_made for item in path_list[i]["needed choices"])):
                            $ path_shown = False
                            break
                    if path_shown:
                        button:
                            xysize (500, 300)
                            if path_list[i]["needed choices"] is None or all(item in persistent.choices_made for item in path_list[i]["needed choices"]):
                                text path_list[i]["title"] style "path_title" xcenter 250
                                add "mod_assets/paths/" + path_list[i]["title"] + ".png" xalign 0.25 yalign 0.5 zoom 0.2
                                text path_list[i]["JP"] style "path_title" xcenter 250 yalign 1.0
                            else:
                                text "LOCKED PATH" style "path_title" xcenter 250
                                frame xysize (384, 216) xalign 0.25 yalign 0.5 background "#000"
                                text "ロックされた道"style "path_title" xcenter 250 yalign 1.0
                            if selected_path == i:
                                background "#ffffff40"
                            else:
                                background "#00000000"
                            hover_background "#ffffff80"
                            action If(path_list[i]["needed choices"] is None or all(item in persistent.choices_made for item in path_list[i]["needed choices"]), [ToggleVariable("selected_path", i, -1)])
    vbox:
        spacing -4
        button:
            xysize (140, 140)
            xalign 1.0
            yalign 1.0
            xpos 1280
            background "#00000000"
            hover_background "#ffffff80"
            text "BACK" style "path_button_text" xalign 0.5 yalign 0.5
            action Hide("path_chooser", StaticTransitionLong)          
        if selected_path != -1:
            frame:
                xalign 1.0
                xpos 1280
                xysize (144, 450)
                background "#0000"
                viewport:
                    mousewheel True
                    draggable True
                    has vbox
                    if path_list[selected_path]["extra options"] is not None:
                        for option in path_list[selected_path]["extra options"]:
                            if not option["hidden"] or all(item in persistent.choices_made for item in option["needed choices"]):
                                button:
                                    xysize (140, 140)
                                    if option["option name"] in extra_selected:
                                        background "#ffffff40"
                                    else:
                                        background "#00000000"
                                    hover_background "#ffffff80"
                                    if option["needed choices"] is None or all(item in persistent.choices_made for item in option["needed choices"]):
                                        text option["option name"] style "path_button_text" xalign 0.5 yalign 0.5
                                    else:
                                        text "?" style "path_button_text" xalign 0.5 yalign 0.5
                                    action If(option["needed choices"] is None or all(item in persistent.choices_made for item in option["needed choices"]), ToggleSetMembership(extra_selected, option["option name"]))
            button:
                xysize (140, 140)
                xalign 1.0
                yalign 1.0
                xpos 1280
                background "#00000000"
                hover_background "#ffffff80"
                text "PLAY" style "path_button_text" xalign 0.5 yalign 0.5
                action Function(renpy.jump_out_of_context, path_list[selected_path]["label"])
            

    timer 5.2 repeat True action SetVariable("current_text", random_list(globals()[char_list])[0])

style path_button is gui_button

style path_button:
    size_group "navigation"
    background "#33333380"
    hover_background "#ffffff80"
    xsize 640
    ysize 80
    hover_sound gui.hover_sound
    activate_sound gui.activate_sound

style path_frame:
    size_group "navigation"
    background "#15151580"
    xsize 640
    ysize 80
    hover_sound gui.hover_sound
    activate_sound gui.activate_sound

style path_button_text:
    font "mod_assets/fonts/FOT-RodinNTLG Pro EB.otf"
    color "#333"
    hover_color "#fff"
    outlines [(0, "#58585800", 0, 0), (0, "#58585800", 0, 0)]
    size 34
    text_align 0.0

style path_text:
    font "mod_assets/fonts/FOT-RodinNTLG Pro EB.otf"
    color "#333"
    outlines [(0, "#58585800", 0, 0), (0, "#58585800", 0, 0)]
    size 50

style path_kan:
    font "mod_assets/fonts/FOT-RodinNTLG Pro EB.otf"
    color "#33333380"
    hover_color "#ffffff80"
    outlines [(0, "#58585800", 0, 0), (0, "#58585800", 0, 0)]
    size 20

style path_title:
    font "mod_assets/fonts/FOT-RodinNTLG Pro EB.otf"
    color "#333"
    hover_color "#fff"
    outlines [(0, "#58585800", 0, 0), (0, "#58585800", 0, 0)]
    size 34
    text_align 0.5