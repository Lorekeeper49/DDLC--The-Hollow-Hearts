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
default choice_filters = {
    "category": [
        {"choice name": "choice", "variable to set": "test_var", "variable value": "value"}, 
        {"choice name": "unchoice", "variable to set": "test_var", "variable value": "no value"}],
}

screen path_chooser:
    add "taiyen cross" xcenter 640 ycenter 640 zoom 2.0
    text current_text style "path_bg_text" xcenter 640 ycenter 360
    add "noise" at occasional_flash
    add "dark"
    style_prefix "path"
    hbox:
        viewport:
            mousewheel True
            draggable True
            has vbox
            frame:
                text "FILTER CHOICES" xalign 0.1 yalign 0.5 style "path_button_text"
                text "選択肢フィルター" xalign 0.1 yalign 1.1 style "path_kan" 
                background "#20202080"
            for category in choice_filters:
                frame:
                    text category xalign 0.1 yalign 0.5 style "path_button_text"
                    text "選択肢フィルター" xalign 0.1 yalign 1.1 style "path_kan" 
                for filt in choice_filters[category]:
                    button:
                        hbox:
                            xalign 0.1 
                            yalign 0.5
                            spacing 10
                            if filt["variable to set"] == filt["variable value"]:
                                frame xysize (40, 40) background "#fff"
                            else:
                                frame xysize (40, 40) background "#000"
                            text filt["choice name"] style "path_button_text"
                        action SetVariable(filt["variable to set"], filt["variable value"])


    
    timer 5.2 repeat True action SetVariable("current_text", random_list(t_list)[0])

style path_button is gui_button

style path_button:
    size_group "navigation"
    background "#33333380"
    hover_background "#ffffff80"
    xsize 330
    ysize 80
    hover_sound gui.hover_sound
    activate_sound gui.activate_sound

style path_frame:
    size_group "navigation"
    background "#15151580"
    xsize 330
    ysize 80
    hover_sound gui.hover_sound
    activate_sound gui.activate_sound

init -1 style path_button_text:
    font "mod_assets/fonts/ThatSoundsGreat-yYLE3.ttf"
    color "#333"
    hover_color "#fff"
    outlines [(0, "#58585800", 0, 0), (0, "#58585800", 0, 0)]
    size 34
    text_align 0.0

init -1 style path_text:
    font "mod_assets/fonts/ThatSoundsGreat-yYLE3.ttf"
    color "#333"
    outlines [(0, "#58585800", 0, 0), (0, "#58585800", 0, 0)]
    size 50

init -1 style path_kan:
    font "mod_assets/fonts/NotoSerifJP-Regular.otf"
    color "#33333380"
    hover_color "#ffffff80"
    outlines [(0, "#58585800", 0, 0), (0, "#58585800", 0, 0)]
    size 20