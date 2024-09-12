label extras:
    stop music fadeout 2.0
    scene black
    with dissolve_scene_full
    "Welcome to the extras!"
    label extras_loop:
        menu:
            "What would you like to view?"

            "Bloopers.":
                call bloopers from _call_bloopers
            "Early Art.":
                call earlyart from _call_earlyart
            "Back to title screen.":
                "Returning to title screen."
                return
        jump extras_loop

label bloopers:
    label bloopers_loop:
        menu:
            "Which blooper would you like to view?"

            "The Struggle of Long Lines. - Taiyen (old microphone)":
                voice "mod_assets/extras/bloopers/The_Struggles_of_Long_Lines.ogg"
                "Sayori quickly heats up the water while Yuri-chan sets out tea cups for everyone with a tea bag in each cup."
            "Tea Struggle. - Taiyen (old microphone)":
                voice "mod_assets/extras/bloopers/Tea_Struggle.ogg"
                "I take a sip of the tea and immediately feel the relaxing sensation that tea often produces."
            "Likes your boy- uhhh. - Hanato":
                $ hanato = "???"
                voice "mod_assets/extras/bloopers/Likes_your_boy-_uhhh.ogg"
                ha "Seems like your boyfriend has joined that club you despise."
            "Back":
                return
        jump bloopers_loop