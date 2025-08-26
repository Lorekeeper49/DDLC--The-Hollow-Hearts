default persistent.cutscenes_watched = []

default video_length = 0
label playcutscene(vid, *, back="black", starttransition=None, endtransition=None):
    $ _show_skip_prompt = False
    play movie ("mod_assets/cutscenes/" + vid + "/movie.webm")
    play sound ("mod_assets/cutscenes/" + vid + "/sound.ogg")
    play music ("mod_assets/cutscenes/" + vid + "/music.ogg")
    play ambience ("mod_assets/cutscenes/" + vid + "/ambience.ogg")
    play cutscene_voice ("voicelines/" + persistent.voice_lang + "/cutscenes/" + vid + ".ogg")
    $ video_length = renpy.sound.get_duration("mod_assets/cutscenes/" + vid + "/movie.webm")
    scene black
    show movie 
    show screen subtitles onlayer textbox
    with starttransition
    if vid in persistent.cutscenes_watched:
        show screen skipper onlayer textbox
    else:
        $ persistent.cutscenes_watched.append(vid)
    $ can_cont = False
    call play_video
    $ can_cont = True
    stop movie 
    stop sound
    stop music
    stop ambience
    stop cutscene_voice
    scene expression back 
    hide screen subtitles onlayer textbox
    with endtransition
    $ _show_skip_prompt = False
    hide screen skipper onlayer textbox
    return

# - cutscenes
image movie = Movie(size=(1280, 720), xpos=0, ypos=0, xanchor=0, yanchor=0, loop=False)

screen skipper:
    if _show_skip_prompt:
        text _("PRESS ENTER TO SKIP") at skip_prompt_dissolve:
            size 20
            color "#ccc"
            align (1.0, 1.0)
            offset (-20, -20)
            font "mod_assets/fonts/FOT-RodinNTLG Pro EB.otf"
        timer 5.0 action SetVariable("_show_skip_prompt", False)

    key "K_RETURN" action If(_show_skip_prompt, Return(), SetVariable("_show_skip_prompt", True))
    key "K_SPACE" action If(_show_skip_prompt, Return(), SetVariable("_show_skip_prompt", True))
    key "mouseup_1" action If(_show_skip_prompt, Return(), SetVariable("_show_skip_prompt", True))

label play_video:
    $ pause(video_length, hard=True)

    return

# TODO: Add functionality for json-defined subtitles
# json structure: [
# { "start": float (seconds), "end": float (seconds), "name": string, "text": string }
# ]

default subtitle_data = []
init python:
    import json
    def load_subtitles(vid):
        global subtitle_data
        try:
            if _preferences.language is None:
                with open("game/mod_assets/cutscenes/" + vid + "/subtitles.json", "r", encoding="utf-8") as f:
                    subtitle_data = json.load(f)
            else:
                with open("game/tl/" + _preferences.language + "/cutscenes/" + vid + "/subtitles.json", "r", encoding="utf-8") as f:
                    subtitle_data = json.load(f)
        except FileNotFoundError:
            subtitle_data = []
            renpy.log("No subtitles found for cutscene: " + vid)

default subtitle_timer = 0.0
screen subtitles:
    timer 0.1 action SetVariable("subtitle_timer", 0.0)
    if subtitle_data:
        for entry in subtitle_data:
            if subtitle_timer >= entry["start"] and subtitle_timer <= entry["end"]:
                frame:
                    style "default"
                    background "#0008"
                    xalign 0.5
                    yalign 0.9
                    padding (10, 5)
                    text "[entry["name"]]" size 22 color "#fff" font "mod_assets/fonts/FOT-RodinNTLG Pro EB.otf"
                    text "[entry["text"]]" size 20 color "#fff" font "mod_assets/fonts/FOT-RodinNTLG Pro EB.otf"
                break
        timer 0.001 action IncrementVariable("subtitle_timer", 0.001)