define extras_dict = {
    "name": {"credits": "", "desc": "", "audio": False, "file": ""}
}

screen extra_selection(extras_dict):
    vbox at navigation_transform(880):
        for name in extras_dict:
            button:
                text name
                add "mod_assets/extras/" + name + ".png"
                action Show("extra_view", dissolve, extras_dict, name) 

screen extra_view(extras_dict, name):
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
        action If(not extras_dict[name]["audio"], Show("extra_fullscreen", dissolve, extras_dict, name), Play("sound", extras_dict[name]["file"]))

screen extra_fullscreen(extras_dict, name):
    textbutton "X" action Hide("extra_fullscreen", dissolve)
    add "mod_assets/extras/" + name + ".png"