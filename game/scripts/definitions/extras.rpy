define extras_dict = {
    "name": {"credits": "", "desc": "Test diescription", "audio": False, "file": "", "JP": ""}
}

screen extra_selection(extras_dict):
    vbox at navigation_transform(880):
        style_prefix "main_menu"
        for name in extras_dict:
            button:
                xsize 400
                text name xpos 25 yalign 0.5 style "main_menu_button_text"
                text extras_dict[name]["JP"] xpos 25 yalign 1.1 style "main_menu_kan"
                action Show("extra_view", dissolve, extras_dict, name, _layer="textbox") 
        frame:
            ysize 720
            background "#0001"

screen extra_view(extras_dict, name):
    add "#0008"
    textbutton "X" xalign 1.0 action Hide("extra_view", dissolve, _layer="textbox")
    vbox:
        label name
        text extras_dict[name]["credits"]
        viewport:
            mousewheel True
            draggable True
            xmaximum 640
            text extras_dict[name]["desc"]
    
    button: 
        add "mod_assets/extras/" + name + ".png" zoom 0.25
        hover_foreground "#fff3" 
        ycenter 360 
        xcenter 960 
        action If(not extras_dict[name]["audio"], Show("extra_fullscreen", dissolve, name, _layer="textbox"), Play("sound", extras_dict[name]["file"]))

screen extra_fullscreen(name):
    add "black"
    textbutton "X" xalign 1.0 action Hide("extra_fullscreen", dissolve, _layer="textbox")
    add "mod_assets/extras/" + name + ".png"