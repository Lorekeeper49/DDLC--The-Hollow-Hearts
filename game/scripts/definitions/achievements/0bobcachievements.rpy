# BobCAchievements Code by Bob Conway 2023
# Version 1.0 - June 6, 2023
# For use with the Ren'Py engine

# Available with a Creative Commons 0 (CC0) license
# Attribution appreciated; please link bobcgames.com

# Software is provided "as is" without warranty of any kind

############################################
#             USAGE DIRECTIONS             #
############################################

# 1) Drop this file (0bobcachievements.rpy) into the game/ folder of your Ren'Py project.

# 2) Add your achievements to the below code as tuples of (reference_id, user title, user description)
#    or (reference_id, user title, user description, True) if you want your achievement name to be hidden
#    when using sbobcachievements.rpy.
#   (You can also replace or remove the two sample achievements.)
#   (If you're using Steam, the reference_ids should be the API name of the achievements.)
#   (This does not currently support progress stats.)
#
#   normal sample: ("sample", _("NAME"), _("DESC/CONDITION"))
#   hidden sample: ("sample", _("NAME"), _("DESC/CONDITION"), True)
define BOBCACHIEVEMENT_LIST = (
    ("newfriends", _("Brand New Friends"), _("Complete the main prologue.")),
    ("qa", _("Complete Questionnaire"), _("Have every possible question from the 20 questions game be asked at least once across however many playthroughs it takes.")),
    ("act1fin", _("This story ain't what it seems..."), _("Complete the first act")),
    ("act2fin", _("Power Overtaken"), _("Complete the second act")),
    ("act3fin", _("Nothing Exists"), _("Complete the final act"))
    )
    
# 3) In your game script, when you want to grant an achievement, type "achieve <reference_id>" without the
#    quotes or <> (and without a leading $). For example, to grant the sample "Started The Game" achievement:
#
#    label my_test_label:
#        "This is some sample script."
#        achieve started
#        "Now you've granted the "Started The Game" achievement!"
#
#    If you need to grant an achievement via python code, use bobcachievement_grant(reference_id)
    
# 4) By default, achievement grants will be displayed using renpy.notify with this prefix text. If you
#    want to display them using a custom screen instead, override the screen variable with a string of
#    the name of the screen you want to use. Or just change the prefix text to whatever you desire.
define BOBCACHIEVEMENT_SCREEN_NAME = "achievement_screen"
define BOBCACHIEVEMENT_NOTIFY_PREFIX = _("Achievement Unlocked!")
define BOBCACHIEVEMENT_SCREEN_TRANSITION = None
    
# 6) That's it! To display achievements to the user, please see directions in sbobcachievements.rpy

#############################################
# YOU SHOULD NOT MODIFY ANYTHING BELOW HERE #
#############################################
python early:
    def parse_bobcachievement(lexer):
        return lexer.rest()
    def bobcachievement_grant(achiname):
        if achiname not in BOBCACHIEVEMENTS_MAP:
            renpy.error("Achievement '" + achiname + "' was not registered. Please modify BOBCACHIEVEMENT_LIST in 0bobcachievements.rpy to add it.")
            return
        if not achievement.has(achiname):
            if BOBCACHIEVEMENT_SCREEN_NAME is not None:
                if BOBCACHIEVEMENT_SCREEN_TRANSITION is not None:
                    renpy.transition(BOBCACHIEVEMENT_SCREEN_TRANSITION)
                renpy.show_screen(BOBCACHIEVEMENT_SCREEN_NAME, achiname, BOBCACHIEVEMENTS_MAP[achiname][0], BOBCACHIEVEMENTS_MAP[achiname][1])
            else:
                renpy.notify(__(BOBCACHIEVEMENT_NOTIFY_PREFIX) + " " + __(BOBCACHIEVEMENTS_MAP[achiname][0]))
            achievement.grant(achiname)
            achievement.sync()
    def lint_bobcachievement(achiname):
        if achiname not in BOBCACHIEVEMENTS_MAP:
            renpy.error("Achievement '" + achiname + "' was not registered. Please modify BOBCACHIEVEMENT_LIST in 0bobcachievements.rpy to add it.")
    renpy.register_statement("achieve", parse=parse_bobcachievement, execute=bobcachievement_grant, lint=lint_bobcachievement)
            
init python:
    # Validate that the achievement list is well-formed and form it into a map for ease of access
    # Map is {reference_id:str : (title:str, description:str, is_hidden:boolean)}
    BOBCACHIEVEMENTS_MAP = {}
    if not isinstance(BOBCACHIEVEMENT_LIST, tuple):
        renpy.error("The BOBCACHIEVEMENT_LIST is not a tuple.")
    else:
        for v in BOBCACHIEVEMENT_LIST:
            if not isinstance(v, tuple):
                renpy.error("Found a malformed achievement in BOBCACHIEVEMENT_LIST: " + str(v))
                continue
            if len(v) != 3 and len(v) != 4:
                renpy.error("Achievement " + str(v[0]) + " did not have three or four portions. Each achievement must have a reference_id, title, and description, and an optional hidden status: " + str(v))
                continue
            if not isinstance(v[0], str):
                renpy.error("Achievement " + str(v[0]) + " reference_id was not a string")
                continue
            if not isinstance(v[1], str):
                renpy.error("Achievement " + str(v[0]) + " title was not a string: " + str(v[1]))
                continue
            if not isinstance(v[2], str):
                renpy.error("Achievement " + str(v[0]) + " description was not a string: " + str(v[2]))
                continue
            ishidden = False
            if len(v) == 4:
                if not isinstance(v[3], bool):
                    renpy.error("Achievement " + str(v[0]) + " hidden flag was not True or False: " + str(v[3]))
                    continue
                ishidden = v[3]
            if v[0] in BOBCACHIEVEMENTS_MAP:
                renpy.error("Achievement " + str(v[0]) + " is defined twice in BOBCACHIEVEMENT_LIST. Each achievement must have a unique reference_id.")
                continue
            BOBCACHIEVEMENTS_MAP[v[0]] = (v[1], v[2], ishidden)
            achievement.register(v[0])
    # Store the total number of achievements, for display
    BOBCACHIEVEMENTS_NUMACHIEVEMENTS = len(BOBCACHIEVEMENTS_MAP)
    del BOBCACHIEVEMENT_LIST

screen achievement_screen(achiname, achievement_title, achievement_description):
    zorder 2000
    timer 5.0 action Hide("achievement_screen")
    use achievement_frame_bg
    fixed at achievement_transform:
        xmaximum 500
        hbox:
            add "mod_assets/achievements/" + achiname + ".png"
            vbox:
                text achievement_title style "achievement_text"
                text achievement_description style "achievement_desc_text"

style achievement_text:
    font "mod_assets/fonts/AlexBrush-Regular.ttf"
    size 30
    color "#000"
    outlines []

style achievement_desc_text:
    font "mod_assets/fonts/AlexBrush-Regular.ttf"
    size 15
    color "#000"
    outlines []

transform achievement_transform():
    ypos 620
    on show:
        xpos -640
        easeout .25 xpos 0
    on hide:
        xpos 0
        easein .25 xpos -640

init -501 screen achievement_frame_bg():
    zorder 1000
    frame at achievement_transform:
        ysize 100
        background "achievement_bg"

image achievement_bg:
    "mod_assets/gui/achievement_bg.png"
    xzoom -1.0
    alpha 0.5