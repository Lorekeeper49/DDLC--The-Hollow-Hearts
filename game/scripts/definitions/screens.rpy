init -1 style ruby_style is default:
    size 12
    yoffset -20

init -1 style default:
    font gui.default_font
    size gui.text_size
    color gui.text_color
    outlines [(2, "#000000aa", 0, 0)]
    line_overlap_split 1
    line_spacing 1
    ruby_style style.ruby_style

init -1 style edited is default:
    font "gui/font/VerilySerifMono.otf"
    kerning 8
    outlines [(10, "#000", 0, 0)]
    xpos gui.text_xpos
    xanchor gui.text_xalign
    xsize gui.text_width
    ypos gui.text_ypos
    text_align gui.text_xalign
    layout ("subtitle" if gui.text_xalign else "tex")

init -1 style normal is default:
    xpos gui.text_xpos
    xanchor gui.text_xalign
    xsize gui.text_width
    ypos gui.text_ypos

    text_align gui.text_xalign
    layout ("subtitle" if gui.text_xalign else "tex")

init -1 style input:
    color gui.accent_color

init -1 style hyperlink_text:
    color gui.accent_color
    hover_color gui.hover_color
    hover_underline True

init -1 style splash_text:
    size 24
    color "#ffffff"
    font gui.default_font
    text_align 0.5
    outlines []

init -1 style storygame_text:
    yalign 0.5
    font "gui/font/Halogen.ttf"
    size 30
    color "#000"
    outlines []

    hover_xoffset -3
    hover_outlines [(3, "#fef", 0, 0), (2, "#fcf", 0, 0), (1, "#faf", 0, 0)]

init -1 style gui_text:
    font gui.interface_font
    color gui.interface_text_color
    size gui.interface_text_size


init -1 style button:
    properties gui.button_properties("button")

init -1 style button_text is gui_text:
    properties gui.button_text_properties("button")
    yalign 0.5


init -1 style label_text is gui_text:
    color gui.accent_color
    size gui.label_text_size

init -1 style prompt_text is gui_text:
    color gui.text_color
    size gui.interface_text_size







init -1 style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

init -1 style bar:
    ysize 18
    base_bar Frame("gui/scrollbar/horizontal_poem_bar.png", tile=False)
    thumb Frame("gui/scrollbar/horizontal_poem_thumb.png", top=6, right=6, tile=True)

init -1 style scrollbar:
    ysize 18
    base_bar Frame("gui/scrollbar/horizontal_poem_bar.png", tile=False)
    thumb Frame("gui/scrollbar/horizontal_poem_thumb.png", top=6, right=6, tile=True)
    unscrollable "hide"
    bar_invert True


init -1 style vscrollbar:
    xsize 18
    base_bar Frame("gui/scrollbar/vertical_poem_bar.png", tile=False)
    thumb Frame("gui/scrollbar/vertical_poem_thumb.png", left=6, top=6, tile=True)
    unscrollable "hide"
    bar_invert True






init -1 style slider:
    ysize 18
    base_bar Frame("gui/scrollbar/horizontal_poem_bar.png", tile=False)
    thumb "gui/slider/horizontal_hover_thumb.png"

init -1 style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


init -1 style frame:
    padding gui.frame_borders.padding
    background Frame("mod_assets/gui/frame.png", gui.frame_borders, tile=gui.frame_tile)




















default nb = "namebox_fake"
init -501 screen say(who, what):
    style_prefix "say"
    
    window:
        id "window"

        text what id "what" font "mod_assets/fonts/NotoSerifJP-Regular.otf"

        if who is not None:

            window:
                style nb
                text who id "who" font "mod_assets/fonts/NotoSerifJP-Regular.otf"



    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0

    use quick_menu

init -1 style window is default
init -1 style window_fake is default
init -1 style say_label is default
init -1 style say_dialogue is default
init -1 style say_thought is say_dialogue

init -1 style namebox is default
init -1 style namebox_fake is default
init -1 style namebox_label is say_label


init -1 style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("mod_assets/gui/textbox.png", xalign=0.5, yalign=1.0)

init -1 style namebox:
    xpos gui.name_xpos+295
    xanchor gui.name_xalign
    xsize 816
    ypos gui.name_ypos-50
    ysize 86
    text_align 0.5

    background Frame("mod_assets/gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

init -1 style window_fake:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("mod_assets/gui/faketextbox.png", xalign=0.5, yalign=1.0)

init -1 style namebox_fake:
    xpos gui.name_xpos+295
    xanchor gui.name_xalign
    xsize 816
    ypos gui.name_ypos-50
    ysize 86

    background Frame("mod_assets/gui/fakenamebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

init -1 style say_label:
    color gui.accent_color
    font gui.name_font
    size gui.name_text_size
    xalign gui.name_xalign
    yalign 0.5
    text_align 0.5
    line_spacing -10
    outlines [ ( 0, "#000", 1, 1) ]

init -1 style say_dialogue:
    xpos gui.text_xpos
    xanchor gui.text_xalign
    xsize gui.text_width
    ypos gui.text_ypos

    text_align gui.text_xalign
    layout ("subtitle" if gui.text_xalign else "tex")

init 499 image ctc:
    xalign 0.81 yalign 0.98 xoffset -5 alpha 0.0 subpixel True
    "gui/ctc.png"
    block:
        easeout 0.75 alpha 1.0 xoffset 0
        easein 0.75 alpha 0.5 xoffset -5
        repeat











init 499 image input_caret:
    Solid("#b59")
    size (2,25) subpixel True
    block:
        linear 0.35 alpha 0
        linear 0.35 alpha 1
        repeat

init -501 screen input(prompt):
    style_prefix "input"

    window:

        has vbox:
            xpos gui.text_xpos
            xanchor 0.5
            ypos gui.text_ypos

        text prompt style "input_prompt"
        input id "input"


init -1 style input_prompt is default

init -1 style input_prompt:
    xmaximum gui.text_width
    xalign gui.text_xalign
    text_align gui.text_xalign

init -1 style input:
    caret "input_caret"
    xmaximum gui.text_width
    xalign 0.5
    text_align 0.5





init -501 screen choice(items,time=None,force=0,mouse=None):
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
                        textbutton "???" xpos 150
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
    
    if mouse is not None:
        timer 1.0/30.0 repeat True action Function(RigMouse, mouse)

init -501 screen choice_menu_bg():

    frame at choice_menu_transform:
        ysize 800
        background "choice_bg"

image choice_bg:
    "mod_assets/gui/choice_bg.png"
    alpha 0.5

init -501 transform choice_menu_transform(xo=0,yo=0):
    on show:
        xpos 1280
        ypos yo
        easeout .25 xpos 740+xo
    on hide:
        xpos 740+xo
        easein .25 xpos 1280


define -1 config.narrator_menu = True


init -1 style choice_button is button
init -1 style choice_button_text is button_text
init -1 style choice_text is text

init -1 style choice_button is default:
    hover_sound gui.hover_sound
    activate_sound gui.activate_sound

init -1 style choice_button_text is default:
    font "mod_assets/fonts/AlexBrush-Regular.ttf"
    color "#fff"
    hover_color "#bbbbbb"
    size 35
    outlines [(1, "#585858", 0, 0), (1, "#585858", 1, 1)]

init -1 style choice_text is default:
    font "mod_assets/fonts/AlexBrush-Regular.ttf"
    color "#fff"
    outlines [(1, "#585858", 0, 0), (1, "#585858", 1, 1)]

init -1 python:
    def RigMouse():
        currentpos = renpy.get_mouse_pos()
        targetpos = [640, 345]
        if currentpos[1] < targetpos[1]:
            renpy.display.draw.set_mouse_pos((currentpos[0] * 9 + targetpos[0]) / 10.0, (currentpos[1] * 9 + targetpos[1]) / 10.0)

init -501 screen quick_menu():


    zorder 2000

    if quick_menu:
        imagebutton idle "mod_assets/gui/menu_button.png" action [SetVariable("option_index", 0), ShowMenu("navigation"), SensitiveIf(renpy.get_screen("navigation") == None)]
        key "K_ESCAPE" action [SetVariable("option_index", 0), ShowMenu("navigation"), SensitiveIf(renpy.get_screen("navigation") == None)]

default -1 quick_menu = True

init -1 python:
    def StartGame():
        if config.developer:
            renpy.jump_out_of_context("dev")
        else:
            renpy.jump_out_of_context("start")
    def Act3():
        renpy.jump_out_of_context("act3")
    def Extras():
        renpy.jump_out_of_context("extras")

default -1 option_index = 0
default -1 aa_status = "OFF"
default -1 aa_status_kan = "{size=20}オッフ{/size}"

init -501 screen navigation():
    
    zorder 3000
    use navigation_border
    vbox at navigation_transform(0, 10):
        style_prefix "navigation"
        spacing 0
        if main_menu:
            textbutton _("CLOSE\n{size=20}閉じる{/size}") hovered [SetVariable("option_index", 0)] action [Hide("achievements"), Hide("preferences"), Hide("file_slots"), Hide("navigation")]
            textbutton _("BEGIN\n{size=20}スタート{/size}") hovered [SetVariable("option_index", 1)] action Function(StartGame)
            textbutton _("BOOKMARKS\n{size=20}しおり{/size}") hovered [SetVariable("option_index", 2)] action [Hide("achievements"), Hide("preferences"), ShowMenu("file_slots"), SensitiveIf(renpy.get_screen("file_slots") == None)]
            textbutton _("ACHIEVEMENTS\n{size=20}アチーブメント{/size}") hovered [SetVariable("option_index", 3)] action [Hide("file_slots"), ShowMenu("achievements"), SensitiveIf(renpy.get_screen("achievements") == None)]
            textbutton _("OPTIONS\n{size=20}オプション{/size}") hovered [SetVariable("option_index", 4)] action [Hide("achievements"), Hide("file_slots"), ShowMenu("preferences"), SensitiveIf(renpy.get_screen("preferences") == None)]
            if renpy.variant("pc"):
                textbutton _("HELP\n{size=20}ヘルプ{/size}") hovered [SetVariable("option_index", 5)]  action [Help("README.html"), Show(screen="dialog", message="The help file has been opened in your browser.", ok_action=Hide("dialog"))]
                textbutton _("DISCORD\n{size=20}ディスコード{/size}") hovered [SetVariable("option_index", 6)] action OpenURL("https://discord.gg/Q3CcJW4Ag2")
            textbutton _("EXTRAS\n{size=20}エクストラー{/size}") hovered [SetVariable("option_index", 7)] action Function(Extras)
            if renpy.variant("pc"):
                textbutton _("QUIT\n{size=20}クイット{/size}") hovered [SetVariable("option_index", 8)] action Quit(confirm=not main_menu)
        else:
            textbutton _("CLOSE\n{size=20}閉じる{/size}") hovered [SetVariable("option_index", 0)] action Return()
            textbutton _("LOG\n{size=20}ログ{/size}") hovered [SetVariable("option_index", 1)] action [Hide("preferences"), Hide("file_slots"), ShowMenu("history"), SensitiveIf(renpy.get_screen("history") == None)]
            textbutton _("AUTO ADVANCE  " + aa_status + "\n{size=20}オート                                                                          " + aa_status_kan + "{/size}") hovered [SetVariable("option_index", 2)] action [Preference("auto-forward", "toggle"), If(aa_status == "OFF", [SetVariable("aa_status", "ON"), SetVariable("aa_status_kan", "{size=20}オン{/size}")], [SetVariable("aa_status", "OFF"), SetVariable("aa_status_kan", "{size=20}オッフ{/size}")])]
            textbutton _("FAST FORWARD\n{size=20}早送り{/size}") hovered [SetVariable("option_index", 3)] action Skip()
            textbutton _("BOOKMARKS\n{size=20}しおり{/size}") hovered [SetVariable("option_index", 4)] action [Hide("history"), Hide("preferences"), ShowMenu("file_slots"), SensitiveIf(renpy.get_screen("file_slots") == None)]
            textbutton _("OPTIONS\n{size=20}オプション{/size}") hovered [SetVariable("option_index", 5)] action [Hide("history"), Hide("file_slots"), ShowMenu("preferences"), SensitiveIf(renpy.get_screen("preferences") == None)]
            if _in_replay:
                textbutton _("END REPLAY\n{size=20}リプレイを終了する{/size}") hovered [SetVariable("option_index", 6)] action EndReplay(confirm=True)
            else:
                textbutton _("TITLE SCREEN\n{size=20}タイトル画面{/size}") hovered [SetVariable("option_index", 6)] action MainMenu()
            if renpy.variant("pc"):
                textbutton _("HELP\n{size=20}ヘルプ{/size}") hovered [SetVariable("option_index", 7)] action [Help("README.html"), Show(screen="dialog", message="The help file has been opened in your browser.", ok_action=Hide("dialog"))]
                textbutton _("QUIT\n{size=20}クイット{/size}") hovered [SetVariable("option_index", 8)] action Quit(confirm=not main_menu) 
            
init -501 screen navigation_border():
    zorder 2500
    text _(str(option_index)) style "navigation_center_text" at navigation_transform(120, -75)
    frame at navigation_transform:
        ysize 720
        xsize 540
        background Solid("#ffffff8f")            

init -501 transform navigation_transform(xo=0,yo=0):
    on show:
        xpos -640
        ypos yo
        easeout .25 xpos 0+xo
    on hide:
        xpos 0+xo
        easein .25 xpos -640



init -1 style navigation_button is gui_button
init -1 style navigation_button_text is gui_button_text

init -1 style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")
    background "#00000000"
    hover_background "#0000008f"
    xsize 540
    ysize 75
    hover_sound gui.hover_sound
    activate_sound gui.activate_sound

init -1 style navigation_button_text:
    properties gui.button_text_properties("navigation_button")
    font "mod_assets/fonts/NotoSerifJP-Regular.otf"
    color "#000"
    hover_color "#fff"
    size 50
    line_spacing -20

init -1 style navigation_text:
    font "mod_assets/fonts/NotoSerifJP-Regular.otf"
    color "#000"
    size 50
    text_align 1.0

init -1 style navigation_center_text:
    font "mod_assets/fonts/Unitblock-mLAwm.ttf"
    color "#000"
    size 750





default -501 dynamics = random_list(bgs)[0]

init -501 screen main_menu(): 
    tag menu
    style_prefix "main_menu"
    add dynamics at bg_transform
    add "menu_art_y" at angle_t(-15)
    add "menu_art_k" at angle_t(180)
    add "menu_art_n" at angle_t(90)
    add "menu_art_s" at angle_t(15)
    add "menu_art_m"
    add "menu_art_a" at angle_t(150)
    use quick_menu

    if gui.show_name:

        vbox:
            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"
    
    add "menu_logo" 
    
    add "menu_fade"

    key "K_ESCAPE" action Quit(confirm=False)

    timer 5.0 repeat True action SetVariable("dynamics", random_list(bgs)[0])

init -501 transform angle_t(a):
    rotate a

init -501 transform bg_transform:
    alpha 0.0
    zoom 1.0
    parallel:
        linear 1.0 alpha 1.0
        3.0
        linear 1.0 alpha 0.0
        repeat
    parallel:
        easein_quint 10.0 zoom 1.2
        easein_quint 10.0 zoom 1.0
        repeat

init -501 screen game_menu():

    frame at game_menu_transform:
        ysize 800
        xsize 540
        background Solid("#ffffff8f") 

init -501 transform game_menu_transform(xo=0,yo=0):
    on show:
        xpos 1280
        ypos yo
        easeout .25 xpos 740+xo
    on hide:
        xpos 740+xo
        easein .25 xpos 1280

init -501 screen about():
    tag menu
    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")


            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")



define -1 gui.about = ""


init -1 style about_label is gui_label
init -1 style about_label_text is gui_label_text
init -1 style about_text is gui_text

init -1 style about_label_text:
    size gui.label_text_size

init -1 python:
    def FileActionMod(name, page=None, **kwargs):
        return FileAction(name)

init -501 default slot_selected = 0

init -501 screen file_slots():

    default page_name_value = FilePageNameInputValue()

    use game_menu

    fixed at game_menu_transform:
        yoffset -10
        order_reverse True
        viewport id "vp":
            mousewheel True
            draggable True
            has vbox
            null height 40

            style_prefix "slot"
            spacing gui.slot_spacing
            for i in range(99):
                $ slot = i + 1
                button:
                    action SetVariable("slot_selected", slot)
                    alternate FileDelete(slot)
                    has vbox
                    add FileScreenshot(slot) 
                    text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                        style "slot_time_text"
                    text FileSaveName(slot):
                        style "slot_name_text"
                    key "save_delete" action FileDelete(slot)
            vbar value YScrollValue(viewport="vp")
                    
        if slot_selected > 0:
            frame:
                xcenter 400
                ycenter 100
                background "#ffffff8a"
                vbox:
                    text "NAME THIS BOOKMARK" font "mod_assets/fonts/Unitblock-mLAwm.ttf"
                    input default FileSaveName(slot_selected) value VariableInputValue("save_name") length 24 font "mod_assets/fonts/Unitblock-mLAwm.ttf"
                    hbox:
                        if not main_menu:
                            button:
                                background "#1eff0080"
                                text "SAVE" font "mod_assets/fonts/Unitblock-mLAwm.ttf"
                                action FileSave(slot_selected)
                        button:
                            background "#ff000080"
                            text "DELETE" font "mod_assets/fonts/Unitblock-mLAwm.ttf"
                            action FileDelete(slot_selected)
                        button:
                            background "#ffffff80"
                            text "LOAD" font "mod_assets/fonts/Unitblock-mLAwm.ttf"
                            action FileLoad(slot_selected)

init -1 style slot_button is gui_button
init -1 style slot_button_text is gui_button_text
init -1 style slot_time_text is slot_button_text
init -1 style slot_name_text is slot_button_text

init -1 style page_button:
    properties gui.button_properties("page_button")

init -1 style page_button_text:
    properties gui.button_text_properties("page_button")
    outlines []

init -1 style slot_button:
    properties gui.button_properties("slot_button")

init -1 style slot_button_text:
    properties gui.button_text_properties("slot_button")
    color "#666"
    outlines []

init -501 screen preferences():

    use game_menu
        
    fixed at game_menu_transform:
        yoffset -10
        order_reverse True
        viewport id "vp":
            mousewheel True
            draggable True
            has vbox
            null height 40
            if config.has_music:
                style_prefix "slider"
                label _("Music Volume")
                hbox:
                    bar value Preference("music volume") hovered [SetLocalVariable("settinginfo", "The volume of the music within the game."), SetLocalVariable("settingdef", "Default: 75%")] unhovered [SetLocalVariable("settinginfo", "Hover over an option to view info about it."), SetLocalVariable("settingdef", "")] xsize 440
            if config.has_sound:
                style_prefix "slider"
                label _("Sound Volume")
                hbox:
                    bar value Preference("sound volume") hovered [SetLocalVariable("settinginfo", "The volume of the sound within the game."), SetLocalVariable("settingdef", "Default: 75%")] unhovered [SetLocalVariable("settinginfo", "Hover over an option to view info about it."), SetLocalVariable("settingdef", "")] xsize 440
            if config.has_voice:
                style_prefix "slider"
                label _("Voice Volume")
                hbox:
                    bar range 2.00 value Preference("voice volume") hovered [SetLocalVariable("settinginfo", "The volume of the voicelines within the game."), SetLocalVariable("settingdef", "Default: 150%")] unhovered [SetLocalVariable("settinginfo", "Hover over an option to view info about it."), SetLocalVariable("settingdef", "")] xsize 440
                    if config.sample_voice:
                        textbutton _("Test") action Play("voice", config.sample_voice)
            if config.has_music or config.has_sound or config.has_voice:
                textbutton _("Reset"):
                    action [Preference("music volume", 0.75), Preference("sound volume", 0.75), Preference("voice volume", 1.50)] 
                    hovered SetLocalVariable("settinginfo", "Resets the volume settings to default.") unhovered SetLocalVariable("settinginfo", "Hover over an option to view info about it.")
                    style "ui_text"
            yoffset -10
            if renpy.variant("pc"):
                vbox:
                    style_prefix "radio"
                    label _("Display")
                    textbutton _("Window") action Preference("display", "window") hovered [SetLocalVariable("settinginfo", "How the game's window is displayed on your screen."), SetLocalVariable("settingdef", "Default: Window")] unhovered [SetLocalVariable("settinginfo", "Hover over an option to view info about it."), SetLocalVariable("settingdef", "")]
                    textbutton _("Fullscreen") action Preference("display", "fullscreen") hovered [SetLocalVariable("settinginfo", "How the game's window is displayed on your screen."), SetLocalVariable("settingdef", "Default: Window")] unhovered [SetLocalVariable("settinginfo", "Hover over an option to view info about it."), SetLocalVariable("settingdef", "")]
            vbox:
                style_prefix "check"
                label _("Fast Forward")
                textbutton _("Unseen Text") hovered [SetLocalVariable("settinginfo", "Fast Forward skips over text you haven't seen yet"), SetLocalVariable("settingdef", "Default: False")] action Preference("skip", "toggle")
                textbutton _("After Choices") hovered [SetLocalVariable("settinginfo", "Fast Forward persists after you make a choice"), SetLocalVariable("settingdef", "Default: False")] action Preference("after choices", "toggle")
            # vbox:
            #     style_prefix "radio"
            #     label _("Language")
            #     textbutton "English" action Language("english")
            #     textbutton "日本語" action Language("japanese")
            null height (4 * gui.pref_spacing)
            hbox:
                style_prefix "slider"
                box_wrap True
                vbox:
                    label _("Information")
                    text _("[settinginfo]")
                    text _("[settingdef]")
    text "v[config.version]":
        xalign 1.0 yalign 1.0
        xoffset -10 yoffset -10

init -1 style pref_label is gui_label
init -1 style pref_label_text is gui_label_text
init -1 style pref_vbox is vbox

init -1 style radio_label is pref_label
init -1 style radio_label_text is pref_label_text
init -1 style radio_button is gui_button
init -1 style radio_button_text is gui_button_text
init -1 style radio_vbox is pref_vbox

init -1 style check_label is pref_label
init -1 style check_label_text is pref_label_text
init -1 style check_button is gui_button
init -1 style check_button_text is gui_button_text
init -1 style check_vbox is pref_vbox

init -1 style slider_label is pref_label
init -1 style slider_label_text is pref_label_text
init -1 style slider_slider is gui_slider
init -1 style slider_button is gui_button
init -1 style slider_button_text is gui_button_text
init -1 style slider_pref_vbox is pref_vbox

init -1 style mute_all_button is check_button
init -1 style mute_all_button_text is check_button_text

init -1 style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 2

init -1 style pref_label_text:
    font "mod_assets/fonts/Unitblock-mLAwm.ttf"
    size 24
    color "#fff"
    outlines [(3, "#585858", 0, 0), (1, "#585858", 1, 1)]
    yalign 1.0

init -1 style pref_vbox:
    xsize 225

init -1 style radio_vbox:
    spacing gui.pref_button_spacing

init -1 style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/check_[prefix_]foreground.png"

init -1 style radio_button_text:
    properties gui.button_text_properties("radio_button")
    font "gui/font/Halogen.ttf"
    outlines []

init -1 style check_vbox:
    spacing gui.pref_button_spacing

init -1 style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

init -1 style check_button_text:
    properties gui.button_text_properties("check_button")
    font "gui/font/Halogen.ttf"
    outlines []

init -1 style slider_slider:
    xsize 350

init -1 style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 10

init -1 style slider_button_text:
    properties gui.button_text_properties("slider_button")

init -1 style slider_vbox:
    xsize 450

init -1 style ui_text:
    font "mod_assets/fonts/Unitblock-mLAwm.ttf"








init -501 screen history():
    predict False

    use game_menu

    fixed at game_menu_transform:
        viewport id "vp":
            mousewheel True
            draggable True
            has vbox
            null height 40
            xmaximum 300
            xoffset -200
            style_prefix "history"

            for h in _history_list:

                window:
                    

                    has fixed:
                        yfit True

                    if h.who:

                        label h.who:
                            style "history_name"



                            if "color" in h.who_args:
                                text_color h.who_args["color"]

                    text h.what
                    if renpy.exists("mod_assets/voicelines/[h.id].ogg"):
                        textbutton "PLAY" action Play("voice", "mod_assets/voicelines/[h.id].ogg")

            if not _history_list:
                label _("The dialogue history is empty.")


init -1 style history_window is empty

init -1 style history_name is gui_label
init -1 style history_name_text is gui_label_text
init -1 style history_text is gui_text

init -1 style history_text is gui_text

init -1 style history_label is gui_label
init -1 style history_label_text is gui_label_text

init -1 style history_window:
    xfill True
    ysize gui.history_height

init -1 style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

init -1 style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

init -1 style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

init -1 style history_label:
    xfill True

init -1 style history_label_text:
    xalign 0.5


init -501 screen name_input(message, ok_action):


    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"
    key "K_RETURN" action [Play("sound", gui.activate_sound), ok_action]

    frame:

        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label _(message):
            style "confirm_prompt"
            xalign 0.5

        input default "[save_name]" value VariableInputValue("save_name") length 24






        hbox:
            xalign 0.5
            spacing 100

            textbutton _("OK") action ok_action

init -501 screen dialog(message, ok_action):


    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label _(message):
            style "confirm_prompt"
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 100

            textbutton _("OK") action ok_action

init 499 image confirm_glitch:
    "gui/overlay/confirm_glitch.png"
    pause 0.02
    "gui/overlay/confirm_glitch2.png"
    pause 0.02
    repeat

init -501 screen confirm(message, yes_action, no_action):


    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:
        
        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label _(message):
            style "confirm_prompt"
            xalign 0.5

        hbox:
            xalign 0.5
            spacing 100

            textbutton _("Yes") action yes_action
            textbutton _("No") action no_action





init -1 style confirm_frame is gui_frame
init -1 style confirm_prompt is gui_prompt
init -1 style confirm_prompt_text is gui_prompt_text
init -1 style confirm_button is gui_medium_button
init -1 style confirm_button_text is gui_medium_button_text

init -1 style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

init -1 style confirm_prompt_text:
    color "#000"
    outlines []
    text_align 0.5
    layout "subtitle"

init -1 style confirm_button:
    properties gui.button_properties("confirm_button")
    hover_sound gui.hover_sound
    activate_sound gui.activate_sound

init -1 style confirm_button_text is navigation_button_text:
    properties gui.button_text_properties("confirm_button")








init -501 screen fake_skip_indicator():
    use skip_indicator

init -501 screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        has hbox:
            spacing 6

        text _("Skipping")

        text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
        text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
        text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"



transform -1 delayed_blink(delay, cycle):
    alpha .5

    pause delay
    block:

        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


init -1 style skip_frame is empty
init -1 style skip_text is gui_text
init -1 style skip_triangle is skip_text

init -1 style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

init -1 style skip_text:
    size gui.notify_text_size

init -1 style skip_triangle:


    font "DejaVuSans.ttf"









init -501 screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text message

    timer 3.25 action Hide('notify')


transform -1 notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


init -1 style notify_frame is empty
init -1 style notify_text is gui_text

init -1 style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

init -1 style notify_text:
    size gui.notify_text_size