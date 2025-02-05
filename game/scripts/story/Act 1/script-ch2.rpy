label act1_ch2_main:
    stop music fadeout 2.0
    scene bg bedroom
    with dissolve_scene_full
    call showlocation("Taiyen's Room\n{size=25}隊円の部屋{/size}","September 30, 2023\n{size=15}2023年9月30日{/size}",405.2, "bg bedroom")
    $ style.say_window = style.window
    $ nb = "namebox"
    show monika forward rhip zorder 2 at t11
    $ add_to_inv("Pen", "ペン", _("A pen for writing"))
    $ add_to_inv("Notebook", "ノートブック", _("My massive collection of notes"))
    $ add_to_inv("PC", "パソコン", _("My crappy laptop."))
    "Routine checkup."
    m om "Any progress?"
    t "No."
    show monika dist cm
    "I'm the only one who knows about her unidentified attribute."
    show monika neut
    t "Your power is still beyond even my comprehension."
    t "I don't get it."
    t "I really don't."
    t "It seems to be similar to copycat in that you have abilities similar to others."
    t "But on the other hand, it also seems to be an entirely new power that we haven't discovered yet."
    m curi "So, what are you thinking?"
    t "Hmm..."
    t "Now that I've joined your literature club, I may be able to gather more data based on how you act in there."
    t "I'll bring my notebook to see what I can jot down."
    m neut "We're still keeping this secret, right?"
    t "Per your request."
    m rdown "Thank you."
    hide monika
    "She leaves."
    "I should head to school."
    scene bg residential_day with wipeleft_scene
    $ style.say_window = style.window_fake
    $ nb = "namebox_fake"
    play music t2
    call showlocation("Residential Street\n{size=25}住宅街{/size}","September 30, 2023\n{size=15}2023年9月30日{/size}",6*60+59+57/60.0, "bg residential_day")
    show lilly norm de zorder 2 at t31
    show sayori turned happ rup zorder 2 at t32
    show yuri turned happ zorder 2 at t33
    s om "Hey, Taiyen!  Over here!"
    "And this is why Monika can't leave my house normally."
    show sayori cm
    t "Hey everyone!  Nice to see ya!"
    t "How are you all doing?"
    y rup om "We're all doing just fine."
    show yuri cm
    t "Good!"
    s om "Koko-tan went on ahead."
    show sayori cm
    t "Figured.  She always does that."
    t "Lilly!  Glad to see you have recovered nicely."
    lil ee "Thank you!"
    show lilly de
    y om "The flu doesn't get her that easily!"
    y dist lup "(How does she even get sick?)"
    show sayori curi
    t "Sorry?"
    y curi "Huh?"
    y "Oh!{w=1}{nw}"
    show yuri happ ldown rdown
    extend "  Nothing."
    show yuri cm
    t "Okay."
    "Could've sworn she said something."
    s happ om "Let's not worry about that right now and get to school!"
    t "Yeah!"
    scene bg class_day with wipeleft_scene
    call showlocation("Class 3-A\n{size=25}3年A組{/size}","September 30, 2023\n{size=15}2023年9月30日{/size}",7*60+29+57/60.0, "bg class_day")
    show lilly norm de zorder 2 at t31
    show sayori turned happ rup zorder 2 at t32
    show yuri turned happ rup zorder 2 at t33
    t "Gotta say, I find it interesting but also fun that all 4 of us are in the same class."
    lil ee "Yeah, we got kinda lucky."
    show lilly de
    t "The only one missing is Koto-chan, who got class B."
    t "But that's fine, I had her class twice in a row in the last 2 years."
    hide lilly
    hide sayori
    hide yuri
    "We all take our seats."
    show yuri turned happ zorder 2 at t11
    "Yuri-chan's got seat 5-5 in the back corner."
    show yuri at t22
    show lilly norm de zorder 2 at l21
    "Lilly has seat 4-5, in front of her sister."
    show lilly at t21
    hide lilly
    hide yuri
    show sayori turned happ zorder 2 at t11
    "Sayori's got seat 2-3, right behind me."
    hide sayori
    "And I have seat 1-3 at the front of the class."
    $ pla = "先生\n{size=15}Teacher{/size}"
    general "Alright class!  Let's begin!"

    stop music fadeout 1.0
    scene bg schoolriverday with dissolve_scene_full
    call showlocation("Sakura River\n{size=25}桜川{/size}","September 30, 2023\n{size=15}2023年9月30日{/size}",11*60+29+57/60.0, "bg schoolriverday")
    $ add_to_inv("Bento", "弁当", _("Just in case I eat with a friend."))
    $ add_to_inv("Chicken Yakisoba", "チキン焼きそば", _("My favorite food."))
    show natsuki turned dist rhip zorder 2 at t11
    t "Oh hello, Natsuki."
    n neut om "Hey, Taiyen."
    t "Whatcha doing?"
    n dist cm "..."
    n cross "I like to come here."
    n turned "See that path?  Just over there?"
    "She points across the water to a path next to a campsite."
    n lhip "Walk along it for about a kilometer and you'll reach a mansion."
    n ldown rdown "It's... where I used to live."
    n cross "My sister and I would use this as an escape from... things I'm going to be talking about in my story..."
    n cm "..."
    t "Where do you live now?"
    n om "Besides the dorms?  Nowhere."
    n turned "I'm currently saving up to buy a small house near the area."
    t "Same here."
    n lsur "That's a dorm village?"
    show natsuki cm
    t "Yes."
    "To seperate from normal schools, this school owns small villages that house the students of each class who opt in for dorms."
    "It's a little more expensive than traditional dorms-"
    "Scratch that, it's a lot more expensive than traditional dorms."
    "And it doesn't even fit the proper definition of the word 'dormitory'."
    "That's why I just call them households."
    "But people see it as better because they can bring out more personality and the introverts generally like being more seperated from their classmates."
    "I wouldn't know though, I've never lived in a traditional dorm."
    "...{w=1}Who the hell am I explaining this to?"
    n rdown om "Wow.  I never look at the map, so I didn't realize how big the town area is."
    show natsuki cm
    t "My dorm's under renovation though."
    t "They're trying to add more rooms to the place."
    n cross om "Huh."
    n turned rhip "For being the founder's son, you'd think you'd have a better place."
    t "I don't know, my family's never been one to brag about their riches."
    n cross "I see."
    show natsuki dist
    "She looks back toward the river."
    n ce cm "..."
    t "..."
    n turned ldown rdown vsur oe om "Ah!"
    t "Huh?"
    "She looks across the river."
    n cross "What?"
    "..."
    "I think I know what this is."
    t "You see your sister?"
    show natsuki turned
    "She points across the river."
    t "There's no one in my view."
    t "This happens to a lot of people."
    show natsuki rhip
    "She pulls back and attempts to regain her composure."
    n lsur rdown "And now I see myself with her over there."
    n dist cm "..."
    n ce om "*Sigh*"
    n cross oe neut "I forgot to grab lunch, I'll be back."
    menu(time=5.0,force=1):
        "Give her food.":
            t "I have food for you."
            n turned rhip "No, you don't have to-"
            t "I insist."
            n cm "..."
            n lhip om "Alright, whatcha got?"
            call .food_prompt
            "I hand her my [selected_item]."
            $ remove_from_inv(selected_item)
            if selected_item == "Chicken Yakisoba":
                n lsur ldown rdown "You're giving me that?"
                "Apparently everyone knows what my favorite food is."
                n rhip "Are you sure?"
                t "Of course."
                n rdown "Wow."
            else:
                n happ "Always gotta have you're favorite food, huh?"
                show natsuki cm
                "Apparently everyone knows what my favorite food is."
            n cross happ "Thanks."
            show natsuki cm
            t "You're welcome!"
        "Let her go.":
            t "Okay."
            hide natsuki
            "She leaves."
            "Maybe I should've given her something..."
            show natsuki cross
            "She comes back with a bento."
    "She sits down on a nearby bench and begins her food."
    "I sit down next to her and begin my food."
    n curi om "Does that happen to you at all?"
    show natsuki cm
    t "What?  Seeing my family like that?"
    n cross om "Yeah."
    show natsuki cm
    t "It's different for everybody."
    t "I have it worse."
    t "They keep telling me their death was my fault."
    show natsuki worr
    t "I don't want to believe them, but at the same time..."
    t "There's concrete evidence that it's true..."
    n turned rhip om "Do I want to know what that means?"
    t "You'll find out eventually..."
    t "I almost don't want to talk about it."
    t "But at the same time, everyone needs to know what happened."
    t "Sayori said she'd be streaming every meeting now, so I'd better deliver."
    n cross laug "She is taking a big doxing risk in doing that."
    show natsuki cm
    t "Sakura Academy looks pretty similar to other schools, we should be fine as long as no one says the name of the school."
    n turned rhip om "30% of her fans attend Sakura Academy."
    t "And how do you know that?"
    n happ "That poll on the notice board.  I'm the one who put it up."
    show natsuki cm
    t "Oh!  I did not notice that."
    t "I've heard you being called the survey girl around the school, I didn't know what that meant until now."
    n cross anno om "I hate that name..."
    n ce "There are far better things to know me by."
    t "You're talking to the so-called 'Black Lab Scientist'!"
    n turned shoc oe "That's who they're referring to?"
    t "Right here in the flesh!"
    

    
    return

label .food_prompt:
    call screen inventory_view(Return())
    if selected_item != "Bento" and selected_item != "Chicken Yakisoba":
        "...{w=1}She can't eat that!"
        jump .food_prompt
    return