label act1_ch5_main:
    stop music fadeout 2.0
    scene bg bedroom
    with dissolve_scene_full
    play music t2
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
    play music t5
    $ window_style = "fake"
    $ nb = "namebox_fake"
    scene bg club_day with wipeleft_scene
    call showlocation("The Literature Club\n{size=25}文芸部{/size}","October 3, 2023\n{size=15}2023年10月3日{/size}",16*60+29+57/60.0, "bg club_day")

    call kstory

    call tstory

    call sstory

    call ystory

    call mstory

    call nstory
   
    return