label mstory(bgreturn="bg club_day"):
    if renpy.music.is_playing(channel="music_swap"):
        $ previouschan = "music_swap"
        stop music_swap fadeout 2.0
    else:
        $ previouschan = "music"
        stop music fadeout 2.0
    scene black with dissolve_scene
    $ style.say_window = style.window
    $ nb = "namebox"
    $ nextscene = "mstory_ch" + str(chapter)
    call expression nextscene from _call_expression_5
    stop music fadeout 2.0
    scene black with dissolve_scene
    $ style.say_window = style.window_fake
    $ nb = "namebox_fake"
    $ renpy.music.play(audio.t5m, channel=previouschan, fadein=2.0)
    scene expression bgreturn with dissolve_scene_half
    return

label mstory_ch2:
    play music confdep
    play ambience storm
    scene bg schoolroofstorm with dissolve_scene_half
    call showlocation("Kanzen Academy Roof","Friday, December 1, 2020",60*12+4+57/60,"bg schoolroofstorm") from _call_showlocation_22
    "Kanzen means 'perfect', but this school far from it's name."
    "I know I'm not allowed to be on the roof when there is a thunderstorm outside due to safety reasons..."
    "But I just can't handle all the chaos inside..."
    m "*Sigh*"
    m "Mom, dad..."
    m "It's been a long time since we said goodbye..."
    "I say that as if it's a sad thought{cps=3}...{w=1}{/cps}\nand it is, even if I did run away from them."
    "This is public knowledge around the school...{w=1}\nand it is the main reason as to why I have been bullied for the past month."
    "It sucks that this school forces you to reveal all your secrets."
    "That's right!  All of them!"
    m "This school's terrible..."
    "Not many think that way...\nSo it may seem..."
    "There's a reason why I don't have any friends."
    "{cps=1}...{/cps}"
    "I remember the first day like it was yesterday..."
    $ renpy.music.set_volume(0.3, delay=0, channel="ambience")
    play sound flashback
    scene bg gym
    show memory_vignette zorder 300 
    with flashback_start
    #call showlocation("Kanzen Academy Gym","Monday, September 2, 2020",12,04,57)
    kiri "Next up, Murikou Monika."
    "The school principal, Kamiyama Kirinani..."
    $ kirinani = "Kamiyama Kirinani"
    kiri "Come on, take the stage!"
    "There is no stage..."
    "..."
    "He runs this school with pride...{w=1}seems to have fun making people do such things they are not okay with..."
    "I 'took the stage' with fear, knowing what I had to do..."
    "I had to {i}hide{/i} the fear..."
    "Everyone here{cps=3}...{/cps}has to hide their negative emotions, especially their hate for the school."
    kiri "We'll know if you tell people you hate this school!"
    m "(Sure you will...)"
    "Words I would soon regret!"
    kiri "Dismissed!"
    "Tch!"
    scene bg schoolroofstorm with flashback_end
    $ renpy.music.set_volume(1, delay=0, channel="ambience")
    "I've seen people be expelled for things they've said about the school..."
    "{i}Outside it!{/i}"
    "'Expelled'{cps=3}...{/cps}more like 'executed'!"
    "They kill people who break the rules to that point."
    "It's illegal!"
    "And yet, the cops are terrified to do a thing!"
    "I'm sure they've tried, ending in failure..."
    "I'm not even sure if the SWAT team will help at this point..."
    m "Gah!"
    "I hate this!"
    play sound bell
    "..."
    "Looks like lunch has decided to end..."
    "For the umpteenth time, I'm heading to class against my will..."
    "Just perfect!"
    "Tehe... pun intended."
    "At least I can make some fun of this place..."
    $ renpy.music.set_volume(0.3, delay=0, channel="ambience")
    scene bg roofentrancestorm with wipeleft_scene
    "Someone's staring at me..."
    m "Who's there?"
    stop ambience
    return

label mstory_ch3:
    call showlocation("???","Monday, August 1, 2020",23,59,57) from _call_showlocation_23

    return

label mstory_ch4:
    call showlocation("???","Monday, August 1, 2020",23,59,57) from _call_showlocation_24

    return

label mstory_ch5:
    call showlocation("???","Monday, August 1, 2020",23,59,57) from _call_showlocation_25

    return