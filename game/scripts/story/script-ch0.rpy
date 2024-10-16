label ch0_main:
    $ style.say_window = style.window
    $ nb = "namebox"
    stop music fadeout 2.0
    call showintro(intro_t) from _call_showintro_6
    scene bg house
    with dissolve_scene_full
    $ restore_all_characters()
    t "Ugh!  My head!"
    "I really need to talk to someone about this."
    "We can't just keep this between me and my sister."
    "The Shinamonpans are next door so that'll be my quickest option."
    scene bg shouse_day with wipeleft
    "I walk up to the Shinamonpans' door."
    "I'm just about to ring the doorbell when the door opens,"
    show sayori turned happ zorder 2 at t11
    "showing Sayori in her school uniform?"
    "On the weekend?"
    call showintro(intro_s) from _call_showintro_7
    s om "Oh!  Hello Taiyen!"
    s "What you brings you here without warning?"
    show sayori cm
    t "It's complicated..."
    t "Look, can I come inside?"
    s rup om "Of course!  You're always welcome here!"
    show sayori cm
    t "Thank you!"
    s rdown om "By the way, don't mind the uniform.  I ran out of normal clothes and forgot to do laundry yesterday."
    t "Of course you did..."
    "I walk inside and Sayori closes the door behind me."
    scene bg slivingroom with wipeleft 
    "Of course I forgot to take my medication today..."
    "I'm already seeing them."
    "I'll just try to ignore them for now."
    show sayori turned rup worr e1a om zorder 2 at t11
    s "You look troubled, what's up?"
    "*Sigh*"
    show sayori rdown cm
    "I take a seat and Sayori sits next to me."
    t "You remember how my parents died over a month ago?"
    "A rhetorical question used to point out who I've been seeing for the past month now."
    s mi "How could I forget something as terrible as that?"
    show sayori cm
    t "Well..."
    "Deep breaths."
    t "A day after that, I started having hallucinations of them."
    t "I talked to my doctor about it, and she gave me some medicine that prevents them from showing up for until 21:00." 
    t "Which is my bedtime."
    s mi "How have they been doing?"
    show sayori cm
    t "They've been pretty tame for the time being."
    t "But last night was..."
    t "strange..."
    t "and terrfiying"
    t "allow me to explain."
    scene black with dissolve_scene_full
    dev "This is meant to be a video cutscene, I haven't finished it yet."
    # $ renpy.movie_cutscene("") #remember to uncomment later
    scene bg slivingroom with dissolve_scene_full 
    show sayori turned worr e1a mh zorder 2 at t11
    s "They were saying you killed them?"
    s rup mi "But-!  That's impossible!  I know what happened."
    s lup "I witnessed you beat the ever-loving shit out of your orphanizer!"
    show sayori ldown rdown cm
    t "Exactly!"
    t "I don't know why-"
    t "..."
    "I couldn't think of anything else to say after that."
    s curi rup e1a om b1b "Say, I've got a weekend club meeting today, you wanna come visit to take your mind off things?"
    "I'm caught a little off gaurd by the abrupt question."
    show sayori cm
    t "Well..."
    t "Actually, you're vice president of the literature club, right?"
    s om "Yes, I am."
    show sayori cm
    t "What exactly do you guys do there?"
    s "We usually read books and discuss them."
    s rup happ om "But we've also been writing our own stories and discussing those as well!"
    s "Honestly, that's the most fun activity we've had yet!"
    show sayori cm
    t "Oh!"
    s rdown "So, what do you say?"
    show sayori cm
    t "Hmm."
    "This actually sounds like a place where I'll be able to present my material as I'm writing it."
    "That could be a fun experience."
    t "You know what?"
    s "Hm?"
    t "Why not?  I'll go ahead and visit after I run to the store and grab some groceries."
    "I am running dangerously low on cooking ingredients and soap."
    s lup rup ce om b1a "YAY!!!"
    s ldown oe "Here!  Let me give our meeting address."
    show sayori cm
    "Sayori pulls out her phone and texts an address to me."
    s om "Come by when you're done!"
    show sayori rdown cm
    t "I will!"
    "I say that with a smile."
    t "Well, I'm off!  I'll text you when I'm on my way."
    "I say as I stand up and walk to the door."
    s rup om "I'll see you there!"
    show sayori cm
    "I gently close the door and walk away from Sayori's house."
    scene bg house with wipeleft
    "Ok, this is starting to get annoying!"
    "Let me take my meds before setting off to the store."
    scene bg kitchen with wipeleft
    "I walk into my kitchen and spot my medication lying on the counter and promptly take it."
    "The hallucinations disappear almost immediately."
    "Now I'm off to go buy some groceries."
    $ style.say_window = style.window_fake
    $ nb = "namebox_fake"
    scene bg store with wipeleft_scene
    play music t2
    "Goodness gracious!  This place is packed!"
    "I might get lost in here."
    "On the plus side, I don't have any prescription to pick up today."
    "But that doesn't account for the massive amount of people within this store."
    "Let's just grab everything before it gets worse."
    scene bg kitchen with wipeleft_scene
    "I managed to grab everything within 15 minutes and drop them off at my house in the kitchen."
    t "I'll organize everything later."
    stop music fadeout 3
    "{cps=1}..."
    "Is my sister here?"
    t "Koto-chan?"
    "No response."
    t "Koto-chan?"
    "No response."
    "I check her room."
    scene bg kotoroom with wipeleft
    t "Koto-chan?"
    "The door's open and there's no sign of her,"
    "meaning that she's probably off playing with her friends."
    "I won't worry about it."
    "Though, what happened to the cleanliness of this room?"
    "Eh... whatever."
    "I head out of the house and set off for the club."
    window hide
    $ audio.deadamb = "mod_assets/sounds/deadamb.ogg"
    play sound deadmantrans
    $ renpy.music.play(audio.deadamb, channel="ambience", fadein=0.5)
    show veins with blink
    scene bg park_01
    show veins
    with ZoomTransition
    $ pause(0.1)
    play sound deadmantransout
    hide veins with blink
    $ renpy.music.stop(channel="ambience", fadeout=0.5)
    call showlocation("Kamiyama Park","September 28, 2023",719.95,"bg park_01") from _call_showlocation_45
    show kotonoha turned casual happ zorder 1 at t41
    show monika forward casual happ zorder 5 at t11
    show natsuki turned casual happ zorder 3 at t22
    show yuri turned casual happ zorder 2 at t44
    show sayori turned happ zorder 4 at t21
    "I arrive and immediately notice 5 girls who look like they're setting up for a party."
    "One of them is Sayori and..."
    "Wait, hold on!"
    "Is that...?"
    t "Koto-chan?"
    hide sayori
    hide monika
    hide natsuki
    hide yuri
    show kotonoha at t11
    k curi om "Hm?"
    show kotonoha turned curi cm
    "She realizes who I am."
    play music t3
    k happ ce mc "Tai-kun!"
    show kotonoha at face
    "Kotonoha runs toward and hugs me like the loving sister that she is."
    t "Whoa hey!  Koto-chan, calm down!"
    "She's about to knock me over when I'm still a little jet-lagged from what happened last night."
    show kotonoha at t11
    k "Alright, alright."
    "She said that in a way that sort of indicated that she basically read my mind and forgot about the situation I'm in."
    show kotonoha oe cm
    t "Been a while since you've done that to me."
    t "Kinda missed it since then."
    show monika forward casual rhip happ zorder 2 at t21
    show kotonoha zorder 3 at t22
    m om "Kotonoha, who's thi-"
    show monika rdown neut om zorder 2 at t21
    "Wait a second!"
    "I know this girl from last year!"
    m "Sakura-senpai?"
    "This is Murikou Monika, one of my big fans."
    $ m_name = "Murikou Monika"
    "We were in the same class last year and we talked quite a bit after she read one of my books and really liked it."
    "We even became friends because of it."
    t "Murikou-san?"
    t "You never told me you were part of this club."
    m nerv om "Oh my gosh!  I'm so sorry, Senpai!  I totally thought I did."
    k lup surp oe om "I thought so too, that's why I never said anything!"
    k ldown rhip e1c om  "Come on, Monika.  He's your senpai!"
    m dist ce om "I know."
    show sayori turned rup happ n2 e1c mb zorder 2 at l41
    show monika zorder 3 at t32
    show kotonoha zorder 3 at t33
    s "You're kinda stealing Natsuki's role here, Koko-tan."
    "I had totally forgotten about that adorable nickname Sayori gave my sister."
    "I'd call her that but I don't want her to be confused as to who's talking."
    show sayori at lhide
    hide sayori
    show monika zorder 2 at t21
    show kotonoha zorder 3 at t22
    "Moving on from that, I attempt to reassure Monika."
    t "It's fine Murikou-san."
    t "We can be forgetful like that sometimes, even if we aren't the type."
    show monika neut oe om zorder 2 at t21
    m "True."
    show kotonoha turned ldown rdown surp e1c cm
    m rhip lpoint "But what about you?  How have you been doing lately?"
    m "That assembly had me worried."
    show kotonoha turned sad ce 
    "I know what she is talking about."
    stop music fadeout 1.0
    scene black with dissolve_scene_full
    dev "This is meant to be a video cutscene, I haven't finished it yet."
    # $ renpy.movie_cutscene("") #remember to uncomment later
    scene bg park_01 with dissolve_scene_full 
    show kotonoha turned casual ldown rdown sad ce cm zorder 1 at t41
    show monika forward casual sad ma zorder 5 at t11
    show natsuki turned casual happ b1b zorder 3 at t22
    show yuri turned casual sad e1a ma zorder 2 at t44
    show sayori turned happ b1b zorder 4 at t21
    "After a while, we release."
    m rhip lpoint mb "Let's change the subject to something less deppressing, shall we?"
    k happ oe b1b "Yeah."
    $ layeredimage_ref("yuri")
    $ layeredimage_ref("monika")
    show kotonoha b1a 
    show monika casual happ 
    show natsuki b1a
    show yuri casual happ 
    show sayori b1a 
    play music t5
    s rup om "Well since Taiyen's joining the literature club, let's introduce the members he doesn't know."
    hide sayori
    hide monika
    hide natsuki
    hide kotonoha
    show yuri zorder 6 at t11
    y rup om "We'll do that ourselves, thank you."
    y "I am Yandere Yuri from class 1-D."
    $ y_name = "Yandere Yuri"
    y rdown laug om "And yes, my family name is 'Yandere'."
    y happ om "Don't question it."
    show yuri cm
    t "I won't Yandere-san."
    y rup om "Just call me Yuri."
    show yuri cm
    t "Alright, Yuri-chan."
    hide yuri
    show natsuki turned casual happ zorder 2 at t11
    "Next is a short pink-haired girl."
    n lhip om "I am Tetsuo Natsuki, class 2-B, the tsundere of the group."
    show natsuki cm
    $ n_name = "Tetsuo Natsuki"
    t "Most tsundere don't like to admit that about themselves."
    "Actually, I don't think I've seen a single tsundere admit that they are as such."
    n cross happ om "Well, I'm quite different from the ones you see in anime or manga."
    show natsuki cm
    t "I can tell."
    n turned lhip om "And since we're in the same club, how about you just call me Natsuki?"
    show natsuki cm
    t "Fine by me, Natsuki."
    show kotonoha turned casual happ zorder 1 at t41
    show monika forward casual happ zorder 5 at t11
    show natsuki ldown zorder 3 at t22
    show yuri turned casual happ zorder 2 at t44
    show sayori turned happ zorder 4 at t21
    "Well, that's everyone."
    "Time to introduce myself."
    t "Well everyone, my name is Sakura Taiyen from class 1-A, I'm the author of many books within the school library."
    n lhip om "It's funny how we literally just read one of your books yesterday and now you're joining the club."
    show natsuki cm
    t "Oh!  Which one?"
    y rup om "'The Salvage Seek'." #subtle reference to Doki Doki Salvaged, the first DDLC mad I ever saw
    y ce "Love how abstract that name is, by the way!"
    show yuri cm oe
    t "That's what I was going for."
    "I state that proudly."
    t "That's actually the first book that I wrote fully and published to the library."
    t "What did you girls think of it?"
    m 4bm "We're bound to talk at the same time, so you should choose the order we say our opinions."
    k lchest om "I don't count for obvious reasons."
    show kotonoha turned cm
    n cross happ ce om "Yeah, you've probably read the book hundreds of times!"
    show natsuki cm
    t "In that case..."
    return

label ch0_end:
    show sayori turned happ zorder 4 at t21
    show natsuki turned casual happ zorder 3 at t22
    show yuri turned casual happ zorder 2 at t44
    show kotonoha turned casual happ zorder 1 at t41
    show monika forward casual happ zorder 5 at t11
    with wipeleft
    t "Well, I'm glad you all liked the book!"
    s rup om "We certainly did!"
    show sayori cm
    y rup om "We can tell you spent a lot of time on it."
    t "Almost a year, to be exact."
    k om "Yeah, he's pretty persistent when it comes to writing things."
    t "Hey, you are too, Koto-chan!"
    k laug ce om b1a "Yeah, you're right, Tai-kun!"
    k oe "We pretty much never stop writing a book until it's finished."
    t "Yeah, we don't."
    show kotonoha happ cm
    y "Wow, you must have a lot of determination."
    n 2bd "Not as much as that striped shirt kid though!"
    "You got that right!"
    show natsuki screamb at h22
    show yuri pani lup om at h44
    show kotonoha nerv mg e1d at h41
    s 4m "AH!!  WE COMPLETELY FORGOT!!!"
    "Jesus Christ, Sayori, you almost gave me a fricking heart attack!"
    m rhip neut ce om "Calm down, Sayori."
    m "We'll throw that welcome party for your friend."
    "How is Monika-chan completely unfazed by this?"
    kmind "Her attribute allows that."
    kmind "She says she knows what people say or do before that say or do that thing."
    kmind happ cm oe "That's all we know about it though."
    show natsuki turned casual happ
    show yuri happ cm
    show sayori turned lup rup happ
    "Okay then."
    t "Doesn't this already count as a welcome party?"
    m laug e1b cm "Um... sort of?"
    m happ e1a om "Sure, we'll call it that."
    kmind "3... 2..."
    "Does she know that I can hear her as well?"
    $ layeredimage_ref("monika")
    show sayori ce om at h21
    show monika casual happ ce om at h11
    show kotonoha lchest happ ce mc at h41
    show natsuki lhip rhip ce om at h22
    show yuri lup ce om at h44
    everyone "Welcome to the literature club Sakura Taiyen!"
    show sayori at t21
    show monika at t11
    show kotonoha at t41
    show natsuki at t22
    show yuri at t44
    everyone "We hope you enjoy your stay!"
    t "Thank you very much, everyone!"
    t "I certainly will enjoy my stay!"
    hide sayori
    hide monika
    hide kotonoha
    hide yuri
    show natsuki at t11
    n ldown oe om "Here, let me give you something!"
    show natsuki rdown cm
    "Natsuki waves her hands in front of me and gives away that she is a food materializer by materializing a cake in front of me."
    kmind "'Food materializer' is the most generic name for her attribute ever."
    "It is, but I don't think there are any better names anyone can think of."
    show yuri turned casual rup happ zorder 2 at t44
    y "That cake is far too big for him."
    show yuri cm
    "Yuri-chan says as knives form above the cake."
    "My nerves are shot at the sight of this."
    n mi "Wait.  Cut it into sixths."
    n "This cake is for everyone."
    show natsuki md
    y om "Very well."
    show natsuki cm
    show yuri cm
    "The cake is cut and a piece is handed off to me, Yuri-chan, Natsuki, and everyone else out of my view."
    t "{rb}Arigatou gozaimasu!{/rb}{rt}Thank you very much!{/rt}"
    "Not the traditional food blessing, but either way, I take a bite."
    "..."
    t "Oh... my... god!  WHAT!?"
    t "Natsuki, there is no way that you just made this out of thin air!"
    t "This tastes amazing!"
    n cross laug ce cm "My methods are secret!"
    "Aw, come on."
    kmind "No matter how hard you try, she'll never tell you."
    "I know, that's why I didn't say that out loud."
    show natsuki at lhide
    show yuri at lhide
    hide natsuki
    hide yuri
    "Also, Koto-chan, since do you use your telegraphic powers so much?"
    kmind "I'm just trying to help you get used to everyone."
    "I already am, but thanks."
    kmind "No problem!"
    "I finish the cake and notice that Natsuki has moved from my view."
    show sayori turned happ zorder 4 at t21
    show natsuki turned casual happ zorder 3 at t22
    show yuri turned casual happ zorder 2 at t44
    show kotonoha turned casual happ zorder 1 at t41
    show monika forward casual happ zorder 5 at t11
    with wipeleft
    "I turn around and notice that everyone is sitting at a picnic table."
    hide natsuki
    hide monika
    hide kotonoha
    hide yuri
    show sayori at t11
    "I promptly take a seat next to Sayori since that was the only seat left."
    hide sayori
    show yuri turned casual rup happ zorder 5 at t11
    y om "Would anyone like some tea?"
    show yuri cm
    show monika forward casual happ zorder 2 at t44
    m om "Yes, please."
    show monika cm
    show sayori turned rup happ om zorder 4 at t21
    s "I'll take some!"
    show sayori cm
    show kotonoha turned casual happ om zorder 1 at t41
    k "That would be nice."
    show kotonoha cm
    show natsuki turned casual happ zorder 3 at t22
    n om "I'll take anything from you, Yuri!"
    show natsuki cm
    t "I think having some tea would be rather relaxing."
    t "But where are you going to do it?"
    t "I dont see a fire anywhere."
    s rdown anno om "You're forgetting about what I can do?"
    s rup angr ce om "I am disappointed!"
    t "Oh my god!  Sayori, I am so sorry, I completely forgot that the happy life attribute,{w=0.3} the attribute that{w=0.3} {i}I{/i}{w=0.3} gave you,{w=0.3} can heat up objects incredibly fast on top of the other things it can do!"
    s oe "Hmm."
    s "I'll let you off the hook this time."
    show sayori cm
    t "Thank you."
    show sayori turned happ oe
    n rhip curi om "What's this about 'giving her' an attribute?"
    show natsuki cm
    t "Long story, we'll talk about it later."
    n "Okay."
    show natsuki turned happ
    "And like in literally every drama, she completely disregards it."
    show monika at lhide
    show kotonoha at lhide
    show natsuki at lhide
    show sayori zorder 4 at t21
    show yuri zorder 3 at t22
    hide monika
    hide kotonoha
    hide natsuki
    "Sayori quickly heats up the water while Yuri-chan sets out tea cups for everyone with a tea bag in each cup."
    hide sayori
    hide yuri
    show natsuki turned casual rup curi zorder 2 at t11
    n om "Can you at least give us a short version?"
    show natsuki cm
    "Okay nevermind, she didn't disregard it."
    t "Doing that will inevitably lead to the long story, so..."
    t "Let's just say..."
    t "..."
    t "You know what, nevermind!"
    t "I can't think of anything to help with this."
    n lhip om "That's fine, I wasn't gonna force you."
    hide natsuki
    show sayori turned rup happ om zorder 4 at t21
    show yuri turned casual happ zorder 3 at t22
    s "Tea's ready!"
    show sayori cm
    "Sayori pours the tea into each cup while everyone thanks her and Yuri-chan greatly."
    hide sayori 
    hide yuri
    "I take a sip of the tea and immediately feel the relaxing sensation that tea often produces."
    "The taste is soothing, and the heat is just right to calm my already calm brain."
    "It also feels familiar somehow."
    show yuri turned casual rup happ zorder 3 at t11
    t "Yuri-chan?"
    y curi om "Yes?"
    show yuri cm
    t "Did you, by any chance, happen to have any acquaintance with my parents?"
    t "Because this feels very similar to their tea."
    y om "Well, this is actually their brand since I ran out of ingredients for my own brand."
    show yuri cm
    t "Oh..."
    mom "You really like that tea, don't you?"
    y nerv e1a "Eh!  I'm sorry!  I didn't mean to bring up something depressing!"
    t "It's fine..."
    $ layeredimage_ref("yuri")
    y casual curi om b1b "That didn't sound very reassuring."
    show yuri cm
    t "I'll be alright, I promise."
    y om "Okay."
    hide yuri
    "I finish the tea."
    show monika forward casual happ at t11
    t "Monika-chan, do you happen to know where the bathroom is?"
    kmind "You've been here before, right?"
    "Have I?"
    kmind "You were only a year old so I don't blame you."
    "I keep on forgetting you have photographic memory, so..."
    m rhip lpoint om "Yeah, here!"
    show waypoint
    "Wait, how'd she create a waypoint?\nThere is no attribute that can do that around here."
    kmind "You tell me, she's not from any of the other sectors."
    "Um{cps=3}mmm...{/cps}{w=1}\nYou know what?  Nevermind."
    window hide
    $ audio.deadamb = "mod_assets/sounds/deadamb.ogg"
    play sound deadmantrans
    $ renpy.music.play(audio.deadamb, channel="ambience", fadein=0.5)
    show veins with blink
    scene bg parkBathroom
    show veins
    with ZoomTransition
    $ pause(0.1)
    play sound deadmantransout
    hide veins with blink
    t "Ow!  What the hell?"
    "Using deadfast speed usually doesn't make me dizzy."
    "Especially to the point where I can barely see."
    "The bluriness fades and I regain my composure."
    "I do my business, and I start heading back."
    "I'm not using deadfast speed again after what just happened."
    show akira 2cb zorder 2 at t11
    $ akira = "Kamiyama Akira"
    ak "Well, hello there!"
    show akira 2ca
    call showintro(intro_ak) from _call_showintro_8
    t "Well, if it isn't Kamiyama Akira!"
    t "How ya doing my man?!"
    ak 4cj "I am doing very well!  Thank you for asking!"
    ak 1cb "Whatcha doing here?"
    show akira 1ca
    t "Sayori offered me to join her literature club and they're having a weekend club meeting to greet me."
    ak 1cj "Oh, nice!"
    t "Would you like to join?"
    "Yes, I know he's from a different school, but my sister is at a club in his school as well, so this ordeal isn't unheard of."
    ak 3cl "Eh.  I never struck myself as the writer."
    t "Despite the fact that people say that you have, and I quote, 'such a way with words'?" #FNF: Doki Doki Takeover reference
    ak 3cf "I've heard that more times than I can count."
    ak 4cl "It's not true, you know, there are people who are much better at that than me."
    ak 4ch "Including you, Taiyen."
    t "Uh... Thanks."
    ak 2cb "Well, I shouldn't take up too much of your time."
    ak 1cb "Go have fun at your club!"
    show akira 1ca
    t "I will!"
    hide akira
    "With that, we exchange goodbyes and I head back to the club."
    scene bg park_01 with wipeleft_scene
    "I finally arrive back."
    show natsuki turned casual rhip lhip angr e1a b1a zorder 2 at t11
    n om "Took you long enough!"
    n "Come on, don't you have deadfast speed?"
    show natsuki cm
    t "About that..."
    t "Does anyone know why I felt dizzy after using it to get to the bathroom?"
    show natsuki ldown rdown curi zorder 3 at t21
    show kotonoha turned casual surp zorder 2 at t22
    k "Tha- doesn't happen..."
    t "Haven't you been watching me this entire time?"
    k  "{cps=1}..."
    k anno ce om "*Sigh* Of course my telegraphic powers get worse by the time you leave!"
    show monika forward casual rhip lpoint neut om zorder 5 at t11
    m "The enviroment is fine so this has to be someone else's doing."
    show monika rdown ldown
    t "Well, I ran into Akira-kun earlier, and his attribute weakens others' so..."
    k curi oe om "Why would he use it here?"
    show kotonoha cm
    t "Let me ask him."
    "I have his number, so I pull out my phone and text him."
    ttext "Hey dude, why are you weakening our attributes?" #subtle foreshadowing
    aktext "I didn't even realize I was doing so.  Apologies."
    ttext "It's fine."
    "I feel things go back to normal immediately after that text."
    k casual om "That was strange."
    show kotonoha cm
    m 2d "Let's just move on."
    $ layeredimage_ref("natsuki")
    show kotonoha happ
    show natsuki casual happ
    hide monika 
    show sayori turned rup happ zorder 5 at t11 
    s "That reminds me!"
    s ldown "Taiyen, may I borrow your phone for a second."
    show sayori cm
    t "Sure."
    "I hand Sayori my phone."
    "I wonder what this is for."
    k e1c om "Oh right, the group chat."
    show kotonoha cm n3
    n rhip laug om "Kotonoha's sentence there basically sums up how much we use it."
    show natsuki rdown happ cm
    s om "There we go!"
    show sayori cm
    "Sayori hands back my phone."
    s om "You are now a part of the club's group chat."
    show sayori cm
    t "Alright, I'll be sure to keep it in mind in case I need something and we aren't in person."
    show sayori turned happ zorder 4 at t21
    show natsuki zorder 3 at t22
    show yuri turned casual happ zorder 2 at t44
    show kotonoha e1a cm n1 zorder 1 at t41
    show monika forward casual happ zorder 5 at t11
    "Everyone, including me, takes back there spots at the table."
    t "So I've been wondering..."
    t "What are each of your favorite books that have been written by the club?"
    t "Let's go in the same order as I called you guys when you were giving your opinions on my book."
    t "Koto-chan will go last since she wasn't part of that selection."
    if s_first:
        voice "voicelines/taiyen/sf.ogg"
        t "So, Sayori will go first."
        hide sayori
        hide natsuki
        hide yuri
        hide kotonoha
        hide monika
        with wipeleft
        show sayori turned happ zorder 2 at t11
        with wipeleft
        call s_favorite from _call_s_favorite
    elif n_first:
        voice "voicelines/taiyen/nf.ogg"
        t "So, Natsuki will go first."
        hide sayori
        hide natsuki
        hide yuri
        hide kotonoha
        hide monika
        with wipeleft
        show natsuki turned casual happ zorder 2 at t11
        with wipeleft
        call n_favorite from _call_n_favorite
    elif y_first:
        voice "voicelines/taiyen/yf.ogg"
        t "So, Yuri-chan will go first."
        hide sayori
        hide natsuki
        hide yuri
        hide kotonoha
        hide monika
        with wipeleft
        show yuri turned casual happ zorder 2 at t11
        with wipeleft
        call y_favorite from _call_y_favorite
    else:
        voice "voicelines/taiyen/mf.ogg"
        t "So, Monika-chan will go first."
        hide sayori
        hide natsuki
        hide yuri
        hide kotonoha
        hide monika
        with wipeleft
        show monika forward casual happ zorder 2 at t11
        with wipeleft
        call m_favorite from _call_m_favorite
    show sayori turned happ zorder 4 at t21
    show natsuki turned casual happ zorder 3 at t22
    show yuri turned casual happ zorder 2 at t44
    show kotonoha turned casual happ zorder 1 at t41
    show monika forward casual happ zorder 5 at t11
    with wipeleft
    if s_second:
        voice "voicelines/taiyen/sn.ogg"
        t "Sayori will go next."
        hide sayori
        hide natsuki
        hide yuri
        hide kotonoha
        hide monika
        with wipeleft
        show sayori turned happ zorder 2 at t11
        with wipeleft
        call s_favorite from _call_s_favorite_1
    elif n_second:
        voice "voicelines/taiyen/nn.ogg"
        t "Natsuki will go next."
        hide sayori
        hide natsuki
        hide yuri
        hide kotonoha
        hide monika
        with wipeleft
        show natsuki turned casual happ zorder 2 at t11
        with wipeleft
        call n_favorite from _call_n_favorite_1
    elif y_second:
        voice "voicelines/taiyen/yn.ogg"
        t "Yuri-chan will go next."
        hide sayori
        hide natsuki
        hide yuri
        hide kotonoha
        hide monika
        with wipeleft
        show yuri turned casual happ zorder 2 at t11
        with wipeleft
        call y_favorite from _call_y_favorite_1
    else:
        voice "voicelines/taiyen/mn.ogg"
        t "Monika-chan will go next."
        hide sayori
        hide natsuki
        hide yuri
        hide kotonoha
        hide monika
        with wipeleft
        show monika forward casual happ zorder 2 at t11
        with wipeleft
        call m_favorite from _call_m_favorite_1
    show sayori turned happ zorder 4 at t21
    show natsuki turned casual happ zorder 3 at t22
    show yuri turned casual happ zorder 2 at t44
    show kotonoha turned casual happ zorder 1 at t41
    show monika forward casual happ zorder 5 at t11
    with wipeleft
    if s_third:
        voice "voicelines/taiyen/sn.ogg"
        t "Sayori will go next."
        hide sayori
        hide natsuki
        hide yuri
        hide kotonoha
        hide monika
        with wipeleft
        show sayori turned happ zorder 2 at t11
        with wipeleft
        call s_favorite from _call_s_favorite_2
    elif n_third:
        voice "voicelines/taiyen/nn.ogg"
        t "Natsuki will go next."
        hide sayori
        hide natsuki
        hide yuri
        hide kotonoha
        hide monika
        with wipeleft
        show natsuki turned casual happ zorder 2 at t11
        with wipeleft
        call n_favorite from _call_n_favorite_2
    elif y_third:
        voice "voicelines/taiyen/yn.ogg"
        t "Yuri-chan will go next."
        hide sayori
        hide natsuki
        hide yuri
        hide kotonoha
        hide monika
        with wipeleft
        show yuri turned casual happ zorder 2 at t11
        with wipeleft
        call y_favorite from _call_y_favorite_2
    else:
        voice "voicelines/taiyen/mn.ogg"
        t "Monika-chan will go next."
        hide sayori
        hide natsuki
        hide yuri
        hide kotonoha
        hide monika
        with wipeleft
        show monika forward casual happ zorder 2 at t11
        with wipeleft
        call m_favorite from _call_m_favorite_2
    show sayori turned happ zorder 4 at t21
    show natsuki turned casual happ zorder 3 at t22
    show yuri turned casual happ zorder 2 at t44
    show kotonoha turned casual happ zorder 1 at t41
    show monika forward casual happ zorder 5 at t11
    with wipeleft
    if s_fourth:
        voice "voicelines/taiyen/sn.ogg"
        t "Sayori will go next."
        hide sayori
        hide natsuki
        hide yuri
        hide kotonoha
        hide monika
        with wipeleft
        show sayori turned happ zorder 2 at t11
        with wipeleft
        call s_favorite from _call_s_favorite_3
    elif n_fourth:
        voice "voicelines/taiyen/nn.ogg"
        t "Natsuki will go next."
        hide sayori
        hide natsuki
        hide yuri
        hide kotonoha
        hide monika
        with wipeleft
        show natsuki turned casual happ zorder 2 at t11
        with wipeleft
        call n_favorite from _call_n_favorite_3
    elif y_fourth:
        voice "voicelines/taiyen/yn.ogg"
        t "Yuri-chan will go next."
        hide sayori
        hide natsuki
        hide yuri
        hide kotonoha
        hide monika
        with wipeleft
        show yuri turned casual happ zorder 2 at t11
        with wipeleft
        call y_favorite from _call_y_favorite_3
    else:
        voice "voicelines/taiyen/mn.ogg"
        t "Monika-chan will go next."
        hide sayori
        hide natsuki
        hide yuri
        hide kotonoha
        hide monika
        with wipeleft 
        show monika forward casual happ zorder 2 at t11
        with wipeleft
        call m_favorite from _call_m_favorite_3
    show sayori turned happ zorder 4 at t21
    show natsuki turned casual happ zorder 3 at t22
    show yuri turned casual happ zorder 2 at t44
    show kotonoha turned casual happ zorder 1 at t41
    show monika forward casual happ zorder 5 at t11
    #voice "voicelines/taiyen/kl.ogg"
    t "And, Koto-chan will go last."
    hide sayori
    hide natsuki
    hide yuri
    hide kotonoha
    hide monika
    with wipeleft
    show kotonoha turned casual happ zorder 2 at t11
    with wipeleft
    call k_favorite from _call_k_favorite
    hide kotonoha
    with wipeleft
    show sayori turned happ zorder 4 at t21
    show natsuki turned casual happ zorder 3 at t22
    show yuri turned casual happ zorder 2 at t44
    show kotonoha turned casual happ zorder 1 at t41
    show monika forward casual happ zorder 5 at t11
    with wipeleft
    "Everyone has shared their opinions now."
    "And it is only now that I realize how late it's gotten."
    m rhip lpoint om "How about we call it a day?"
    show monika cm
    n lhip rhip om "Yeah, I'm beat."
    show natsuki cm
    t "How?  We barely did anything that could be considered exhausting."
    n curi om "Honestly, I have no idea."
    show natsuki cm
    s rup om "Well, we're gonna get going here so..."
    show sayori cm
    t "Thank you very much everyone for allowing me to join the club, I'll be sure to come by next time."
    m om "You're very welcome, Senpai!"
    m "And, just so you know, the clubroom is in classroom 5-A."
    show monika ldown cm
    t "Got it!"
    show sayori lup ce mc
    show monika lpoint happ om 
    show kotonoha lup ce mc 
    show natsuki happ ce om 
    show yuri ce om 
    everyone "See you later, everyone!"
    show sayori ldown oe cm zorder 3 at t21
    hide monika
    show kotonoha ldown oe cm zorder 2 at t22
    hide natsuki
    hide yuri
    "I start the walk home with Sayori and Koto-chan."
    scene bg residential_day with wipeleft_scene
    call showlocation("Residential Street","September 28, 2023",1199.95,"bg residential_day") from _call_showlocation_46
    show sayori turned rup happ zorder 3 at t21
    show kotonoha turned casual happ zorder 2 at t22
    s om "So, anyone in the club you like?"
    show sayori cm
    t "Sayori, that'd be kinda fast."
    k om "Love at first sight is a thing."
    show kotonoha cm
    t "Agreed."
    s rdown laug om "Yeah, that would be kinda fast, would it?"
    show sayori cm
    t "But currently, I already like them {i}all{/i} as friends."
    s rup happ om "Good!  That's what I wanted for the first day!"
    "After a little more chat, we head into our houses and call it a day."
    stop music fadeout 1
    scene black with dissolve_scene_full
    play music ghostmenu
    $ akira = "???"
    ha "Seems like your boyfriend has joined that club you despise."
    its "Well, how infuriating."
    ina "Seems like {i}we'll{/i} need to up our game a bit if we want to take over the school."
    ak "We sure will.  I hope your plan works, boss."
    kiri "Oh, don't worry.{w=1}  It will."
    return

label s_favorite:
    s rup om "Well, to be honest..."
    s laug om "I don't have a favorite."
    show sayori cm
    t "Really?"
    s tap om "There's just- too many to choose from."
    s turned rup lup happ om "Everyone here has written great books, I don't know what to pick."
    show sayori cm
    t "Does that mean you recommend all of them?"
    s ldown "Hm,{w=0.5} sure."
    t "Alright, then.  I'll be sure to keep an eye out for them."
    hide sayori with wipeleft
    return

label n_favorite:
    n rhip lhip fs neut ce "..."
    "...?"
    n om "Do I have to say my embarrassing answer?"
    show natsuki cm
    "Usually I'd answer 'no' to this, but..."
    "That kinda ruins the point of the question, doesn't it?"
    n cross ff angr om e1c "Actually- just don't even think about it me!"
    n "Just say it."
    n cm e1a b1c "..."
    n om "My favorite book from the club is..."
    n "The Book of Markov."
    n "Written by Yandere Yuri."
    show natsuki cm zorder 3 at t21
    show yuri turned casual nerv e1b om zorder 2 at t22
    y "Wh-what?"
    y shy neut n5 "Uuuu!"
    kmind "Uh..."
    "I'm confused, what's happening here."
    kmind "I knew there were rumors about these two liking each other, but I didn't think that they were even somewhat true."
    "I've heard that ship before."
    n turned rhip lhip ce om "It ain't what you guys think!"
    n happ oe om "It's just that Yuri wrote the most engaging story yet!"
    n "It's hard to beat."
    show natsuki cm
    y happ "Well, the book's in the clubroom if you want to read it."
    kmind "Along with all the rest of the books we've written here."
    t "I'll keep that in mind then."
    hide natsuki
    hide yuri
    with wipeleft
    return

label y_favorite:
    y rup lup e1b om "I'm gonna be honest even though it's a little embarrassing."
    y "Slice of Life isn't something I'm usually into..."
    y e1a "But my favorite book from the club is Jumping Idol Bakers by Tetsuo Natsuki." #mixing Parfait Girls with my favorite game here
    show yuri cm
    "That name sort of reminds me of a certain rhythm game I've become obsessed with lately."
    y ce om "The story is really charming and beautiful, and it made me cry more times than I can count."
    y ldown oe "It truly is worthwhile to reread it too, since you can experience everything again as if it were first time."
    y e1b "That is{cps=3}...{/cps} if you're like me and forget the story until the reread."
    show yuri cm zorder 3 at t21
    show natsuki 2bt zorder 2 at t22
    n "Aw, Yuri.  You're gonna make me blush."
    "I don't know why, but seeing this makes me giggle a bit."
    t "Well, that may very well be a nice read."
    t "I'll be sure to look out for it."
    hide natsuki
    hide yuri
    with wipeleft
    return

label m_favorite:
    m lpoint om "I don't really have a favorite, to be honest."
    m ldown rhip om "I mainly look for good writing when it comes to these kinds of things."
    m "But everybody has such good writing skills that I can't choose who has the best."
    m rdown "So, I'll just say that I like all of them and end off my opinion here."
    t "Well, I'll be looking out for those then."
    hide monika with wipeleft
    return

label k_favorite:
    k lup om "As you know, I don't actually think about this sort of stuff."
    k "So I don't really have a favorite."
    k "And I can't really choose between the most memorable ones either."
    show kotonoha cm
    t "Just as I expected, so should I just move on?"
    k ldown om "I'm getting a little tired so go ahead."
    show kotonoha cm
    t "Very well."
    hide kotonoha with wipeleft
    return