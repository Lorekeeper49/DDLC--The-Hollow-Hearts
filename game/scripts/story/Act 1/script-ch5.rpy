label act1_ch5_main:
    stop music fadeout 2.0
    scene bg bedroom
    with dissolve_scene_full
    call showlocation("Taiyen's Room\n{size=25}隊円の部屋{/size}","October 3, 2023\n{size=15}2023年10月3日{/size}",6*60+0+0/60.0,"bg bedroom")
    $ window_style = ""
    $ nb = "namebox"
    show yuri turned anno rup om zorder 2 at t11
    "Routine Therapy."
    y ce "*Sigh* No good."
    t "What's wrong?"
    y oe "My pay's been dropping lately, I don't think I'm taking enough notes."
    t "You're doing fine."
    t "Haven't you been taking more notes now that I'm part of the literature club?"
    y laug "I've forgotten to bring my notebook on several occasions."
    t "That's a surprise."
    y happ "No one's perfect, Taiyen-kun."
    t "Have you considered asking for a raise?"
    y anno "I'm not gonna get one with my current performance!"
    t "You think...  You think Iru could take over?"
    "Still not used to that name."
    y laug lup "How much work do you think she's done?"
    t "...Zero."
    y ldown "Exactly."
    y rdown "I didn't even know she existed until yesterday."
    show yuri cm
    t "I thought you would at least have some suspicion given how much Lilly might've mentioned her."
    y om "I never believed her until now."
    "She seems unsure about who Iru is.  Don't blame her."
    "I wanna know who Iru is as well, I don't know if I ever met her."
    show yuri neut
    t "Anyway, I've got no plans for today.  Wanna do another session during lunch?"
    y om "I was actually having some trouble finishing my story and I want to make sure I can do that before club."
    t "Then I'll just go about my day as usual."
    show yuri cm
    "Yuri-chan begins packing her things."
    t "Hey, Yuri-chan?"
    y curi "Hm?"
    t "Thanks for everything regarding therapy.  I really needed it."
    show yuri happ
    "She smiles."
    play sound door
    hide yuri
    "..."
    t "*Sigh*"
    t "I've got a lot to take care of..."
    $ window_style = "fake"
    $ nb = "namebox_fake"
    scene bg club_day with wipeleft_scene
    play music t5
    call showlocation("The Literature Club\n{size=25}文芸部{/size}","October 3, 2023\n{size=15}2023年10月3日{/size}",15*60+29+57/60.0, "bg club_day")
    "As I had so much to do, I couldn't find enough free time to think back."
    "I'll be talking to you later tonight."
    show kotonoha turned angr lup zorder 2 at t11
    k om "Alright everyone, I think I'll go first today.  I wanna get this out as soon as possible."
    if ctold:
        "No one seems to be mentioning yesterday."
        "Must be still trying to process it."
    t "You seem angry."
    k ce "That would be an understatement..."
    call kstory
    show kotonoha turned angr rhip ce zorder 2 at t11
    k om "Guy's a fucking asshole."
    t "Sounds like it."
    t "Is it possible that he was also lying to himself?"
    k anno oe "It is, but I'm not so sure if he did do that."
    t "I think I know an acquaintance of his, maybe I can ask their opinion of this."
    k angr "Let me know what he says."
    t "Will do."
    hide kotonoha
    t "Anyway, I'll go next."
    call tstory
    t "You all already know this part of the story."
    t "But as it would turn out..."
    t "Sayori lied to me."
    show lilly norm a1 zorder 2 at t11
    t "Obviously Lilly is still alive."
    t "And the others are as well."
    hide lilly
    t "She... didn't put them out of their misery like she was asked to..."
    show sayori turned dist rup zorder 2 at t11
    t "I don't know where they are now..."
    t "But their suffering needs to be ended."
    hide sayori
    t "..."
    t "Who's next?"
    show sayori turned neut rup zorder 2 at t11
    s om "Me."
    call sstory
    show sayori turned neut rup zorder 2 at t11
    s om "If you're wondering how it is that we found out what pre-life is, I honestly doesn't remember."
    t "I think we just found out through studying patterns of birth."
    s laug "Right."
    s neut "Anyway, now that I know the story of Natsuki-chan, I now know who that storm is."
    s rdown "Luna Aoruguri."
    s laug "I have no idea how to spell that name, by the way."
    hide sayori
    show natsuki cross neut zorder 2 at t11
    n om "Jesus.  That explains her personality."
    n turned rhip "...And why she went crazy so many times."
    n rdown "I'll talk about in my story."
    n rhip "I volunteer to go last."
    hide natsuki
    show yuri turned happ zorder 2 at t21
    show lilly norm de zorder 2 at t22
    y om "Us."
    call ystory
    show yuri turned dist zorder 2 at t21
    show lilly norm a1 zorder 2 at t22
    t "So that's what happened to her."
    t "Hm..."
    t "The description of what came out of her sounds familiar, but I'm not sure what it is."
    hide lilly 
    hide yuri
    show kotonoha turned neut lup zorder 2 at t11
    k om "Sounds like wraiths."
    show kotonoha cm
    t "Huh?"
    t "But that wasn't..."
    t "Is that how someone sabotaged us?"
    k ldown rhip om "I don't know, but we can discuss this later, okay?"
    t "Okay..."
    hide kotonoha
    show monika forward neut rhip zorder 2 at t11
    m om "Alright, I'm next."
    call mstory
    show monika forward neut rhip zorder 2 at t11
    m om "You guys know the rest of the story..."
    m ce "*Sigh*"
    m dist oe "Yeah, a lot happened during the fight...  I'd rather not rewrite those events."
    m neut "Natsuki, you're up."
    hide monika
    show natsuki cross neut zorder 2 at t11
    n om "Got it."
    call nstory
    "We all stayed silent for a good few minutes."
    show monika forward dist rhip zorder 2 at t11
    m om "I think we should call it a day."
    "Everyone agrees."
    scene black with dissolve_scene_full
    $ window_style = ""
    $ nb = "namebox"
    "CONTROLLER..."
    "I don't know what your plan is or what you want to do..."
    "But it's clear who your boss is..."
    "And I bet he doesn't have good plans for me considering how he is today."
    "And all because of me..."
    "I just hope I can trust you..."
    if ctold:
        "Maybe I can, since you told everyone about yourself yesterday..."
        "But that doesn't tell me everything..."
    "..."
    return