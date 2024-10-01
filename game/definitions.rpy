define persistent.demo = True
define persistent.steam = ("steamapps" in config.basedir.lower())
define config.developer = True
default entirestory = False

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
    renpy.music.register_channel("ambience", mixer="music", tight=True)
    renpy.music.register_channel("music_swap", mixer="music", tight=True)
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
    def openMidnight():
        for root, dirs, files in os.walk("C:/"):  
            if "TheMidnightClub.exe" in files:  
                filepathFound = os.path.join(root, "TheMidnightClub.exe")
        os.system(filepathFound)
    def silhouette_matrix(r,g,b,a=1.0):
        return im.matrix((0, 0, 0, 0, r, 0, 0, 0, 0, g, 0, 0, 0, 0, b, 0, 0, 0, a, 0,))
    def silhouetted(filename, r,g,b, a = 1.0):
        return im.MatrixColor(Image(filename), silhouette_matrix(r,g,b,a))
    def random_chance(chance):
        n = random.uniform(1.0, 100.0)
        return n < chance
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

# - mod music
define audio.confession = "mod_assets/music/Confession.mp3"
define audio.depressed = "mod_assets/music/Depressed.mp3"
define audio.argument = "mod_assets/music/Argument.mp3"
define audio.itsomitheme = "mod_assets/music/Itsomi's Theme.mp3"
define audio.confdep = "<from 2>mod_assets/music/DDMC_Track_Series_Lost_In_Emotion.mp3"

# - ambience
define audio.storm = "<loop 1 to 90>mod_assets/ambience/storm.mp3"
define audio.forest = "<loop 1 to 38>mod_assets/ambience/forest.mp3"
define audio.deadamb = "mod_assets/sounds/deadamb.ogg"
define audio.mansion = "<loop 1 to 38>mod_assets/ambience/mansion.ogg"
define audio.clock = "mod_assets/ambience/clock.mp3"

# - mod sound effects
define audio.bell = "mod_assets/sounds/school-bell.ogg"
define audio.kamibell = "mod_assets/sounds/kami-bell.ogg"
define audio.deadmantrans = "mod_assets/sounds/deadman-whoosh.mp3"
define audio.deadmantransout = "mod_assets/sounds/deadman-whoosh-out.ogg"
define audio.flashback = "mod_assets/sounds/flashback.ogg"
define audio.heartbeat = "mod_assets/sounds/Human-Heartbeat-www.fesliyanstudios.com-www.fesliyanstudios.com.mp3"
define audio.splatter = "mod_assets/sounds/splattt-6295.mp3"
define audio.lightswitch = "mod_assets/sounds/Light-Turning-On-A2-www.fesliyanstudios.com.mp3"
define audio.bang = "mod_assets/sounds/bang.ogg"
define audio.fallout = "mod_assets/sounds/fall.mp3"
define audio.jumpscare = "<loop 3>mod_assets/sounds/jumpscare.ogg"
define audio.door = "mod_assets/sounds/open_door.ogg"
define audio.footsteps = "mod_assets/sounds/footsteps.ogg"

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

    capture_images("bg", lambda x: x.startswith("mod_assets/bg/"))
    
    print(renpy.display.image.list_images())

# - characters
image sayori 1 = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/a.png")
image sayori 1a = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/a.png")
image sayori 1b = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/b.png")
image sayori 1c = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/c.png")
image sayori 1d = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/d.png")
image sayori 1e = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/e.png")
image sayori 1f = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/f.png")
image sayori 1g = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/g.png")
image sayori 1h = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/h.png")
image sayori 1i = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/i.png")
image sayori 1j = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/j.png")
image sayori 1k = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/k.png")
image sayori 1l = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/l.png")
image sayori 1m = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/m.png")
image sayori 1n = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/n.png")
image sayori 1o = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/o.png")
image sayori 1p = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/p.png")
image sayori 1q = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/q.png")
image sayori 1r = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/r.png")
image sayori 1s = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/s.png")
image sayori 1t = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/t.png")
image sayori 1u = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/u.png")
image sayori 1v = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/v.png")
image sayori 1w = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/w.png")
image sayori 1x = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/x.png")
image sayori 1y = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/y.png")

image sayori 2 = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/a.png")
image sayori 2a = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/a.png")
image sayori 2b = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/b.png")
image sayori 2c = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/c.png")
image sayori 2d = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/d.png")
image sayori 2e = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/e.png")
image sayori 2f = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/f.png")
image sayori 2g = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/g.png")
image sayori 2h = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/h.png")
image sayori 2i = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/i.png")
image sayori 2j = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/j.png")
image sayori 2k = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/k.png")
image sayori 2l = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/l.png")
image sayori 2m = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/m.png")
image sayori 2n = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/n.png")
image sayori 2o = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/o.png")
image sayori 2p = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/p.png")
image sayori 2q = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/q.png")
image sayori 2r = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/r.png")
image sayori 2s = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/s.png")
image sayori 2t = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/t.png")
image sayori 2u = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/u.png")
image sayori 2v = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/v.png")
image sayori 2w = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/w.png")
image sayori 2x = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/x.png")
image sayori 2y = im.Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/y.png")

image sayori 3 = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/a.png")
image sayori 3a = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/a.png")
image sayori 3b = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/b.png")
image sayori 3c = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/c.png")
image sayori 3d = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/d.png")
image sayori 3e = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/e.png")
image sayori 3f = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/f.png")
image sayori 3g = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/g.png")
image sayori 3h = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/h.png")
image sayori 3i = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/i.png")
image sayori 3j = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/j.png")
image sayori 3k = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/k.png")
image sayori 3l = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/l.png")
image sayori 3m = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/m.png")
image sayori 3n = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/n.png")
image sayori 3o = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/o.png")
image sayori 3p = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/p.png")
image sayori 3q = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/q.png")
image sayori 3r = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/r.png")
image sayori 3s = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/s.png")
image sayori 3t = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/t.png")
image sayori 3u = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/u.png")
image sayori 3v = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/v.png")
image sayori 3w = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/w.png")
image sayori 3x = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/x.png")
image sayori 3y = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/y.png")

image sayori 4 = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/a.png")
image sayori 4a = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/a.png")
image sayori 4b = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/b.png")
image sayori 4c = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/c.png")
image sayori 4d = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/d.png")
image sayori 4e = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/e.png")
image sayori 4f = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/f.png")
image sayori 4g = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/g.png")
image sayori 4h = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/h.png")
image sayori 4i = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/i.png")
image sayori 4j = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/j.png")
image sayori 4k = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/k.png")
image sayori 4l = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/l.png")
image sayori 4m = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/m.png")
image sayori 4n = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/n.png")
image sayori 4o = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/o.png")
image sayori 4p = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/p.png")
image sayori 4q = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/q.png")
image sayori 4r = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/r.png")
image sayori 4s = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/s.png")
image sayori 4t = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/t.png")
image sayori 4u = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/u.png")
image sayori 4v = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/v.png")
image sayori 4w = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/w.png")
image sayori 4x = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/x.png")
image sayori 4y = im.Composite((960, 960), (0, 0), "sayori/2l.png", (0, 0), "sayori/2r.png", (0, 0), "sayori/y.png")

image sayori 5 = im.Composite((960, 960), (0, 0), "sayori/3a.png")
image sayori 5a = im.Composite((960, 960), (0, 0), "sayori/3a.png")
image sayori 5b = im.Composite((960, 960), (0, 0), "sayori/3b.png")
image sayori 5c = im.Composite((960, 960), (0, 0), "sayori/3c.png")
image sayori 5d = im.Composite((960, 960), (0, 0), "sayori/3d.png")

image sayori 1ba = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/a.png")
image sayori 1bb = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/b.png")
image sayori 1bc = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/c.png")
image sayori 1bd = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/d.png")
image sayori 1be = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/e.png")
image sayori 1bf = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/f.png")
image sayori 1bg = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/g.png")
image sayori 1bh = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/h.png")
image sayori 1bi = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/i.png")
image sayori 1bj = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/j.png")
image sayori 1bk = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/k.png")
image sayori 1bl = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/l.png")
image sayori 1bm = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/m.png")
image sayori 1bn = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/n.png")
image sayori 1bo = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/o.png")
image sayori 1bp = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/p.png")
image sayori 1bq = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/q.png")
image sayori 1br = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/r.png")
image sayori 1bs = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/s.png")
image sayori 1bt = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/t.png")
image sayori 1bu = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/u.png")
image sayori 1bv = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/v.png")
image sayori 1bw = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/w.png")
image sayori 1bx = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/x.png")
image sayori 1by = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/y.png")

image sayori 2ba = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/a.png")
image sayori 2bb = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/b.png")
image sayori 2bc = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/c.png")
image sayori 2bd = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/d.png")
image sayori 2be = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/e.png")
image sayori 2bf = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/f.png")
image sayori 2bg = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/g.png")
image sayori 2bh = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/h.png")
image sayori 2bi = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/i.png")
image sayori 2bj = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/j.png")
image sayori 2bk = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/k.png")
image sayori 2bl = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/l.png")
image sayori 2bm = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/m.png")
image sayori 2bn = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/n.png")
image sayori 2bo = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/o.png")
image sayori 2bp = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/p.png")
image sayori 2bq = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/q.png")
image sayori 2br = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/r.png")
image sayori 2bs = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/s.png")
image sayori 2bt = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/t.png")
image sayori 2bu = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/u.png")
image sayori 2bv = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/v.png")
image sayori 2bw = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/w.png")
image sayori 2bx = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/x.png")
image sayori 2by = im.Composite((960, 960), (0, 0), "sayori/1bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/y.png")

image sayori 3ba = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/a.png")
image sayori 3bb = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/b.png")
image sayori 3bc = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/c.png")
image sayori 3bd = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/d.png")
image sayori 3be = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/e.png")
image sayori 3bf = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/f.png")
image sayori 3bg = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/g.png")
image sayori 3bh = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/h.png")
image sayori 3bi = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/i.png")
image sayori 3bj = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/j.png")
image sayori 3bk = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/k.png")
image sayori 3bl = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/l.png")
image sayori 3bm = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/m.png")
image sayori 3bn = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/n.png")
image sayori 3bo = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/o.png")
image sayori 3bp = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/p.png")
image sayori 3bq = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/q.png")
image sayori 3br = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/r.png")
image sayori 3bs = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/s.png")
image sayori 3bt = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/t.png")
image sayori 3bu = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/u.png")
image sayori 3bv = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/v.png")
image sayori 3bw = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/w.png")
image sayori 3bx = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/x.png")
image sayori 3by = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/1br.png", (0, 0), "sayori/y.png")

image sayori 4ba = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/a.png")
image sayori 4bb = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/b.png")
image sayori 4bc = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/c.png")
image sayori 4bd = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/d.png")
image sayori 4be = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/e.png")
image sayori 4bf = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/f.png")
image sayori 4bg = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/g.png")
image sayori 4bh = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/h.png")
image sayori 4bi = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/i.png")
image sayori 4bj = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/j.png")
image sayori 4bk = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/k.png")
image sayori 4bl = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/l.png")
image sayori 4bm = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/m.png")
image sayori 4bn = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/n.png")
image sayori 4bo = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/o.png")
image sayori 4bp = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/p.png")
image sayori 4bq = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/q.png")
image sayori 4br = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/r.png")
image sayori 4bs = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/s.png")
image sayori 4bt = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/t.png")
image sayori 4bu = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/u.png")
image sayori 4bv = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/v.png")
image sayori 4bw = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/w.png")
image sayori 4bx = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/x.png")
image sayori 4by = im.Composite((960, 960), (0, 0), "sayori/2bl.png", (0, 0), "sayori/2br.png", (0, 0), "sayori/y.png")

image sayori glitch:
    "sayori/glitch1.png"
    pause 0.01666
    "sayori/glitch2.png"
    pause 0.01666
    repeat


image natsuki 11 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/1t.png")
image natsuki 1a = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/a.png")
image natsuki 1b = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/b.png")
image natsuki 1c = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/c.png")
image natsuki 1d = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/d.png")
image natsuki 1e = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/e.png")
image natsuki 1f = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/f.png")
image natsuki 1g = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/g.png")
image natsuki 1h = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/h.png")
image natsuki 1i = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/i.png")
image natsuki 1j = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/j.png")
image natsuki 1k = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/k.png")
image natsuki 1l = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/l.png")
image natsuki 1m = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/m.png")
image natsuki 1n = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/n.png")
image natsuki 1o = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/o.png")
image natsuki 1p = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/p.png")
image natsuki 1q = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/q.png")
image natsuki 1r = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/r.png")
image natsuki 1s = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/s.png")
image natsuki 1t = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/t.png")
image natsuki 1u = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/u.png")
image natsuki 1v = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/v.png")
image natsuki 1w = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/w.png")
image natsuki 1x = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/x.png")
image natsuki 1y = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/y.png")
image natsuki 1z = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/z.png")

image natsuki 21 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/1t.png")
image natsuki 2a = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/a.png")
image natsuki 2b = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/b.png")
image natsuki 2c = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/c.png")
image natsuki 2d = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/d.png")
image natsuki 2e = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/e.png")
image natsuki 2f = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/f.png")
image natsuki 2g = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/g.png")
image natsuki 2h = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/h.png")
image natsuki 2i = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/i.png")
image natsuki 2j = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/j.png")
image natsuki 2k = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/k.png")
image natsuki 2l = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/l.png")
image natsuki 2m = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/m.png")
image natsuki 2n = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/n.png")
image natsuki 2o = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/o.png")
image natsuki 2p = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/p.png")
image natsuki 2q = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/q.png")
image natsuki 2r = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/r.png")
image natsuki 2s = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/s.png")
image natsuki 2t = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/t.png")
image natsuki 2u = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/u.png")
image natsuki 2v = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/v.png")
image natsuki 2w = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/w.png")
image natsuki 2x = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/x.png")
image natsuki 2y = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/y.png")
image natsuki 2z = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/z.png")

image natsuki 31 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/1t.png")
image natsuki 3a = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/a.png")
image natsuki 3b = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/b.png")
image natsuki 3c = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/c.png")
image natsuki 3d = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/d.png")
image natsuki 3e = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/e.png")
image natsuki 3f = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/f.png")
image natsuki 3g = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/g.png")
image natsuki 3h = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/h.png")
image natsuki 3i = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/i.png")
image natsuki 3j = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/j.png")
image natsuki 3k = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/k.png")
image natsuki 3l = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/l.png")
image natsuki 3m = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/m.png")
image natsuki 3n = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/n.png")
image natsuki 3o = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/o.png")
image natsuki 3p = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/p.png")
image natsuki 3q = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/q.png")
image natsuki 3r = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/r.png")
image natsuki 3s = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/s.png")
image natsuki 3t = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/t.png")
image natsuki 3u = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/u.png")
image natsuki 3v = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/v.png")
image natsuki 3w = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/w.png")
image natsuki 3x = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/x.png")
image natsuki 3y = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/y.png")
image natsuki 3z = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/z.png")

image natsuki 41 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/1t.png")
image natsuki 4a = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/a.png")
image natsuki 4b = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/b.png")
image natsuki 4c = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/c.png")
image natsuki 4d = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/d.png")
image natsuki 4e = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/e.png")
image natsuki 4f = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/f.png")
image natsuki 4g = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/g.png")
image natsuki 4h = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/h.png")
image natsuki 4i = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/i.png")
image natsuki 4j = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/j.png")
image natsuki 4k = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/k.png")
image natsuki 4l = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/l.png")
image natsuki 4m = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/m.png")
image natsuki 4n = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/n.png")
image natsuki 4o = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/o.png")
image natsuki 4p = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/p.png")
image natsuki 4q = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/q.png")
image natsuki 4r = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/r.png")
image natsuki 4s = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/s.png")
image natsuki 4t = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/t.png")
image natsuki 4u = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/u.png")
image natsuki 4v = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/v.png")
image natsuki 4w = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/w.png")
image natsuki 4x = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/x.png")
image natsuki 4y = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/y.png")
image natsuki 4z = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/z.png")

image natsuki 12 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2t.png")
image natsuki 12a = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2ta.png")
image natsuki 12b = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2tb.png")
image natsuki 12c = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2tc.png")
image natsuki 12d = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2td.png")
image natsuki 12e = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2te.png")
image natsuki 12f = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2tf.png")
image natsuki 12g = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2tg.png")
image natsuki 12h = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2th.png")
image natsuki 12i = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/2ti.png")

image natsuki 42 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2t.png")
image natsuki 42a = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2ta.png")
image natsuki 42b = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2tb.png")
image natsuki 42c = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2tc.png")
image natsuki 42d = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2td.png")
image natsuki 42e = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2te.png")
image natsuki 42f = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2tf.png")
image natsuki 42g = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2tg.png")
image natsuki 42h = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2th.png")
image natsuki 42i = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/2ti.png")

image natsuki 51 = im.Composite((960, 960), (18, 22), "natsuki/1t.png", (0, 0), "natsuki/3.png")
image natsuki 5a = im.Composite((960, 960), (18, 22), "natsuki/a.png", (0, 0), "natsuki/3.png")
image natsuki 5b = im.Composite((960, 960), (18, 22), "natsuki/b.png", (0, 0), "natsuki/3.png")
image natsuki 5c = im.Composite((960, 960), (18, 22), "natsuki/c.png", (0, 0), "natsuki/3.png")
image natsuki 5d = im.Composite((960, 960), (18, 22), "natsuki/d.png", (0, 0), "natsuki/3.png")
image natsuki 5e = im.Composite((960, 960), (18, 22), "natsuki/e.png", (0, 0), "natsuki/3.png")
image natsuki 5f = im.Composite((960, 960), (18, 22), "natsuki/f.png", (0, 0), "natsuki/3.png")
image natsuki 5g = im.Composite((960, 960), (18, 22), "natsuki/g.png", (0, 0), "natsuki/3.png")
image natsuki 5h = im.Composite((960, 960), (18, 22), "natsuki/h.png", (0, 0), "natsuki/3.png")
image natsuki 5i = im.Composite((960, 960), (18, 22), "natsuki/i.png", (0, 0), "natsuki/3.png")
image natsuki 5j = im.Composite((960, 960), (18, 22), "natsuki/j.png", (0, 0), "natsuki/3.png")
image natsuki 5k = im.Composite((960, 960), (18, 22), "natsuki/k.png", (0, 0), "natsuki/3.png")
image natsuki 5l = im.Composite((960, 960), (18, 22), "natsuki/l.png", (0, 0), "natsuki/3.png")
image natsuki 5m = im.Composite((960, 960), (18, 22), "natsuki/m.png", (0, 0), "natsuki/3.png")
image natsuki 5n = im.Composite((960, 960), (18, 22), "natsuki/n.png", (0, 0), "natsuki/3.png")
image natsuki 5o = im.Composite((960, 960), (18, 22), "natsuki/o.png", (0, 0), "natsuki/3.png")
image natsuki 5p = im.Composite((960, 960), (18, 22), "natsuki/p.png", (0, 0), "natsuki/3.png")
image natsuki 5q = im.Composite((960, 960), (18, 22), "natsuki/q.png", (0, 0), "natsuki/3.png")
image natsuki 5r = im.Composite((960, 960), (18, 22), "natsuki/r.png", (0, 0), "natsuki/3.png")
image natsuki 5s = im.Composite((960, 960), (18, 22), "natsuki/s.png", (0, 0), "natsuki/3.png")
image natsuki 5t = im.Composite((960, 960), (18, 22), "natsuki/t.png", (0, 0), "natsuki/3.png")
image natsuki 5u = im.Composite((960, 960), (18, 22), "natsuki/u.png", (0, 0), "natsuki/3.png")
image natsuki 5v = im.Composite((960, 960), (18, 22), "natsuki/v.png", (0, 0), "natsuki/3.png")
image natsuki 5w = im.Composite((960, 960), (18, 22), "natsuki/w.png", (0, 0), "natsuki/3.png")
image natsuki 5x = im.Composite((960, 960), (18, 22), "natsuki/x.png", (0, 0), "natsuki/3.png")
image natsuki 5y = im.Composite((960, 960), (18, 22), "natsuki/y.png", (0, 0), "natsuki/3.png")
image natsuki 5z = im.Composite((960, 960), (18, 22), "natsuki/z.png", (0, 0), "natsuki/3.png")



image natsuki 1ba = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/a.png")
image natsuki 1bb = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/b.png")
image natsuki 1bc = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/c.png")
image natsuki 1bd = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/d.png")
image natsuki 1be = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/e.png")
image natsuki 1bf = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/f.png")
image natsuki 1bg = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/g.png")
image natsuki 1bh = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/h.png")
image natsuki 1bi = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/i.png")
image natsuki 1bj = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/j.png")
image natsuki 1bk = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/k.png")
image natsuki 1bl = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/l.png")
image natsuki 1bm = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/m.png")
image natsuki 1bn = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/n.png")
image natsuki 1bo = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/o.png")
image natsuki 1bp = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/p.png")
image natsuki 1bq = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/q.png")
image natsuki 1br = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/r.png")
image natsuki 1bs = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/s.png")
image natsuki 1bt = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/t.png")
image natsuki 1bu = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/u.png")
image natsuki 1bv = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/v.png")
image natsuki 1bw = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/w.png")
image natsuki 1bx = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/x.png")
image natsuki 1by = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/y.png")
image natsuki 1bz = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/z.png")

image natsuki 2ba = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/a.png")
image natsuki 2bb = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/b.png")
image natsuki 2bc = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/c.png")
image natsuki 2bd = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/d.png")
image natsuki 2be = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/e.png")
image natsuki 2bf = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/f.png")
image natsuki 2bg = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/g.png")
image natsuki 2bh = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/h.png")
image natsuki 2bi = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/i.png")
image natsuki 2bj = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/j.png")
image natsuki 2bk = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/k.png")
image natsuki 2bl = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/l.png")
image natsuki 2bm = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/m.png")
image natsuki 2bn = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/n.png")
image natsuki 2bo = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/o.png")
image natsuki 2bp = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/p.png")
image natsuki 2bq = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/q.png")
image natsuki 2br = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/r.png")
image natsuki 2bs = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/s.png")
image natsuki 2bt = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/t.png")
image natsuki 2bu = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/u.png")
image natsuki 2bv = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/v.png")
image natsuki 2bw = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/w.png")
image natsuki 2bx = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/x.png")
image natsuki 2by = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/y.png")
image natsuki 2bz = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/z.png")

image natsuki 3ba = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/a.png")
image natsuki 3bb = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/b.png")
image natsuki 3bc = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/c.png")
image natsuki 3bd = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/d.png")
image natsuki 3be = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/e.png")
image natsuki 3bf = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/f.png")
image natsuki 3bg = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/g.png")
image natsuki 3bh = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/h.png")
image natsuki 3bi = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/i.png")
image natsuki 3bj = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/j.png")
image natsuki 3bk = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/k.png")
image natsuki 3bl = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/l.png")
image natsuki 3bm = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/m.png")
image natsuki 3bn = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/n.png")
image natsuki 3bo = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/o.png")
image natsuki 3bp = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/p.png")
image natsuki 3bq = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/q.png")
image natsuki 3br = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/r.png")
image natsuki 3bs = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/s.png")
image natsuki 3bt = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/t.png")
image natsuki 3bu = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/u.png")
image natsuki 3bv = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/v.png")
image natsuki 3bw = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/w.png")
image natsuki 3bx = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/x.png")
image natsuki 3by = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/y.png")
image natsuki 3bz = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/z.png")

image natsuki 4ba = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/a.png")
image natsuki 4bb = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/b.png")
image natsuki 4bc = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/c.png")
image natsuki 4bd = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/d.png")
image natsuki 4be = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/e.png")
image natsuki 4bf = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/f.png")
image natsuki 4bg = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/g.png")
image natsuki 4bh = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/h.png")
image natsuki 4bi = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/i.png")
image natsuki 4bj = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/j.png")
image natsuki 4bk = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/k.png")
image natsuki 4bl = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/l.png")
image natsuki 4bm = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/m.png")
image natsuki 4bn = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/n.png")
image natsuki 4bo = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/o.png")
image natsuki 4bp = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/p.png")
image natsuki 4bq = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/q.png")
image natsuki 4br = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/r.png")
image natsuki 4bs = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/s.png")
image natsuki 4bt = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/t.png")
image natsuki 4bu = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/u.png")
image natsuki 4bv = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/v.png")
image natsuki 4bw = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/w.png")
image natsuki 4bx = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/x.png")
image natsuki 4by = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/y.png")
image natsuki 4bz = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/z.png")

image natsuki 12ba = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2bta.png")
image natsuki 12bb = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2btb.png")
image natsuki 12bc = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2btc.png")
image natsuki 12bd = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2btd.png")
image natsuki 12be = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2bte.png")
image natsuki 12bf = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2btf.png")
image natsuki 12bg = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2btg.png")
image natsuki 12bh = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2bth.png")
image natsuki 12bi = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/2bti.png")

image natsuki 42ba = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2bta.png")
image natsuki 42bb = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2btb.png")
image natsuki 42bc = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2btc.png")
image natsuki 42bd = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2btd.png")
image natsuki 42be = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2bte.png")
image natsuki 42bf = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2btf.png")
image natsuki 42bg = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2btg.png")
image natsuki 42bh = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2bth.png")
image natsuki 42bi = im.Composite((960, 960), (0, 0), "natsuki/2bl.png", (0, 0), "natsuki/2br.png", (0, 0), "natsuki/2bti.png")

image natsuki 5ba = im.Composite((960, 960), (18, 22), "natsuki/a.png", (0, 0), "natsuki/3b.png")
image natsuki 5bb = im.Composite((960, 960), (18, 22), "natsuki/b.png", (0, 0), "natsuki/3b.png")
image natsuki 5bc = im.Composite((960, 960), (18, 22), "natsuki/c.png", (0, 0), "natsuki/3b.png")
image natsuki 5bd = im.Composite((960, 960), (18, 22), "natsuki/d.png", (0, 0), "natsuki/3b.png")
image natsuki 5be = im.Composite((960, 960), (18, 22), "natsuki/e.png", (0, 0), "natsuki/3b.png")
image natsuki 5bf = im.Composite((960, 960), (18, 22), "natsuki/f.png", (0, 0), "natsuki/3b.png")
image natsuki 5bg = im.Composite((960, 960), (18, 22), "natsuki/g.png", (0, 0), "natsuki/3b.png")
image natsuki 5bh = im.Composite((960, 960), (18, 22), "natsuki/h.png", (0, 0), "natsuki/3b.png")
image natsuki 5bi = im.Composite((960, 960), (18, 22), "natsuki/i.png", (0, 0), "natsuki/3b.png")
image natsuki 5bj = im.Composite((960, 960), (18, 22), "natsuki/j.png", (0, 0), "natsuki/3b.png")
image natsuki 5bk = im.Composite((960, 960), (18, 22), "natsuki/k.png", (0, 0), "natsuki/3b.png")
image natsuki 5bl = im.Composite((960, 960), (18, 22), "natsuki/l.png", (0, 0), "natsuki/3b.png")
image natsuki 5bm = im.Composite((960, 960), (18, 22), "natsuki/m.png", (0, 0), "natsuki/3b.png")
image natsuki 5bn = im.Composite((960, 960), (18, 22), "natsuki/n.png", (0, 0), "natsuki/3b.png")
image natsuki 5bo = im.Composite((960, 960), (18, 22), "natsuki/o.png", (0, 0), "natsuki/3b.png")
image natsuki 5bp = im.Composite((960, 960), (18, 22), "natsuki/p.png", (0, 0), "natsuki/3b.png")
image natsuki 5bq = im.Composite((960, 960), (18, 22), "natsuki/q.png", (0, 0), "natsuki/3b.png")
image natsuki 5br = im.Composite((960, 960), (18, 22), "natsuki/r.png", (0, 0), "natsuki/3b.png")
image natsuki 5bs = im.Composite((960, 960), (18, 22), "natsuki/s.png", (0, 0), "natsuki/3b.png")
image natsuki 5bt = im.Composite((960, 960), (18, 22), "natsuki/t.png", (0, 0), "natsuki/3b.png")
image natsuki 5bu = im.Composite((960, 960), (18, 22), "natsuki/u.png", (0, 0), "natsuki/3b.png")
image natsuki 5bv = im.Composite((960, 960), (18, 22), "natsuki/v.png", (0, 0), "natsuki/3b.png")
image natsuki 5bw = im.Composite((960, 960), (18, 22), "natsuki/w.png", (0, 0), "natsuki/3b.png")
image natsuki 5bx = im.Composite((960, 960), (18, 22), "natsuki/x.png", (0, 0), "natsuki/3b.png")
image natsuki 5by = im.Composite((960, 960), (18, 22), "natsuki/y.png", (0, 0), "natsuki/3b.png")
image natsuki 5bz = im.Composite((960, 960), (18, 22), "natsuki/z.png", (0, 0), "natsuki/3b.png")


image natsuki 1 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/1t.png")
image natsuki 2 = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/1t.png")
image natsuki 3 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/1t.png")
image natsuki 4 = im.Composite((960, 960), (0, 0), "natsuki/2l.png", (0, 0), "natsuki/2r.png", (0, 0), "natsuki/1t.png")
image natsuki 5 = im.Composite((960, 960), (18, 22), "natsuki/1t.png", (0, 0), "natsuki/3.png")

image natsuki scream = im.Composite((960, 960), (0, 0), "natsuki/1l.png", (0, 0), "natsuki/1r.png", (0, 0), "natsuki/scream.png")
image natsuki screamb = im.Composite((960, 960), (0, 0), "natsuki/1bl.png", (0, 0), "natsuki/1br.png", (0, 0), "natsuki/scream.png")
image natsuki vomit = "natsuki/vomit.png"

image n_blackeyes = "images/natsuki/blackeyes.png"
image n_eye = "images/natsuki/eye.png"


image yuri 1 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/a.png")
image yuri 2 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/a.png")
image yuri 3 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/a.png")
image yuri 4 = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/a2.png")

image yuri 1a = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/a.png")
image yuri 1b = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/b.png")
image yuri 1c = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/c.png")
image yuri 1d = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/d.png")
image yuri 1e = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/e.png")
image yuri 1f = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/f.png")
image yuri 1g = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/g.png")
image yuri 1h = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/h.png")
image yuri 1i = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/i.png")
image yuri 1j = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/j.png")
image yuri 1k = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/k.png")
image yuri 1l = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/l.png")
image yuri 1m = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/m.png")
image yuri 1n = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/n.png")
image yuri 1o = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/o.png")
image yuri 1p = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/p.png")
image yuri 1q = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/q.png")
image yuri 1r = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/r.png")
image yuri 1s = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/s.png")
image yuri 1t = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/t.png")
image yuri 1u = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/u.png")
image yuri 1v = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/v.png")
image yuri 1w = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/w.png")

image yuri 1y1 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y1.png")
image yuri 1y2 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y2.png")
image yuri 1y3 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y3.png")
image yuri 1y4 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y4.png")
image yuri 1y5 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y5.png")
image yuri 1y6 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y6.png")
image yuri 1y7 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/1r.png", (0, 0), "yuri/y7.png")

image yuri 2a = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/a.png")
image yuri 2b = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/b.png")
image yuri 2c = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/c.png")
image yuri 2d = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/d.png")
image yuri 2e = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/e.png")
image yuri 2f = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/f.png")
image yuri 2g = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/g.png")
image yuri 2h = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/h.png")
image yuri 2i = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/i.png")
image yuri 2j = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/j.png")
image yuri 2k = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/k.png")
image yuri 2l = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/l.png")
image yuri 2m = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/m.png")
image yuri 2n = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/n.png")
image yuri 2o = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/o.png")
image yuri 2p = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/p.png")
image yuri 2q = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/q.png")
image yuri 2r = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/r.png")
image yuri 2s = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/s.png")
image yuri 2t = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/t.png")
image yuri 2u = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/u.png")
image yuri 2v = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/v.png")
image yuri 2w = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/w.png")

image yuri 2y1 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y1.png")
image yuri 2y2 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y2.png")
image yuri 2y3 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y3.png")
image yuri 2y4 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y4.png")
image yuri 2y5 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y5.png")
image yuri 2y6 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y6.png")
image yuri 2y7 = im.Composite((960, 960), (0, 0), "yuri/1l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y7.png")

image yuri 3a = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/a.png")
image yuri 3b = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/b.png")
image yuri 3c = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/c.png")
image yuri 3d = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/d.png")
image yuri 3e = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/e.png")
image yuri 3f = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/f.png")
image yuri 3g = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/g.png")
image yuri 3h = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/h.png")
image yuri 3i = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/i.png")
image yuri 3j = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/j.png")
image yuri 3k = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/k.png")
image yuri 3l = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/l.png")
image yuri 3m = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/m.png")
image yuri 3n = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/n.png")
image yuri 3o = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/o.png")
image yuri 3p = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/p.png")
image yuri 3q = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/q.png")
image yuri 3r = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/r.png")
image yuri 3s = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/s.png")
image yuri 3t = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/t.png")
image yuri 3u = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/u.png")
image yuri 3v = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/v.png")
image yuri 3w = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/w.png")

image yuri 3y1 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y1.png")
image yuri 3y2 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y2.png")
image yuri 3y3 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y3.png")
image yuri 3y4 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y4.png")
image yuri 3y5 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y5.png")
image yuri 3y6 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y6.png")
image yuri 3y7 = im.Composite((960, 960), (0, 0), "yuri/2l.png", (0, 0), "yuri/2r.png", (0, 0), "yuri/y7.png")

image yuri 4a = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/a2.png")
image yuri 4b = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/b2.png")
image yuri 4c = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/c2.png")
image yuri 4d = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/d2.png")
image yuri 4e = im.Composite((960, 960), (0, 0), "yuri/3.png", (0, 0), "yuri/e2.png")

image yuri 1ba = im.Composite((960, 960), (0, 0), "yuri/a.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bb = im.Composite((960, 960), (0, 0), "yuri/b.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bc = im.Composite((960, 960), (0, 0), "yuri/c.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bd = im.Composite((960, 960), (0, 0), "yuri/d.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1be = im.Composite((960, 960), (0, 0), "yuri/e.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bf = im.Composite((960, 960), (0, 0), "yuri/f.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bg = im.Composite((960, 960), (0, 0), "yuri/g.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bh = im.Composite((960, 960), (0, 0), "yuri/h.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bi = im.Composite((960, 960), (0, 0), "yuri/i.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bj = im.Composite((960, 960), (0, 0), "yuri/j.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bk = im.Composite((960, 960), (0, 0), "yuri/k.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bl = im.Composite((960, 960), (0, 0), "yuri/l.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bm = im.Composite((960, 960), (0, 0), "yuri/m.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bn = im.Composite((960, 960), (0, 0), "yuri/n.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bo = im.Composite((960, 960), (0, 0), "yuri/o.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bp = im.Composite((960, 960), (0, 0), "yuri/p.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bq = im.Composite((960, 960), (0, 0), "yuri/q.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1br = im.Composite((960, 960), (0, 0), "yuri/r.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bs = im.Composite((960, 960), (0, 0), "yuri/s.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bt = im.Composite((960, 960), (0, 0), "yuri/t.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bu = im.Composite((960, 960), (0, 0), "yuri/u.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bv = im.Composite((960, 960), (0, 0), "yuri/v.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")
image yuri 1bw = im.Composite((960, 960), (0, 0), "yuri/w.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/1br.png")

image yuri 2ba = im.Composite((960, 960), (0, 0), "yuri/a.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bb = im.Composite((960, 960), (0, 0), "yuri/b.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bc = im.Composite((960, 960), (0, 0), "yuri/c.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bd = im.Composite((960, 960), (0, 0), "yuri/d.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2be = im.Composite((960, 960), (0, 0), "yuri/e.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bf = im.Composite((960, 960), (0, 0), "yuri/f.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bg = im.Composite((960, 960), (0, 0), "yuri/g.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bh = im.Composite((960, 960), (0, 0), "yuri/h.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bi = im.Composite((960, 960), (0, 0), "yuri/i.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bj = im.Composite((960, 960), (0, 0), "yuri/j.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bk = im.Composite((960, 960), (0, 0), "yuri/k.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bl = im.Composite((960, 960), (0, 0), "yuri/l.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bm = im.Composite((960, 960), (0, 0), "yuri/m.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bn = im.Composite((960, 960), (0, 0), "yuri/n.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bo = im.Composite((960, 960), (0, 0), "yuri/o.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bp = im.Composite((960, 960), (0, 0), "yuri/p.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bq = im.Composite((960, 960), (0, 0), "yuri/q.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2br = im.Composite((960, 960), (0, 0), "yuri/r.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bs = im.Composite((960, 960), (0, 0), "yuri/s.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bt = im.Composite((960, 960), (0, 0), "yuri/t.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bu = im.Composite((960, 960), (0, 0), "yuri/u.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bv = im.Composite((960, 960), (0, 0), "yuri/v.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")
image yuri 2bw = im.Composite((960, 960), (0, 0), "yuri/w.png", (0, 0), "yuri/1bl.png", (0, 0), "yuri/2br.png")

image yuri 3ba = im.Composite((960, 960), (0, 0), "yuri/a.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bb = im.Composite((960, 960), (0, 0), "yuri/b.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bc = im.Composite((960, 960), (0, 0), "yuri/c.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bd = im.Composite((960, 960), (0, 0), "yuri/d.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3be = im.Composite((960, 960), (0, 0), "yuri/e.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bf = im.Composite((960, 960), (0, 0), "yuri/f.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bg = im.Composite((960, 960), (0, 0), "yuri/g.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bh = im.Composite((960, 960), (0, 0), "yuri/h.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bi = im.Composite((960, 960), (0, 0), "yuri/i.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bj = im.Composite((960, 960), (0, 0), "yuri/j.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bk = im.Composite((960, 960), (0, 0), "yuri/k.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bl = im.Composite((960, 960), (0, 0), "yuri/l.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bm = im.Composite((960, 960), (0, 0), "yuri/m.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bn = im.Composite((960, 960), (0, 0), "yuri/n.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bo = im.Composite((960, 960), (0, 0), "yuri/o.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bp = im.Composite((960, 960), (0, 0), "yuri/p.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bq = im.Composite((960, 960), (0, 0), "yuri/q.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3br = im.Composite((960, 960), (0, 0), "yuri/r.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bs = im.Composite((960, 960), (0, 0), "yuri/s.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bt = im.Composite((960, 960), (0, 0), "yuri/t.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bu = im.Composite((960, 960), (0, 0), "yuri/u.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bv = im.Composite((960, 960), (0, 0), "yuri/v.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")
image yuri 3bw = im.Composite((960, 960), (0, 0), "yuri/w.png", (0, 0), "yuri/2bl.png", (0, 0), "yuri/2br.png")

image yuri 4ba = im.Composite((960, 960), (0, 0), "yuri/a2.png", (0, 0), "yuri/3b.png")
image yuri 4bb = im.Composite((960, 960), (0, 0), "yuri/b2.png", (0, 0), "yuri/3b.png")
image yuri 4bc = im.Composite((960, 960), (0, 0), "yuri/c2.png", (0, 0), "yuri/3b.png")
image yuri 4bd = im.Composite((960, 960), (0, 0), "yuri/d2.png", (0, 0), "yuri/3b.png")
image yuri 4be = im.Composite((960, 960), (0, 0), "yuri/e2.png", (0, 0), "yuri/3b.png")

image yuri cuts = "yuri/cuts.png"

image yuri dragon:
    "yuri 3"
    0.25
    parallel:
        "yuri/dragon1.png"
        0.01
        "yuri/dragon2.png"
        0.01
        repeat
    parallel:
        0.01
        choice:
            xoffset -1
            xoffset -2
            xoffset -5
            xoffset -6
            xoffset -9
            xoffset -10
        0.01
        xoffset 0
        repeat
    time 0.55
    xoffset 0
    "yuri 3"


image monika 1 = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/a.png")
image monika 2 = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/a.png")
image monika 3 = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/a.png")
image monika 4 = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/a.png")
image monika 5 = im.Composite((960, 960), (0, 0), "monika/3a.png")

image monika 1a = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/a.png")
image monika 1b = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/b.png")
image monika 1c = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/c.png")
image monika 1d = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/d.png")
image monika 1e = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/e.png")
image monika 1f = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/f.png")
image monika 1g = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/g.png")
image monika 1h = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/h.png")
image monika 1i = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/i.png")
image monika 1j = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/j.png")
image monika 1k = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/k.png")
image monika 1l = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/l.png")
image monika 1m = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/m.png")
image monika 1n = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/n.png")
image monika 1o = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/o.png")
image monika 1p = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/p.png")
image monika 1q = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/q.png")
image monika 1r = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/r.png")

image monika 2a = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/a.png")
image monika 2b = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/b.png")
image monika 2c = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/c.png")
image monika 2d = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/d.png")
image monika 2e = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/e.png")
image monika 2f = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/f.png")
image monika 2g = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/g.png")
image monika 2h = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/h.png")
image monika 2i = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/i.png")
image monika 2j = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/j.png")
image monika 2k = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/k.png")
image monika 2l = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/l.png")
image monika 2m = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/m.png")
image monika 2n = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/n.png")
image monika 2o = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/o.png")
image monika 2p = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/p.png")
image monika 2q = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/q.png")
image monika 2r = im.Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/2r.png", (0, 0), "monika/r.png")

image monika 3a = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/a.png")
image monika 3b = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/b.png")
image monika 3c = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/c.png")
image monika 3d = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/d.png")
image monika 3e = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/e.png")
image monika 3f = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/f.png")
image monika 3g = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/g.png")
image monika 3h = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/h.png")
image monika 3i = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/i.png")
image monika 3j = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/j.png")
image monika 3k = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/k.png")
image monika 3l = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/l.png")
image monika 3m = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/m.png")
image monika 3n = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/n.png")
image monika 3o = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/o.png")
image monika 3p = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/p.png")
image monika 3q = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/q.png")
image monika 3r = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/1r.png", (0, 0), "monika/r.png")

image monika 4a = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/a.png")
image monika 4b = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/b.png")
image monika 4c = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/c.png")
image monika 4d = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/d.png")
image monika 4e = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/e.png")
image monika 4f = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/f.png")
image monika 4g = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/g.png")
image monika 4h = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/h.png")
image monika 4i = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/i.png")
image monika 4j = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/j.png")
image monika 4k = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/k.png")
image monika 4l = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/l.png")
image monika 4m = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/m.png")
image monika 4n = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/n.png")
image monika 4o = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/o.png")
image monika 4p = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/p.png")
image monika 4q = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/q.png")
image monika 4r = im.Composite((960, 960), (0, 0), "monika/2l.png", (0, 0), "monika/2r.png", (0, 0), "monika/r.png")

image monika 5a = im.Composite((960, 960), (0, 0), "monika/3a.png")
image monika 5b = im.Composite((960, 960), (0, 0), "monika/3b.png")

image monika 1ba = im.Composite((960, 960), (0, 0), "mod_assets/characters/monika/1bl.png", (0, 0), "mod_assets/characters/monika/1br.png", (0, 0), "monika/a.png")
image monika 1bb = im.Composite((960, 960), (0, 0), "mod_assets/characters/monika/1bl.png", (0, 0), "mod_assets/characters/monika/1br.png", (0, 0), "monika/b.png")
image monika 1bc = im.Composite((960, 960), (0, 0), "mod_assets/characters/monika/1bl.png", (0, 0), "mod_assets/characters/monika/1br.png", (0, 0), "monika/c.png")
image monika 1bd = im.Composite((960, 960), (0, 0), "mod_assets/characters/monika/1bl.png", (0, 0), "mod_assets/characters/monika/1br.png", (0, 0), "monika/d.png")
image monika 1be = im.Composite((960, 960), (0, 0), "mod_assets/characters/monika/1bl.png", (0, 0), "mod_assets/characters/monika/1br.png", (0, 0), "monika/e.png")
image monika 1bf = im.Composite((960, 960), (0, 0), "mod_assets/characters/monika/1bl.png", (0, 0), "mod_assets/characters/monika/1br.png", (0, 0), "monika/f.png")
image monika 1bg = im.Composite((960, 960), (0, 0), "mod_assets/characters/monika/1bl.png", (0, 0), "mod_assets/characters/monika/1br.png", (0, 0), "monika/g.png")
image monika 1bh = im.Composite((960, 960), (0, 0), "mod_assets/characters/monika/1bl.png", (0, 0), "mod_assets/characters/monika/1br.png", (0, 0), "monika/h.png")
image monika 1bi = im.Composite((960, 960), (0, 0), "mod_assets/characters/monika/1bl.png", (0, 0), "mod_assets/characters/monika/1br.png", (0, 0), "monika/i.png")
image monika 1bj = im.Composite((960, 960), (0, 0), "mod_assets/characters/monika/1bl.png", (0, 0), "mod_assets/characters/monika/1br.png", (0, 0), "monika/j.png")
image monika 1bk = im.Composite((960, 960), (0, 0), "mod_assets/characters/monika/1bl.png", (0, 0), "mod_assets/characters/monika/1br.png", (0, 0), "monika/k.png")
image monika 1bl = im.Composite((960, 960), (0, 0), "mod_assets/characters/monika/1bl.png", (0, 0), "mod_assets/characters/monika/1br.png", (0, 0), "monika/l.png")
image monika 1bm = im.Composite((960, 960), (0, 0), "mod_assets/characters/monika/1bl.png", (0, 0), "mod_assets/characters/monika/1br.png", (0, 0), "monika/m.png")
image monika 1bn = im.Composite((960, 960), (0, 0), "mod_assets/characters/monika/1bl.png", (0, 0), "mod_assets/characters/monika/1br.png", (0, 0), "monika/n.png")
image monika 1bo = im.Composite((960, 960), (0, 0), "mod_assets/characters/monika/1bl.png", (0, 0), "mod_assets/characters/monika/1br.png", (0, 0), "monika/o.png")
image monika 1bp = im.Composite((960, 960), (0, 0), "mod_assets/characters/monika/1bl.png", (0, 0), "mod_assets/characters/monika/1br.png", (0, 0), "monika/p.png")
image monika 1bq = im.Composite((960, 960), (0, 0), "mod_assets/characters/monika/1bl.png", (0, 0), "mod_assets/characters/monika/1br.png", (0, 0), "monika/q.png")
image monika 1br = im.Composite((960, 960), (0, 0), "mod_assets/characters/monika/1bl.png", (0, 0), "mod_assets/characters/monika/1br.png", (0, 0), "monika/r.png")

image monika 2ba = im.Composite((960, 960), (0, 0), "mod_assets/characters/monika/1bl.png", (0, 0), "mod_assets/characters/monika/2br.png", (0, 0), "monika/a.png")
image monika 2bb = im.Composite((960, 960), (0, 0), "mod_assets/characters/monika/1bl.png", (0, 0), "mod_assets/characters/monika/2br.png", (0, 0), "monika/b.png")
image monika 2bc = im.Composite((960, 960), (0, 0), "mod_assets/characters/monika/1bl.png", (0, 0), "mod_assets/characters/monika/2br.png", (0, 0), "monika/c.png")
image monika 2bd = im.Composite((960, 960), (0, 0), "mod_assets/characters/monika/1bl.png", (0, 0), "mod_assets/characters/monika/2br.png", (0, 0), "monika/d.png")
image monika 2be = im.Composite((960, 960), (0, 0), "mod_assets/characters/monika/1bl.png", (0, 0), "mod_assets/characters/monika/2br.png", (0, 0), "monika/e.png")
image monika 2bf = im.Composite((960, 960), (0, 0), "mod_assets/characters/monika/1bl.png", (0, 0), "mod_assets/characters/monika/2br.png", (0, 0), "monika/f.png")
image monika 2bg = im.Composite((960, 960), (0, 0), "mod_assets/characters/monika/1bl.png", (0, 0), "mod_assets/characters/monika/2br.png", (0, 0), "monika/g.png")
image monika 2bh = im.Composite((960, 960), (0, 0), "mod_assets/characters/monika/1bl.png", (0, 0), "mod_assets/characters/monika/2br.png", (0, 0), "monika/h.png")
image monika 2bi = im.Composite((960, 960), (0, 0), "mod_assets/characters/monika/1bl.png", (0, 0), "mod_assets/characters/monika/2br.png", (0, 0), "monika/i.png")
image monika 2bj = im.Composite((960, 960), (0, 0), "mod_assets/characters/monika/1bl.png", (0, 0), "mod_assets/characters/monika/2br.png", (0, 0), "monika/j.png")
image monika 2bk = im.Composite((960, 960), (0, 0), "mod_assets/characters/monika/1bl.png", (0, 0), "mod_assets/characters/monika/2br.png", (0, 0), "monika/k.png")
image monika 2bl = im.Composite((960, 960), (0, 0), "mod_assets/characters/monika/1bl.png", (0, 0), "mod_assets/characters/monika/2br.png", (0, 0), "monika/l.png")
image monika 2bm = im.Composite((960, 960), (0, 0), "mod_assets/characters/monika/1bl.png", (0, 0), "mod_assets/characters/monika/2br.png", (0, 0), "monika/m.png")
image monika 2bn = im.Composite((960, 960), (0, 0), "mod_assets/characters/monika/1bl.png", (0, 0), "mod_assets/characters/monika/2br.png", (0, 0), "monika/n.png")
image monika 2bo = im.Composite((960, 960), (0, 0), "mod_assets/characters/monika/1bl.png", (0, 0), "mod_assets/characters/monika/2br.png", (0, 0), "monika/o.png")
image monika 2bp = im.Composite((960, 960), (0, 0), "mod_assets/characters/monika/1bl.png", (0, 0), "mod_assets/characters/monika/2br.png", (0, 0), "monika/p.png")
image monika 2bq = im.Composite((960, 960), (0, 0), "mod_assets/characters/monika/1bl.png", (0, 0), "mod_assets/characters/monika/2br.png", (0, 0), "monika/q.png")
image monika 2br = im.Composite((960, 960), (0, 0), "mod_assets/characters/monika/1bl.png", (0, 0), "mod_assets/characters/monika/2br.png", (0, 0), "monika/r.png")

image monika 3ba = im.Composite((960, 960), (0, 0), "mod_assets/characters/monika/2bl.png", (0, 0), "mod_assets/characters/monika/1br.png", (0, 0), "monika/a.png")
image monika 3bb = im.Composite((960, 960), (0, 0), "mod_assets/characters/monika/2bl.png", (0, 0), "mod_assets/characters/monika/1br.png", (0, 0), "monika/b.png")
image monika 3bc = im.Composite((960, 960), (0, 0), "mod_assets/characters/monika/2bl.png", (0, 0), "mod_assets/characters/monika/1br.png", (0, 0), "monika/c.png")
image monika 3bd = im.Composite((960, 960), (0, 0), "mod_assets/characters/monika/2bl.png", (0, 0), "mod_assets/characters/monika/1br.png", (0, 0), "monika/d.png")
image monika 3be = im.Composite((960, 960), (0, 0), "mod_assets/characters/monika/2bl.png", (0, 0), "mod_assets/characters/monika/1br.png", (0, 0), "monika/e.png")
image monika 3bf = im.Composite((960, 960), (0, 0), "mod_assets/characters/monika/2bl.png", (0, 0), "mod_assets/characters/monika/1br.png", (0, 0), "monika/f.png")
image monika 3bg = im.Composite((960, 960), (0, 0), "mod_assets/characters/monika/2bl.png", (0, 0), "mod_assets/characters/monika/1br.png", (0, 0), "monika/g.png")
image monika 3bh = im.Composite((960, 960), (0, 0), "mod_assets/characters/monika/2bl.png", (0, 0), "mod_assets/characters/monika/1br.png", (0, 0), "monika/h.png")
image monika 3bi = im.Composite((960, 960), (0, 0), "mod_assets/characters/monika/2bl.png", (0, 0), "mod_assets/characters/monika/1br.png", (0, 0), "monika/i.png")
image monika 3bj = im.Composite((960, 960), (0, 0), "mod_assets/characters/monika/2bl.png", (0, 0), "mod_assets/characters/monika/1br.png", (0, 0), "monika/j.png")
image monika 3bk = im.Composite((960, 960), (0, 0), "mod_assets/characters/monika/2bl.png", (0, 0), "mod_assets/characters/monika/1br.png", (0, 0), "monika/k.png")
image monika 3bl = im.Composite((960, 960), (0, 0), "mod_assets/characters/monika/2bl.png", (0, 0), "mod_assets/characters/monika/1br.png", (0, 0), "monika/l.png")
image monika 3bm = im.Composite((960, 960), (0, 0), "mod_assets/characters/monika/2bl.png", (0, 0), "mod_assets/characters/monika/1br.png", (0, 0), "monika/m.png")
image monika 3bn = im.Composite((960, 960), (0, 0), "mod_assets/characters/monika/2bl.png", (0, 0), "mod_assets/characters/monika/1br.png", (0, 0), "monika/n.png")
image monika 3bo = im.Composite((960, 960), (0, 0), "mod_assets/characters/monika/2bl.png", (0, 0), "mod_assets/characters/monika/1br.png", (0, 0), "monika/o.png")
image monika 3bp = im.Composite((960, 960), (0, 0), "mod_assets/characters/monika/2bl.png", (0, 0), "mod_assets/characters/monika/1br.png", (0, 0), "monika/p.png")
image monika 3bq = im.Composite((960, 960), (0, 0), "mod_assets/characters/monika/2bl.png", (0, 0), "mod_assets/characters/monika/1br.png", (0, 0), "monika/q.png")
image monika 3br = im.Composite((960, 960), (0, 0), "mod_assets/characters/monika/2bl.png", (0, 0), "mod_assets/characters/monika/1br.png", (0, 0), "monika/r.png")

image monika 4ba = im.Composite((960, 960), (0, 0), "mod_assets/characters/monika/2bl.png", (0, 0), "mod_assets/characters/monika/2br.png", (0, 0), "monika/a.png")
image monika 4bb = im.Composite((960, 960), (0, 0), "mod_assets/characters/monika/2bl.png", (0, 0), "mod_assets/characters/monika/2br.png", (0, 0), "monika/b.png")
image monika 4bc = im.Composite((960, 960), (0, 0), "mod_assets/characters/monika/2bl.png", (0, 0), "mod_assets/characters/monika/2br.png", (0, 0), "monika/c.png")
image monika 4bd = im.Composite((960, 960), (0, 0), "mod_assets/characters/monika/2bl.png", (0, 0), "mod_assets/characters/monika/2br.png", (0, 0), "monika/d.png")
image monika 4be = im.Composite((960, 960), (0, 0), "mod_assets/characters/monika/2bl.png", (0, 0), "mod_assets/characters/monika/2br.png", (0, 0), "monika/e.png")
image monika 4bf = im.Composite((960, 960), (0, 0), "mod_assets/characters/monika/2bl.png", (0, 0), "mod_assets/characters/monika/2br.png", (0, 0), "monika/f.png")
image monika 4bg = im.Composite((960, 960), (0, 0), "mod_assets/characters/monika/2bl.png", (0, 0), "mod_assets/characters/monika/2br.png", (0, 0), "monika/g.png")
image monika 4bh = im.Composite((960, 960), (0, 0), "mod_assets/characters/monika/2bl.png", (0, 0), "mod_assets/characters/monika/2br.png", (0, 0), "monika/h.png")
image monika 4bi = im.Composite((960, 960), (0, 0), "mod_assets/characters/monika/2bl.png", (0, 0), "mod_assets/characters/monika/2br.png", (0, 0), "monika/i.png")
image monika 4bj = im.Composite((960, 960), (0, 0), "mod_assets/characters/monika/2bl.png", (0, 0), "mod_assets/characters/monika/2br.png", (0, 0), "monika/j.png")
image monika 4bk = im.Composite((960, 960), (0, 0), "mod_assets/characters/monika/2bl.png", (0, 0), "mod_assets/characters/monika/2br.png", (0, 0), "monika/k.png")
image monika 4bl = im.Composite((960, 960), (0, 0), "mod_assets/characters/monika/2bl.png", (0, 0), "mod_assets/characters/monika/2br.png", (0, 0), "monika/l.png")
image monika 4bm = im.Composite((960, 960), (0, 0), "mod_assets/characters/monika/2bl.png", (0, 0), "mod_assets/characters/monika/2br.png", (0, 0), "monika/m.png")
image monika 4bn = im.Composite((960, 960), (0, 0), "mod_assets/characters/monika/2bl.png", (0, 0), "mod_assets/characters/monika/2br.png", (0, 0), "monika/n.png")
image monika 4bo = im.Composite((960, 960), (0, 0), "mod_assets/characters/monika/2bl.png", (0, 0), "mod_assets/characters/monika/2br.png", (0, 0), "monika/o.png")
image monika 4bp = im.Composite((960, 960), (0, 0), "mod_assets/characters/monika/2bl.png", (0, 0), "mod_assets/characters/monika/2br.png", (0, 0), "monika/p.png")
image monika 4bq = im.Composite((960, 960), (0, 0), "mod_assets/characters/monika/2bl.png", (0, 0), "mod_assets/characters/monika/2br.png", (0, 0), "monika/q.png")
image monika 4br = im.Composite((960, 960), (0, 0), "mod_assets/characters/monika/2bl.png", (0, 0), "mod_assets/characters/monika/2br.png", (0, 0), "monika/r.png")

image monika 5ba = im.Composite((960, 960), (0, 0), "monika/3ba.png")

image monika g1:
    "monika/g1.png"
    xoffset 35 yoffset 55
    parallel:
        zoom 1.00
        linear 0.10 zoom 1.03
        repeat
    parallel:
        xoffset 35
        0.20
        xoffset 0
        0.05
        xoffset -10
        0.05
        xoffset 0
        0.05
        xoffset -80
        0.05
        repeat
    time 1.25
    xoffset 0 yoffset 0 zoom 1.00
    "monika 3"

image monika g2:
    block:
        choice:
            "monika/g2.png"
        choice:
            "monika/g3.png"
        choice:
            "monika/g4.png"
    block:
        choice:
            pause 0.05
        choice:
            pause 0.1
        choice:
            pause 0.15
        choice:
            pause 0.2
    repeat


image akira 1a = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/1l.png", (0, 0), "mod_assets/characters/akira/1r.png", (0, 0), "mod_assets/characters/akira/a.png")
image akira 1aa = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/1l.png", (0, 0), "mod_assets/characters/akira/1r.png", (0, 0), "mod_assets/characters/akira/a.png")
image akira 1ab = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/1l.png", (0, 0), "mod_assets/characters/akira/1r.png", (0, 0), "mod_assets/characters/akira/b.png")
image akira 1ac = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/1l.png", (0, 0), "mod_assets/characters/akira/1r.png", (0, 0), "mod_assets/characters/akira/c.png")
image akira 1ad = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/1l.png", (0, 0), "mod_assets/characters/akira/1r.png", (0, 0), "mod_assets/characters/akira/d.png")
image akira 1ae = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/1l.png", (0, 0), "mod_assets/characters/akira/1r.png", (0, 0), "mod_assets/characters/akira/e.png")
image akira 1af = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/1l.png", (0, 0), "mod_assets/characters/akira/1r.png", (0, 0), "mod_assets/characters/akira/f.png")
image akira 1ag = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/1l.png", (0, 0), "mod_assets/characters/akira/1r.png", (0, 0), "mod_assets/characters/akira/g.png")
image akira 1ah = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/1l.png", (0, 0), "mod_assets/characters/akira/1r.png", (0, 0), "mod_assets/characters/akira/h.png")
image akira 1ai = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/1l.png", (0, 0), "mod_assets/characters/akira/1r.png", (0, 0), "mod_assets/characters/akira/i.png")
image akira 1aj = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/1l.png", (0, 0), "mod_assets/characters/akira/1r.png", (0, 0), "mod_assets/characters/akira/j.png")
image akira 1ak = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/1l.png", (0, 0), "mod_assets/characters/akira/1r.png", (0, 0), "mod_assets/characters/akira/k.png")
image akira 1al = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/1l.png", (0, 0), "mod_assets/characters/akira/1r.png", (0, 0), "mod_assets/characters/akira/l.png")
image akira 1am = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/1l.png", (0, 0), "mod_assets/characters/akira/1r.png", (0, 0), "mod_assets/characters/akira/m.png")
image akira 1an = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/1l.png", (0, 0), "mod_assets/characters/akira/1r.png", (0, 0), "mod_assets/characters/akira/n.png")
image akira 1ao = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/1l.png", (0, 0), "mod_assets/characters/akira/1r.png", (0, 0), "mod_assets/characters/akira/o.png")
image akira 1ap = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/1l.png", (0, 0), "mod_assets/characters/akira/1r.png", (0, 0), "mod_assets/characters/akira/p.png")

image akira 1b = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/1b.png", (0, 0), "mod_assets/characters/akira/a.png")
image akira 1ba = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/1b.png", (0, 0), "mod_assets/characters/akira/a.png")
image akira 1bb = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/1b.png", (0, 0), "mod_assets/characters/akira/b.png")
image akira 1bc = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/1b.png", (0, 0), "mod_assets/characters/akira/c.png")
image akira 1bd = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/1b.png", (0, 0), "mod_assets/characters/akira/d.png")
image akira 1be = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/1b.png", (0, 0), "mod_assets/characters/akira/e.png")
image akira 1bf = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/1b.png", (0, 0), "mod_assets/characters/akira/f.png")
image akira 1bg = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/1b.png", (0, 0), "mod_assets/characters/akira/g.png")
image akira 1bh = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/1b.png", (0, 0), "mod_assets/characters/akira/h.png")
image akira 1bi = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/1b.png", (0, 0), "mod_assets/characters/akira/i.png")
image akira 1bj = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/1b.png", (0, 0), "mod_assets/characters/akira/j.png")
image akira 1bk = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/1b.png", (0, 0), "mod_assets/characters/akira/k.png")
image akira 1bl = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/1b.png", (0, 0), "mod_assets/characters/akira/l.png")
image akira 1bm = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/1b.png", (0, 0), "mod_assets/characters/akira/m.png")
image akira 1bn = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/1b.png", (0, 0), "mod_assets/characters/akira/n.png")
image akira 1bo = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/1b.png", (0, 0), "mod_assets/characters/akira/o.png")
image akira 1bp = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/1b.png", (0, 0), "mod_assets/characters/akira/p.png")

image akira 1c = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/1c.png", (0, 0), "mod_assets/characters/akira/a.png")
image akira 1ca = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/1c.png", (0, 0), "mod_assets/characters/akira/a.png")
image akira 1cb = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/1c.png", (0, 0), "mod_assets/characters/akira/b.png")
image akira 1cc = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/1c.png", (0, 0), "mod_assets/characters/akira/c.png")
image akira 1cd = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/1c.png", (0, 0), "mod_assets/characters/akira/d.png")
image akira 1ce = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/1c.png", (0, 0), "mod_assets/characters/akira/e.png")
image akira 1cf = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/1c.png", (0, 0), "mod_assets/characters/akira/f.png")
image akira 1cg = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/1c.png", (0, 0), "mod_assets/characters/akira/g.png")
image akira 1ch = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/1c.png", (0, 0), "mod_assets/characters/akira/h.png")
image akira 1ci = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/1c.png", (0, 0), "mod_assets/characters/akira/i.png")
image akira 1cj = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/1c.png", (0, 0), "mod_assets/characters/akira/j.png")
image akira 1ck = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/1c.png", (0, 0), "mod_assets/characters/akira/k.png")
image akira 1cl = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/1c.png", (0, 0), "mod_assets/characters/akira/l.png")
image akira 1cm = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/1c.png", (0, 0), "mod_assets/characters/akira/m.png")
image akira 1cn = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/1c.png", (0, 0), "mod_assets/characters/akira/n.png")
image akira 1co = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/1c.png", (0, 0), "mod_assets/characters/akira/o.png")
image akira 1cp = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/1c.png", (0, 0), "mod_assets/characters/akira/p.png")

image akira 2a = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/2l.png", (0, 0), "mod_assets/characters/akira/2r.png", (0, 0), "mod_assets/characters/akira/a.png")
image akira 2aa = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/2l.png", (0, 0), "mod_assets/characters/akira/2r.png", (0, 0), "mod_assets/characters/akira/a.png")
image akira 2ab = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/2l.png", (0, 0), "mod_assets/characters/akira/2r.png", (0, 0), "mod_assets/characters/akira/b.png")
image akira 2ac = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/2l.png", (0, 0), "mod_assets/characters/akira/2r.png", (0, 0), "mod_assets/characters/akira/c.png")
image akira 2ad = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/2l.png", (0, 0), "mod_assets/characters/akira/2r.png", (0, 0), "mod_assets/characters/akira/d.png")
image akira 2ae = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/2l.png", (0, 0), "mod_assets/characters/akira/2r.png", (0, 0), "mod_assets/characters/akira/e.png")
image akira 2af = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/2l.png", (0, 0), "mod_assets/characters/akira/2r.png", (0, 0), "mod_assets/characters/akira/f.png")
image akira 2ag = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/2l.png", (0, 0), "mod_assets/characters/akira/2r.png", (0, 0), "mod_assets/characters/akira/g.png")
image akira 2ah = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/2l.png", (0, 0), "mod_assets/characters/akira/2r.png", (0, 0), "mod_assets/characters/akira/h.png")
image akira 2ai = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/2l.png", (0, 0), "mod_assets/characters/akira/2r.png", (0, 0), "mod_assets/characters/akira/i.png")
image akira 2aj = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/2l.png", (0, 0), "mod_assets/characters/akira/2r.png", (0, 0), "mod_assets/characters/akira/j.png")
image akira 2ak = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/2l.png", (0, 0), "mod_assets/characters/akira/2r.png", (0, 0), "mod_assets/characters/akira/k.png")
image akira 2al = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/2l.png", (0, 0), "mod_assets/characters/akira/2r.png", (0, 0), "mod_assets/characters/akira/l.png")
image akira 2am = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/2l.png", (0, 0), "mod_assets/characters/akira/2r.png", (0, 0), "mod_assets/characters/akira/m.png")
image akira 2an = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/2l.png", (0, 0), "mod_assets/characters/akira/2r.png", (0, 0), "mod_assets/characters/akira/n.png")
image akira 2ao = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/2l.png", (0, 0), "mod_assets/characters/akira/2r.png", (0, 0), "mod_assets/characters/akira/o.png")
image akira 2ap = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/2l.png", (0, 0), "mod_assets/characters/akira/2r.png", (0, 0), "mod_assets/characters/akira/p.png")

image akira 2b = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/2b.png", (0, 0), "mod_assets/characters/akira/a.png")
image akira 2ba = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/2b.png", (0, 0), "mod_assets/characters/akira/a.png")
image akira 2bb = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/2b.png", (0, 0), "mod_assets/characters/akira/b.png")
image akira 2bc = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/2b.png", (0, 0), "mod_assets/characters/akira/c.png")
image akira 2bd = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/2b.png", (0, 0), "mod_assets/characters/akira/d.png")
image akira 2be = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/2b.png", (0, 0), "mod_assets/characters/akira/e.png")
image akira 2bf = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/2b.png", (0, 0), "mod_assets/characters/akira/f.png")
image akira 2bg = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/2b.png", (0, 0), "mod_assets/characters/akira/g.png")
image akira 2bh = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/2b.png", (0, 0), "mod_assets/characters/akira/h.png")
image akira 2bi = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/2b.png", (0, 0), "mod_assets/characters/akira/i.png")
image akira 2bj = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/2b.png", (0, 0), "mod_assets/characters/akira/j.png")
image akira 2bk = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/2b.png", (0, 0), "mod_assets/characters/akira/k.png")
image akira 2bl = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/2b.png", (0, 0), "mod_assets/characters/akira/l.png")
image akira 2bm = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/2b.png", (0, 0), "mod_assets/characters/akira/m.png")
image akira 2bn = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/2b.png", (0, 0), "mod_assets/characters/akira/n.png")
image akira 2bo = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/2b.png", (0, 0), "mod_assets/characters/akira/o.png")
image akira 2bp = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/2b.png", (0, 0), "mod_assets/characters/akira/p.png")

image akira 2c = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/2c.png", (0, 0), "mod_assets/characters/akira/a.png")
image akira 2ca = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/2c.png", (0, 0), "mod_assets/characters/akira/a.png")
image akira 2cb = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/2c.png", (0, 0), "mod_assets/characters/akira/b.png")
image akira 2cc = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/2c.png", (0, 0), "mod_assets/characters/akira/c.png")
image akira 2cd = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/2c.png", (0, 0), "mod_assets/characters/akira/d.png")
image akira 2ce = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/2c.png", (0, 0), "mod_assets/characters/akira/e.png")
image akira 2cf = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/2c.png", (0, 0), "mod_assets/characters/akira/f.png")
image akira 2cg = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/2c.png", (0, 0), "mod_assets/characters/akira/g.png")
image akira 2ch = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/2c.png", (0, 0), "mod_assets/characters/akira/h.png")
image akira 2ci = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/2c.png", (0, 0), "mod_assets/characters/akira/i.png")
image akira 2cj = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/2c.png", (0, 0), "mod_assets/characters/akira/j.png")
image akira 2ck = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/2c.png", (0, 0), "mod_assets/characters/akira/k.png")
image akira 2cl = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/2c.png", (0, 0), "mod_assets/characters/akira/l.png")
image akira 2cm = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/2c.png", (0, 0), "mod_assets/characters/akira/m.png")
image akira 2cn = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/2c.png", (0, 0), "mod_assets/characters/akira/n.png")
image akira 2co = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/2c.png", (0, 0), "mod_assets/characters/akira/o.png")
image akira 2cp = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/2c.png", (0, 0), "mod_assets/characters/akira/p.png")

image akira 3a = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/3l.png", (0, 0), "mod_assets/characters/akira/2r.png", (0, 0), "mod_assets/characters/akira/a.png")
image akira 3aa = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/3l.png", (0, 0), "mod_assets/characters/akira/2r.png", (0, 0), "mod_assets/characters/akira/a.png")
image akira 3ab = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/3l.png", (0, 0), "mod_assets/characters/akira/2r.png", (0, 0), "mod_assets/characters/akira/b.png")
image akira 3ac = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/3l.png", (0, 0), "mod_assets/characters/akira/2r.png", (0, 0), "mod_assets/characters/akira/c.png")
image akira 3ad = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/3l.png", (0, 0), "mod_assets/characters/akira/2r.png", (0, 0), "mod_assets/characters/akira/d.png")
image akira 3ae = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/3l.png", (0, 0), "mod_assets/characters/akira/2r.png", (0, 0), "mod_assets/characters/akira/e.png")
image akira 3af = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/3l.png", (0, 0), "mod_assets/characters/akira/2r.png", (0, 0), "mod_assets/characters/akira/f.png")
image akira 3ag = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/3l.png", (0, 0), "mod_assets/characters/akira/2r.png", (0, 0), "mod_assets/characters/akira/g.png")
image akira 3ah = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/3l.png", (0, 0), "mod_assets/characters/akira/2r.png", (0, 0), "mod_assets/characters/akira/h.png")
image akira 3ai = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/3l.png", (0, 0), "mod_assets/characters/akira/2r.png", (0, 0), "mod_assets/characters/akira/i.png")
image akira 3aj = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/3l.png", (0, 0), "mod_assets/characters/akira/2r.png", (0, 0), "mod_assets/characters/akira/j.png")
image akira 3ak = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/3l.png", (0, 0), "mod_assets/characters/akira/2r.png", (0, 0), "mod_assets/characters/akira/k.png")
image akira 3al = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/3l.png", (0, 0), "mod_assets/characters/akira/2r.png", (0, 0), "mod_assets/characters/akira/l.png")
image akira 3am = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/3l.png", (0, 0), "mod_assets/characters/akira/2r.png", (0, 0), "mod_assets/characters/akira/m.png")
image akira 3an = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/3l.png", (0, 0), "mod_assets/characters/akira/2r.png", (0, 0), "mod_assets/characters/akira/n.png")
image akira 3ao = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/3l.png", (0, 0), "mod_assets/characters/akira/2r.png", (0, 0), "mod_assets/characters/akira/o.png")
image akira 3ap = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/3l.png", (0, 0), "mod_assets/characters/akira/2r.png", (0, 0), "mod_assets/characters/akira/p.png")

image akira 3a2 = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/3l.png", (0, 0), "mod_assets/characters/akira/1r.png", (0, 0), "mod_assets/characters/akira/a.png")
image akira 3aa2 = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/3l.png", (0, 0), "mod_assets/characters/akira/1r.png", (0, 0), "mod_assets/characters/akira/a.png")
image akira 3ab2 = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/3l.png", (0, 0), "mod_assets/characters/akira/1r.png", (0, 0), "mod_assets/characters/akira/b.png")
image akira 3ac2 = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/3l.png", (0, 0), "mod_assets/characters/akira/1r.png", (0, 0), "mod_assets/characters/akira/c.png")
image akira 3ad2 = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/3l.png", (0, 0), "mod_assets/characters/akira/1r.png", (0, 0), "mod_assets/characters/akira/d.png")
image akira 3ae2 = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/3l.png", (0, 0), "mod_assets/characters/akira/1r.png", (0, 0), "mod_assets/characters/akira/e.png")
image akira 3af2 = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/3l.png", (0, 0), "mod_assets/characters/akira/1r.png", (0, 0), "mod_assets/characters/akira/f.png")
image akira 3ag2 = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/3l.png", (0, 0), "mod_assets/characters/akira/1r.png", (0, 0), "mod_assets/characters/akira/g.png")
image akira 3ah2 = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/3l.png", (0, 0), "mod_assets/characters/akira/1r.png", (0, 0), "mod_assets/characters/akira/h.png")
image akira 3ai2 = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/3l.png", (0, 0), "mod_assets/characters/akira/1r.png", (0, 0), "mod_assets/characters/akira/i.png")
image akira 3aj2 = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/3l.png", (0, 0), "mod_assets/characters/akira/1r.png", (0, 0), "mod_assets/characters/akira/j.png")
image akira 3ak2 = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/3l.png", (0, 0), "mod_assets/characters/akira/1r.png", (0, 0), "mod_assets/characters/akira/k.png")
image akira 3al2 = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/3l.png", (0, 0), "mod_assets/characters/akira/1r.png", (0, 0), "mod_assets/characters/akira/l.png")
image akira 3am2 = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/3l.png", (0, 0), "mod_assets/characters/akira/1r.png", (0, 0), "mod_assets/characters/akira/m.png")
image akira 3an2 = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/3l.png", (0, 0), "mod_assets/characters/akira/1r.png", (0, 0), "mod_assets/characters/akira/n.png")
image akira 3ao2 = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/3l.png", (0, 0), "mod_assets/characters/akira/1r.png", (0, 0), "mod_assets/characters/akira/o.png")
image akira 3ap2 = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/3l.png", (0, 0), "mod_assets/characters/akira/1r.png", (0, 0), "mod_assets/characters/akira/p.png")

image akira 3b = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/3b.png", (0, 0), "mod_assets/characters/akira/a.png")
image akira 3ba = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/3b.png", (0, 0), "mod_assets/characters/akira/a.png")
image akira 3bb = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/3b.png", (0, 0), "mod_assets/characters/akira/b.png")
image akira 3bc = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/3b.png", (0, 0), "mod_assets/characters/akira/c.png")
image akira 3bd = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/3b.png", (0, 0), "mod_assets/characters/akira/d.png")
image akira 3be = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/3b.png", (0, 0), "mod_assets/characters/akira/e.png")
image akira 3bf = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/3b.png", (0, 0), "mod_assets/characters/akira/f.png")
image akira 3bg = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/3b.png", (0, 0), "mod_assets/characters/akira/g.png")
image akira 3bh = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/3b.png", (0, 0), "mod_assets/characters/akira/h.png")
image akira 3bi = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/3b.png", (0, 0), "mod_assets/characters/akira/i.png")
image akira 3bj = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/3b.png", (0, 0), "mod_assets/characters/akira/j.png")
image akira 3bk = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/3b.png", (0, 0), "mod_assets/characters/akira/k.png")
image akira 3bl = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/3b.png", (0, 0), "mod_assets/characters/akira/l.png")
image akira 3bm = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/3b.png", (0, 0), "mod_assets/characters/akira/m.png")
image akira 3bn = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/3b.png", (0, 0), "mod_assets/characters/akira/n.png")
image akira 3bo = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/3b.png", (0, 0), "mod_assets/characters/akira/o.png")
image akira 3bp = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/3b.png", (0, 0), "mod_assets/characters/akira/p.png")

image akira 3c = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/3c.png", (0, 0), "mod_assets/characters/akira/a.png")
image akira 3ca = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/3c.png", (0, 0), "mod_assets/characters/akira/a.png")
image akira 3cb = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/3c.png", (0, 0), "mod_assets/characters/akira/b.png")
image akira 3cc = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/3c.png", (0, 0), "mod_assets/characters/akira/c.png")
image akira 3cd = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/3c.png", (0, 0), "mod_assets/characters/akira/d.png")
image akira 3ce = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/3c.png", (0, 0), "mod_assets/characters/akira/e.png")
image akira 3cf = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/3c.png", (0, 0), "mod_assets/characters/akira/f.png")
image akira 3cg = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/3c.png", (0, 0), "mod_assets/characters/akira/g.png")
image akira 3ch = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/3c.png", (0, 0), "mod_assets/characters/akira/h.png")
image akira 3ci = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/3c.png", (0, 0), "mod_assets/characters/akira/i.png")
image akira 3cj = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/3c.png", (0, 0), "mod_assets/characters/akira/j.png")
image akira 3ck = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/3c.png", (0, 0), "mod_assets/characters/akira/k.png")
image akira 3cl = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/3c.png", (0, 0), "mod_assets/characters/akira/l.png")
image akira 3cm = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/3c.png", (0, 0), "mod_assets/characters/akira/m.png")
image akira 3cn = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/3c.png", (0, 0), "mod_assets/characters/akira/n.png")
image akira 3co = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/3c.png", (0, 0), "mod_assets/characters/akira/o.png")
image akira 3cp = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/3c.png", (0, 0), "mod_assets/characters/akira/p.png")

image akira 4a = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/4.png", (0, 0), "mod_assets/characters/akira/a.png")
image akira 4aa = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/4.png", (0, 0), "mod_assets/characters/akira/a.png")
image akira 4ab = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/4.png", (0, 0), "mod_assets/characters/akira/b.png")
image akira 4ac = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/4.png", (0, 0), "mod_assets/characters/akira/c.png")
image akira 4ad = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/4.png", (0, 0), "mod_assets/characters/akira/d.png")
image akira 4ae = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/4.png", (0, 0), "mod_assets/characters/akira/e.png")
image akira 4af = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/4.png", (0, 0), "mod_assets/characters/akira/f.png")
image akira 4ag = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/4.png", (0, 0), "mod_assets/characters/akira/g.png")
image akira 4ah = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/4.png", (0, 0), "mod_assets/characters/akira/h.png")
image akira 4ai = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/4.png", (0, 0), "mod_assets/characters/akira/i.png")
image akira 4aj = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/4.png", (0, 0), "mod_assets/characters/akira/j.png")
image akira 4ak = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/4.png", (0, 0), "mod_assets/characters/akira/k.png")
image akira 4al = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/4.png", (0, 0), "mod_assets/characters/akira/l.png")
image akira 4am = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/4.png", (0, 0), "mod_assets/characters/akira/m.png")
image akira 4an = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/4.png", (0, 0), "mod_assets/characters/akira/n.png")
image akira 4ao = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/4.png", (0, 0), "mod_assets/characters/akira/o.png")
image akira 4ap = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/4.png", (0, 0), "mod_assets/characters/akira/p.png")

image akira 4b = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/4b.png", (0, 0), "mod_assets/characters/akira/a.png")
image akira 4ba = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/4b.png", (0, 0), "mod_assets/characters/akira/a.png")
image akira 4bb = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/4b.png", (0, 0), "mod_assets/characters/akira/b.png")
image akira 4bc = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/4b.png", (0, 0), "mod_assets/characters/akira/c.png")
image akira 4bd = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/4b.png", (0, 0), "mod_assets/characters/akira/d.png")
image akira 4be = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/4b.png", (0, 0), "mod_assets/characters/akira/e.png")
image akira 4bf = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/4b.png", (0, 0), "mod_assets/characters/akira/f.png")
image akira 4bg = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/4b.png", (0, 0), "mod_assets/characters/akira/g.png")
image akira 4bh = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/4b.png", (0, 0), "mod_assets/characters/akira/h.png")
image akira 4bi = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/4b.png", (0, 0), "mod_assets/characters/akira/i.png")
image akira 4bj = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/4b.png", (0, 0), "mod_assets/characters/akira/j.png")
image akira 4bk = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/4b.png", (0, 0), "mod_assets/characters/akira/k.png")
image akira 4bl = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/4b.png", (0, 0), "mod_assets/characters/akira/l.png")
image akira 4bm = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/4b.png", (0, 0), "mod_assets/characters/akira/m.png")
image akira 4bn = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/4b.png", (0, 0), "mod_assets/characters/akira/n.png")
image akira 4bo = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/4b.png", (0, 0), "mod_assets/characters/akira/o.png")
image akira 4bp = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/4b.png", (0, 0), "mod_assets/characters/akira/p.png")

image akira 4c = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/4c.png", (0, 0), "mod_assets/characters/akira/a.png")
image akira 4ca = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/4c.png", (0, 0), "mod_assets/characters/akira/a.png")
image akira 4cb = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/4c.png", (0, 0), "mod_assets/characters/akira/b.png")
image akira 4cc = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/4c.png", (0, 0), "mod_assets/characters/akira/c.png")
image akira 4cd = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/4c.png", (0, 0), "mod_assets/characters/akira/d.png")
image akira 4ce = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/4c.png", (0, 0), "mod_assets/characters/akira/e.png")
image akira 4cf = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/4c.png", (0, 0), "mod_assets/characters/akira/f.png")
image akira 4cg = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/4c.png", (0, 0), "mod_assets/characters/akira/g.png")
image akira 4ch = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/4c.png", (0, 0), "mod_assets/characters/akira/h.png")
image akira 4ci = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/4c.png", (0, 0), "mod_assets/characters/akira/i.png")
image akira 4cj = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/4c.png", (0, 0), "mod_assets/characters/akira/j.png")
image akira 4ck = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/4c.png", (0, 0), "mod_assets/characters/akira/k.png")
image akira 4cl = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/4c.png", (0, 0), "mod_assets/characters/akira/l.png")
image akira 4cm = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/4c.png", (0, 0), "mod_assets/characters/akira/m.png")
image akira 4cn = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/4c.png", (0, 0), "mod_assets/characters/akira/n.png")
image akira 4co = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/4c.png", (0, 0), "mod_assets/characters/akira/o.png")
image akira 4cp = im.Composite((960, 960), (0, 0), "mod_assets/characters/akira/4c.png", (0, 0), "mod_assets/characters/akira/p.png")

# Character may be removed
image ida 1a = im.Composite((960, 960), (0, 0), "mod_assets/characters/ida/1.png", (0, 0), "mod_assets/characters/ida/a.png")
image ida 1b = im.Composite((960, 960), (0, 0), "mod_assets/characters/ida/1.png", (0, 0), "mod_assets/characters/ida/b.png")
image ida 1c = im.Composite((960, 960), (0, 0), "mod_assets/characters/ida/1.png", (0, 0), "mod_assets/characters/ida/c.png")
image ida 1d = im.Composite((960, 960), (0, 0), "mod_assets/characters/ida/1.png", (0, 0), "mod_assets/characters/ida/d.png")
image ida 1e = im.Composite((960, 960), (0, 0), "mod_assets/characters/ida/1.png", (0, 0), "mod_assets/characters/ida/e.png")
image ida 1e2 = im.Composite((960, 960), (0, 0), "mod_assets/characters/ida/1.png", (0, 0), "mod_assets/characters/ida/e2.png")
image ida 1f = im.Composite((960, 960), (0, 0), "mod_assets/characters/ida/1.png", (0, 0), "mod_assets/characters/ida/f.png")
image ida 1f2 = im.Composite((960, 960), (0, 0), "mod_assets/characters/ida/1.png", (0, 0), "mod_assets/characters/ida/f2.png")
image ida 1g = im.Composite((960, 960), (0, 0), "mod_assets/characters/ida/1.png", (0, 0), "mod_assets/characters/ida/g.png")
image ida 1h = im.Composite((960, 960), (0, 0), "mod_assets/characters/ida/1.png", (0, 0), "mod_assets/characters/ida/h.png")
image ida 1i = im.Composite((960, 960), (0, 0), "mod_assets/characters/ida/1.png", (0, 0), "mod_assets/characters/ida/i.png")
image ida 1j = im.Composite((960, 960), (0, 0), "mod_assets/characters/ida/1.png", (0, 0), "mod_assets/characters/ida/j.png")
image ida 1k = im.Composite((960, 960), (0, 0), "mod_assets/characters/ida/1.png", (0, 0), "mod_assets/characters/ida/k.png")
image ida 1l = im.Composite((960, 960), (0, 0), "mod_assets/characters/ida/1.png", (0, 0), "mod_assets/characters/ida/l.png")
image ida 1m = im.Composite((960, 960), (0, 0), "mod_assets/characters/ida/1.png", (0, 0), "mod_assets/characters/ida/m.png")
image ida 1n = im.Composite((960, 960), (0, 0), "mod_assets/characters/ida/1.png", (0, 0), "mod_assets/characters/ida/n.png")
image ida 1o = im.Composite((960, 960), (0, 0), "mod_assets/characters/ida/1.png", (0, 0), "mod_assets/characters/ida/o.png")
image ida 1p = im.Composite((960, 960), (0, 0), "mod_assets/characters/ida/1.png", (0, 0), "mod_assets/characters/ida/p.png")
image ida 1q = im.Composite((960, 960), (0, 0), "mod_assets/characters/ida/1.png", (0, 0), "mod_assets/characters/ida/q.png")
image ida 1r = im.Composite((960, 960), (0, 0), "mod_assets/characters/ida/1.png", (0, 0), "mod_assets/characters/ida/r.png")
image ida 1r2 = im.Composite((960, 960), (0, 0), "mod_assets/characters/ida/1.png", (0, 0), "mod_assets/characters/ida/r2.png")
image ida 1s = im.Composite((960, 960), (0, 0), "mod_assets/characters/ida/1.png", (0, 0), "mod_assets/characters/ida/s.png")
image ida 1s2 = im.Composite((960, 960), (0, 0), "mod_assets/characters/ida/1.png", (0, 0), "mod_assets/characters/ida/s2.png")
image ida 1t = im.Composite((960, 960), (0, 0), "mod_assets/characters/ida/1.png", (0, 0), "mod_assets/characters/ida/t.png")
image ida 1t2 = im.Composite((960, 960), (0, 0), "mod_assets/characters/ida/1.png", (0, 0), "mod_assets/characters/ida/t2.png")
image ida 1u = im.Composite((960, 960), (0, 0), "mod_assets/characters/ida/1.png", (0, 0), "mod_assets/characters/ida/u.png")
image ida 1u2 = im.Composite((960, 960), (0, 0), "mod_assets/characters/ida/1.png", (0, 0), "mod_assets/characters/ida/u2.png")
image ida 1v = im.Composite((960, 960), (0, 0), "mod_assets/characters/ida/1.png", (0, 0), "mod_assets/characters/ida/v.png")
image ida 1w = im.Composite((960, 960), (0, 0), "mod_assets/characters/ida/1.png", (0, 0), "mod_assets/characters/ida/w.png")

image ida 2a = im.Composite((960, 960), (0, 0), "mod_assets/characters/ida/2.png", (0, 0), "mod_assets/characters/ida/a.png")
image ida 2b = im.Composite((960, 960), (0, 0), "mod_assets/characters/ida/2.png", (0, 0), "mod_assets/characters/ida/b.png")
image ida 2c = im.Composite((960, 960), (0, 0), "mod_assets/characters/ida/2.png", (0, 0), "mod_assets/characters/ida/c.png")
image ida 2d = im.Composite((960, 960), (0, 0), "mod_assets/characters/ida/2.png", (0, 0), "mod_assets/characters/ida/d.png")
image ida 2e = im.Composite((960, 960), (0, 0), "mod_assets/characters/ida/2.png", (0, 0), "mod_assets/characters/ida/e.png")
image ida 2e2 = im.Composite((960, 960), (0, 0), "mod_assets/characters/ida/2.png", (0, 0), "mod_assets/characters/ida/e2.png")
image ida 2f = im.Composite((960, 960), (0, 0), "mod_assets/characters/ida/2.png", (0, 0), "mod_assets/characters/ida/f.png")
image ida 2f2 = im.Composite((960, 960), (0, 0), "mod_assets/characters/ida/2.png", (0, 0), "mod_assets/characters/ida/f2.png")
image ida 2g = im.Composite((960, 960), (0, 0), "mod_assets/characters/ida/2.png", (0, 0), "mod_assets/characters/ida/g.png")
image ida 2h = im.Composite((960, 960), (0, 0), "mod_assets/characters/ida/2.png", (0, 0), "mod_assets/characters/ida/h.png")
image ida 2i = im.Composite((960, 960), (0, 0), "mod_assets/characters/ida/2.png", (0, 0), "mod_assets/characters/ida/i.png")
image ida 2j = im.Composite((960, 960), (0, 0), "mod_assets/characters/ida/2.png", (0, 0), "mod_assets/characters/ida/j.png")
image ida 2k = im.Composite((960, 960), (0, 0), "mod_assets/characters/ida/2.png", (0, 0), "mod_assets/characters/ida/k.png")
image ida 2l = im.Composite((960, 960), (0, 0), "mod_assets/characters/ida/2.png", (0, 0), "mod_assets/characters/ida/l.png")
image ida 2m = im.Composite((960, 960), (0, 0), "mod_assets/characters/ida/2.png", (0, 0), "mod_assets/characters/ida/m.png")
image ida 2n = im.Composite((960, 960), (0, 0), "mod_assets/characters/ida/2.png", (0, 0), "mod_assets/characters/ida/n.png")
image ida 2o = im.Composite((960, 960), (0, 0), "mod_assets/characters/ida/2.png", (0, 0), "mod_assets/characters/ida/o.png")
image ida 2p = im.Composite((960, 960), (0, 0), "mod_assets/characters/ida/2.png", (0, 0), "mod_assets/characters/ida/p.png")
image ida 2q = im.Composite((960, 960), (0, 0), "mod_assets/characters/ida/2.png", (0, 0), "mod_assets/characters/ida/q.png")
image ida 2r = im.Composite((960, 960), (0, 0), "mod_assets/characters/ida/2.png", (0, 0), "mod_assets/characters/ida/r.png")
image ida 2r2 = im.Composite((960, 960), (0, 0), "mod_assets/characters/ida/2.png", (0, 0), "mod_assets/characters/ida/r2.png")
image ida 2s = im.Composite((960, 960), (0, 0), "mod_assets/characters/ida/2.png", (0, 0), "mod_assets/characters/ida/s.png")
image ida 2s2 = im.Composite((960, 960), (0, 0), "mod_assets/characters/ida/2.png", (0, 0), "mod_assets/characters/ida/s2.png")
image ida 2t = im.Composite((960, 960), (0, 0), "mod_assets/characters/ida/2.png", (0, 0), "mod_assets/characters/ida/t.png")
image ida 2t2 = im.Composite((960, 960), (0, 0), "mod_assets/characters/ida/2.png", (0, 0), "mod_assets/characters/ida/t2.png")
image ida 2u = im.Composite((960, 960), (0, 0), "mod_assets/characters/ida/2.png", (0, 0), "mod_assets/characters/ida/u.png")
image ida 2u2 = im.Composite((960, 960), (0, 0), "mod_assets/characters/ida/2.png", (0, 0), "mod_assets/characters/ida/u2.png")
image ida 2v = im.Composite((960, 960), (0, 0), "mod_assets/characters/ida/2.png", (0, 0), "mod_assets/characters/ida/v.png")
image ida 2w = im.Composite((960, 960), (0, 0), "mod_assets/characters/ida/2.png", (0, 0), "mod_assets/characters/ida/w.png")


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
define mom = DynamicCharacter('mom', what_prefix='“', what_suffix='”', ctc="ctc", ctc_position="fixed")
define st = DynamicCharacter('st_name', what_prefix='“', what_suffix='”', ctc="ctc", ctc_position="fixed")
define a = DynamicCharacter('aoruguri', image='aoruguri', what_prefix='“', what_suffix='”', ctc="ctc", ctc_position="fixed")
define mi = DynamicCharacter('mio', image='mio', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define ti = DynamicCharacter('tina', image='tina', what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define en = DynamicCharacter('en_name', image="engeki", what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define ma = DynamicCharacter('mari', image="mari", what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define d = DynamicCharacter('dominion', image="dominion", what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed")
define dev = Character('demomode', ctc="ctc", ctc_position="fixed") #delete for full release
default demomode = "Developer"
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
default player = "Sakura Taiyen"
default s_name = "Shinamonpan Sayori"
default m_name = "Murikou Monika"
default n_name = "Tetsuo Natsuki"
default y_name = "Yandere Yuri"
default k_name = "Sakura Kotonoha"
default akira = "Kamiyama Akira"
default hanato = "???"
default kirinani = "???"
default itsomi = "???"
default inari = "???"
default mom = "Mother"
default everyone = "Everyone"
default lilly = "Yandere Lilly"
default st_name = "Us"
default aoruguri = "Hidden Girl"
default mio = "Mio"
default tina = "Tina"
default en_name = "Luna Engeki"
default mari = "Kusunoki Mari"
default dominion = "Luna Dominion"
default pla = "General Name"

default s_readstory = False
default s_first = False
default s_second = False
default s_third = False
default s_fourth = False
default s_last = False
default n_readstory = False
default n_first = False
default n_second = False
default n_third = False
default n_fourth = False
default n_last = False
default y_readstory = False
default y_first = False
default y_second = False
default y_third = False
default y_fourth = False
default y_last = False
default m_readstory = False
default m_first = False
default m_second = False
default m_third = False
default m_fourth = False
default m_last = False
default k_readstory = False
default k_first = False
default k_second = False
default k_third = False
default k_fourth = False
default k_last = False


default storysread = 0

default sectext = ""
default minutext = ""
default hourtext = ""

# - appeals
default n_appeal = 0
default s_appeal = 0
default y_appeal = 0
default m_appeal = 0

# - trust values
default k_trust = 10

# - choices
default change = "*"
default cute = False
default known = False
default found_breaker = False
default secrets = False
default en_out = False
default persistent.choices_made = []

# - miscellaneous
default settinginfo = "Hover over an option to view info about it."
default settingdef = ""

default previouschan = "music"

default startnow = False

default devmode = config.developer

default save_name = ""