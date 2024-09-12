label tstory(r=True,bgreturn="bg club_day"):
    if renpy.music.is_playing(channel="music_swap"):
        $ previouschan = "music_swap"
        stop music_swap fadeout 2.0
    else:
        $ previouschan = "music"
        stop music fadeout 2.0
    scene black with dissolve_scene
    $ style.say_window = style.window
    $ nb = "namebox"
    $ nextscene = "tstory_ch" + str(chapter)
    call expression nextscene from _call_expression_8
    stop music fadeout 2.0
    stop sound fadeout 2.0
    scene black with dissolve_scene
    $ style.say_window = style.window_fake
    $ nb = "namebox_fake"
    $ audio.t5 = "<from 0 loop 4.444>bgm/5.ogg"
    if r:
        $ renpy.music.play(audio.t5, channel=previouschan, fadein=2.0)
    scene expression bgreturn with dissolve_scene_half
    return

label tstory_ch2:
    scene bg factory with dissolve_scene_half
    call showlocation("Palace Factories Inc.","September 29, 2015",20*60+4+57/60.0,"bg factory") from _call_showlocation_31
    $ pla = "Worker"
    t "Oi!  Stop slacking off!  Get back to work!"
    general "You're not the boss of me!"
    t "Hey, don't make me report that attitude to your real boss, who is out sick for the week."
    t "So, like it or not, I'm your boss for this week!"
    t "And I don't know about you, but I personally wouldn't want to be fired by my substitute boss!"
    "God, do these guys ever learn?"
    "I may sound strict, but this is how the actual boss is with slacking workers."
    
    return

label tstory_ch3:
    scene bg factory with dissolve_scene_half
    call showlocation("Palace Factories Inc.","October 1, 2015",20*60+4+57/60.0,"bg factory") from _call_showlocation_32
    t "So... this is who I'm taking care of for the rest of the week."
    "NAME: [[UNKNOWN]"
    "ATTRIBUTE: STORM"
    "APPEARANCE: BLACK HAIR, BLUE EYES, SHORT STATURE"
    if known or config.developer:
        scene bg club_day with None
        t "..."
        m "Something wro-{nw}"
        t "Hold on a second."
        t "(Black hair, blue eyes...)"
        t "(Attribute: Storm...)"
        t "I just described Aoruguri!"
        show sayori turned neut om at t21
        show monika forward neut om at t11
        show kotonoha turned neut om at t41
        show natsuki turned neut om at t22
        show yuri turned neut om at t44
        everyone "*Quiet gasp*"
        "Everyone looks at me in shock."
        t "This all happened 8 years ago (I'm not surprised she didn't recognize me)."
        t "Now I understand why her voice seemed so familiar for so long..."
        t "Sorry, I'm going off topic!"
        t "Let's continue."
        scene bg factory with blink

    return

label tstory_ch4:
    scene bg factory with dissolve_scene_half
    call showlocation("Palace Factories Inc.","October 1, 2015",20*60+4+57/60.0,"bg factory") from _call_showlocation_33

    return

label tstory_ch5:
    scene bg factory with dissolve_scene_half
    call showlocation("Palace Factories Inc.","October 2, 2015",20*60+4+57/60.0,"bg factory") from _call_showlocation_34
    s "It is done."
    t "Thank you."
    "The experiment went horribly wrong!"
    "Their personalities completely changed to ones they hate."
    "Things they used to like but now hate."
    "Not only that, their attributes changed too!"
    "ONE's now a copycat,"
    "TWO's now a rampant image,"
    "And THREE's now an ordinary girl."
    t "Dammit!  I didn't know this would happen!"

    return

label storyresponse_start:
    $ yref()
    $ sref()
    $ nref()
    $ kotoref()
    $ storysread = 0
    $ skip_transition = False
    label storyresponse_loop:
        $ skip_story = False
        if renpy.music.get_playing() and not (renpy.music.get_playing() == audio.t5 or renpy.music.get_playing() == audio.t5c):
            $ renpy.music.play(audio.t5, fadeout=1.0, if_changed=True)
        $ skip_transition = False
        if not renpy.music.get_playing():
            play music t5
    label storyresponse_start2:
        if chapter == 0:
            show sayori turned happ zorder 4 at t21
            show natsuki turned casual happ oe cm zorder 3 at t22
            show yuri turned casual happ zorder 2 at t44
            show kotonoha turned ldown casual happ zorder 1 at t41
            show monika 1ba zorder 5 at t11
            with wipeleft
        else:
            show sayori turned happ zorder 4 at t21
            show natsuki turned happ oe cm zorder 3 at t22
            show yuri turned happ zorder 2 at t44
            show kotonoha turned happ zorder 1 at t41
            show monika forward happ zorder 5 at t11
            with wipeleft
            dev "Skipping over this since it is actually unfinished and I wanted to this demo out as fast as possible."
            $ storysread = 5

        $ skip_story = False
        if storysread == 0:
            voice "voicelines/taiyen/first.ogg"
            $ menutext = "The person who should go first is..."
        else:
            voice "voicelines/taiyen/next.ogg"
            $ menutext = "The person who should go next is..."
        if chapter == 0:
            if storysread == 0:
                $ storysread = 1
            $ k_readstory = True
            $ k_last = True
        menu:
            t "[menutext]"

            "Sayori" if not s_readstory:
                $ s_readstory = True
                if storysread == 0:
                    $ s_first = True
                elif storysread == 1:
                    $ s_second = True
                elif storysread == 2:
                    $ s_third = True
                elif storysread == 3:
                    $ s_fourth = True
                else:
                    $ s_last = True
                call storyresponse_sayori from _call_storyresponse_sayori
            "Natsuki" if not n_readstory:
                $ n_readstory = True
                if storysread == 0:
                    $ n_first = True
                elif storysread == 1:
                    $ n_second = True
                elif storysread == 2:
                    $ n_third = True
                elif storysread == 3:
                    $ n_fourth = True
                else:
                    $ n_last = True
                call storyresponse_natsuki from _call_storyresponse_natsuki
            "Yuri" if not y_readstory:
                $ y_readstory = True
                if storysread == 0:
                    $ y_first = True
                elif storysread == 1:
                    $ y_second = True
                elif storysread == 2:
                    $ y_third = True
                elif storysread == 3:
                    $ y_fourth = True
                else:
                    $ y_last = True
                call storyresponse_yuri from _call_storyresponse_yuri
            "Monika" if not m_readstory:
                $ m_readstory = True
                if storysread == 0:
                    $ m_first = True
                elif storysread == 1:
                    $ m_second = True
                elif storysread == 2:
                    $ m_third = True
                elif storysread == 3:
                    $ m_fourth = True
                else:
                    $ m_last = True
                call storyresponse_monika from _call_storyresponse_monika
            "Kotonoha" if not k_readstory:
                $ k_readstory = True
                if storysread == 0:
                    $ k_first = True
                elif storysread == 1:
                    $ k_second = True
                elif storysread == 2:
                    $ k_third = True
                elif storysread == 3:
                    $ k_fourth = True
                else:
                    $ k_last = True
                call storyresponse_kotonoha from _call_storyresponse_kotonoha
        $ storysread += 1
        if storysread <= 4:
            jump storyresponse_loop


    $ s_readstory = False
    $ n_readstory = False
    $ y_readstory = False
    $ m_readstory = False
    $ k_readstory = False
    $ storysread = 0
    return

label storyresponse_sayori:
    hide sayori
    hide natsuki
    hide yuri
    hide kotonoha
    hide monika
    with wipeleft
    
    show sayori turned happ zorder 2 at t11
    with wipeleft
    voice "voicelines/taiyen/sayori.ogg"
    t "Sayori."
    $ nextscene = "ch" + str(chapter) + "_s"
    call expression nextscene from _call_expression_9
    hide sayori with wipeleft
    return

label storyresponse_natsuki:
    hide sayori
    hide natsuki
    hide yuri
    hide kotonoha
    hide monika
    with wipeleft
    
    if chapter == 0: 
        show natsuki turned casual happ zorder 2 at t11
        with wipeleft
    else:
        show natsuki turned happ zorder 2 at t11
        with wipeleft
    voice "voicelines/taiyen/natsuki.ogg"
    t "Natsuki."
    $ nextscene = "ch" + str(chapter) + "_n"
    call expression nextscene from _call_expression_10
    hide natsuki with wipeleft
    return

label storyresponse_yuri:
    hide sayori
    hide natsuki
    hide yuri
    hide kotonoha
    hide monika
    with wipeleft
    
    if chapter == 0: 
        show yuri turned casual happ zorder 2 at t11
        with wipeleft
    else:
        show yuri turned happ zorder 2 at t11
        with wipeleft
    #voice "voicelines/taiyen/yuri.ogg"
    t "Yuri-chan."
    $ nextscene = "ch" + str(chapter) + "_y"
    call expression nextscene from _call_expression_11
    hide yuri with wipeleft
    return

label storyresponse_kotonoha:
    hide sayori
    hide natsuki
    hide yuri
    hide kotonoha
    hide monika
    with wipeleft
    
    if chapter == 0: 
        show kotonoha turned casual happ zorder 2 at t11
        with wipeleft
    else:
        show kotonoha turned happ zorder 2 at t11
        with wipeleft
    # #voice "voicelines/taiyen/koto.ogg"
    t "Koto-chan."
    $ nextscene = "ch" + str(chapter) + "_k"
    call expression nextscene from _call_expression_12
    hide kotonoha with wipeleft
    return

label storyresponse_monika:
    hide sayori
    hide natsuki
    hide yuri
    hide kotonoha
    hide monika
    with wipeleft

    if chapter == 0: 
        show monika forward casual happ zorder 2 at t11
        with wipeleft
    else:
        show monika forward happ zorder 2 at t11
        with wipeleft
    if chapter == 0:
        voice "voicelines/taiyen/murikou.ogg"
        t "Murikou-san."
    else:
        #voice "voicelines/taiyen/monika.ogg"
        t "Monika-chan."
    $ storyopinion = "med"
    $ nextscene = "ch" + str(chapter) + "_m"
    call expression nextscene from _call_expression_13
    hide monika with wipeleft
    return

label ch0_m:
    m rhip e1b om "How about you just call me 'Monika' since we're in the same club and you're doing that with everybody else?"
    show monika cm
    "We've gotten pretty close as friends now so..."
    t "Sure, I'm fine with that, Monika-chan."
    t "And by that logic, you should probably be calling Taiyen."
    m e1a om "You're right!"
    m lean happ om "Taiyen-senpai."
    show monika cm
    "Okay, now I'm embarrassed."
    m forward rhip happ om "Anyway!"
    m "On with my opinion."
    m lpoint "I think that this is a very enjoyable book."
    m "I like how you gave the narrator a conciousness as if he's witnessed all of it happen from a bird's eye view."
    show monika cm
    t "I'll be honest."
    t "I kinda did that on accident."
    m "Well, you actually did that really well!"
    m "I also like how you wrote a poem at the start."
    t "Also by accident."
    m rdown ldown laug ce om "Haha, of course you did!"
    m happ oe om "But, on to the story."
    m rhip lpoint "I really like what you've done with this story."
    m "It's very deep, dark, and emotional."
    m "I like it a lot!"
    m ldown "But if you want more details on what we think of the story, ask Yuri."
    if y_readstory:
        t "I already have."
        m rdown ce "Great!"
    else:
        t "I will."
    m rhip lpoint oe "Well!"
    m "There's my opinion!"
    show monika cm
    t "Thank you very much, Monika-chan."
    m om "You're welcome!"
    return

label ch0_s:
    s rup om "Alright."
    s "Well, gotta say..."
    s lup "I've been missing out!"
    s ldown "What you've done here is really enjoyable and emotional."
    s "It really hits you where it hurts with the feelings."
    s ce "And I think that's the best kind of story!"
    show sayori oe cm
    "Something about how she said that last part felt off for some reason."
    "Have we not won the war or something?"
    "Unlikely."
    "I'll just ignore it."
    t "I'm glad you liked it!"
    t "Got anything else to say about it?"
    s rdown om "Not really."
    show sayori cm
    t "Then I'll move on."
    s om "Okay."
    return

label ch0_y:
    y om "With pleasure!"
    y "So..."
    if m_readstory:
        y "As monika said,"
    y "I will be be focusing more on the story for this review."
    y e1b "Also, I have a habit of rambling, so apologies for that."
    show yuri cm
    t "That's fine."
    t "I'm used to reading extremely long reviews on what I publish."
    y e1a om "Good."
    if storysread > 1:
        y rup "So, like the others said,"
    else:
        y rup "So, like the others will say,"
    y "This story is deeper than I thought it would be."
    y lup "I love how each character has their own problems to deal with."
    y "And those problems are dealt with in such dramatizing ways."
    show yuri cm
    t "I actually kinda based that off of how I am in those situations."
    y ldown curi om "Really?"
    y "That's surprising."
    y "Especially considering you're a dead man."
    show yuri cm
    "Why is that a stereotype?"
    "..."
    "Wait, hold on."
    t "You know what attribute I have?"
    y om "Well I am a yangire."
    show yuri cm
    t "Um..."
    t "I haven't encountered a yangire yet."
    t "But my experience with the tamer varient, the yandere, was not pleasent."
    t "I almost died."
    y rdown happ om "Well, I can assure you..."
    y "I never had, and still don't have, any intention of hurting anyone..."
    y 2br "Unless they deserve it."
    "I know that face all too well."
    t "I apologize, but I'm still gonna be cautious around you until that's verified."
    y turned casual rup dist om "That's fine, I get that a lot."
    y happ om "Anyway."
    y "Besides what I've already said."
    y rdown "I don't think I have anything else to say about this book."
    show yuri cm
    t "Alright!"
    t "Thank you very much for your opinion!"
    y rup ce om "You're very welcome!"
    return

label ch0_n:
    if storysread > 1:
        n cross om "Well, unlike everyone else, I'm gonna be mainly criticizing this book."
    else:
        n cross om "Well, I'm gonna be mainly criticizing this book."
    show natsuki cm
    t "I like your angle."
    t "Whenever I look at the reviews for my work, I mainly look for criticisms so I know what I could do better."
    n mi "In that case, you better open your ears."
    show natsuki md
    t "Way ahead of you."
    n turned om "Good."
    n cross "Now, on with the book."
    n "Gotta say, the story you have here is very intriguing and funny."
    n mi "But..."
    n "It leaves a lot of questions."
    n "Like, how did Lucia get out from following the novel's script?"
    n "That's probably the biggest question."
    show natsuki md
    t "I actually plan on making a sequel that answers those questions."
    "That actually might be what I write for this club."
    n mi "Well it better be good."
    n "A lot of sequels lately have been terrible."
    show natsuki md
    t "I'll try to make it good."
    t "Even though I've never made a sequel before."
    n turned lhip rhip happ om "Well, I have nothing else to say."
    show natsuki cm
    t "Alright!"
    t "Thanks for your criticisms."
    t "I'll take them into account."
    return

label ch2_k:


    return

label ch2_s:


    return

label ch2_n:


    return

label ch2_y:


    return

label ch2_m:


    return

label ch3_k:


    return

label ch3_s:


    return

label ch3_n:


    return

label ch3_y:


    return

label ch3_m:


    return

label ch4_k:


    return

label ch4_s:


    return

label ch4_n:


    return

label ch4_y:


    return

label ch4_m:


    return

label ch5_k:


    return

label ch5_s:


    return

label ch5_n:


    return

label ch5_y:


    return

label ch5_m:


    return