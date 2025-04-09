label mstory(bgreturn="bg club_day"):
    scene black with dissolve_scene
    $ window_style = ""
    $ nb = "namebox"
    $ nextscene = "mstory_ch" + str(chapter)
    $ char_perspective = "Monika"
    $ aoruguri = "ルナ煽るぐり\n{size=15}Luna Aoruguri{/size}"
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
    scene bg schoolroofstorm with dissolve_scene_full
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
    play music confdep
    scene bg gym with dissolve_scene_full
    call showlocation("Kanzen Academy Gym\n{size=25}完全学園高校のジム{/size}","September 2, 2020\n{size=15}2020年9月2日{/size}",60*12+4+57/60,"bg gym")
    show aoruguri turned zorder 2 at t11
    m "So, you've been stalking me?"
    a cross ce om "If that's what we're calling it, then I've been stalking everyone." 
    m "What's going on with you?  Why are you doing this?"
    a "..."
    a "I don't have an answer for that."
    a "There's a rumor going around, they think I'm in love with the principal."
    m "That's called a pedophile."
    a "No, that's called a ephebophile."
    m "Ephe-what?"
    a "Trust me, it's not used often."
    m "Neither is your name."
    m "No offense."
    a "None taken."
    a "As I was saying, my true feelings are actually the opposite of what people are saying."
    a "I hate the principal with every fiber of my being!"
    a "And yet, I have to tolerate him because...!"
    a "..."
    a "Because he provides for me..."
    a "I'm homeless."
    a "I live within this school."
    a "And no, I don't the dorms."
    a "I'm quite literally broke."
    a "And therefore, I've become a test subject in all his little experiments about control."
    a "Speaking of, I have another experiment tomorrow.  That's gonna be fucking fun!"
    m "No one's ever said anything about him ever doing any experiments..."
    m "What the hell is he doing to you down there?!"
    a "If you really want to know, then sneak your way in somehow."
    a "Tomorrow; September 3, 2020, 15:45."
    a "Don't be late, or you'll miss your chance."
    return

label mstory_ch4:
    scene bg gym with dissolve_scene_full
    call showlocation("Kanzen Academy Gym\n{size=25}完全学園高校のジム{/size}","September 3, 2020\n{size=15}2020年9月3日{/size}",60*15+29+57/60,"bg gym")
    play sound bell
    $ pause(1.0)
    "It's time."
    m "Stealth, don't fail me now."
    "I notice that Luna is going to the basement that I didn't even know the school had and I follow behind."
    "As I follow, she stops behind a wall and talks to me."
    a "Just so you know, this area is heavily guarded."
    "Not a problem."
    a "Also, once I step in there, I won't remember anything from that point forward until I leave."
    a "It's an error he wants to fix, that's what he told me."
    a "His explanation is how I know about the experments in the first place."
    "She begins walking further."
    "At this point, I set my visibility to false and follow her."
    scene bg power_room with wipeleft_scene
    play ambience factory
    "My abilities are like none other."
    "It might seem similar to copycat where I have the powers of other attributes."
    "But it is not."
    show aoruguri turned zorder 2 at t11
    "I don't even know how to describe it."
    show aoruguri ce
    "It's like the world is digital and I'm able to control the parameters of anything and everything."
    "As if I'm some sort of administrator."
    show aoruguri cross
    "Or at least I assume..."
    "I haven't exactly learned how to do much yet."
    show aoruguri at t41
    "But it is for this reason that I am able to hide myself from the eyes of people and not be detected by anything."
    "Even heat detectors or super sonic radars."
    "I'm so caught up my own abilities, I'm not even paying to what Luna is doing."
    show aoruguri turned
    "She seems to be picking up random tools?"
    show aoruguri angr
    "Now stabbing herself in the arm with a screwdriver."
    show aoruguri om
    "It looks like she's trying to disassemble herself."
    hide aoruguri
    kiri "Almost perfect!"
    "That voice!"
    "No!"
    kiri "Soon, we'll be able to fully control a person!"
    "Don't tell me."
    kiri "Now we just need a volunteer to partake as a CONTROLLER."
    show aoruguri turned ce zorder 2 at t11
    a om "I... still... have... memory..."
    a angr "No..."
    a oe "He's done it."
    stop ambience
    scene black with None
    return

label mstory_ch5:
    "After what I saw in that experiment, we decided that it was time to finally destroy the school without killing any students."
    "We spent a couple months researching the building and the best way to demolish the building safely."
    "Until..."
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
    m "I'm in the same boat."
    m "My abilities are... unique."
    m "..."
    m "So, what's the plan?"
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