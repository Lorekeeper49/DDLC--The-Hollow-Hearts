default cute = False
default known = False
default found_breaker = False
default secrets = False
default en_out = False
default followed = False
default persistent.choices_made = []
define extra_selected = []
define selected_path = -1

default act2_choice_filters = {
    "HIDDEN GIRL": { "variable to set": "hidden_girl",
        "buttons": [
        {"choice name": "REVEALED", "variable value": "revealed", "needed choices": ["Hidden Girl Revealed"]}, 
        {"choice name": "HIDDEN", "variable value": "hidden", "needed choices": ["Hidden Girl Kept Secret"]}
        ]
    },
}

default act2_path_list = [
    {"title": "The Timid Storm", "needed choices": ["Hidden Girl Revealed"], "category": "HIDDEN GIRL", "filter value": "revealed", "label": "act2", "extra options": [{"option name": "item", "needed choices": ["niajnfoie"]}]},
    {"title": "The Hidden Girl", "needed choices": ["Hidden Girl Kept Secret"], "category": "HIDDEN GIRL", "filter value": "hidden", "label": "act2_alt", "extra options": []},
]

# define your choice filter variables here.  You must use define and not default or there will be an error.
# don't edit these variables in the story or reloading will reset them
define hidden_girl = None


transform occasional_flash:
    parallel:
        linear 0.1 alpha 0.5
        5.0
        linear 0.1 alpha 1.0
        repeat

style path_bg_text:
    font "mod_assets/fonts/Unitblock-mLAwm.ttf"
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
                    frame:
                        text category xalign 0.1 yalign 0.5 style "path_button_text"
                        text "選択肢フィルター" xalign 0.1 yalign 1.1 style "path_kan" 
                    for filt in choice_filters[category]["buttons"]:
                        button:
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
                        hbox:
                            yalign 0.5
                            spacing 10
                            if globals()[choice_filters[category]["variable to set"]] is None:
                                frame xysize (40, 40) background "#fff"
                            else:
                                frame xysize (40, 40) background "#000"
                            text "UNFILTER" style "path_button_text"
                        action SetVariable(choice_filters[category]["variable to set"], None)
    viewport:
        mousewheel True
        draggable True
        has vbox
        spacing 10
        for i in range(len(path_list)):
            if globals()[choice_filters[path_list[i]["category"]]["variable to set"]] is None or globals()[choice_filters[path_list[i]["category"]]["variable to set"]] == path_list[i]["filter value"]:
                button:
                    xpos 640
                    xysize (500, 300)
                    if filt["needed choices"] is None or all(item in persistent.choices_made for item in filt["needed choices"]):
                        text path_list[i]["title"] style "path_title" xcenter 250
                        add "mod_assets/paths/" + path_list[i]["title"] + ".png" xalign 0.25 yalign 0.5 zoom 0.2
                    else:
                        text "LOCKED PATH" style "path_title" xcenter 250
                        frame xysize (384, 216) xalign 0.25 yalign 0.5
                    if selected_path == i:
                        background "#ffffff40"
                    else:
                        background "#00000000"
                    hover_background "#ffffff80"
                    action If(filt["needed choices"] is None or all(item in persistent.choices_made for item in filt["needed choices"]), SetVariable("selected_path", i))
    vbox:
        button:
            xysize (140, 140)
            xalign 1.0
            yalign 1.0
            xpos 1280
            background "#00000000"
            hover_background "#ffffff80"
            text "BACK" style "path_button_text" xalign 0.5 yalign 0.5
            action Hide("path_chooser", dissolve_scene)          
        if selected_path != -1:
            button:
                xysize (140, 140)
                xalign 1.0
                yalign 1.0
                xpos 1280
                background "#00000000"
                hover_background "#ffffff80"
                text "PLAY" style "path_button_text" xalign 0.5 yalign 0.5
                action Function(renpy.jump_out_of_context, path_list[selected_path]["label"])
            viewport:
                mousewheel True
                draggable True
                has vbox
                if path_list[selected_path]["extra options"] is not None:
                    for option in path_list[selected_path]["extra options"]:
                        button:
                            xysize (140, 140)
                            xalign 1.0
                            xpos 1280
                            if option["option name"] in extra_selected:
                                background "#ffffff40"
                            else:
                                background "#00000000"
                            hover_background "#ffffff80"
                            if option["needed choices"] is None or all(item in persistent.choices_made for item in option["needed choices"]):
                                text option["option name"] style "path_button_text" xalign 0.5 yalign 0.5
                            else:
                                text "?" style "path_button_text" xalign 0.5 yalign 0.5
                            action If(option["needed choices"] is None or all(item in persistent.choices_made for item in option["needed choices"]), If(option["option name"] in extra_selected, RemoveFromSet(extra_selected, option["option name"]), AddToSet(extra_selected, option["option name"])))
            

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
    font "mod_assets/fonts/ThatSoundsGreat-yYLE3.ttf"
    color "#333"
    hover_color "#fff"
    outlines [(0, "#58585800", 0, 0), (0, "#58585800", 0, 0)]
    size 34
    text_align 0.0

style path_text:
    font "mod_assets/fonts/ThatSoundsGreat-yYLE3.ttf"
    color "#333"
    outlines [(0, "#58585800", 0, 0), (0, "#58585800", 0, 0)]
    size 50

style path_kan:
    font "mod_assets/fonts/NotoSerifJP-Regular.otf"
    color "#33333380"
    hover_color "#ffffff80"
    outlines [(0, "#58585800", 0, 0), (0, "#58585800", 0, 0)]
    size 20

style path_title:
    font "mod_assets/fonts/ThatSoundsGreat-yYLE3.ttf"
    color "#333"
    hover_color "#fff"
    outlines [(0, "#58585800", 0, 0), (0, "#58585800", 0, 0)]
    size 34
    text_align 0.5