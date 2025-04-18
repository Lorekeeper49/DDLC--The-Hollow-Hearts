label tstory(bgreturn="bg club_day"):
    scene black with dissolve_scene
    $ window_style = ""
    $ nb = "namebox"
    $ nextscene = "tstory_ch" + str(chapter)
    $ char_perspective = "Taiyen"
    call expression nextscene 
    $ char_perspective = "Taiyen"
    stop ambience fadeout 2.0
    stop music fadeout 2.0
    stop sound fadeout 2.0
    scene black with dissolve_scene
    $ window_style = "fake"
    $ nb = "namebox_fake"
    scene expression bgreturn with dissolve_scene_half
    return

label tstory_ch2:
    play ambience factory
    scene bg factory with dissolve_scene_half
    call showlocation("Palace Factories Inc.\n{size=25}株式会社宮殿工場{/size}","June 29, 2018\n{size=15}2018年6月29日{/size}",20*60+4+57/60.0,"bg factory")
    $ pla = "被雇用者\n{size=15}Worker{/size}"
    t "Oi!  Stop slacking off!  Get back to work!"
    general "You're not the boss of me!"
    t "Hey, don't make me report that attitude to your real boss, who is out sick for the week."
    t "So, like it or not, I'm your boss for this week!"
    t "And I don't know about you, but I personally wouldn't want to be fired by my substitute boss!"
    "God, do these guys ever learn?"
    "I may sound strict, but this is how the actual boss is with slacking workers."
    scene bg office with wipeleft_scene
    t "How are the calculations coming along?"
    kiri "Things are looking good."
    kiri "If we do this right, the volunteers will have their attributes changed in no time."
    t "Awesome!"
    "We're working on a new substance codenamed Breaker."
    "Despite it's name, it's not something that reacts when too much power is used and turns off your abilities."
    "What it actually is a way to extract a person's attribute so it can be placed in someone else."
    "The only downside is that it actually removes the attribute from the person, rendering them powerless."
    "So we're using it as a way to change out attributes until we find a way to extract them without removing them."
    kiri "And that's it!"
    kiri "There they are; the final calculations!"
    t "They're looking good!"
    t "Let's make the chemical."
    "This is gonna work, I know it."
    return

label tstory_ch3:
    play ambience factory
    scene bg factory with dissolve_scene_half
    call showlocation("Palace Factories Inc.\n{size=25}株式会社宮殿工場{/size}","July 1, 2018\n{size=15}2018年7月1日{/size}",20*60+4+57/60.0,"bg factory")
    t "So... this is who I'm taking care of for the rest of the week."
    "NAME: LUNA AORUGURI"
    "ATTRIBUTE: STORM"
    "APPEARANCE: BLACK HAIR, BLUE EYES, SHORT STATURE"
    "PERSONALITY: [[UNKNOWN]"
    "I'm just babysitting her."
    "When she's my age."
    "Did she really have that bad of a family?"
    "I've dealt with my fair share of bad family members."
    "But I'm not sure if she's in worse condition."
    "I've been briefed on her situation."
    "Sort of..."
    "One of our volunteers, Kusonoki Mari, is her biological mother."
    "She was abused as a kid and raised to be a vigilante, but it never reached fruition."
    "She killed her own parents."
    "It was an accident, but it saved her."
    "But her love life..."
    "She wanted kids, but not like this."
    "She was raped."
    "In fact, I just realized..."
    "All our volunteers had a bad past."
    "ONE: Was controlled his whole life."
    "TWO: Ran away from his family."
    "THREE: Used for experiments."
    "FOUR: Raped."
    "FIVE: Committed several crimes."
    "They all had a bad past."
    "And they're trying to fix it."
    return

label tstory_ch4:
    play ambience factory
    scene bg factory with dissolve_scene_half
    $ char_perspective = "Lilly"
    call showlocation("Palace Factories Inc.\n{size=25}株式会社宮殿工場{/size}","July 3, 2018\n{size=15}2018年7月3日{/size}",20*60+4+57/60.0,"bg factory")
    t "Are you ready?"
    lil "Yes."
    t "Stab her."
    "Here goes nothing."
    "The needle goes in and..."
    stop ambience
    play sound static
    show noise
    $ pause(0.2)
    stop sound
    hide noise
    $ pause(0.05)
    play sound static
    show noise
    $ pause(0.1)
    stop sound
    hide noise
    $ pause(0.05)
    play sound static
    show noise
    $ pause(0.1)
    stop sound
    hide noise
    $ pause(0.1)
    play sound static
    show noise
    $ pause(0.5)
    stop sound
    hide noise
    show veins onlayer foreground 
    show darkred
    play ambience creepy
    $ pause(1.0)
    play sound static
    show noise onlayer foreground zorder 12 with None
    $ pause(0.25)
    stop sound
    hide noise onlayer foreground
    scene black 
    show noise zorder 10 at noisefade(0, 0, 0.1)
    $ pause(1.0)
    play sound static
    show explore_text "アアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアア\nあああああああああああああああああああああああああああああああああああああああああああああああああ\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼\nアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアア\nあああああああああああああああああああああああああああああああああああああああああああああああああ\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼\nアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアア\nあああああああああああああああああああああああああああああああああああああああああああああああああ\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼\nアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアア\nあああああああああああああああああああああああああああああああああああああああああああああああああ\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼\nアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアア\nあああああああああああああああああああああああああああああああああああああああああああああああああ\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼\nアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアア\nあああああああああああああああああああああああああああああああああああああああああああああああああ\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼\nアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアア\nあああああああああああああああああああああああああああああああああああああああああああああああああ\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼\nアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアア\nあああああああああああああああああああああああああああああああああああああああああああああああああ\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼\nアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアア\nあああああああああああああああああああああああああああああああああああああああああああああああああ\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼\nアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアア\nあああああああああああああああああああああああああああああああああああああああああああああああああ\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼\nアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアア\nあああああああああああああああああああああああああああああああああああああああああああああああああ\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼\nアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアア\nあああああああああああああああああああああああああああああああああああああああああああああああああ\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼\nアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアア\nあああああああああああああああああああああああああああああああああああああああああああああああああ\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼\nアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアア\nあああああああああああああああああああああああああああああああああああああああああああああああああ\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼\nアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアア\nあああああああああああああああああああああああああああああああああああああああああああああああああ\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼\nアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアア\nあああああああああああああああああああああああああああああああああああああああああああああああああ\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼\nアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアア\nあああああああああああああああああああああああああああああああああああああああああああああああああ\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼\nアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアア\nあああああああああああああああああああああああああああああああああああああああああああああああああ\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼\nアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアア\nあああああああああああああああああああああああああああああああああああああああああああああああああ\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼\nアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアア\nあああああああああああああああああああああああああああああああああああああああああああああああああ\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼\nアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアア\nあああああああああああああああああああああああああああああああああああああああああああああああああ\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼\nアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアア\nあああああああああああああああああああああああああああああああああああああああああああああああああ\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼\nアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアア\nあああああああああああああああああああああああああああああああああああああああああああああああああ\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼\nアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアア\nあああああああああああああああああああああああああああああああああああああああああああああああああ\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼\nアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアア\nあああああああああああああああああああああああああああああああああああああああああああああああああ\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼\nアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアア\nあああああああああああああああああああああああああああああああああああああああああああああああああ\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼\n" zorder 1 at truecenter with None
    $ pause(1.0)           
    stop sound     
    stop ambience
    play sound fall2
    hide explore_text
    hide noise
    hide veins onlayer foreground
    with None
    $ pause(1.0)
    $ char_perspective = "Taiyen"
    scene bg factory 
    show lilly norm a2e zorder 2 at t11
    with dissolve_scene_full
    t "Are you okay?"
    lil c2e "Sort of..."
    show lilly a2e
    hide lilly
    "What happened?!"
    "What went wrong?"
    "I had it all right."
    "This happened on the last test too."
    "Why was the first one the only one that...?"
    lil "Do you know what-{nw}"
    t "Don't.  Ask me."
    t "Do the results on your own time."
    t "I need to find out why you went crazy."
    with wipeleft_scene
    play ambience factory
    t "That can't be!"
    t "Our calculations..."
    t "We need to cancel the other tests right now!"
    "Our calculations were wrong from the beginning."
    "This was doomed from the start."
    "We were never meant to play God like this."
    "The only reason the first test went so well is because he resisted the effects."
    "God Dammit!"
    t "We need to end their suffering."
    with wipeleft_scene
    show sayori turned casual pani zorder 2 at t11
    s om "What?!"
    s rup "You can't possibly ask me to-{nw}"
    t "I don't want to hear it!"
    t "They can't live on like this."
    return

label tstory_ch5:
    play ambience factory
    scene bg factory with dissolve_scene_half
    call showlocation("Palace Factories Inc.\n{size=25}株式会社宮殿工場{/size}","July 4, 2018\n{size=15}2018年7月4日{/size}",20*60+4+57/60.0,"bg factory")
    s "It is done."
    t "Thank you."
    "The experiment went horribly wrong!"
    "Their personalities completely changed to ones they hate."
    "Things they used to like but now hate."
    "Not only that, their attributes changed too!"
    "ONE's now a copycat,"
    "TWO's now a rampant image,"
    "And THREE's now an ordinary girl."
    "We got the results we wanted, but not in the way we wanted."
    t "Dammit!  I didn't know this would happen!"
    t "Guess we were right not to trust a black substance."
    t "That sounded racist.  That's not what I meant."
    t "I just..."
    t "..."
    t "We need to get rid of the rest of them, make sure no one gets their hands on the substance."
    t "This experiment was a mistake!"
    return