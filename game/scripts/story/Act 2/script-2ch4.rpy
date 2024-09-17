#Name: The Nightmare Mansion
label act2_ch4_main:
    if not known:
        jump act2_ch4_alt
    stop music fadeout 2.0
    play ambience mansion
    scene bg mansion
    with dissolve_scene_full
    call showlocation("Wraith Mansion","October 11, 2023",23*60+14+57/60.0,"bg tree") from _call_showlocation_43
    k "We're here."
    "Welp, here we go..."
    a "Everyone got their flashlights?"
    "Everyone shows their flashlights."
    a "Good."
    "*Deep breath*"
    "I've seen this place before, but I've never been inside."
    a "Here goes nothing."
    "We all walk inside."
    scene bg foyer
    show screen flashlight 
    with wipeleft_scene
    "...{w=1}Huh?"
    show kotonoha turned casual curi om zorder 2 at t11
    k "Something wrong?"
    a "No?  Just thought... this place looked familiar..."
    show tina turned curi om zorder 2 at l21
    show kotonoha at t22
    ti "Huh?  I thought the Kamiyama family was the only one that lived here."
    show tina at t21
    a "So that's why you wanted to come here!"
    "Do these people seriously not question any plans?"
    ti neut "Yeah, this won't tell us where he is...  But this may give us a hint as to why he's doing everything's he's doing."
    k rhip anno "Alright, Aoruguri, let's see how you are with arrangements!"
    hide tina
    hide kotonoha
    a "Alright.  Since this is a big place, we'll split up!"
    show kotonoha turned casual anno rhip zorder 2 at t22
    show akira 4ad zorder 2 at t21
    a "Kotonoha and Akira will take this floor,"
    hide akira
    hide kotonoha
    show mari crossed b hat zorder 2 at t22
    show tina turned suit cross anno zorder 2 at t21
    a "Mari and Tina will search upstairs,"
    hide tina
    hide mari
    show lilly norm se zorder 2 at t11
    a "and Lilly and I will head to the basement."
    hide lilly
    show tina turned suit cross anno om zorder 2 at t11
    ti "The basement's been blocked for God knows how long, good luck finding it."
    show tina cm
    a "I'm sure we'll find it easily."
    hide tina
    scene bg dining
    show screen flashlight 
    with wipeleft_scene
    "..."
    "Why does this place look so...?"
    lil "Behind you!"
    show screen wraith
    "Stay calm!  Gotta hold my flashlight on it's face!"
    "Whew."
    show lilly c2e zorder 2 at t11
    lil "Are you okay?"
    a "Yeah, thanks."
    a "Why aren't you using your true form?"
    lil c2c2 "Normally I would, but then I wouldn't be able to use my flashlight, the only thing that works on these."
    a "Oh."
    "Not sure how that works, but I don't know how dolls work, I've never had one in my life."
    "I didn't even know one could be alive!"
    a "Well anyway, come on.  I found the basement back here."
    scene bg first_room
    show screen flashlight 
    with wipeleft_scene
    "Well, here we go."
    call explore("first_room") from _call_explore_2
    call act2_ch4_alt
   
    return

label act2_ch4_alt:
    stop music fadeout 2.0
    play ambience mansion
    a "{cps=3}...?{/cps}"
    scene bg final_room
    with dissolve_scene_full
    call showlocation("???","October 11, 2023",0*60+0+0/60.0,"bg final_room")
    a "Huh?  Where am I?"
    "Why is there blood?"
    a "Hey, what the fuck?"
    "I immediately try the door."
    a "*Struggling* Hey!  Let me out!  *Bangs door*"
    "..."
    a "No answer."
    "Why do I even try?  That never works..."
    $ pla = "???"
    general "YOU KNOW THIS PLACE."
    a "Who's there?"
    "My memory's all fuzzy."
    general "YOU DON'T KNOW US."
    a "What?"
    general "WE KNOW YOU."
    a "Cut the bullshit!"
    a "Tell me who you are!"
    stop ambience
    show wraith_black at t11
    show wraith_black1 at t21
    show wraith_black2 at t22
    show wraith_black3 at t41
    show wraith_black4 at t44
    general "YOUR SISTER."
    a "Huh?"
    

    return