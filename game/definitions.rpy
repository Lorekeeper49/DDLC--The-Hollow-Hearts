define persistent.demo = False
define persistent.steam = ("steamapps" in config.basedir.lower())
define config.developer = True
define config.console = True
default can_cont = True

python early:
    import singleton
    me = singleton.SingleInstance()

init python:
    import re
    import os
    import random
    config.keymap['game_menu'].remove('mouseup_3')
    config.keymap['hide_windows'].append('mouseup_3')
    config.keymap['self_voicing'] = []
    config.keymap['clipboard_voicing'] = []
    config.keymap['toggle_skip'] = []
    renpy.music.register_channel("ambience", mixer="ambience", loop=True, tight=True)
    renpy.music.register_channel("ambience2", mixer="ambience", loop=True, tight=True)
    renpy.music.register_channel("ambience3", mixer="ambience", loop=True, tight=True)
    renpy.music.register_channel("music_swap", mixer="music", loop=True, tight=True)
    renpy.music.register_channel("music_poem", mixer="music", loop=True, tight=True)
    renpy.music.register_channel("cutscene_voice", mixer="voice", loop=False, tight=True)
    renpy.music.register_channel("jump0", mixer="music", loop=True, tight=True)
    renpy.music.register_channel("jump1", mixer="music", loop=True, tight=True)
    renpy.music.register_channel("jump2", mixer="music", loop=True, tight=True)
    renpy.music.register_channel("jump3", mixer="music", loop=True, tight=True)
    renpy.music.register_channel("jump4", mixer="music", loop=True, tight=True)
    renpy.music.register_channel("jump5", mixer="music", loop=True, tight=True)
    renpy.music.register_channel("jump6", mixer="music", loop=True, tight=True)
    renpy.music.register_channel("jump7", mixer="music", loop=True, tight=True)
    renpy.music.register_channel("jump8", mixer="music", loop=True, tight=True)
    renpy.music.register_channel("jump9", mixer="music", loop=True, tight=True)
    renpy.music.register_channel("jump10", mixer="music", loop=True, tight=True)
    renpy.music.register_channel("jump11", mixer="music", loop=True, tight=True)
    renpy.music.register_channel("jump12", mixer="music", loop=True, tight=True)
    renpy.music.register_channel("jump13", mixer="music", loop=True, tight=True)
    renpy.music.register_channel("jump14", mixer="music", loop=True, tight=True)
    renpy.music.register_channel("jump15", mixer="music", loop=True, tight=True)
    config.tag_layer['bg'] = 'background'
    config.tag_layer['fg'] = 'foreground'
    def get_pos(channel='music'):
        pos = renpy.music.get_pos(channel=channel)
        if pos: return pos
        return 0
    def delete_all_saves():
        for savegame in renpy.list_saved_games(fast=True):
            renpy.unlink_save(savegame)
    def delete_character(name):
        import os
        try: os.remove(config.basedir + "/characters/" + name + ".chr")
        except: pass
    def restore_all_characters():
        pass
    def restore_relevant_characters():
        restore_all_characters()
    def pause(time=None):
        global _windows_hidden
        if not time:
            _windows_hidden = True
            renpy.ui.saybehavior(afm=" ")
            renpy.ui.interact(mouse='pause', type='pause', roll_forward=None)
            _windows_hidden = False
            return
        if time <= 0: return
        _windows_hidden = True
        renpy.pause(time)
        _windows_hidden = False
    def RigMouse(mousey):
        currentpos = renpy.get_mouse_pos()
        targetpos = [640, mousey]
        if currentpos[1] != targetpos[1]:
            renpy.display.draw.set_mouse_pos((currentpos[0] * 9 + targetpos[0]) / 10.0, (currentpos[1] * 9 + targetpos[1]) / 10.0)
    def random_list(l):
        random.shuffle(l)
        return l
    # Silhouette code comes from here: https://www.renpy.org/wiki/renpy/doc/cookbook/Turn_an_image_into_a_silhouette
    def silhouette_matrix(r,g,b,a=1.0):
        return im.matrix((0, 0, 0, 0, r, 0, 0, 0, 0, g, 0, 0, 0, 0, b, 0, 0, 0, a, 0,))
    def silhouetted(filename, r,g,b, a = 1.0):
        return im.MatrixColor(Image(filename), silhouette_matrix(r,g,b,a))
    def random_chance(chance):
        n = random.uniform(1.0, 100.0)
        return n < chance
    def sound_start(trans, st, at):
        renpy.sound.play(audio.static)
    def sound_stop(trans, st, at):
        renpy.sound.stop()
    def say_blocking():
        global can_cont
        return can_cont
    def get_langs():
        import os
        return [f.path for f in os.scandir("game/voicelines") if f.is_dir()]
    config.say_allow_dismiss = say_blocking
default filepathFound = ""



define audio.t1 = "mod_assets/music/After Dark.ogg"
define audio.t2 = "<loop 4.499>bgm/2.ogg"
define audio.t2g = "bgm/2g.ogg"
define audio.t2g2 = "<from 4.499 loop 4.499>bgm/2.ogg"
define audio.t2g3 = "<loop 4.492>bgm/2g2.ogg"
define audio.t3 = "<loop 4.618>bgm/3.ogg"
define audio.t3g = "<to 15.255>bgm/3g.ogg"
define audio.t3g2 = "<from 15.255 loop 4.618>bgm/3.ogg"
define audio.t3g3 = "<loop 4.618>bgm/3g2.ogg"
define audio.t3m = "<loop 4.618>bgm/3.ogg"
define audio.t4 = "<loop 19.451>bgm/4.ogg"
define audio.t4g = "<loop 1.000>bgm/4g.ogg"
define audio.t5 = "<loop 4.444>bgm/5.ogg"
define audio.t5s = "<loop 4.444>bgm/5_sayori.ogg"
define audio.t5n = "<loop 4.444>bgm/5_natsuki.ogg"
define audio.t5y = "<loop 4.444>bgm/5_yuri.ogg"
define audio.t5m = "<loop 4.444>bgm/5_monika.ogg"
define audio.t5b = "<loop 4.444>bgm/5.ogg"
define audio.t6 = "<loop 10.893>bgm/6.ogg"
define audio.t6g = "<loop 10.893>bgm/6g.ogg"
define audio.t6r = "<to 39.817 loop 0>bgm/6r.ogg"
define audio.t6s = "<loop 43.572>bgm/6s.ogg"
define audio.t7 = "<loop 2.291>bgm/7.ogg"
define audio.t7a = "<loop 4.316 to 12.453>bgm/7.ogg"
define audio.t7g = "<loop 31.880>bgm/7g.ogg"
define audio.t8 = "<loop 9.938>bgm/8.ogg"
define audio.t9 = "<loop 3.172>bgm/9.ogg"
define audio.t9g = "<loop 1.532>bgm/9g.ogg"
define audio.t10 = "<loop 5.861>bgm/10.ogg"
define audio.t10y = "<loop 0>bgm/10-yuri.ogg"
define audio.td = "<loop 36.782>bgm/d.ogg"

define audio.m1 = "<loop 0>bgm/m1.ogg"
define audio.mend = "<loop 6.424>bgm/monika-end.ogg"

define audio.ghostmenu = "<loop 0>bgm/ghostmenu.ogg"
define audio.g1 = "<loop 0>bgm/g1.ogg"
define audio.g2 = "<loop 0>bgm/g2.ogg"
define audio.hb = "<loop 0>bgm/heartbeat.ogg"

define audio.closet_open = "sfx/closet-open.ogg"
define audio.closet_close = "sfx/closet-close.ogg"
define audio.page_turn = "sfx/pageflip.ogg"
define audio.fall = "sfx/fall.ogg"
define audio.fall2 = "sfx/fall2.ogg"

# - mod music
define audio.confession = "mod_assets/music/Confession.mp3"
define audio.depressed = "mod_assets/music/Depressed.mp3"
define audio.argument = "mod_assets/music/Argument.mp3"
define audio.itsomitheme = "mod_assets/music/Itsomi_s Theme.mp3"
define audio.confdep = "<from 2>mod_assets/music/DDMC_Track_Series_Lost_In_Emotion.mp3"
define audio.tears = "mod_assets/music/2018-08-21_-_Tears_Wont_Stop_-_David_Fesliyan.mp3"

# - ambience
define audio.storm = "<loop 1 to 90>mod_assets/ambience/storm.mp3"
define audio.forest = "<loop 1 to 38>mod_assets/ambience/forest.mp3"
define audio.deadamb = "mod_assets/sounds/deadamb.ogg"
define audio.creepy = "<loop 5>mod_assets/ambience/creepy.ogg"
define audio.clock = "mod_assets/ambience/clock.mp3"
define audio.epic_storm = "mod_assets/ambience/epic_storm.mp3"
define audio.factory = "<loop 11.945>mod_assets/ambience/revolvingdoors.ogg"
define audio.river = "mod_assets/ambience/river-rapids-23199.mp3"

# - mod sound effects
define audio.bell = "mod_assets/sounds/school-bell.ogg"
define audio.kamibell = "mod_assets/sounds/kami-bell.ogg"
define audio.deadmantrans = "mod_assets/sounds/deadman-whoosh.mp3"
define audio.deadmantransout = "mod_assets/sounds/deadman-whoosh-out.ogg"
define audio.flashback = "mod_assets/sounds/flashback.ogg"
define audio.heartbeat = "mod_assets/sounds/Human-Heartbeat-www.fesliyanstudios.com-www.fesliyanstudios.com.mp3"
define audio.splatter = "mod_assets/sounds/splattt-6295.mp3"
define audio.lightswitch = "mod_assets/sounds/Light-Turning-On-A2-www.fesliyanstudios.com.mp3"
define audio.light_cut = "mod_assets/sounds/light_cut.ogg"
define audio.bang = "mod_assets/sounds/bang.ogg"
define audio.beat = "mod_assets/sounds/beat.ogg"
define audio.fallout = "mod_assets/sounds/fall.mp3"
define audio.jumpscare = "<loop 5>mod_assets/sounds/jumpscare.ogg"
define audio.door = "mod_assets/sounds/open_door.ogg"
define audio.footsteps = "mod_assets/sounds/footsteps.ogg"
define audio.grass_move = "mod_assets/sounds/grass_movement.ogg"
define audio.static = "mod_assets/sounds/static.ogg"
define audio.thunder = "mod_assets/sounds/thunder.mp3"
define audio.thunder2 = "mod_assets/sounds/thunder2.ogg"

image black = "#000000"
image dark = "#000000e4"
image darkred = "#110000c8"
image white = "#ffffff"
image splash = "bg/splash.png"
image end:
    truecenter
    "gui/end.png"
image bg residential_day = "bg/residential.png"
image bg class_day = "bg/class.png"
image bg corridor = "bg/corridor.png"
image bg club_day = "bg/club.png"
image bg club_day2:
    choice:
        "bg club_day"
    choice:
        "bg club_day"
    choice:
        "bg club_day"
    choice:
        "bg club_day"
    choice:
        "bg club_day"
    choice:
        "bg/club-skill.png"
image bg closet = "bg/closet.png"
image bg bedroom = "bg/bedroom.png"
image bg sayori_bedroom = "bg/sayori_bedroom.png"
image bg house = "bg/house.png"
image bg kitchen = "bg/kitchen.png"

image bg notebook = "bg/notebook.png"
image bg notebook-glitch = "bg/notebook-glitch.png"

image bg glitch = LiveTile("bg/glitch.jpg")

image glitch_color:
    ytile 3
    zoom 2.5
    parallel:
        "bg/glitch-red.png"
        0.1
        "bg/glitch-green.png"
        0.1
        "bg/glitch-blue.png"
        0.1
        repeat
    parallel:
        yoffset 720
        linear 0.5 yoffset 0
        repeat
    parallel:
        choice:
            xoffset 0
        choice:
            xoffset 10
        choice:
            xoffset 20
        choice:
            xoffset 35
        choice:
            xoffset -10
        choice:
            xoffset -20
        choice:
            xoffset -30
        0.01
        repeat
    parallel:
        alpha 0.6
        linear 0.15 alpha 0.1
        0.2
        alpha 0.6
        linear 0.15 alpha 0.1
        0.2
        alpha 0.7
        linear 0.45 alpha 0



image glitch_color2:
    ytile 3
    zoom 2.5
    parallel:
        "bg/glitch-red.png"
        0.1
        "bg/glitch-green.png"
        0.1
        "bg/glitch-blue.png"
        0.1
        repeat
    parallel:
        yoffset 720
        linear 0.5 yoffset 0
        repeat
    parallel:
        choice:
            xoffset 0
        choice:
            xoffset 10
        choice:
            xoffset 20
        choice:
            xoffset 35
        choice:
            xoffset -10
        choice:
            xoffset -20
        choice:
            xoffset -30
        0.01
        repeat
    parallel:
        alpha 0.7
        linear 0.45 alpha 0

define -501 bgs = []
# - mod backgrounds
init -501 python:
    def capture_images(prefix, filt):
        for file in filter(filt, renpy.list_files()):
            renpy.image(" ".join([prefix, os.path.splitext(os.path.split(file)[1])[0]]), file)
            bgs.append(" ".join([prefix, os.path.splitext(os.path.split(file)[1])[0]]))
        bgs.append("bg sayori_bedroom")
        bgs.append("bg house")
        bgs.append("bg residential_day")
        bgs.append("bg class_day")
        bgs.append("bg corridor")
        bgs.append("bg club_day")
        bgs.append("bg bedroom")
        bgs.append("bg closet")
        bgs.append("bg kitchen")

    capture_images("bg", lambda x: x.startswith("mod_assets/bg/"))
    
    print(renpy.display.image.list_images())

image bg vision_background:
    function sound_start
    "noise"
    0.15
    function sound_stop
    parallel:
        choice:
            "bg bad_bedroom"
        choice:
            "bg bedroom1"
        choice:
            "bg bedroom2"
        choice:
            "bg bedroom3"
        choice:
            "bg dark_dining"
        choice:
            "bg dark_kitchen"
        choice:
            "bg dark_bathroom"
        choice:
            "bg foyer"
        choice:
            "bg hall1"
        choice:
            "bg hall2"
        choice:
            "bg top_kitchen"
        choice:
            "bg storage"
        choice:
            "bg final_room"
        5.0
        choice:
            0.0
        choice:
            0.1
        choice:
            0.2
        choice:
            0.3
        choice:
            0.4
        choice:
            0.5
        choice:
            0.6
        choice:
            0.7
        choice:
            0.8
        choice:
            0.9
        choice:
            1.0
        choice:
            1.1
        choice:
            1.2
        choice:
            1.3
        choice:
            1.4
        choice:
            1.5
        choice:
            1.6
        choice:
            1.7
        choice:
            1.8
        choice:
            1.9
        choice:
            2.0
        function sound_start
        "noise"
        0.05
        choice:
            0.0
        choice:
            0.01
        choice:
            0.02
        choice:
            0.03
        choice:
            0.04
        choice:
            0.05
        choice:
            0.06
        choice:
            0.07
        choice:
            0.08
        choice:
            0.09
        choice:
            0.1
        function sound_stop
        repeat
    parallel:
        zoom 1.0
        choice:
            linear 5.0 zoom 1.05
        choice:
            linear 6.0 zoom 1.05
        choice:
            linear 7.0 zoom 1.05
        choice:
            linear 8.0 zoom 1.05
        choice:
            linear 9.0 zoom 1.05
        choice:
            linear 10.0 zoom 1.05
        0.0
        choice:
            linear 5.0 zoom 1.0
        choice:
            linear 6.0 zoom 1.0
        choice:
            linear 7.0 zoom 1.0
        choice:
            linear 8.0 zoom 1.0
        choice:
            linear 9.0 zoom 1.0
        choice:
            linear 10.0 zoom 1.0
        repeat

# - sayers
define ha = DynamicCharacter('hanato', image='hanato', what_prefix='“', what_suffix='”', ctc="ctc", ctc_position="fixed")
define hamind = DynamicCharacter('hanato', image='hanato', what_prefix='(', what_suffix=')', ctc="ctc", ctc_position="fixed")
define narrator = Character(ctc="ctc", ctc_position="fixed")
define t = DynamicCharacter('player', what_prefix='“', what_suffix='”', ctc="ctc", ctc_position="fixed")
define ttext = DynamicCharacter('player', what_prefix='<', what_suffix='>', ctc="ctc", ctc_position="fixed")
define s = DynamicCharacter('s_name', image='sayori', what_prefix='“', what_suffix='”', ctc="ctc", ctc_position="fixed")
define m = DynamicCharacter('m_name', image='monika', what_prefix='“', what_suffix='”', ctc="ctc", ctc_position="fixed")
define n = DynamicCharacter('n_name', image='natsuki', what_prefix='“', what_suffix='”', ctc="ctc", ctc_position="fixed")
define y = DynamicCharacter('y_name', image='yuri', what_prefix='“', what_suffix='”', ctc="ctc", ctc_position="fixed")
define lil = DynamicCharacter('lilly', image='lilly', what_prefix='“', what_suffix='”', ctc="ctc", ctc_position="fixed")
define k = DynamicCharacter('k_name', image='kotonoha', what_prefix='“', what_suffix='”', ctc="ctc", ctc_position="fixed")
define ak = DynamicCharacter('akira', image='akira', what_prefix='“', what_suffix='”', ctc="ctc", ctc_position="fixed")
define aktext = DynamicCharacter('akira', what_prefix='<', what_suffix='>', ctc="ctc", ctc_position="fixed")
define its = DynamicCharacter('itsomi', image='itsomi', what_prefix='“', what_suffix='”', ctc="ctc", ctc_position="fixed")
define kiri = DynamicCharacter('kirinani', image='kirinani', what_prefix='“', what_suffix='”', ctc="ctc", ctc_position="fixed")
define ina = DynamicCharacter('inari', image='inari', what_prefix='“', what_suffix='”', ctc="ctc", ctc_position="fixed")
define kmind = DynamicCharacter('k_name', image='kotonoha', what_prefix='(', what_suffix=')', ctc="ctc", ctc_position="fixed")
define everyone = DynamicCharacter('everyone', what_prefix='“', what_suffix='”', ctc="ctc", ctc_position="fixed")
define a = DynamicCharacter('aoruguri', image='aoruguri', what_prefix='“', what_suffix='”', ctc="ctc", ctc_position="fixed")
define ti = DynamicCharacter('tina', image='tina', what_prefix='“', what_suffix='”', ctc="ctc", ctc_position="fixed")
define en = DynamicCharacter('en_name', image="engeki", what_prefix='“', what_suffix='”', ctc="ctc", ctc_position="fixed")
define ma = DynamicCharacter('mari', image="mari", what_prefix='“', what_suffix='”', ctc="ctc", ctc_position="fixed")
define d = DynamicCharacter('dominion', image="dominion", what_prefix='“', what_suffix='”', ctc="ctc", ctc_position="fixed")
define sei = DynamicCharacter('seiei', image='seiei', what_prefix='“', what_suffix='”', ctc="ctc", ctc_position="fixed")
define ara = DynamicCharacter('ara_name', image='aragaki', what_prefix='“', what_suffix='”', ctc="ctc", ctc_position="fixed")
define general = DynamicCharacter('pla', what_prefix='“', what_suffix='”', ctc="ctc", ctc_position="fixed")

define _dismiss_pause = config.developer



default persistent.playthrough = 0
# - endings
default persistent.endings = 0
default persistent.strueending = False
default persistent.mtrueending = False
default persistent.ntrueending = False
default persistent.ytrueending = False
default persistent.suicide = False
default persistent.noone = False
default persistent.sgood = False
default persistent.sbad = False
default persistent.mgood = False
default persistent.mbad = False
default persistent.ngood = False
default persistent.nbad = False
default persistent.ygood = False
default persistent.ybad = False

default persistent.end_questions_asked = 0

default persistent.anticheat = 0
default persistent.first_load = None
define config.mouse = None
default allow_skipping = True
default basedir = config.basedir
default chapter = 0
default act = 0
default currentpos = 0
default faint_effect = None


# - names
default player = "桜隊円\n{size=15}Sakura Taiyen{/size}"
default s_name = "シナモンパン佐代里\n{size=15}Shinamonpan Sayori{/size}"
default m_name = "無理高モニカ\n{size=15}Murikou Monika{/size}"
default n_name = "ルナ菜月\n{size=15}Luna Natsuki{/size}"
default y_name = "ヤンデレ百合\n{size=15}Yandere Yuri{/size}"
default k_name = "桜言葉\n{size=15}Sakura Kotonoha{/size}"
default akira = "神山秋羅\n{size=15}Kamiyama Akira{/size}"
default hanato = "神山華翔\n{size=15}Kamiyama Hanato{/size}"
default kirinani = "神山霧何\n{size=15}Kamiyama Kirinani{/size}"
default itsomi = "神山イツォミ\n{size=15}Kamiyama Itsomi{/size}"
default inari = "神山稲荷\n{size=15}Kamiyama Inari{/size}"
default everyone = "みんな\n{size=15}Everyone{/size}"
default lilly = "ヤンデレリリー\n{size=15}Yandere Lilly{/size}"
default aoruguri = "ルナ煽るぐり\n{size=15}Luna Aoruguri{/size}"
default tina = "高佐氏ティナ\n{size=15}Takasashi Tina{/size}"
default en_name = "ルナ演劇\n{size=15}Luna Engeki{/size}"
default mari = "楠まり\n{size=15}Kusunoki Mari{/size}"
default dominion = "ルナどみにおん\n{size=15}Luna Dominion{/size}"
default seiei = "窃盗精鋭\n{size=15}Settou Seiei{/size}"
default ara_name = "桜荒垣\n{size=15}Sakura Aragaki{/size}"
default pla = "General Name"

# - choices
default cute = False
default known = False
default found_breaker = False
default secrets = False
default en_out = False
default followed = False
default persistent.choices_made = []

# - miscellaneous
default previouschan = "music"

default startnow = False

default devmode = config.developer

default save_name = ""