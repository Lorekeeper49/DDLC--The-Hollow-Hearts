label act1_ch2_main:
    stop music fadeout 2.0
    scene bg residential_day
    with dissolve_scene_full
    play music t2
    call showlocation("Residential Street","September 30, 2023",405.2, "bg residential") from _call_showlocation_4
    "Back to school after quite the weekend!"
    "Unlike most people though, I actually really like school.  It's a lot of fun to learn new things and have our knowledge tested on what was learned previously."
    "Plus, I have the literature club to look forward to everyday!"
    "That should be a lot of fun!"
    kmind "It sure is!"
    show sayori turned happ ce om zorder 2 at t11
    call addappeal("Sayori",0,s_appeal) from _call_addappeal
    show sayori zorder 2 at face
    "My train of thought is then broken by Sayori glomping me from behind."
    t "AH JESUS!"
    "Every time Sayori does this, she manages to knock me down to the floor, and {i}this{/i} is no exception!"
    t "Okay, Bun-chan, calm down!  CALM DOWN!"
    s oe tap pout "*Gasp* The safeword!"
    "She's referring to the nickname 'Bun-chan'."
    show kotonoha turned happ lup om zorder 1 at l41
    call addtrust("Kotonoha",0,k_trust) from _call_addtrust
    k "How does that safeword even work?"
    show kotonoha cm at t21
    show sayori turned rup happ at t22
    "Sayori gets off me."
    "Well, the English translation of her family name is 'cinnamon bun' but..."
    t "I don't know, probably because it's..."
    menu (time=3,force=0):
        "Cute.":
            t "Cute--like her?"
            call addappeal("Sayori",1,s_appeal) from _call_addappeal_1
            $ s_appeal += 1
            show sayori flus n3
            "Every time I compliment Sayori like this in her presence, she always blushes as if she likes me."
            "--You know like in {i}that{/i} sense."
            $ cute = True
        "Straight and to the point.":
            t "Straight and to the point?"
            call addappeal("Natsuki",1,n_appeal) from _call_addappeal_2
            $ n_appeal += 1
        "Simple and elegant.":
            t "Simple and elegant?"
            call addappeal("Yuri",1,y_appeal) from _call_addappeal_3
            $ y_appeal += 1
        "Freeform.":
            t "Freeform?"
            call addappeal("Monika",1,m_appeal) from _call_addappeal_4
            $ m_appeal += 1
    k lup om "I don't know, I think there might be something else going on."
    if cute:
        "Okay Koto-chan, admit it, you read my mind."
        kmind ldown cm "Yeah, I totally did."
    else:
        t "Maybe..."
    "Ignoring that, we continue on to the school."
    scene bg school_day with wipeleft_scene
    "Here we are at the 5 story school built by my family that is..."
    call showlocation("Sakura Academy","September 30, 2023",419.95) from _call_showlocation_5 
    "I feel like my thoughts were interrupted there."
    "Anyway, let's see here..."
    "English first, huh?"
    "A morning challenge, I like it!"
    stop music fadeout 0.5
    scene bg corridor with wipeleft_scene
    show kotonoha turned happ at t21
    show sayori turned happ at t22
    "We each arrive at our classes and promptly exchange goodbyes."
    hide kotonoha
    hide sayori
    play sound bell
    scene bg schoolriverday with wipeleft_scene
    play music t8 
    call showlocation("Sakura Academy River","September 30, 2023",725.45) from _call_showlocation_6 
    "It is now lunchtime, and I am hanging out at the river at the back of the school."
    "As always, I've gotten myself a delicious chicken yakisoba."
    "These are always really good around this time of year."
    "I don't know what it is, but seasons tend to mess with the texture of food that I change what I get for lunch every season."
    show natsuki turned curi rhip at l11
    call addappeal("Natsuki",0,n_appeal) from _call_addappeal_5
    n om "Oh, so you're the person I always see sittting here."
    show natsuki cm
    t "And you're the person I always see walking by here."
    t "Hey Natsuki."
    n dist om "Hello Taiyen."
    show natsuki cm
    "Still indifferent about me despite last time, huh?"
    "That's fine, I get that a lot, especially when fans finally meet me in person."
    "For some reason though, something feels off this time around."
    "Maybe I should check in on that when I have the chance."
    n curi om "It's interesting that we actually {i}know{/i} each other now instead of just being ignorant."
    show natsuki cm
    t "I agree."
    t "Would you like to take a seat?"
    "I pat the spot next to me on the bench."
    n happ om "Sure!"
    n dist om "(As long nobody gets any ideas...)"
    show natsuki cm
    t "(They'd more likely do that with Sayori and me.)"
    n rdown curi om "Pardon?"
    show natsuki cm
    t "That's an unimportant matter."
    n "Ok."
    show natsuki happ
    "She takes a seat where I indicated."
    n rhip lhip om "I saw you walking with your sister--for obvious reasons."
    n "But you also walked with Sayori."
    n ldown curi om "You do that every day, right?"
    show natsuki cm
    t "Yeah?"
    n rdown om "I don't know about you."
    n cross laug ce om "But I'd say you have a crush on her."
    show natsuki cm
    t "Why do I get that so much?"
    "Her laughs during that response just teased me even more."
    t "Like seriously, it's absurd how many times I hear that."
    n turned rhip lhip happ oe om "Well, I'm sure many would agree that it's fun to tease you."
    show natsuki cm
    "Tell that to Sayori."
    show natsuki ldown curi
    t "Speaking of crushes, how do you feel about people shipping you with Yuri-chan?"
    n dist om "Um...{w=0.5}  Honestly..."
    n "I'm fine with ships in general as long as they aren't..."
    n e1a "You know..."
    t "NSFW?"
    n e1b "Yeah, that."
    n e1a "I just... kinda feel indifferent about it, you know?"
    n "'Natyuri' is kinda of a weird thing."
    t "Not really, there are similar ships out there."
    $ nref()
    n rdown curi om "Sorry, I only familiar with a few select manga and anime."
    n "Could you name one?"
    show natsuki cm
    t "Takara?"
    t "From..."
    menu (time=3,force=1):
        "Parfait Girls.":
            t "...Parfait Girls?"
            call addappeal("Natsuki",2,n_appeal) from _call_addappeal_6
            $ n_appeal += 2
            n rhip lhip curi om "You know that one?"
        "Unknown.":
            t "I don't know, I've only heard of it a little while ago."
            n rhip lhip curi om "If you're talking about Taka x Nakara from Parfait Girls..."
    n ldown dist om "That's..."
    stop music fadeout 1.0
    n sad om "That's the manga my mother made..."
    show natsuki cm
    "Oh...{w=0.5}\nI didn't know that was a serious topic."
    t "I'm sorry!  I didn't know that was a hard topic for you!"
    t "I didn't even know that your mother was that one's mangaka."
    n e1a om "No, you're fine."
    n e1b "It's just..."
    n fs rdown neut ce cm "..."
    "I think I can put it together."
    play music depressed
    t "Hey it's okay."
    t "To tell you the truth..."
    t "I'm still trying to get over my loss."
    n rhip lhip sad oe om "You don't get it!"
    n ce "She's been gone for a year and a half."
    show natsuki cm
    "Jesus, that long!"
    n cry ce om "And it sucks even more that I had to watch her die!"
    show natsuki cm
    "That's-"
    "Oh my god!"
    scene black with dissolve_scene
    "In my shock, all I can do is comfort her."
    "I've never heard of anyone who's suffered a loss for that long."
    "So I just stay here with her like this for a while."
    scene bg schoolriverday with dissolve_scene_half
    play sound bell
    $ pause(4)
    "The bell ruins the moment."
    show natsuki turned rhip dist at t11
    n om "Thanks Taiyen."
    n "I'll... see you at club."
    show natsuki cm
    t "Yeah, see you."
    show natsuki at lhide
    hide natsuki
    stop music fadeout .5
    "*Sigh* jeez."
    "That was something."
    "Welp, now I know that there are more people I need to take care than just one if I want my friends to be happy."
    "Just hope I can do it correctly."
    play sound bell
    scene bg corridor with wipeleft_scene 
    play music t3
    call showlocation("The Literature Club","September 30, 2023",915.0) from _call_showlocation_7
    "At the end of the day, I usually go to the security room to monitor the clubs from the cameras while doing homework."
    "But from now on, someone else is taking that job because I'll be going to the Literature Club every day!"
    scene bg club_day with wipeleft
    show kotonoha turned happ zorder 1 at t41
    show natsuki turned happ zorder 3 at t22
    show yuri turned happ zorder 2 at t44
    show sayori turned happ zorder 4 at t21
    "Walking into class 5-A, I see the expected scene of all the girls looking at me."
    "...minus Monika-chan."
    hide kotonoha 
    hide natsuki 
    hide sayori 
    call addappeal("Yuri",0,y_appeal) from _call_addappeal_7
    hide yuri 
    "Then the door opens."
    show monika 4n zorder 2 at l11
    call addappeal("Monika",0,m_appeal) from _call_addappeal_8
    m "I'm back!  Sorry that took so long."
    m 4b "Oh!  Taiyen, konnichiwa."
    m 2n "Being the popular girl that I am, I ran into a bunch of fans."
    show monika at t21
    show natsuki turned rhip lhip curi zorder 1 at t22
    n om "Can't you faze through them?"
    show natsuki cm
    m forward flus ce om "Don't you remember what happened last time I did that?"
    show monika cm
    n ldown dist om "Oh yeah, {i}that{/i} was a nightmare."
    "What happened?"
    kmind "It's best not to talk about it."
    "Understandable given Natsuki's response."
    show monika forward rhip lpoint happ oe zorder 2 at t21
    hide natsuki
    show monika at t11
    if renpy.music.get_playing():
        stop music fadeout .5
    m rdown om "Well, now that we're all properly here,"
    m rhip "let's start sharing our stories!"
    play music t5
    m rdown ldown "I believe Sayori goes first today."
    show monika cm
    t "Not that I'm against that, but isn't it pretty much tradition that the new guy goes first?"
    show sayori 2a zorder 1 at r44
    t "No offense to Sayori of course."
    "Her face says: 'none taken'."
    show sayori at rhide
    hide sayori
    m 3n "We would normally do that, but we kinda already did you last time."
    "I was the {i}only one{/i} who was done."
    show natsuki turned rhip lhip anno zorder 1 at l41
    n om "You say that like he's out of the question."
    n rdown "I'm sure he wrote {i}something{/i} for today!"
    show natsuki cm
    t "In fact, I did."
    show natsuki happ
    m forward happ rhip om "In that case, we'll go by tradition today."
    m rdown "So you're up, the Imfamous Book Writing Taiyen-senpai!"
    "I get my own title, nice."
    show kotonoha turned happ zorder 1 at t41
    show natsuki ldown zorder 3 at t22
    show monika cm zorder 5 at t11
    show yuri turned happ zorder 2 at t44
    show sayori turned happ zorder 4 at t21
    "Taking the stage at the front of the room, I grab my newly written chapter and set it down in front of me."
    t "This book doesn't have a name yet, but it is based off true events that happened to me as a child."
    t "Enjoy."
    return

label act1_ch2_end:
    hide kotonoha
    hide natsuki
    hide monika
    hide yuri
    hide sayori
    "Having heard everyone's opinions, I step down from the pedestal and sit at my seat."
    show monika forward happ zorder 2 at t11
    m om "{i}Now{/i} it is Sayori's turn."
    hide monika
    $ currentpos = get_pos()
    $ audio.t5s = "<from " + str(currentpos) + " loop 4.444>bgm/5_sayori.ogg"
    stop music fadeout 2.0
    play music_swap t5s fadein 2.0
    show sayori turned rup happ zorder 2 at t11
    s om "Okay!"
    show sayori cm
    "She takes the stage on the pedestal."
    s om "My book for today is new!"
    s tap nerv om "It also doesn't have a name yet."
    n "Don't you usually come up with the name first?"
    s "I couldn't think of one over last night this time."
    m "That's okay, Sayori."
    s turned rup happ om "Anyway..."
    s rdown "Enjoy."
    "She begins reading the story."
    call sstory from _call_sstory
    show sayori turned rup happ zorder 2 at t11
    "Reading the male lines out loud like that was a little difficult...\nespecially when I'm not used to following along like that."
    "Not only that, but this story also seemed horrifyingly familiar..."
    "I don't know how to feel about that..."
    s rup om "So, what do all think so far?"
    s rdown "We'll start with..."
    s "Taiyen!"
    show sayori cm
    "Well I'm not bringing up the familiarity since it I have a hunch that it might be something that we don't really want to talk about right now."
    menu:
        "Great":
            t "Okay, I've read your all your other stories before..."
            t "But compared to them, this is something else!"
            t "I never knew you could write in such a style that is{w=1} basically the exact opposite of how {i}you{/i} are!"
            t "Especially considering most of your stories are based off {i}your{/i} personality."
            t "This is definitely something that I'm looking forward to for future chapters!"
            s om "Thank you very much!"
            call addappeal("Sayori",2,s_appeal) from _call_addappeal_9
            $ s_appeal += 2
        "Good":
            t "This is very interesting."
            t "May be a little confusing at first, but I know you're someone like me who likes jump straight into things."
            t "You might not have done that here, but it still is kinda fast action."
            t "I also know you known to write allegories, and good ones at that."
            t "It might take me a little while to figure the meaning here, but I'll be attached either way."
            s om "Thank you!"
            call addappeal("Sayori",1,s_appeal) from _call_addappeal_10
            $ s_appeal += 1
        "No opinion":
            t "Well, it's just the first chapter."
            t "I haven't really been form opinions on your stories from just one chapter in the past."
            t "I'll have to wait for more chapters before I can develop a proper opinion."
            s om "That's okay."
            pass
    s "Next up, Natsuki!"
    hide sayori
    show natsuki turned lsur rhip om zorder 2 at t11
    n "When did you start writing dark stories like this?"
    t "Since the beginning?"
    t "At least, her first story I read was pretty dark..."
    t "And every one after that..."
    n cross "Not like this."
    n "This sounds like it's setting up for something intense right off the bad."
    n neut "It also seems to be pitch black mysterious which I'm not sure how to feel about..."
    n turned lhip rhip "But, either way..."
    n happ "This could get really good."
    hide natsuki
    show sayori turned happ rup om zorder 2 at t11
    s "Thank you very much!"
    s "Yuri-chan shall go next!"
    hide sayori
    show yuri turned lsur rup om zorder 2 at t11
    y "This cinnamon bun has gone sour!"
    y "And I don't mean that in a bad way or anything."
    y "It's just that this story is seems to be setting up to more intense then your others."
    y "I'm looking forward to this!"
    show monika forward happ rhip lpoint at r44
    m om "Same opinion!"
    show kotonoha turned happ at l31
    k om "Same"
    show kotonoha at lhide
    show monika at rhide
    hide kotonoha
    hide monika
    hide yuri
    show sayori turned happ rup om zorder 2 at t11
    s om "Alright, thank you everyone!"
    hide sayori
    "She steps off the pedestal."
    show monika forward rhip happ zorder 2 at t11
    m om "Next up, the Ever Cheerful Natsuki."
    hide monika
    $ currentpos = get_pos()
    $ audio.t5n = "<from " + str(currentpos) + " loop 4.444>bgm/5_natsuki.ogg"
    stop music_swap fadeout 2.0
    play music t5n fadein 2.0
    show natsuki turned happ zorder 3 at t11
    n om "Okay."
    show natsuki cm
    "She takes the stage happily."
    t "Hold on, I'm sure I'll hear the others', but does Sayori have a title?"
    show monika forward lpoint happ zorder 1 at r44
    m om "Yes, 'Cinnamon Bun Sayori'!"
    t "Didn't I make that one for her?"
    show kotonoha turned lup happ zorder 2 at l41
    k "Yes.  In fact, she told us to use it!"
    t "Fine by me."
    show monika at rhide
    show kotonoha at lhide
    hide monika
    hide kotonoha
    t "Anyway, go ahead Natsuki."
    show natsuki rhip
    n om "Alright."
    n "This one's called 'Too Far For These Feelings...'."
    n "Enjoy!"
    "She begins reading the story."
    "It's a love story about a couple-named {rb}Anuawl{/rb}{rt}On-yu-all{/rt} and Sivad-who live kilometers from each other but still managed to fall in love, hence the name."
    "Sivad-the female-seems to live in a castle of sorts..."
    "And Anuawl-the male-lives in this sort of confusing cottage thing that is meant to be barren."
    "And no, this ain't no Romeo and Juliet, princess cliché."
    "The chapter ends with Anuawl meeting Sivad in her room."
    n "Alright, Sayori will start us for this one."
    hide natsuki
    show sayori tap pout zorder 2 at t11
    s "On-uu-owl...  On-uu-all... On-yu-all..."
    s turned neut om rup "Sorry, that name is just hard to pronounce with such a spelling."
    n "I don't blame you for struggling, I had trouble myself, in fact."
    s happ "Well, anyway..."
    s "For a first chapter, this goes really in depth and it puts you into curiosity."
    s "It's almost like it's setting up for something harsh already, and I like that."
    s tap nerv om "Well, I don't know if 'harsh' is the right word."
    hide sayori
    show monika forward happ lpoint om zorder 2 at t11
    m "I was about to say the same thing as Sayori, so you can just skip me."
    hide monika
    show kotonoha turned happ lup om zorder 2 at t11
    k "Same here!"
    hide kotonoha
    show natsuki turned happ lhip rhip om zorder 2 at t11
    n "Then that's 3 down."
    n "Let's have Taiyen-kun go next."
    show natsuki cm
    menu:
        "Great":
            t "I'll admit that despite the fact that I've written one myself, I'm not into love stories as a whole."
            t "That being said, I'm liking this one a lot."
            t "I love how this takes the exact oppisite of the girl next door, and somehow manages to figure out a way to make fun of the original trope at the same time."
            t "A perfect idea for a bad cliché."
            n om "Thank you very much!"
            call addappeal("Natsuki",2,n_appeal) from _call_addappeal_11
            $ n_appeal += 2
        "Good":
            t "I'll admit that despite the fact that I've written one myself, I'm not into love stories as a whole."
            t "That being said, this story seems to draw me in pretty well."
            t "It's almost like I want see what would happen if Sayori and I were in the oppisite situation we're in right now."
            t "I don't mean to imply that were dating or anything, I just love how this story basically hates on the whole girl next cliché."
            n om "Thank you very much!"
            call addappeal("Natsuki",1,n_appeal) from _call_addappeal_12
            $ n_appeal += 1
        "No opinion":
            t "Well, I've had my fair share of love stories so I'm not sure if I can say anything yet."
            t "I'll wait for more chapters before I develop an opinion."
            n om "That's fine."
            pass
    n happ om "Lastly, Yuri."
    hide natsuki 
    show yuri turned lsur rup om zorder 2 at t11
    y "I'm in shock!"
    y "This may be your best one yet!"
    y laug "I know that it may too early to say that considering it's only the first chapter."
    y happ "But I'm already hooked."
    y "I'm excited to see what this story will have in store for us in the next chapters."
    hide yuri
    show natsuki turned happ zorder 2 at t11
    n om "Thank you so much, everyone!"
    hide natsuki
    "She steps off the pedestal."
    show monika forward rhip happ zorder 2 at t11
    m om "Next is the Shy but Gracious Yuri."
    hide monika
    $ currentpos = get_pos()
    $ audio.t5y = "<from " + str(currentpos) + " loop 4.444>bgm/5_yuri.ogg"
    stop music fadeout 2.0
    play music_swap t5y fadein 2.0
    show yuri turned rup happ zorder 2 at t11
    y om "Understood."
    show yuri cm 
    "She takes the stage with unnecessary but radiating grace."
    y rup om b2b "This ones called 'Stories From the Dark Days'."
    "Why does she look sad?"
    y "Enjoy."
    call ystory from _call_ystory
    show yuri turned rup happ b2b zorder 2 at t11
    "..."
    y om "So, how-"
    show yuri at t41
    show monika forward lsur at r44
    show sayori turned lsur om at r33
    show natsuki turned lsur om at rightin(720)
    show kotonoha turned neut om at r11
    everyone "Fuck, that's deep!"
    $ yref()
    show yuri turned lsur om
    everyone "Oh-"
    show monika lsur ce at s44
    show sayori dist ce cm at s33
    show natsuki dist ce cm at sink(720)
    show kotonoha neut ce cm at s11
    everyone "{rb}Gomenasai...{/rb}{rt}Apologies...{/rt}"
    y "No, you're fine."
    show monika at rhide
    show sayori at rhide
    show natsuki at rhide
    show kotonoha at rhide
    hide monika
    hide sayori
    hide natsuki
    hide kotonoha
    show yuri at t11
    y "I didn't hear you in that, Taiyen;"
    "You can tell?"
    y "What did you think?"
    menu:
        "Great":
            t "Well, you know I'm not one to cuss..."
            t "But I agree fully."
            t "This is very deep and emotional."
            t "I also like how this feels like it actually happened at some point in the past."
            t "I'm not gonna ask if it did since that might be a personal topic if so..."
            t "But I'm definitely looking forward to anything else that happened in these 'Dark Days'."
            call addappeal("Yuri",2,y_appeal) from _call_addappeal_13
            $ y_appeal += 2
        "Good":
            t "This is my cup of tea!"
            t "Deep stories have always been good to me."
            t "I also like how this feels like it actually happened at some point in the past."
            t "I'm not gonna ask if it did since that might be a personal topic if so..."
            t "But I'm definitely looking forward to anything else that happened in these 'Dark Days'."
            call addappeal("Yuri",1,y_appeal) from _call_addappeal_14
            $ y_appeal += 1
        "No opinion":
            t "While I am fond of deep and dark stories..."
            t "This one may not be doing it for me yet."
            t "Later chapters will decide, that's for sure."
            pass
    y happ om "Well, thank you everyone."
    hide yuri
    "She steps off the pedestal."
    $ currentpos = get_pos()
    $ audio.t5m = "<from " + str(currentpos) + " loop 4.444>bgm/5_monika.ogg"
    stop music_swap fadeout 2.0
    play music t5m fadein 2.0
    show monika forward rhip happ zorder 2 at t11
    m om "My turn!"
    show monika cm
    t "'The Inspirational and Beautiful Monika'!"
    show monika curi rdown
    t "Or so I've heard from my classmates."
    m laug e1b n2 om "Yep, that's my title.  Hehehe..."
    $ mref()
    m happ om "Anyway,"
    m "This one's called 'The Not-so-Perfect Girl'."
    m "Enjoy."
    call mstory from _call_mstory
    show monika forward rhip happ zorder 2 at t11
    m om "Apologies for the cliffhangar, but that's where the introduction ends."
    m "Let's have Kotonoha go first this time."
    hide monika
    show kotonoha turned happ zorder 2 at t11
    k om "Okay!"
    k "So this story has a lot of potential, but I have a feeling that this could get deep into lore for potentially good reason."
    k cm "..."
    "Her eyes are darting around"
    k ce om "Oh- tehaha...{w=3}{nw}"
    show kotonoha oe
    extend "Literally everyone had the same opinion."
    k happ "Except for maybe Taiyen."
    menu:
        "Great":
            t "I mean, I sort of did."
            t "I loved it, but it's hard to make predictions for this one like I usually do."
            call addappeal("Monika",2,m_appeal) from _call_addappeal_15
            $ m_appeal += 2
        "Good":
            t "I mean, I sort of did."
            t "I liked it, but it's hard to make predictions for this one like I usually do."
            call addappeal("Monika",1,m_appeal) from _call_addappeal_16
            $ m_appeal += 1
        "No opinion":
            t "No, I did."
            pass
    hide kotonoha
    show monika forward rhip happ zorder 2 at t11
    m om "That's understandable."
    m "Well, that's it for me-"
    stop music_swap
    t "Wait a second!"
    m neut "Huh?"
    t "Kanzen Academy is a real place that burned down 3 years ago!"
    t "And the things I've heard about it match what that story said!"
    show natsuki turned shoc om zorder 1 at r44
    n "Wait, hold on, WHAT?!"
    show yuri turned shoc om zorder 1 at l41
    y "Wait, Monika, you went to that school, didn't you?!"
    "She did?!"
    t "Is this a true story?"
    show natsuki at rhide
    show yuri at lhide
    hide yuri
    hide natsuki
    m ce "*sigh*"
    m rdown "Yes..."
    m "And honestly..."
    m pani cm "I'm terrified to write this fully..."
    "What?"
    t "You don't have to."
    m neut om "I know...{nw=2}"
    show monika oe cm
    extend "\nI want to."
    "Kirinani... Kirinani..."
    play sound flashback
    scene bg residential_day
    show hanato 1a zorder 3 at t21
    show inari 1a zorder 2 at t22
    show memory_vignette zorder 300 
    with flashback_start
    ha "Seriously Inari, did you even {i}listen{/i} to what Kirinani told {i}each{/i} of us to do?"
    scene bg club_day
    show monika forward neut oe cm rhip zorder 2 at t11
    with flashback_end
    "!!!"
    t "{b}CRAP!{/b}"
    show kotonoha turned curi oe om zorder 1 at r41
    show monika curi oe om zorder 5 at t11
    show natsuki turned curi oe om zorder 3 at l22
    show yuri turned curi oe om zorder 2 at l44
    show sayori turned curi oe om zorder 4 at r21
    everyone "What?"
    "Because I'm panicking, I said that out loud without thinking!"
    t "I can't explain much right now, but we might be friends with the people of that wretched school, and it could be bad if I'm correct about this!"
    t "I'm gonna look into this as soon as possible and report back once I have an answer!"
    everyone "Okay..."
    show kotonoha zorder 1 at rhide
    show natsuki zorder 3 at lhide
    show yuri zorder 2 at lhide
    show sayori zorder 4 at rhide
    hide kotonoha
    hide sayori
    hide natsuki
    hide yuri
    m cm "Uh..."
    m happ om "Anyway..."
    "She steps off the pedestal."
    m om "Lastly, the Cherry Blossom Kotonoha!"
    hide monika
    $ audio.t5c = "<from 0 loop 4.444>bgm/5.ogg"
    play music t5c
    show kotonoha turned happ zorder 2 at t11
    k om "One story chapter coming right up!"
    show kotonoha cm
    "Even after hearing that title so many times, I still wonder who the heck came up with it."
    "I mean, seriously... 'Sakura' {i}means{/i} 'cherry blossom'!"
    "Then again, I made up the 'Cinnamon Bun Sayori' title 'Shinamonpan' means 'cinnamon bun' so I'm kinda one to talk."
    k om "This ones called 'Nighttime Endeavors'."
    k "Enjoy!"
    call kstory(False) from _call_kstory
    show monika forward lhip zorder 2 at t11
    m om "So that's what you've been doing..."
    hide monika
    show kotonoha turned zorder 2 at t11
    k ce om "Yes."
    k oe "Like Monika's story, this is a true story."
    k "However, this one's more investigative than anything."
    show kotonoha cm
    t "So I don't have to worry about Akira."
    k "That is correct."
    "Good."
    k lup "This story's for providing information so I don't think we need to worry about opinions."
    "Well, that's interesting."
    hide kotonoha
    "She steps down from the pedestal."
    play music t5
    show monika forward rhip happ zorder 2 at t11
    m om "Whew, what a line-up!"
    m "I certainly am excited to see what's gonna happen in all of these books!"
    show monika cm
    t "I should mention that we are just past the time limit."
    m happ e1b om "That's only the second time, and we apologize"
    show monika cm
    t "No, it's alright.  As you know, there's no way to get into trouble in this scenario unless you're still in the building when the gate closes in about 10 minutes."
    m e1a om "Right, we have time."
    show kotonoha turned happ zorder 1 at t41
    show natsuki turned happ zorder 3 at t22
    show monika ldown zorder 5 at t11
    show yuri turned happ zorder 2 at t44
    show sayori turned happ zorder 4 at t21
    "We each exchange goodbyes--aside from the people walking together--and head home to call it a day."
    stop music fadeout 1
    scene black with dissolve_scene_full
    play music ghostmenu
    $ kirinani = "???"
    kiri "Hanato-kun, are you sure about this?"
    "Hanato?"
    ha "Of course I am, onii-chan!  I {i}want{/i} Taiyen-kun to hear us this time."
    "I think I know these people."
    kiri "Alright, he's all yours."
    "His voice sounds horribly familiar."
    ha "Oh, don't worry about that."
    "*Sigh*"
    "Why are you making me listen to making me listen to you on purpose this time, Hanato?"
    ha "*Creepy giggle* Oh, nothing."
    ha "I just want you to know that you're being watched..."
    "Not just watched, but also stalked."
    ha "By Itsomi, sure."
    ha "But also by me!"
    ha "Now that I have entered your daydream, I know your every move from this point forward."
    ha "So, you better think hard about your choices {i}before{/i} you make them..."
    ha "because once you do-"
    "-there's no going back and you guys can easily ruin my day."
    ha "Or worse.  *Creepy giggle*"
    ha "That's your message."
    ha "I'll be talking to you while you're awake now."
    ha "Be ready."
    ha "*Creepy giggle*"
    call showintro(intro_ha) from _call_showintro
    return