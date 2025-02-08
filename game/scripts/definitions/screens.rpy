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
    font "mod_assets/fonts/NotoSerifJP-Regular.otf"
    color "#fff"
    hover_color "#bbbbbb"
    size 35
    outlines [(1, "#585858", 0, 0), (1, "#585858", 1, 1)]

init -1 style choice_text is default:
    font "mod_assets/fonts/NotoSerifJP-Regular.otf"
    color "#fff"
    outlines [(1, "#585858", 0, 0), (1, "#585858", 1, 1)]

init -1 python:
    def RigMouse():
        currentpos = renpy.get_mouse_pos()
        targetpos = [640, 345]
        if currentpos[1] < targetpos[1]:
            renpy.display.draw.set_mouse_pos((currentpos[0] * 9 + targetpos[0]) / 10.0, (currentpos[1] * 9 + targetpos[1]) / 10.0)

init -501 screen quick_menu():
    if quick_menu:
        frame:
            background Solid("#00000056")
            vbox:
                imagebutton idle "mod_assets/gui/menu_button.png" action [SetVariable("option_index", 0), ShowMenu("navigation", _layer="textbox"), SensitiveIf(renpy.get_screen("navigation") == None)]
                if not main_menu and can_cont:
                    if preferences.afm_enable:
                        imagebutton idle "mod_assets/gui/auto_on.png" action Preference("auto-forward", "disable")
                    else:
                        imagebutton idle "mod_assets/gui/auto_off.png" action Preference("auto-forward", "enable")
        key "K_TAB" action Preference("auto-forward", "toggle")
        key "K_ESCAPE" action [SetVariable("option_index", 0), ShowMenu("navigation", _layer="textbox"), SensitiveIf(renpy.get_screen("navigation") == None)]

default -1 quick_menu = True

init -1 python:
    def StartGame():
        renpy.jump_out_of_context("start")
    def Act1():
        renpy.jump_out_of_context("act1")
    def Act2():
        renpy.jump_out_of_context("act2")
    def Act2_alt():
        renpy.jump_out_of_context("act2_alt")
    def Act3():
        renpy.jump_out_of_context("act3")
    def Extras():
        renpy.jump_out_of_context("extras")
    def Developer():
        renpy.jump_out_of_context("dev")

default option_index = 0
init -501 screen navigation():
    
    use navigation_border
    vbox at navigation_transform(0, 80):
        style_prefix "navigation"
        spacing 0
        if main_menu:
            button:
                at button_transform
                text "CLOSE" xalign 0.1 yalign 0.5 style "navigation_button_text"
                text "閉じる" xalign 0.1 yalign 1.1 style "navigation_kan" 
                hovered [SetVariable("option_index", 0)] 
                action [Hide("achievements", _layer="textbox"), Hide("preferences", _layer="textbox"), Hide("file_slots", _layer="textbox"), Hide("navigation", _layer="textbox")]
            button:
                at button_transform
                text "ACT SELECT" xalign 0.1 yalign 0.5 style "navigation_button_text"
                text "アクト選択へ" xalign 0.1 yalign 1.1 style "navigation_kan" 
                hovered [SetVariable("option_index", 1)] 
                action [Hide("achievements", _layer="textbox"), Hide("preferences", _layer="textbox"), Hide("file_slots", _layer="textbox"), Hide("navigation", _layer="textbox"), Show("acts", _layer="textbox")]
            button:
                at button_transform
                text "BOOKMARKS" xalign 0.1 yalign 0.5 style "navigation_button_text"
                text "しおり" xalign 0.1 yalign 1.1 style "navigation_kan" 
                hovered [SetVariable("option_index", 2)] 
                action [Hide("achievements", _layer="textbox"), Hide("preferences", _layer="textbox"), ShowMenu("file_slots", _layer="textbox"), SensitiveIf(renpy.get_screen("file_slots") == None)]
            button:
                at button_transform
                text "ACHIEVEMENTS" xalign 0.1 yalign 0.5 style "navigation_button_text"
                text "アチーブメント" xalign 0.1 yalign 1.1 style "navigation_kan" 
                hovered [SetVariable("option_index", 3)] 
                action [Hide("preferences", _layer="textbox"), Hide("file_slots", _layer="textbox"), ShowMenu("achievements", _layer="textbox"), SensitiveIf(renpy.get_screen("achievements") == None)]
            button:
                at button_transform
                text "OPTIONS" xalign 0.1 yalign 0.5 style "navigation_button_text"
                text "オプション" xalign 0.1 yalign 1.1 style "navigation_kan" 
                hovered [SetVariable("option_index", 4)] 
                action [Hide("achievements", _layer="textbox"), Hide("file_slots", _layer="textbox"), ShowMenu("preferences", _layer="textbox"), SensitiveIf(renpy.get_screen("preferences") == None)]
            if renpy.variant("pc"):
                button:
                    at button_transform
                    text "HELP" xalign 0.1 yalign 0.5 style "navigation_button_text"
                    text "ヘルプ" xalign 0.1 yalign 1.1 style "navigation_kan" 
                    hovered [SetVariable("option_index", 5)] 
                    action [Help("README.html"), Show(screen="dialog", message="The help file has been opened in your browser.", ok_action=Hide("dialog"), _layer="textbox")]
                button:
                    at button_transform
                    text "DISCORD" xalign 0.1 yalign 0.5 style "navigation_button_text"
                    text "ディスコード" xalign 0.1 yalign 1.1 style "navigation_kan" 
                    hovered [SetVariable("option_index", 6)] 
                    action OpenURL("https://discord.gg/Q3CcJW4Ag2")
            button:
                at button_transform
                text "EXTRAS" xalign 0.1 yalign 0.5 style "navigation_button_text"
                text "エクストラー" xalign 0.1 yalign 1.1 style "navigation_kan" 
                hovered [SetVariable("option_index", 7)] 
                action Function(Extras)
            if renpy.variant("pc"):
                button:
                    at button_transform
                    text "QUIT" xalign 0.1 yalign 0.5 style "navigation_button_text"
                    text "クイット" xalign 0.1 yalign 1.1 style "navigation_kan" 
                    hovered [SetVariable("option_index", 8)] 
                    action Quit(confirm=not main_menu)
        else:
            button:
                at button_transform
                text "CLOSE" xalign 0.1 yalign 0.5 style "navigation_button_text"
                text "閉じる" xalign 0.1 yalign 1.1 style "navigation_kan" 
                hovered [SetVariable("option_index", 0)] 
                action [SetVariable("selected_item", "Nothing\n{size=20}何も無い{/size}"), Return()]
            button:
                at button_transform
                text "LOG" xalign 0.1 yalign 0.5 style "navigation_button_text"
                text "ログ" xalign 0.1 yalign 1.1 style "navigation_kan" 
                hovered [SetVariable("option_index", 1)] 
                action [Hide("preferences", _layer="textbox"), Hide("file_slots", _layer="textbox"), Hide("inventory_view", _layer="textbox"), ShowMenu("history", _layer="textbox"), SensitiveIf(renpy.get_screen("history") == None)]
            button:
                at button_transform
                text "INVENTORY" xalign 0.1 yalign 0.5 style "navigation_button_text"
                text "在庫" xalign 0.1 yalign 1.1 style "navigation_kan" 
                hovered [SetVariable("option_index", 2)] 
                action [Hide("preferences", _layer="textbox"), Hide("file_slots", _layer="textbox"), Hide("history", _layer="textbox"), ShowMenu("inventory_view", _layer="textbox"), SensitiveIf(renpy.get_screen("inventory_view") == None)]
            button:
                at button_transform
                text "FAST FORWARD" xalign 0.1 yalign 0.5 style "navigation_button_text"
                text "早送り" xalign 0.1 yalign 1.1 style "navigation_kan" 
                hovered [SetVariable("option_index", 3)] 
                action Skip()
            button:
                at button_transform
                text "BOOKMARKS" xalign 0.1 yalign 0.5 style "navigation_button_text"
                text "しおり" xalign 0.1 yalign 1.1 style "navigation_kan" 
                hovered [SetVariable("option_index", 4)] 
                action [Hide("history", _layer="textbox"), Hide("preferences", _layer="textbox"), Hide("inventory_view", _layer="textbox"), ShowMenu("file_slots", _layer="textbox"), SensitiveIf(renpy.get_screen("file_slots") == None)]
            button:
                at button_transform
                text "OPTIONS" xalign 0.1 yalign 0.5 style "navigation_button_text"
                text "オプション" xalign 0.1 yalign 1.1 style "navigation_kan" 
                hovered [SetVariable("option_index", 5)] 
                action [Hide("history", _layer="textbox"), Hide("file_slots", _layer="textbox"), Hide("inventory_view", _layer="textbox"), ShowMenu("preferences", _layer="textbox"), SensitiveIf(renpy.get_screen("preferences") == None)]
            if _in_replay:
                button:
                    at button_transform
                    text "END REPLAY" xalign 0.1 yalign 0.5 style "navigation_button_text"
                    text "リプレイを終了する" xalign 0.1 yalign 1.1 style "navigation_kan" 
                    hovered [SetVariable("option_index", 6)] 
                    action EndReplay(confirm=True)
            else:
                button:
                    at button_transform
                    text "TITLE SCREEN" xalign 0.1 yalign 0.5 style "navigation_button_text"
                    text "タイトル画面" xalign 0.1 yalign 1.1 style "navigation_kan" 
                    hovered [SetVariable("option_index", 6)] 
                    action MainMenu()
            if renpy.variant("pc"):
                button:
                    at button_transform
                    text "HELP" xalign 0.1 yalign 0.5 style "navigation_button_text"
                    text "ヘルプ" xalign 0.1 yalign 1.1 style "navigation_kan" 
                    hovered [SetVariable("option_index", 7)] 
                    action [Help("README.html"), Show(screen="dialog", message="The help file has been opened in your browser.", ok_action=Hide("dialog"), _layer="textbox")]
                button:
                    at button_transform
                    text "QUIT" xalign 0.1 yalign 0.5 style "navigation_button_text"
                    text "クイット" xalign 0.1 yalign 1.1 style "navigation_kan" 
                    hovered [SetVariable("option_index", 8)] 
                    action Quit(confirm=not main_menu) 

init -501 screen acts():
    use navigation_border
    vbox at navigation_transform(0, 80):
        style_prefix "navigation"
        spacing 0
        button:
            at button_transform
            text "BACK" xalign 0.1 yalign 0.5 style "navigation_button_text" 
            text "バック" xalign 0.1 yalign 1.1 style "navigation_kan" 
            hovered [SetVariable("option_index", 0)] 
            action [Hide("acts", _layer="textbox"), Show("navigation", _layer="textbox")]
        button:
            at button_transform
            text "PROLOGUE" xalign 0.1 yalign 0.5 style "navigation_button_text"
            text "プロローグ" xalign 0.1 yalign 1.1 style "navigation_kan" 
            hovered [SetVariable("option_index", 1)] 
            action Function(StartGame)
        button:
            at button_transform
            text "ACT 1" xalign 0.1 yalign 0.5 style "navigation_button_text"
            text "アクト１" xalign 0.1 yalign 1.1 style "navigation_kan" 
            hovered [SetVariable("option_index", 2)] 
            action If(achievement.has("newfriends"), Function(Act1), Show(screen="dialog", message="Complete the Prologue first.", ok_action=Hide("dialog")))
        button:
            at button_transform
            text "ACT 2" xalign 0.1 yalign 0.5 style "navigation_button_text"
            text "アクト２" xalign 0.1 yalign 1.1 style "navigation_kan" 
            hovered [SetVariable("option_index", 3)] 
            action If(achievement.has("act1fin"), [Hide("acts", _layer="textbox"), Show("act2choice", _layer="textbox")], Show(screen="dialog", message="Complete Act 1 first.", ok_action=Hide("dialog")))
        button:
            at button_transform
            text "ACT 3" xalign 0.1 yalign 0.5 style "navigation_button_text"
            text "アクト３" xalign 0.1 yalign 1.1 style "navigation_kan" 
            hovered [SetVariable("option_index", 4)] 
            action If(achievement.has("act2fin"), Function(Act3), Show(screen="dialog", message="Complete Act 2 first.", ok_action=Hide("dialog")))
        if config.developer:
            button:
                at button_transform
                text "DEVELOPER MODE" xalign 0.1 yalign 0.5 style "navigation_button_text"
                text "デベロッパーモード" xalign 0.1 yalign 1.1 style "navigation_kan" 
                hovered [SetVariable("option_index", 5)] 
                action Function(Developer)

default unlock_jp = ""
default unlock_en = ""
init -501 screen act2choice():
    zorder 3000
    frame:
        xysize (1280, 720)
        background Solid("#646464b9")
    style_prefix "explore"
    text "道を選んで下さい\nCHOOSE YOUR PATH" xcenter 640 ycenter 40
    button xcenter 360 ycenter 360 xysize (500, 300) hovered If("Hidden Girl Revealed" not in persistent.choices_made, [SetVariable("unlock_jp", "この道を開くために、彼女に質問する"), SetVariable("unlock_en", "ASK HER THE QUESTION TO UNLOCK")]) unhovered [SetVariable("unlock_jp", ""), SetVariable("unlock_en", "")] action If("Hidden Girl Revealed" in persistent.choices_made, Function(Act2), NullAction())
    text "知られざる少女\nREVEALED" xcenter 360 ycenter 360
    text "[unlock_jp]" xcenter 640 ycenter 190
    text "[unlock_en]" xcenter 640 ycenter 530
    button xcenter 920 ycenter 360 xysize (500, 300) hovered If("Hidden Girl Kept Secret" not in persistent.choices_made, [SetVariable("unlock_jp", "この道を開くために、彼女に質問してはいけない"), SetVariable("unlock_en", "DON'T ASK HER THE QUESTION TO UNLOCK")]) unhovered [SetVariable("unlock_jp", ""), SetVariable("unlock_en", "")] action If("Hidden Girl Kept Secret" in persistent.choices_made, Function(Act2_alt), NullAction())
    text "隠れた少女\nHIDDEN" xcenter 920 ycenter 360
    button xcenter 640 ycenter 695 xysize (1280, 100) action [Hide("act2choice", _layer="textbox"), Show("acts", _layer="textbox")]
    text "バック\nBACK" xcenter 640 ycenter 680

init -501 image nav_f:
    "mod_assets/gui/nav_f.png"
    alpha 0.5

init -501 image game_menu_f:
    "mod_assets/gui/game_menu_f.png"
    alpha 0.5

init -501 screen navigation_border():
    zorder 2500
    frame at navigation_transform:
        ysize 720
        xsize 540
        background Solid("#ffffff")
        text _(str(option_index)) style "navigation_center_text" yalign 0.5 xalign 0.5
    add "nav_f" at navigation_transform

init -501 transform navigation_transform(xo=0,yo=0):
    on show:
        xpos -640
        ypos yo
        easeout .25 xpos xo
    on hide:
        xpos xo
        easein .25 xpos -640

init -501 transform button_transform:
    on hover:
        xsize 540
        ysize 80
        linear 0.25 xsize 550 ysize 90
    on idle:
        xsize 550
        ysize 90
        linear 0.25 xsize 540 ysize 80



init -1 style navigation_button is gui_button

init -1 style navigation_button:
    size_group "navigation"
    background "#ffffff00"
    hover_background "#000"
    xsize 540
    ysize 80
    hover_sound gui.hover_sound
    activate_sound gui.activate_sound
    yanchor 1.0

init -1 style navigation_button_text:
    font "mod_assets/fonts/ThatSoundsGreat-yYLE3.ttf"
    color "#000"
    hover_color "#fff"
    outlines [(0, "#58585800", 0, 0), (0, "#58585800", 0, 0)]
    size 34
    text_align 0.0

init -1 style navigation_text:
    font "mod_assets/fonts/ThatSoundsGreat-yYLE3.ttf"
    color "#000"
    outlines [(0, "#58585800", 0, 0), (0, "#58585800", 0, 0)]
    size 50

init -1 style navigation_kan:
    font "mod_assets/fonts/NotoSerifJP-Regular.otf"
    color "#00000080"
    hover_color "#ffffff80"
    outlines [(0, "#58585800", 0, 0), (0, "#58585800", 0, 0)]
    size 20

init -1 style navigation_center_text:
    font "mod_assets/fonts/ThatSoundsGreat-yYLE3.ttf"
    color "#00000010"
    outlines [(0, "#58585800", 0, 0), (0, "#58585800", 0, 0)]
    size 700
    text_align 0.5





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
        ysize 720
        xsize 540
        background Solid("#ffffff")
    add "game_menu_f" at game_menu_transform

init -501 transform game_menu_transform(xo=0,yo=0):
    on show:
        xpos 1280
        ypos yo
        easeout .25 xpos 740+xo
    on hide:
        xpos 740+xo
        easein .25 xpos 1280

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
                    has vbox
                    add FileScreenshot(slot) 
                    text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("EMPTY")):
                        style "slot_time_text"
                    text FileSaveName(slot):
                        style "slot_name_text"
            vbar value YScrollValue(viewport="vp")
                    
        if slot_selected > 0:
            frame:
                xcenter 400
                ycenter 100
                background "#8181818a"
                vbox:
                    xalign 0.5
                    text "しおりの名前\nNAME OF BOOKMARK" font "mod_assets/fonts/NotoSerifJP-Regular.otf" size 10 xalign 0.5 text_align 0.5
                    input default FileSaveName(slot_selected) value VariableInputValue("save_name") length 24 font "mod_assets/fonts/NotoSerifJP-Regular.otf"
                    hbox:
                        if not main_menu:
                            button:
                                background "#1eff0080" 
                                text "セーブ\nSAVE" font "mod_assets/fonts/NotoSerifJP-Regular.otf" size 10 text_align 0.5 ypos -5
                                action FileSave(slot_selected)
                        button:
                            background "#ff000080"
                            text "デリート\nDELETE" font "mod_assets/fonts/NotoSerifJP-Regular.otf" size 10 text_align 0.5 ypos -5
                            action FileDelete(slot_selected)
                        button:
                            background "#ffffff80"
                            text "ロード\nLOAD" font "mod_assets/fonts/NotoSerifJP-Regular.otf" size 10 text_align 0.5 ypos -5
                            action FileLoad(slot_selected)

default selected_item = "Nothing"
default JP_item_name = "何も無い"
default item_desc = ""
init -501 screen inventory_view(item_action=None):
    use game_menu
    style_prefix "inventory"
    fixed at game_menu_transform:
        frame:
            ysize 200
            xsize 540
            background Solid("#00000090")
        vbox:
            
            label "[selected_item]\n{size=20}[JP_item_name]{/size}"
            text item_desc
            viewport id "vp":
                yoffset 100
                grid 5 100:
                    for item in range(len(inventory)):
                        button:
                            background "mod_assets/inventory/[inventory[item]].png"
                            hover_foreground Solid("#ffffff59")
                            xysize (100, 100)
                            action [SetVariable("selected_item", inventory[item]), SetVariable("JP_item_name", JPitems[item]), SetVariable("item_desc", items_desc[item])]
        if item_action is not None:
            textbutton "Use [selected_item]\n{size=15}使用[JP_item_name]{/size}" yalign 0.95 action item_action


init -1 style slot_button is gui_button
init -1 style slot_button_text is gui_button_text
init -1 style slot_time_text is slot_button_text
init -1 style slot_name_text is slot_button_text

init -1 style inventory_label:
    bottom_margin 2

init -1 style inventory_label_text:
    font "mod_assets/fonts/NotoSerifJP-Regular.otf"
    size 34
    color "#fff"
    line_spacing -15
    outlines [(3, "#585858", 0, 0), (1, "#585858", 1, 1)]
    yalign 1.0

init -1 style inventory_text:
    font "mod_assets/fonts/NotoSerifJP-Regular.otf"
    size 15
    color "#fff"

init -1 style inventory_button_text:
    font "mod_assets/fonts/NotoSerifJP-Regular.otf"
    color "#000"
    hover_color "#a8a8a8"
    size 35
    outlines [(1, "#58585800", 0, 0), (1, "#58585800", 1, 1)]

init -1 style page_button:
    properties gui.button_properties("page_button")

init -1 style page_button_text:
    properties gui.button_text_properties("page_button")
    outlines []

init -1 style slot_button:
    properties gui.button_properties("slot_button")
    background "mod_assets/gui/slot_idle_background.png"
    hover_background "mod_assets/gui/slot_hover_background.png"

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
                hbox:
                    label "Music Volume" yalign 0.5
                    text "音楽ボリューム" yalign 0.75 style "pref_JP_label_text"
                hbox:
                    bar value Preference("music volume")
                hbox:
                    label "Ambience Volume" yalign 0.5
                    text "環境音ボリューム" yalign 0.75 style "pref_JP_label_text"
                hbox:
                    bar value Preference("ambience volume")
            if config.has_sound:
                style_prefix "slider"
                hbox:
                    label "Sound Volume" yalign 0.5
                    text "物音ボリューム" yalign 0.75 style "pref_JP_label_text"
                hbox:
                    bar value Preference("sound volume")
            if config.has_voice:
                style_prefix "slider"
                hbox:
                    label "Voice Volume" yalign 0.5
                    text "声ボリューム" yalign 0.75 style "pref_JP_label_text"
                hbox:
                    bar value Preference("voice volume")
                    if config.sample_voice:
                        textbutton _("Test") yalign 0.5 action Play("voice", config.sample_voice)
            if config.has_music or config.has_sound or config.has_voice:
                style_prefix "slider"
                textbutton _("Reset") action [Preference("music volume", 0.75), Preference("sound volume", 0.75), Preference("voice volume", 1.00), Preference("ambience volume", 0.75)] 
            yoffset -10
            if renpy.variant("pc"):
                vbox:
                    style_prefix "radio"
                    hbox:
                        label "Display" yalign 0.5
                        text "ディスプレイ" yalign 0.75 style "pref_JP_label_text"
                    textbutton _("Window") action Preference("display", "window")
                    textbutton _("Fullscreen") action Preference("display", "fullscreen")
            vbox:
                xsize 440
                style_prefix "check"
                hbox:
                    label "Fast Forward" yalign 0.5
                    text "早送り" yalign 0.75 style "pref_JP_label_text"
                textbutton _("Unseen Text") action Preference("skip", "toggle")
                textbutton _("After Choices") action Preference("after choices", "toggle")
            vbox:
                xsize 440
                style_prefix "radio"
                hbox:
                    label "Text Language" yalign 0.5
                    text "文字言語" yalign 0.75 style "pref_JP_label_text"
                textbutton "English" action Language(None)
                textbutton "日本語" action Language("japanese")
            vbox:
                xsize 440
                style_prefix "radio"
                hbox:
                    label "Voice Language" yalign 0.5
                    text "声言語" yalign 0.75 style "pref_JP_label_text"
                for lang in lang_list: 
                    textbutton lang[lang.rindex('\\')+1:] action SetVariable("persistent.voice_lang", lang[lang.rindex('\\')+1:])
            null height (4 * gui.pref_spacing)

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
    font "mod_assets/fonts/ThatSoundsGreat-yYLE3.ttf"
    size 24
    color "#000"
    outlines [(3, "#58585800", 0, 0), (1, "#58585800", 1, 1)]
    yalign 1.0

init -1 style pref_JP_label_text:
    font "mod_assets/fonts/NotoSerifJP-Regular.otf"
    size 15
    color "#00000080"
    outlines [(3, "#58585800", 0, 0), (1, "#58585800", 1, 1)]
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
    font "mod_assets/fonts/NotoSerifJP-Regular.otf"
    color "#000"
    hover_color "#a8a8a8"
    outlines []

init -1 style check_vbox:
    spacing gui.pref_button_spacing

init -1 style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

init -1 style check_button_text:
    properties gui.button_text_properties("check_button")
    font "mod_assets/fonts/NotoSerifJP-Regular.otf"
    color "#000"
    hover_color "#a8a8a8"
    outlines [(3, "#58585800", 0, 0), (1, "#58585800", 1, 1)]

init -1 style slider_slider:
    xsize 440

init -1 style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 10

init -1 style slider_button_text:
    properties gui.button_text_properties("slider_button")
    font "mod_assets/fonts/NotoSerifJP-Regular.otf"
    color "#000"
    hover_color "#a8a8a8"
    outlines [(3, "#58585800", 0, 0), (1, "#58585800", 1, 1)]

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
    font "mod_assets/fonts/NotoSerifJP-Regular.otf"

init -1 style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")
    font "mod_assets/fonts/NotoSerifJP-Regular.otf"

init -1 style history_label:
    xfill True

init -1 style history_label_text:
    xalign 0.5

init -501 screen dialog(message, ok_action):


    modal True

    zorder 200
    layer "textbox"

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

            textbutton "オーケー\n{size=15}OK{/size}" action ok_action

init -501 screen confirm(message, yes_action, no_action):


    modal True

    zorder 200
    layer "textbox"

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

            textbutton "はい\n{size=15}YES{/size}" action yes_action
            textbutton "いいえ\n{size=15}NO{/size}" action no_action





init -1 style confirm_frame is gui_frame
init -1 style confirm_prompt is gui_prompt
init -1 style confirm_prompt_text is gui_prompt_text
init -1 style confirm_button is gui_medium_button
init -1 style confirm_button_text is gui_medium_button_text

init -1 style confirm_frame:
    background Frame("mod_assets/gui/frame.png", gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

init -1 style confirm_prompt_text:
    color "#000"
    outlines []
    text_align 0.5
    layout "subtitle"
    font "mod_assets/fonts/NotoSerifJP-Regular.otf"

init -1 style confirm_button:
    properties gui.button_properties("confirm_button")
    hover_sound gui.hover_sound
    activate_sound gui.activate_sound

init -1 style confirm_button_text is navigation_button_text:
    properties gui.button_text_properties("confirm_button")
    font "mod_assets/fonts/NotoSerifJP-Regular.otf"








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