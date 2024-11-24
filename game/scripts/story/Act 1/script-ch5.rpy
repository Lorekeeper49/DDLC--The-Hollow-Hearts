label act1_ch5_main:
    stop music fadeout 2.0
    scene bg bedroom
    with dissolve_scene_full
    play music t2
    call showlocation("Taiyen's Room","October 3, 2023",6*60+0+0/60.0,"bg bedroom") from _call_showlocation_16
    if not secrets:
        "So before I start the day, can I tell people now?"
        hamind "I wouldn't take my chances."
        hamind "I think it would be fine, I wouldn't tell him anything now."
        hamind "But... there's no telling what he'll get out of me on the reports."
        hamind "So for that reason, I'm still gonna be preventing you from telling everyone."
        "Got it."
    "Welp, time to start the day."
   
    return