# Really recommend you have assets for these (the Ren'Py Engine logo is easy to find in the SDK):
define audio.CRED_MUSIC = "bgm/m1.ogg"
image CRED_MODLOGO = "gui/logo.png"
image CRED_BACKGROUND = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0, loop=False)
image CRED_ENGINELOGO = "mod_assets/renpylogo.png"

default _show_skip_prompt = False
# default credit_xoffset = -275 (Change/uncomment this and the two lines using it to move the credits left or right.)

transform scroll_credits(credit_height=256):
    subpixel True
    yoffset config.screen_height
    linear 224.0 yoffset -credit_height # Adjust for scroll duration/speed depending on how many entries there are + how long credits BGM is

transform skip_prompt_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    4.0
    linear 0.5 alpha 0.0
define SECTION = -1
init python:
    SECTION_COLORS = [
        "#fff",
        "#fff",
        "#78dafc",
        "#f7a8e6",
        "#9e80f9",
        "#80ebf9",
        "#fff",
        "#7ceccf"
    ]

    SPACER = ("", 20, "#000")

    def section(header, names, current_color):
        entries = []

        if header.startswith("~"):
            global SECTION
            SECTION += 1
            entries.append((header.strip("~"), 25, "#fff"))
            current_color = SECTION_COLORS[SECTION] if SECTION < len(SECTION_COLORS) else "#ffe066"


        else:
            entries.append((header, 20, current_color))

        entries += [(name, 15, "#fff") for name in names]
        entries.append(SPACER)
        
        return entries, current_color

    RAW_CREDITS = [ # This is where your credits go!
        ("~{u}ORIGINAL GAME | オリジナルゲームのチーマ{/u}~", ["Team Salvato | チームサルヴァート"]),
        ("~{u}DIRECTOR | ディレクター{/u}~", ["Lorekeeper49 | ロアキーパー４９"]),
        ("~{u}VOICE ACTING | 声優{/u}~", []),
        ("SAKURA TAIYEN | 桜隊円", ["Lorekeeper49 | ロアキーパー４９"]),
        ("MURIKO MONIKA | 無理高モニカ", ["Willow Redwood"]),
        ("SHINAMONPAN SAYORI | シナモンパン佐代里", ["???"]),
        ("LUNA NATSUKI | ルナ菜月", ["???"]),
        ("YANDERE YURI | ヤンデレ百合", ["???"]),
        ("YANDERE LILLY | ヤンデレリリー", ["???"]),
        ("SAKURA KOTONOHA | 桜言葉", ["???"]),
        ("KAMIYAMA ITSOMI | 神山イツォミ", ["???"]),
        ("KAMIYAMA KIRINANI | 神山霧何", ["???"]),
        ("KAMIYAMA HANATO | 神山華翔", ["???"]),
        ("KAMIYAMA INARI | 神山稲荷", ["???"]),
        ("KAMIYAMA AKIRA | 神山秋羅", ["LRKade"]),
        ("LUNA AORUGURI | ルナ煽るぐり", ["???"]),
        ("LUNA DOMINION | ルナどみにおん", ["???"]),
        ("LUNA ENGEKI | ルナ演劇", ["???"]),
        ("TAKASASHI TINA | 高佐氏ティナ", ["???"]),
        ("KUSANOKI MARI | 楠まり", ["???"]),
        ("LUNA TETSUO | ルナ哲夫", ["???"]),
        ("SETTOU SEIEI | 窃盗精鋭", ["???"]),
        ("Extras | エクストラ", ["???"]),

        ("~{u}ART | 美術{/u}~", []),
        ("ORIGINAL DDLC SPRITES | オリジナルドキドキ文芸部のスプライト", ["Satchley"]),
        ("SAKURA KOTONOHA | 桜言葉", ["Cyrke", "Danko", "Doki Senate"]),
        ("KAMIYAMA AKIRA | 神山秋羅", ["LvcyLu"]),
        ("TAKASASHI TINA | 高佐氏ティナ", ["JohnRDVSMarston", "AJtheYandere", "CPG Yuri", "depressedjoanna a.k.a. staticquit", "Chronos#1609", "Terra#2080", "yagamirai10#7046", "Frithian"]),
        ("YANDERE LILLY | ヤンデレリリー", ["JohnRDVSMarston", "AJtheYandere", "CPG Yuri", "depressedjoanna a.k.a. staticquit", "Z. Awesomeness"]),
        ("LUNA TETSUO (DADSUKI) | ルナ哲夫", ["SovietSpartan", "RedLeader"]),
        ("KUSANOKI MARI | 楠まり", ["「N E K O L A I S」"]),
        ("SETTOU SEIEI (CANON MC) | 窃盗精鋭（キャノンMC）", ["Stormblazed76", "Satchely", "Blue Quacker", "Sweggory"]),
        ("LUNA ENGEKI (SAYURI) | ルナ演劇（サユリ）", ["Hoeruko", "Ian Suller_Blogger", "Matic"]),
        ("ORIGINAL DDLC BACKGROUNDS | オリジナルドキドキ文芸部の背景", ["Velinquent"]),
        ("NEW BACKGROUNDS | 新しい背景", ["Kimagure After | きまぐれアフター", "Kjkjmulo", "Uncle Mugen", "osumashi", "Min-Chiri | みんちりえ", "Crashpunk", "Minikle with edits by Nuxill", "Alex [[ORG]#9077", "LvcyLu", "tropicalmonsoon"]),
        ("LOGO | ロゴ", ["LvcyLu"]),
        ("ACT LOGOS | アクト・ロゴ", ["Leomonade33"]),

        ("~{u}MUSIC | 音楽{/u}~", []),
        ("After Dark", ["Mr.Kitty"]),
        ("After Dark Piano Cover (Title Screen song)", ["949"]),
        ("revolvingdoors", ["DeadAirspace#4433"]),
        ("DDMC Track Series: Lost In Emotion", ["Luma"]),
        ("Confesssion of a Time | 時の告白", ["MC.Dummy.Composer"]),
        ("Depression of Life | 人生の憂鬱", ["MC.Dummy.Composer"]),
        ("Argument Over an Endeavor | 努力をめぐる論争", ["MC.Dummy.Composer"]),
        ("The One Who Stalks (Kamiyama Itsomi's Theme) | ストーカー（神山イツォミのテーマ）", ["MC.Dummy.Composer"]),

        ("~{u}SOUNDS & AMBIENCE | 物音と環境音{/u}~", ["Fesliyan Studios", "Pixabay", "KENNEY"]),

        ("~{u}FONTS | フォント{/u}~", ["Noto Serif JP", "TypeSETit (Alex Brush)", "Krafti Lab", "Unitblock", "That Sounds Great by GraphicSauce", "FOT-RodinNTLG Pro EB"]),

        ("~{u}MISC | その他{/u}~", []),
        ("Mood Pose Tool", ["Chronos", "Yagamirai", "Terra", "DiabloGraves"]),
        ("Autofocus", ["Elckarow", "Pseurae", "Q™"]),
        ("Background Detection Code", ["「N E K O L A I S」"]),
        ("CAMERA SHAKE", ["Ren'Py cookbook"]),
        ("ZOOM TRANSITION", ["Celeste"]),
        ("SILHOUETTE CODE", ["Ren'Py cookbook"]),
        ("ACHIEVEMENTS", ["bobcgames"]),
        ("CREDITS CODE", ["Retronika"]),

        
        ("~{u}Special Thanks | スペシャルサンクス{/u}~", ["DDMC Community | DDMCコミュニティ", "THH Discord | ザー・ホロー・ハーツ・ディスコード", "Team Salvato | チームサルヴァート", "You! | 貴方！"]),

        # Technically you can add more text using the bruteforce thing below, but it's not recommended.
        SPACER,
        SPACER,
        SPACER,
        SPACER,
        SPACER,
        SPACER,
        SPACER,
        SPACER,
        SPACER,
        SPACER,
        SPACER,
        SPACER,
        SPACER,
        SPACER,
        SPACER,
        SPACER,
        SPACER,
        SPACER
    ]

    credits_content = []
    current_color = "#fff"
    for entry in RAW_CREDITS:
        if len(entry) == 2:
            header, names = entry
            section_entries, current_color = section(header, names, current_color)
            credits_content += section_entries
        else:
            credits_content.append(entry)

    credit_height = sum( # Because guessing the yoffset manually is LAME
        e[2][1] + 20 if e[1] == "image" else int(e[1] * 1.175) + 20 # Treat images differently.
        for e in credits_content
    )

screen credits(credit_height=256):
    # Fullscreen container
    frame:
        style "default"
        background None
        xysize (config.screen_width, config.screen_height)

        # Scroll the whole container upward
        fixed:
            at scroll_credits(credit_height=credit_height)
            xalign 0.5

            vbox:
                spacing 20
                #xoffset credit_xoffset

                for entry in credits_content:
                    if entry[1] == "image":
                        add entry[0] size entry[2]
                    else:
                        text entry[0] size entry[1] color entry[2] font "mod_assets/fonts/FOT-RodinNTLG Pro EB.otf"

    if _show_skip_prompt:
        text _("PRESS ENTER TO SKIP") at skip_prompt_dissolve:
            size 20
            color "#ccc"
            align (1.0, 1.0)
            offset (-20, -20)
            font "mod_assets/fonts/FOT-RodinNTLG Pro EB.otf"
        timer 5.0 action SetVariable("_show_skip_prompt", False)

    key "K_RETURN" action If(_show_skip_prompt, Return(), SetVariable("_show_skip_prompt", True)) # Return if the prompt is visible
    key "K_SPACE" action If(_show_skip_prompt, Return(), SetVariable("_show_skip_prompt", True))
    key "mouseup_1" action If(_show_skip_prompt, Return(), SetVariable("_show_skip_prompt", True))

label mah_credits:
    $ _show_skip_prompt = False
    window hide
    scene black
    with fade
    stop music fadeout 1.0
    #play movie "mod_assets/cutscenes/CREDITS.webm"
    show movie zorder 1:
        alpha 0.0
        linear 5.0 alpha 1.0
    pause 14.0
    show menu_logo zorder 2:
        xalign 0.5 yalign 0.5
        #xoffset credit_xoffset
        alpha 0.0
        linear 5.0 alpha 1.0
    pause 16.0
    hide menu_logo with dissolve_scene
    pause 1.0
    show screen credits(credit_height=credit_height) zorder 2
    $ renpy.pause(225.0, hard=True)
    stop movie fadeout 1.0
    hide screen credits 
    hide movie
    with dissolve
    scene black with dissolve
    pause 2.0
    $ _show_skip_prompt = False # Set back to False (player might come back)
    return