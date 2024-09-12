#Name: It Begins
#Kotonoha will die here
label act2_ch5_main:
    stop music fadeout 2.0
    scene bg residential_day
    with dissolve_scene_full
    play music t2
    call showlocation("Residential Street","Monday, September 30, 2023",6,45,12) from _call_showlocation_44
   
    return