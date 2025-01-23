#Name: It Begins
#Kotonoha will die here
label act2_ch5_main:
    stop music fadeout 2.0
    scene bg residential_day
    with dissolve_scene_full
    play music t2
    call showlocation("Residential Street\n{size=25}住宅街{/size}","October 12, 2023\n{size=15}2023年10月12日{/size}",6,45,12) from _call_showlocation_44
    
    achieve act2fin
    return

label act2_ch5_alt:
    stop music fadeout 2.0
    scene bg residential_day
    with dissolve_scene_full
    play music t2
    call showlocation("Residential Street\n{size=25}住宅街{/size}","October 12, 2023\n{size=15}2023年10月12日{/size}",6,45,12)

    #Cutscene notes
    t "Did you laugh like that when you killed my sister?"
    kiri "..."
    kiri "I was wondering where she was."
    t "What?"
    a "*panting*"
    "Aoruguri sees visions of her killing Kotonoha."
    a "*Screaming*"
    t "Aoruguri?"
    a "(I did it...)"
    t "Calm down."
    a "Taiyen..."
    t "..."
    a "I KILLED YOUR SISTER!!!"
    t "!!!"
    "Aoruguri strikes herself then comes close to Kirinani in emotional distress, pelting him constantly."
    "Taiyen tries to get her to calm down."
    a "RUUUUUUNNNN!!!"
    "Taiyen does so with the others."
    ma "What are you doing?"
    t "You heard your daughter!  Run!  Go for it!"
    ma "But..."
    t "You sure you want to get caught up in that like my sister did!?"
    ma "..."
    t "Stay here, I'll try to calm her down."
    "Sayori & Monika" "Wait-"
    "Taiyen dashes away before they could say anything."
    n "Fucking boy doesn't take his own advice!"
    "Back at the school, Taiyen stops Aoruguri and Kirinani from hitting each other at full force and launches something at Kirinani himself."
    a "What are you doing?  Do you want me to kill you too?"
    t "I couldn't just leave you!"
    t "Besides, alone, you're most likely gonna die before or after I do."
    kiri "I'll make sure it's after!"
    "Kirinani hurls something at Taiyen as he breaks through it and comes fact to face with Kirinani."
    t "See what I mean?"
    kiri "WHERE IS EVERYONE!?"
    "Taiyen gets knocked back."
    ak "They didn't like your plan."
    "Kirinani gets enraged."
    t "How did you..."
    ak "Don't mind it."
    ak "YOU TWO!  BEYOND MAX!  NOOOWWW!!!"
    "One epic fight later."
    ak "Two people is not enough."
    t "Well, we knocked him out."
    ak "You haven't."
    ak "You ever heard of hysterical strength?"
    ak "He's got that in spades."
    ak "Especially when 'unconscious'."
    t "*Sigh*"
    ak "Let's get out of here."
    a "*Sobbing* Taiyen...  I'm so sorry..."
    #End of cutscene

    achieve act2fin
    return