label act1_ch2_main:
    stop music fadeout 2.0
    scene bg residential_day
    with dissolve_scene_full
    play music t2
    call showlocation("Residential Street","September 30, 2023",405.2, "bg residential") from _call_showlocation_4
    
    return

label act1_ch2_end:
    
    stop music fadeout 1
    scene black with dissolve_scene_full
    play music ghostmenu
    $ kirinani = "???"
    kiri "Hanato-kun, are you sure about this?"
    "Hanato?"
    ha "Of course I am, father!  I {i}want{/i} Taiyen-kun to hear us this time."
    "I think I know these people."
    kiri "Alright, he's all yours."
    "His voice sounds horribly familiar."
    ha "Oh, don't worry about that."
    "*Sigh*"
    "Why are you making me listen to making me listen to you on purpose this time, Hanato?"
    ha "*Creepy giggle* Oh, nothing."
    ha "I just want you to know that you're being watched..."
    "Not just watched, but also stalked."
    ha "By Itsomi, sure."
    ha "But also by me!"
    ha "Now that I have entered your daydream, I know your every move from this point forward."
    ha "So, you better think hard about your choices {i}before{/i} you make them..."
    ha "because once you do-"
    "-there's no going back and you guys can easily ruin my day."
    ha "Or worse.  *Creepy giggle*"
    ha "That's your message."
    ha "I'll be talking to you while you're awake now."
    ha "Be ready."
    ha "*Creepy giggle*"
    call showintro(intro_ha) from _call_showintro
    return