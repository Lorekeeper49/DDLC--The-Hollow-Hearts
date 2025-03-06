label mstory(bgreturn="bg club_day"):
    scene black with dissolve_scene
    $ window_style = ""
    $ nb = "namebox"
    $ nextscene = "mstory_ch" + str(chapter)
    $ char_perspective = "Monika"
    call expression nextscene 
    $ char_perspective = "Taiyen"
    stop music fadeout 2.0
    stop sound fadeout 2.0
    scene black with dissolve_scene
    $ window_style = "fake"
    $ nb = "namebox_fake"
    scene expression bgreturn with dissolve_scene_half
    return

label mstory_ch2:
    play music confdep
    play ambience storm
    scene bg schoolroofstorm with dissolve_scene_half
    call showlocation("Kanzen Academy Roof\n{size=25}完全学園高校の屋根{/size}","October 1, 2020\n{size=15}2020年10月1日{/size}",60*12+4+57/60,"bg schoolroofstorm")
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
    "..."
    "I remember the first day like it was yesterday..."
    $ renpy.music.set_volume(0.3, delay=0, channel="ambience")
    play sound flashback
    scene bg gym
    show memory_vignette zorder 300 
    with flashback_start
    $ kirinani = "神山霧何\n{size=15}Kamiyama Kirinani{/size}"
    call showlocation("Kanzen Academy Gym\n{size=25}完全学園高校のジム{/size}","September 2, 2020\n{size=15}2020年9月2日{/size}",60*12+4+57/60,"bg gym")
    kiri "Next up, Murikou Monika."
    "The school principal, Kamiyama Kirinani..."
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
    $ renpy.music.set_volume(1, delay=0, channel="ambience")
    stop ambience
    return

label mstory_ch3:
    call showlocation("???","Monday, August 1, 2020",23,59,57)

    return

label mstory_ch4:
    

    return

label mstory_ch5:
    play ambience storm
    scene bg schoolroofstorm with dissolve_scene_half
    call showlocation("Kanzen Academy Roof\n{size=25}完全学園高校の屋根{/size}","November 1, 2020\n{size=15}2020年11月1日{/size}",60*11+59+57/60,"bg schoolroofstorm")
    show aoruguri turned zorder 2 at t11
    "..."
    a om "This weather should keep the three of us alone."
    show aoruguri cm
    "Glad to have a storm with me."
    a cross om "This is about as much as I know how to do so my powers won't be much help from here."
    show aoruguri cm
    m "Alright, what's the plan?"
    a om "Well, as you know, schools are required by protocol to have sprinklers around the building in case of a fire."
    a doub "They use a deluge sprinkler system, which seems like overkill for a school, but at least that makes the plan faster."
    show aoruguri cm
    m "Wait, hold on.  Are you suggesting we fill the sprinklers up with petrol and burn down the school?"
    a angr om "Correct."
    a turned rhip "But of course, we don't want any casualties."
    a lhip "So we're gonna have to do it while no students are inside the building."
    show aoruguri cm
    m "Well, lucky for us, all clubs are required to be outside today."
    m "And next week if today won't work."
    a om "It'll have to work!"
    a ldown "I've got no idea if the principal is looking at us right now and I'm not taking any chances!"
    a cross "I've got a reputation for skipping class, so I'll go fill up the sprinklers."
    a doub "That is if I can figure out how to do it."
    show aoruguri cm
    m "Well we've only got 4-5 hours, so you better get to work."


    return