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