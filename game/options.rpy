define config.name = "ドキドキ文芸部：ザー・ホロー・ハーツ | DDLC: The Hollow Hearts"





define gui.show_name = False




define config.version = "1.0"





define gui.about = _("")






define build.name = "THH"






define config.has_sound = True
define config.has_music = True
define config.has_voice = True

define config.sample_voice = "voicelines/test.ogg"










define config.main_menu_music = audio.t1










define config.enter_transition = Dissolve(.2)
define config.exit_transition = Dissolve(.2)




define config.after_load_transition = None




define config.end_game_transition = Dissolve(.5)
















define config.window = "auto"




define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)







default preferences.text_cps = 50





default preferences.afm_time = 30

default preferences.music_volume = 0.75
default preferences.sfx_volume = 0.75
default preferences.ambience_volume = 0.75
default preferences.voice_volume = 1.50















define config.save_directory = "DDLCTheHollowHearts"







define config.window_icon = "mod_assets/logo.png"



define config.allow_skipping = True
define config.has_autosave = False
define config.autosave_on_quit = False
define config.autosave_slots = 0
define config.layers = ['behind_background', 'background', 'forebackground', 'master', 'transient', 'screens', 'foreground', 'cutscenes', 'overlay', 'textbox']
define config.say_layer = "textbox"
define config.image_cache_size = 64
define config.predict_statements = 50
define config.rollback_enabled = config.developer
define config.menu_clear_layers = ["textbox"]
define config.gl_test_image = "white"
define config.voice_filename_format = f"voicelines/{persistent.voice_lang}/{filename}"

init python:
    import os
    if len(renpy.loadsave.location.locations) > 1: del(renpy.loadsave.location.locations[1])
    renpy.game.preferences.pad_enabled = False
    def replace_text(s):
        s = s.replace('--', u'\u2014') 
        s = s.replace(' - ', u'\u2014') 
        return s
    config.replace_text = replace_text

    def game_menu_check():
        if quick_menu: renpy.call_in_new_context('_game_menu')

    config.game_menu_action = game_menu_check

    def force_integer_multiplier(width, height):
        if float(width) / float(height) < float(config.screen_width) / float(config.screen_height):
            return (width, float(width) / (float(config.screen_width) / float(config.screen_height)))
        else:
            return (float(height) * (float(config.screen_width) / float(config.screen_height)), height)

    def autovoiceline(id):
        if renpy.exists(f"voicelines/{persistent.voice_lang}/{id}.ogg"):
            _preferences.afm_time = 0.5
            return f"{id}.ogg"
        elif renpy.exists(f"voicelines/{persistent.voice_lang}/{id}.mp3"):
            _preferences.afm_time = 0.5
            return f"{id}.mp3"
        elif renpy.exists(f"voicelines/{persistent.voice_lang}/{id}.wav"):
            _preferences.afm_time = 0.5
            return f"{id}.wav"
        else:
            _preferences.afm_time = 30
            return f"{id}"
    config.auto_voice = autovoiceline



init python:
    build.archive("scripts", "mod")
    build.archive("mod_assets", "mod")
    build.archive("voicelines", "mod")
    build.archive("translations", "mod")

    build.classify("**.rpy", None)
    build.classify("**.rpa", None)
    
    build.classify("game/mod_assets/**", "mod_assets all")
    build.classify("game/scripts/**", "scripts all")
    build.classify("game/**.rpyc", "scripts all")
    build.classify("game/**.txt", "scripts all")
    build.classify("game/voicelines/**", "voicelines all")
    build.classify("game/tl/**", "translations all")

    
    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('**.psd', None)
    build.classify('**.sublime-project', None)
    build.classify('**.sublime-workspace', None)
    build.classify('/music/*.*', None)
    build.classify('script-regex.txt', None)
    build.classify('/game/10', None)
    build.classify('/game/cache/*.*', None)









    build.documentation('*.html')
    build.documentation('*.txt')

    build.include_old_themes = False











define build.itch_project = "teamsalvato/ddlc"