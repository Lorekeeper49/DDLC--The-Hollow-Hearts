label kstory(r=True,bgreturn="bg club_day"):
    if renpy.music.is_playing(channel="music_swap"):
        $ previouschan = "music_swap"
        stop music_swap fadeout 2.0
    else:
        $ previouschan = "music"
        stop music fadeout 2.0
    scene black with dissolve_scene
    $ style.say_window = style.window
    $ nb = "namebox"
    $ nextscene = "kstory_ch" + str(chapter)
    call expression nextscene from _call_expression_4
    stop music fadeout 2.0
    stop sound fadeout 2.0
    scene black with dissolve_scene
    $ style.say_window = style.window_fake
    $ nb = "namebox_fake"
    if r:
        $ renpy.music.play(audio.t5c, channel=previouschan, fadein=2.0)
    scene expression bgreturn with dissolve_scene_half
    return

label kstory_ch2:
    scene bg city_street_night with dissolve_scene_half
    call showlocation("Bustling Streets","September 29, 2023",20*60+4+57/60.0,"bg city_street_night") from _call_showlocation_17
    k "Ugh!  Why is that so difficult!?"
    "I look around after getting kicked out."
    "The game I was playing is hard as balls trapped in an air fryer!"
    "{cps=3}...{/cps}"
    "That is officially the weirdest thing I've ever said, especially in my head."
    k "*Sigh* Jacob?"
    "He comes out."
    show jacob 1bh1 zorder 2 at t11
    $ pause(0.5)
    call showintro(intro_j) from _call_showintro_3
    j "*Sigh* That is an embarrasing death."
    k "They were swarming us!"
    j 1be "Wanna do another attempt?"
    k "We can't, it's late and the club's probably worried."
    j 2ba "Right.  Let's head back to HQ."
    hide jacob
    "We walk for a bit."
    $ pause(3.0)
    "I stop."
    show jacob 2ba zorder 2 at t11
    k "It's...  It's not right!"
    j "What?  Me being here?"
    k "No-"
    j 1bh1 "I get it.  There's no way an Ordinary man like me-"
    k "That's not what I'm talking about!"
    show jacob 1ba
    k "We're breaking into so many abandoned places..."
    k "going through so many dangers..."
    k "meeting so many fates...!"
    k "It's not right!  None of this is right!"
    k "So many people have died!"
    k "Ian...  Himari...  Charlotte...  Shiro...!"
    k "Not to mention all the people who went missing and never came back!"
    k "And for what?  To get at an overgrown mimic who's to powerful for his own good?"
    k "Face it, Jacob!"
    k "We're never gonna kill Kirinani!"
    k "It's impossible!"
    k "*Sob*"
    $ pause(1.0)
    show jacob 2ba
    j "Maybe so..."
    j "{i}If{/i} we didn't have help from his own family."
    k "What?"
    j "Follow me, I know where he is."
    scene bg shed_night with wipeleft_scene
    call showlocation("Shed Hideout","September 29, 2023",20*60+14+57/60.0,"bg shed_night") from _call_showlocation_18
    show akira 1ac zorder 2 at t11
    "...{w=1}Huh?"
    hide akira
    show jacob 2ba zorder 2 at t11
    k "Akira?  Why him?  He's like Kirinani's right hand man!"
    j 1ba "Well, why do {i}you{/i} like him?"
    k "Uh-?  *Flustered noise*\n...Fair point..."
    j 2ba "He's a spy, and a good one at that."
    j 1be "Oi!  Akira!"
    k "Eh-W-Wait!"
    show akira 1ac zorder 2 at t22
    show jacob at t21
    "Akira comes over."
    k "I wanted you to at least explain things before calling him over!"
    "No one takes notice of me."
    ak 4ac "Jacob...  Did you do it again?"
    j 2bh1 "*Sigh*"
    ak 2ae "Ugh!  Jacob, I told you not to use STASIS to train!  It is unhealthy and doesn't actually do anything to the physical body.\n{{While he is yelling, He is not shouting STASIS, that's just the capitalisation of the device}"
    j 2be "Yeah, yeah...  Listen, Kotonoha's here, say hi."
    show akira 4ae
    "He looks at me."
    ak 4ag "So... we're finally telling {i}her{/i} about me, huh?"
    ak 1ag "Good, I don't have to hide anymore."
    hide jacob
    show akira at t11
    ak "Hi Kotonoha, it's me.  I spy on my family."
    k "You sound like you're tired of this job."
    ak 4ak "I'm not tired of the job, I'm tired of staying up until midnight every day."
    "Right, he's like me; one of the unlucky ones that actually get tired."
    k "You can take a break at any time."
    ak 4ag "Actually, I can't!"
    ak 3ag "My brother's doing so much evil, I can't take my eyes off him for a second!"
    k "That reminds me, why would a copycat who can give his comrades attributes not give them the ability to not get tired?"
    ak 4ak "I've asked him that same question, and his answer was 'I wish it worked that way'.  And frankly, I agree."
    "Your telling me?  I wish {i}I{/i} could give people attributes, let alone the ability to not get tired."
    k "So, this is what you've been doing behind my back!"
    ak 1ao "Yes... and it ain't easy."
    "If only we could make it easier."
    "Well at least I know I can trust him."
    "That is reassuring."
    return

label kstory_ch3:
    scene bg pasteur_night with dissolve_scene_half
    call showlocation("Kanzen Academy Ruins","September 30, 2023",60*23+59+57/60.0,"bg pasteur_night") from _call_showlocation_19
    k "You sure we'll be able find anything here?"
    k "The place is completely destroyed."
    show jacob 2ba zorder 2 at t11
    j "Yeah, Luna really did a number on this place."
    k "Not to mention the fact that they cleaned up the place so well it's almost like it never existed."
    j 1ba "Which means we're going underground!"
    scene bg sewer_hall with wipeleft_scene
    "Shit..."
    "I can barely see."
    "Don't like the sewers already, but {i}this{/i} is worse!"
    show jacob 2ba zorder 2 at t11
    j 2ba "We could get lost in here if we're not careful."
    "No need to state the obvious..."
    j 1ba "If I'm correct about this, there should be a factory nearby..."
    hide jacob
    "We look around."
    k "Found it!"
    "Convenient that the door's labeled."
    k "Locked!"
    j "There's another door that leads to a business room, it might have a spare key they left behind. {{Calling out}"
    k "Okay, I'll stay here!"
    "{cps=1}...{/cps}"
    "It's so quiet..."
    $ pause(1.0)
    scene bg sewerwatched with dissolve_scene
    $ pause(1.0)
    k "Eh?"
    "Am I... being watched?"
    show jacob 1ba zorder 2 at r11
    j "I'm back!"
    k "Ah!  Jesus Christ!"
    k "Ha...  Hi!"
    k "You scared the shit out of me!  Jesus!"
    j 2bb "Tehehe, sorry!"
    "Sure sounds like it!"
    j 1ba "Anyway, let's get moving."
    show jacob 2ba at lhide 
    $ pause(1.0)
    hide jacob
    $ pause(1.0)
    scene bg sewer_hall with dissolve_scene
    $ pause(1.0)
    scene bg factory with wiperight_scene
    k "We're{nw}"
    scene bg club_day with None
    play sound bang
    $ pause(1.0)
    play sound bang
    $ pause(1.0)
    play sound bang
    $ pause(1.0)
    play sound bang
    show bg club_dark with None
    $ pause(0.15)
    show bg club_day with None
    $ pause(0.15)
    show bg club_dark with None
    $ pause(0.15)
    show bg club_day with None
    $ pause(0.55)
    play sound bang
    show bg club_dark with None
    $ pause(0.15)
    show bg club_day with None
    $ pause(0.15)
    show bg club_dark with None
    $ pause(0.15)
    show bg club_day with None
    $ pause(0.55)
    play sound bang
    show bg club_dark with None
    $ pause(0.15)
    show bg club_day with None
    $ pause(0.15)
    show bg club_dark with None
    $ pause(0.15)
    show bg club_day with None
    $ pause(0.55)
    play audio bang
    play audio fall
    show bg club_dark with None
    $ pause(5.0)
    play sound jumpscare
    show lilly doll a0 zorder 2 at face
    $ pause(0.5)
    t "GET OUT NOW!!!{w=0.5}{nw}"
    scene bg sky with wipeleft_scene
    $ pause(1.0)
    return

label kstory_ch4:
    call showlocation("???","October 1, 2023",23,59,57) from _call_showlocation_20

    return

label kstory_ch5:
    call showlocation("???","October 2, 2023",23,59,57) from _call_showlocation_21

    return