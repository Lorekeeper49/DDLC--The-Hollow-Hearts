label ch0_main:
    $ style.say_window = style.window
    $ nb = "namebox"
    stop music fadeout 2.0
    play music confdep
    scene bg tlivingroom
    with dissolve_scene_full
    $ restore_all_characters()
    $ pla = "???"
    $ aoruguri = "ルナ煽るぐり\n{size=15}Luna Aoruguri"
    general "IT'S YOUR FAULT."
    "Shut up."
    general "IT'S YOUR FAULT AND YOU KNOW IT."
    "My parents are dead and all you can is try and humiliate me?"
    general "..."
    "That's what I thought!"
    play sound door
    scene bg house with wipeleft_scene
    call showlocation("Sakura Home\n{size=25}桜のホーム{/size}","September 28, 2023\n{size=15}2023年9月28日{/size}",7*60+59+57/60.0,"bg house")
    t "*Sigh*"
    show yuri turned casual curi rup zorder 2 at t11
    y om "Taiyen?"
    t "Hey Yuri-chan..."
    call showintro(intro_y)
    y "You doing alright?"
    t "Take a guess..."
    y worr ce rdown "My guess is no..."
    t "You're correct..."
    y e1a "Wanna talk about it?"
    t "Well, they're shouting at me again..."
    "My parents were murdered a month ago and ever since then, I've been shouted at by voices telling me it's all my fault."
    y rup "Think you're ever going to get used to it?"
    t "You tell me..."
    show yuri cm
    "She says nothing."
    t "You wanna know what's not helping?"
    t "The fact that the murderer looked a lot like ONE."
    y dist lup om "You've said this before..."
    y sad "If what you say is true, then I don't know how to help you..."
    t "It's fine..."
    t "You being here is enough, my friend."
    y ma "..."
    "Yuri-chan is training to be a therapist, so I'm glad she's here to try and help me through this."
    $ layeredimage_ref("yuri")
    show yuri turned casual worr rup
    y om "Here, maybe I can help take your mind off things."
    y rdown "Follow me."
    scene bg street1 with wipeleft_scene
    show yuri turned casual happ rup zorder 2 at t11
    t "Yuri-chan, where are you taking me?"
    y om "Just keep going."
    show yuri cm
    t "You realize I can run super fast, right?  Just send me the location and I'd be there in seconds."
    y om rdown "I don't wanna ruin the surprise, though."
    show yuri cm
    t "Need I remind you that I am not your boyfriend?"
    y rup om "You don't need to be."
    stop music fadeout 1.0
    scene bg park_01 with wipeleft_scene
    y "We're here."
    t "And where is-{nw}"
    $ style.say_window = style.window_fake
    $ nb = "namebox_fake"
    play music t2
    show sayori turned casual happ rup lup ce om zorder 2 at t11
    s "Ah!  Yuri-chan!  Brought a friend?"
    t "Sayori?"
    s oe "Ah!  Taiyen!"
    call showintro(intro_s)
    t "What are you doing here?  This isn't a livestream, is it?"
    s ldown "Sort of is, sort of isn't."
    s "See the camera?"
    show yuri turned casual pani rup lup om zorder 2 at l21
    show sayori at t22
    y "Wait, Sayori!  We're doing that now?"
    s lup "Of course!  Gotta tell my fans about all my friends!"
    y shy casual "But, I haven't had time to ready myself yet!"
    t "How can you be a therapist when you're this shy about showing yourself to people?"
    y "That's not..."
    s rdown ldown "Come on, Yuri-chan!"
    show sayori cry cm rup at t11
    s "Don't you wanna take care of people like me?"
    "How does she change emotion so fast like that?"
    kmind "Because yes."
    "?"
    show sayori at lhide
    show yuri at lhide
    hide yuri
    hide sayori
    show kotonoha turned casual happ lchest zorder 2 at r11
    k om "Hiya Tai-kun!"
    t "Koto-chan?  You're here too?"
    call showintro(intro_k)
    show kotonoha cm
    t "Did the Midnight Club get some new recruits?  What's happening here?"
    k ldown rhip om "Well first of all, no.  Just thought I'd join a club from my actual school."
    t "And that club is...?"
    show kotonoha at t11
    hide kotonoha
    show monika forward casual happ lpoint rhip zorder 2 at t11 
    m om "The Literature Club!"
    m ldown "Hello there, Student Council President!"
    t "Murikou-san?"
    m lpoint sedu "Ah ah!  If you're gonna be participating in club activites, you gotta call everyone by their first name."
    m "Especially the president."
    call showintro(intro_m)
    show monika cm
    t "Right, sorry."
    t "Monika-chan, right?"
    m nerv om ldown "Not sure about that honorific, but sure!"
    t "Alright."
    show monika happ cm
    t "So, I haven't had time to approve clubs yet so I don't know which members are in which club."
    m lpoint om "Well, everyone you see here is a member of the literature club."
    m "We have our president, Murikou Monika, me,"
    hide monika
    show sayori turned casual happ rup zorder 2 at t11
    m "our vice president, Shinamonpan Sayori,"
    hide sayori
    show yuri turned casual happ rup zorder 2 at t11
    m "our club secretary, Yandere Yuri,"
    hide yuri
    show kotonoha turned casual happ rhip zorder 2 at t11
    m "our newest member, Sakura Kotonoha,"
    hide kotonoha
    m "and our tsundere type member, Luna Natsuki...\nwho is late today because she's having trouble gathering the essentials."
    show monika forward casual happ lpoint rhip zorder 2 at t11 
    t "Alright, well I guess I should introduce myself."
    t "You probably already know this, but I am Sakura Taiyen, the Student Council President and the son of the school's founder."
    m ldown om "Well hello there Taiyen, your sister has told us all about you."
    t "I'm sure she did, we are really close twins after all."
    show sayori turned casual laug rup zorder 2 at l21 
    show monika at t22
    s om "'Really close' is an understatement."
    show sayori at t22
    hide sayori
    hide monika
    show natsuki turned casual nerv om zorder 2 at t11
    n "Hey guys!  I'm here!  Sorry that took so long!"
    m "Ah, there she is!"
    show yuri turned casual worr ce om rup lup zorder 2 at l21
    show natsuki at t22
    y "Natsuki, you really gotta work on getting these priorities straight."
    n angr rhip "Hey, we had a ton of plans for today and I had a lot of things to grab so it was hard to keep track of them!"
    call showintro(intro_n)
    show yuri at lhide
    hide yuri
    show natsuki at t11
    n happ "Now if you'll excuse me, let's get this party started!"
    stop music fadeout 1.0
    $ style.say_window = style.window
    $ nb = "namebox"
    scene bg park_01 with dissolve_scene_full
    play music confdep
    "Everyone's having so much fun together..."
    "I wish I could have fun like that..."
    "I just..."
    "I can't!"
    "I'm such a coward!"
    a "..."
    stop music fadeout 1.0
    $ style.say_window = style.window_fake
    $ nb = "namebox_fake"
    scene bg park_01 with dissolve_scene_full
    play music t8
    show natsuki turned casual happ rhip lhip zorder 2 at t11
    n om "Alright newbie!  Let's see what you're here for!"
    t "I wouldn't call myself a newbie.  Yuri-chan practically dragged me here so I don't really know if I want to join yet."
    n ldown "Oh, come on!"
    n sedu "Don't you wanna join a club full of incredibly cute girls?"
    t "Wha- Hey!  I am the Student Council President, you know I'm better than that!"
    n cm "Sure."
    show natsuki at t22
    show kotonoha turned casual laug lup om zorder 2 at l21
    k "Hey, Natsuki?  Maybe don't tease my twin brother."
    show kotonoha cm at t21
    n lsur "Oh."
    n flus "Yeah, sorry about that.  Didn't realize who I was talking to."
    t "It's fine.  I can take it.  My parents used to tease me every two seconds."
    hide kotonoha
    hide natsuki
    "Sayori has started livestreaming now and everyone seems to be handling it nicely."
    show yuri shy casual ce zorder 2 at t11
    "I worry about Yuri-chan though.  She's not used to being shown to hundreds of people."
    show yuri happ oe
    "But it seems like she's holding strong."
    hide yuri
    show monika forward casual happ rpoint rhip zorder 2 at t11
    m om "Hey, Sayori!  Move that camera over here, I wanna tell you're fans what we're about to do."
    hide monika
    show sayori turned casual happ rup zorder 2 at t11
    s om "Okay!"
    hide sayori
    "Glad everyone's having fun!"
    "I might actually join this!"
    t "Hm?"
    $ style.say_window = style.window
    $ nb = "namebox"
    scene bg park_01 with wipeleft_scene
    a "..."
    "That was close."
    "Why does that boy sound so familiar?"
    a "Hm."
    "I should move somewhere else."
    $ style.say_window = style.window_fake
    $ nb = "namebox_fake"
    scene bg park_01 with wipeleft_scene
    t "What was..."
    show kotonoha turned casual curi om lup zorder 2 at t11
    k "Something wrong Tai-kun?"
    t "Oh, no.  Just thought someone else was watching us."
    k rhip ldown cm e1c "..."
    hide kotonoha
    show monika forward casual happ lpoint rhip zorder 2 at t11
    m om "Okay, everyone!  Let's start the first activity!"
    m ldown "Since we have a couple new members here, let's play 20 Questions and learn about them!"
    "Hardly literature related, but I'll allow it."
    hide monika
    show kotonoha turned casual happ zorder 2 at t11
    "Koto-chan takes the stage."
    hide kotonoha
    show yuri turned casual happ rup zorder 2 at t11
    y om "Taiyen, you count too."
    show yuri cm
    t "Huh?  But I haven't made any-"
    y om rdown "You made the decision to be here."
    show yuri cm
    "She has a point."
    t "Fine."
    hide yuri 
    show kotonoha turned casual happ zorder 2 at t11
    "I join my sister on the stage."
    "...That doesn't exist."
    kmind rhip anno "Just pretend it's there."
    hide kotonoha
    show monika forward casual happ lpoint rhip zorder 2 at t11
    m om "The rules are simple;"
    m ldown "You both will get 10 questions each, you get to choose who asks each question, but you will not be able to choose the same person twice consecutively."
    m lpoint "However, I will be asking the first question this time just to give everyone time to think of their questions."
    m "I will be asking you both this question, so that will leave 9 for each of you."
    show monika zorder 2 at t41
    show sayori turned casual happ rup zorder 2 at t42
    show natsuki turned casual happ rhip zorder 2 at t43
    show yuri turned casual happ rup zorder 2 at t44
    m "So!  First, a literature question:"
    m ldown "In your opinion (assuming you have written something), what's the best thing you've written?"
    $ last_chosen = "monika"
    $ koto_chosen = "monika"
    $ choice_list = ["monika", "sayori", "natsuki", "yuri", "chat"]
    show monika cm
    t "A choice-based adventure by the name of 'Hollow'."
    t "It was very fun to write and something I have actually never done before writing it."
    t "I won't give anything away in-case you haven't seen it yet."
    t "But it honestly turned out really well."
    hide yuri
    hide sayori
    hide monika
    hide natsuki
    show kotonoha turned casual happ lup zorder 2 at t11
    k om "As for me, Salvation."
    k ldown "Specifically, the huge remake and rewrite that came out recently."
    k rhip "It was a lot of fun remaking that story and seeing how I can improve upon the last time I did it."
    k lup "The story is completely different from the original by the way, just saying."
    hide kotonoha
    show monika forward casual happ rhip zorder 2 at t41
    show sayori turned casual happ rup zorder 2 at t42
    show natsuki turned casual happ rhip zorder 2 at t43
    show yuri turned casual happ rup zorder 2 at t44
    m om lpoint "Alright, now you can choose."
    m ldown "And to make things more interesting, let's allow Sayori's chat to ask questions as well."
    m lpoint "And since you can't choose the same person twice, I'm not in the first selection."
    menu:
        m ldown "So, who will you choose?"
        
        "Monika" if last_chosen != "monika" and koto_chosen != "monika":
            $ last_chosen = "monika"
            "Ignore this, this option never happens, it's just to make copying the menu easier."
        "Sayori" if last_chosen != "sayori" and koto_chosen != "sayori":
            $ last_chosen = "sayori"
            s om "Don't know how I haven't asked you this yet, but what is your general process for writing?"
            show sayori cm
            t "I don't really have one to be honest."
            t "I just think of a topic and setting, then write my ideas based on that."
            t "It usually takes me no time to think of the plot."
            t "It usually takes me multiple months to complete the story."
            t "My writing style is very annoying."
        "Natsuki" if last_chosen != "natsuki" and koto_chosen != "natsuki":
            $ last_chosen = "natsuki"
            n om "What's the hardest thing you've ever had to write?"
            show natsuki cm
            t "Bias in any form."
            t "Especially racial, sexual, and social bias."
            t "Koto-chan and I had a writing assignment back in Junior-High School where we had to literally protray sexual bias so we could better understand it."
            t "It was the single most infuriating thing either of us have ever written."
        "Yuri" if last_chosen != "yuri" and koto_chosen != "yuri":
            $ last_chosen = "yuri"
            y om "Why did you start writing in the first place?"
            show yuri cm
            t "Well it's not about why I started, it's more about why I continued."
            t "I had always been inspired by the amazing stories the creative minds can muster, and I wanted to try developing an original story myself."
            t "However, I didn't start with something original."
            t "In fact, I started with an embarassingly bad fan-rewrite of an indie horror game."
            t "Half of it wasn't even close to correct with lore of that game, it was so bad."
            show monika ce
            show natsuki ce
            show yuri ce
            show sayori ce
            "Everyone chuckles."
            show monika oe
            show natsuki oe
            show yuri oe
            show sayori oe
            t "I'm not sure why I kept writing after that."
            t "Frankly, I should've realized that I had no talent."
            t "But with time, I slowly gained talent."
            "Take that Aragaki!"
        "Sayori's chat" if last_chosen != "chat" and koto_chosen != "chat":
            $ last_chosen = "chat"

    hide yuri
    hide sayori
    hide monika
    hide natsuki
    show kotonoha turned casual happ lup zorder 2 at t11
    k om "To make sure there is a little bit more variety in who I chose, I'm prohibiting myself from picking the same person Tai-kun just chose."
    k rhip "So..."
    $ koto_chosen = renpy.random.choice([person_chosen for person_chosen in choice_list if person_chosen not in [koto_chosen, last_chosen, "chat"]])
    if koto_chosen == "monika":
        k rdown "I'll choose Monika."
        show monika forward happ casual rhip zorder 2 at r22
        show kotonoha cm at t21
        "Ignore this, this option never happens, it's just to make copying the menu easier."
    if koto_chosen == "sayori":
        k rdown "I'll choose Sayori."
        show sayori turned happ casual rup zorder 2 at r22
        show kotonoha cm at t21
        s om "Don't know how I haven't asked you this yet, but what is your general process for writing?"
        show sayori cm
        k ldown om "It is a very sequential way of writing."
        k rhip "I usually think of the characters first, then think of the plot."
        k rdown "Any ideas or new characters that come in during the plot are decided later."
    if koto_chosen == "natsuki":
        k rdown "I'll choose Natsuki."
        show natsuki turned happ casual rhip zorder 2 at r22
        show kotonoha cm at t21
        n om "What's the hardest thing you've ever had to write?"
        show natsuki cm
        k anno ldown rhip om "Bias in any form."
        k ce "Especially racial, sexual, and social bias."
        k oe lup "Tai-kun and I had a writing assignment back in Junior-High School where we had to literally protray sexual bias so we could better understand it."
        k ldown "It was the single most infuriating thing either of us have ever written."
    if koto_chosen == "yuri":
        k rdown "I'll choose Yuri."
        show yuri turned happ casual rup zorder 2 at r22
        show kotonoha cm at t21
        y om "Why did you start writing in the first place?"
        show yuri cm
        k om "Mainly because my brother did."
        k ldown rhip "He made a very interesting story and I wanted to see if I could top it."
        k rdown "We're kinda rivals in that sense."
    if koto_chosen == "chat":
        k rdown "I'll choose Sayori's chat."
        show sayori turned happ casual rup zorder 2 at r22
        show kotonoha cm at t21

    hide kotonoha
    show monika forward casual happ rhip zorder 2 at t41
    show sayori turned casual happ rup zorder 2 at t42
    show natsuki turned casual happ rhip zorder 2 at t43
    show yuri turned casual happ rup zorder 2 at t44
    t "You know, I'll do the same thing Koto-chan is doing; prohibit myself from picking the person she just chose."
    t "Just to add more variety to the table."
    t "So, in that case..."
    menu:
        "Next Question."
        
        "Monika" if last_chosen != "monika" and koto_chosen != "monika":
            $ last_chosen = "monika"
            m om "So, what exactly does your name mean?"
            show monika cm
            t "Well, nevermind the weird English translation."
            t "I mean, technically, it's supposed to be 'Taien', not 'Taiyen'.  But that's besides the point."
            t "Everyone knows {rb}桜{/rb}{rt}Sakura{/rt} means cherry blossom."
            t "{rb}隊{/rb}{rt}Tai{/rt} means squad."
            t "{rb}円{/rb}{rt}En{/rt} means circle, round, or yen."
            t "So basically squad money or round squad."
        "Sayori" if last_chosen != "sayori" and koto_chosen != "sayori":
            $ last_chosen = "sayori"
            s om "What's the first thing you've ever written?"
            show sayori cm
            t "There's that really bad horror rewrite I never finished."
            t "As for one I did finish..."
            t "I rushed a story that was set within an abandoned waterpark."
            t "Honestly, it was a timed project, but I had plenty of time to properly write it."
            t "I should've picked more times to write, that would've made it more fleshed out."
        "Natsuki" if last_chosen != "natsuki" and koto_chosen != "natsuki":
            $ last_chosen = "natsuki"
            n om "Have you read manga before, and if so, what's your opinion on it?"
            show natsuki cm
            t "Specifically not asking if it's literature, huh?"
            n cross anno om "I've already given up on that fight with Yuri."
            show natsuki cm
            "Oh, so you've already gone through the seemingly unwinnable war."
            show natsuki happ
            t "Well anyway..."
            show natsuki turned casual happ rhip
            t "Believe it or not, I've actually have never read manga."
            t "But I do believe it is a very nice and creative form of media."
            t "And by the way, I believe anything written is literature, including manga."
        "Yuri" if last_chosen != "yuri" and koto_chosen != "yuri":
            $ last_chosen = "yuri"
            y om "What are some clichés you try to avoid?"
            show yuri cm
            t "I don't try to avoid clichés."
            t "I honestly find them inevitable."
            t "So I just accept it if I end up writing a cliché."
        "Sayori's chat" if last_chosen != "chat" and koto_chosen != "chat":
            $ last_chosen = "chat"

    hide yuri
    hide sayori
    hide monika
    hide natsuki
    show kotonoha turned casual happ lup zorder 2 at t11
    $ koto_chosen = renpy.random.choice([person_chosen for person_chosen in choice_list if person_chosen not in [koto_chosen, last_chosen, "chat"]])
    if koto_chosen == "monika":
        k om "I'll choose Monika."
        show monika forward happ casual rhip zorder 2 at r22
        show kotonoha cm at t21
        m om "What does your name mean?"
        show monika cm
        k om rhip "Well first of all (even though you didn't get it wrong), it's 'Kotonoha', not 'Kotoba'."
        k ldown anno ce "People get that wrong all the time, and it's all thanks to the common pronounciation of my kanji."
        k rdown "Honestly, it probably should be written as '{rb}言の葉{/rb}{rt}Kotonoha{/rt}'..."
        k lup "Everyone knows {rb}桜{/rb}{rt}Sakura{/rt} means cherry blossom."
        k rhip "{rb}言{/rb}{rt}Koto{/rt} means word and is the kanji used when referring to the action of talking."
        k ldown "{rb}葉{/rb}{rt}Ha{/rt} means leaf."
        k rdown "Together, they make up the noun 'word'."
    if koto_chosen == "sayori":
        k om "I'll choose Sayori."
        show sayori turned happ casual rup zorder 2 at r22
        show kotonoha cm at t21
        s om "What's the first thing you've ever written?"
        show sayori cm
        k om "Salvation."
        k ldown rhip "I've already talked about the remake, but the original is actually the first thing that I've written."
        k rdown "Looking back, it is very nice story with a lot of fun quirks."
        k rhip "It really turned out well."
    if koto_chosen == "natsuki":
        k om "I'll choose Natsuki."
        show natsuki turned happ casual rhip zorder 2 at r22
        show kotonoha cm at t21
        n om "Have you read manga before, and if so, what's your opinion on it?"
        show natsuki cm
        k rhip om "Specifically not asking if it's literature, huh?"
        show kotonoha cm
        n cross anno om "I've already given up on that fight with Yuri."
        show natsuki cm
        k ldown b1e om "Oh, so you've already gone through the seemingly unwinnable war."
        show natsuki happ
        $ layeredimage_ref("kotonoha")
        k lup rdown om "Well anyway..."
        show natsuki turned casual happ rhip
        k ldown "I have read manga, and I believe it's a nice form of media."
        k lup "My favorite being one hero based one that's a lot of fun."
        k ldown rhip "And by the way, I believe anything written is literature, including manga."
    if koto_chosen == "yuri":
        k om "I'll choose Yuri."
        show yuri turned happ casual rup zorder 2 at r22
        show kotonoha cm at t21
        y om "What are some clichés you try to avoid?"
        show yuri cm
        k ldown rhip "Things like 'in the nick of time'."
        k lup "That's where a lot of ex-machinas come from."
        k anno ce "And I really don't like ex-machinas..."
        k oe "That's basically the main thing I try to avoid."
    if koto_chosen == "chat":
        k om "I'll choose Sayori's chat."
        show sayori turned happ casual rup zorder 2 at r22
        show kotonoha cm at t21

    hide kotonoha
    show monika forward casual happ rhip zorder 2 at t41
    show sayori turned casual happ rup zorder 2 at t42
    show natsuki turned casual happ rhip zorder 2 at t43
    show yuri turned casual happ rup zorder 2 at t44
    menu:
        "Next Question."
        
        "Monika" if last_chosen != "monika" and koto_chosen != "monika":
            $ last_chosen = "monika"
            m om "Where does most of your inspiration come from?"
            show monika cm
            t "A lot of it (albeit, too much) comes from my favorite medias out there."
            t "I actually used to practically steal ideas from them."
            t "That's not a good way to be original."
            t "So I try to limit myself from taking too much inspiration these days."
        "Sayori" if last_chosen != "sayori" and koto_chosen != "sayori":
            $ last_chosen = "sayori"
            s om "What is your fondest memory?"
            show sayori cm
            t "This is gonna sound weird out of context, especially because it involves you and you like me so..."
            show natsuki shoc at h43
            n om rdown "HUH?!"
            "Chat's going nuts."
            t "That's right, you heard it here first folks!"
            t "This is official confirmation from the love interest himself: Sayori likes me."
            show sayori nerv
            t "She confessed a year ago and I was left kinda unsurprised to say the least."
            t "The only problem is, I don't know how I feel about her."
            t "And I probably should work that out because she's been waiting for a response for longer than she should've been by now."
            s tap nerv om "Yeah, I'm starting to think that I should try to suck it up and move on."
            t "Well, we'll see what happens in the future."
            s turned happ rup om "Yeah."
            show sayori cm
            n "..."
            n "O-okay then."
            show natsuki happ rhip cm at t43
            t "Anyway..."
            t "Honestly, meeting you is my fondest memory."
            t "You really helped me learn how to connect with people and friends and I will always be grateful for that."
            s laug lup "Aww!"
        "Natsuki" if last_chosen != "natsuki" and koto_chosen != "natsuki":
            $ last_chosen = "natsuki"
            n om "Besides writing, what do you do in your free time?"
            show yuri cm
            t "Play games, watch shows, hang out with friends."
            t "Yeah, I'm generic."
        "Yuri" if last_chosen != "yuri" and koto_chosen != "yuri":
            $ last_chosen = "yuri"
            y om "What's your favorite novel?"
            show yuri cm
            t "Not sure if I can say the name on stream but my favorite novel is a very intricate one that takes place in multiple dimensions."
            t "One of the main characters gets a sharp object that allows him to cross dimensions and the other gets one that only tells the truth."
            t "It ends up turning into a really interesting story with a lot of good plot points."
            t "It's a lot of fun to go through."
            t "I can tell you all the title later."
        "Sayori's chat" if last_chosen != "chat" and koto_chosen != "chat":
            $ last_chosen = "chat"

    hide yuri
    hide sayori
    hide monika
    hide natsuki
    show kotonoha turned casual happ lup zorder 2 at t11
    $ koto_chosen = renpy.random.choice([person_chosen for person_chosen in choice_list if person_chosen not in [koto_chosen, last_chosen, "chat"]])
    if koto_chosen == "monika":
        k om "I'll choose Monika."
        show monika forward happ casual rhip zorder 2 at r22
        show kotonoha cm at t21
        m om "Where does most of your inspiration come from?"
        show monika cm
        k ldown rhip om "In true rival fashion, I tend to take a lot of inspiration from my brother."
        k laug rdown "However, that usually doesn't go too well.  My own ideas tend to be a lot better than the inspiration."
    if koto_chosen == "sayori":
        k om "I'll choose Sayori."
        show sayori turned happ casual rup zorder 2 at r22
        show kotonoha cm at t21
        s om "What is your fondest memory?"
        show sayori cm
        k om "The first time me and Tai-kun collaborated on a story."
        k ldown rhip "We have a habit of telling each other our plots for our next stories and for this one, we happened to have the same plot ideas by accident."
        k rdown "So we decided to collaborate on it."
        k rhip "It ended up being a really fun experience and it lead up to multiple other collaborations later on down the line."
    if koto_chosen == "natsuki":
        k om "I'll choose Natsuki."
        show natsuki turned happ casual rhip zorder 2 at r22
        show kotonoha cm at t21
        n om "Besides writing, what do you do in your free time?"
        show natsuki cm
        k om "Play games, watch shows, hang out with friends."
        k laug rhip ldown "Yeah, I'm generic."
    if koto_chosen == "yuri":
        k om "I'll choose Yuri."
        show yuri turned happ casual rup zorder 2 at r22
        show kotonoha cm at t21
        y om "What's your favorite novel?"
        show yuri cm
        k laug ldown rhip om "I don't read novels as often as I should to be honest."
        k happ "But my favorite is probably that medieval one that Tai-kun over here hasn't read yet."
        show kotonoha cm
        t "I'll get to it, don't worry!"
    if koto_chosen == "chat":
        k om "I'll choose Sayori's chat."
        show sayori turned happ casual rup zorder 2 at r22
        show kotonoha cm at t21

    hide kotonoha
    show monika forward casual happ rhip zorder 2 at t41
    show sayori turned casual happ rup zorder 2 at t42
    show natsuki turned casual happ rhip zorder 2 at t43
    show yuri turned casual happ rup zorder 2 at t44
    menu:
        "Next Question."
        
        "Monika" if last_chosen != "monika" and koto_chosen != "monika":
            $ last_chosen = "monika"
            m om "What story do you think has the best writing?"
            show monika cm
            t "That is a very difficult question to answer..."
            t "There's so many of them!"
            t "Medieval wizards, everyone being a hero, multiple dimensions, feeling isekai, the list goes on."
            t "It'll probably be forever before I come up with a proper answer."
        "Sayori" if last_chosen != "sayori" and koto_chosen != "sayori":
            $ last_chosen = "sayori"
            s om "What's something that you think has been done to death?"
            show sayori cm
            t "The main hero falling in love with a female friend or the damsel he's rescuing."
            t "It happens way too often, and most of the time, it doesn't exactly influence either party's action."
            t "Enough said."
        "Natsuki" if last_chosen != "natsuki" and koto_chosen != "natsuki":
            $ last_chosen = "natsuki"
            n om "What's your favorite adaptation you have seen?"
            show natsuki cm
            t "An 8 movie series about a boy becoming a renowned wizard."
            t "Despite the original author's controversy."
            t "And no, contrary to what these TV studios believe, that series does not need a remake."
        "Yuri" if last_chosen != "yuri" and koto_chosen != "yuri":
            $ last_chosen = "yuri"
            y om "What's your favorite type of story?"
            show yuri cm
            t "Ones that are meant to tell you a meaningful message to live by."
            t "That's actually the type of writer I aspire to be."
            t "One that writes stories with messages that help people out."
        "Sayori's chat" if last_chosen != "chat" and koto_chosen != "chat":
            $ last_chosen = "chat"

    hide yuri
    hide sayori
    hide monika
    hide natsuki
    show kotonoha turned casual happ lup zorder 2 at t11
    $ koto_chosen = renpy.random.choice([person_chosen for person_chosen in choice_list if person_chosen not in [koto_chosen, last_chosen, "chat"]])
    if koto_chosen == "monika":
        k om "I'll choose Monika."
        show monika forward happ casual rhip zorder 2 at r22
        show kotonoha cm at t21
        m om "What story do you think has the best writing?"
        show monika cm
        k laug ldown rhip "Unfortunately, I don't look at enough stories to answer that question..."
    if koto_chosen == "sayori":
        k om "I'll choose Sayori."
        show sayori turned happ casual rup zorder 2 at r22
        show kotonoha cm at t21
        s om "What's something that you think has been done to death?"
        show sayori cm
        k anno ldown rhip ce om "Ex-machinas..."
        k oe "I'm tired of people getting saved by someone in the nick of time like that..."
        k rdown "Part of why I don't like them so much."
    if koto_chosen == "natsuki":
        k om "I'll choose Natsuki."
        show natsuki turned happ casual rhip zorder 2 at r22
        show kotonoha cm at t21
        n om "What's your favorite adaptation you have seen?"
        show natsuki cm
        k om "A medieval magic one with dragons that's..."
        k laug rhip "...way too hard to summarize."
        k ldown rdown "You'll have to watch the show in order to understand."
        k happ rhip "Just know, it's rated M for a reason."
    if koto_chosen == "yuri":
        k om "I'll choose Yuri."
        show yuri turned happ casual rup zorder 2 at r22
        show kotonoha cm at t21
        y om "What's your favorite type of story?"
        show yuri cm
        k om "Ones that are meant to tell you a meaningful message to live by."
        k ldown rhip "That's actually the type of writer Tai-kun over here aspires to be."
        k rdown "One that writes stories with messages that help people out."
    if koto_chosen == "chat":
        k om "I'll choose Sayori's chat."
        show sayori turned happ casual rup zorder 2 at r22
        show kotonoha cm at t21

    hide kotonoha
    show monika forward casual happ rhip zorder 2 at t41
    show sayori turned casual happ rup zorder 2 at t42
    show natsuki turned casual happ rhip zorder 2 at t43
    show yuri turned casual happ rup zorder 2 at t44
    menu:
        "Next Question."
        
        "Monika" if last_chosen != "monika" and koto_chosen != "monika":
            $ last_chosen = "monika"
            m om "What's your favorite genre?"
            show monika cm
            t "Action."
            t "Enough said."
        "Sayori" if last_chosen != "sayori" and koto_chosen != "sayori":
            $ last_chosen = "sayori"
            s om "How do you come up with the names of your characters?"
            show sayori cm
            t "I don't."
            t "Seriously, I don't that much thought at all towards the name for my characters."
            t "Except Japanese names."
            t "Usually for those, I think of the spelling/pronounciation first, then I think about the kanji and what it means."
            t "That's about it."
        "Natsuki" if last_chosen != "natsuki" and koto_chosen != "natsuki":
            $ last_chosen = "natsuki"
            n om "What tips do you have to help people improve on their writing?"
            show natsuki cm
            t "There's a lot, but here's the main one I can give:"
            t "If you have a location where a lot of things are or happen, draw a map of the place so you know where everything is and you don't add anything unnecessary."
            t "I can't tell you how many times I have gotten lost in my locations because I didn't have a damn map of the place!"
            t "It helps tremendously to have a map, trust me."
        "Yuri" if last_chosen != "yuri" and koto_chosen != "yuri":
            $ last_chosen = "yuri"
            y om "What's your opinion on horror?"
            show yuri cm
            t "Standalone horror tends to not work."
            t "It doesn't seem to scare me all that well."
            t "Personally I prefer psychological horror."
        "Sayori's chat" if last_chosen != "chat" and koto_chosen != "chat":
            $ last_chosen = "chat"
            
    hide yuri
    hide sayori
    hide monika
    hide natsuki
    show kotonoha turned casual happ lup zorder 2 at t11
    $ koto_chosen = renpy.random.choice([person_chosen for person_chosen in choice_list if person_chosen not in [koto_chosen, last_chosen, "chat"]])
    if koto_chosen == "monika":
        k om "I'll choose Monika."
        show monika forward happ casual rhip zorder 2 at r22
        show kotonoha cm at t21
        m om "What's your favorite genre?"
        show monika cm
        k om "Psychological horror."
        k ldown rhip "Really nice way to grasp people's hearts."
        k rdown "Don't think I need to say anything else about it."
    if koto_chosen == "sayori":
        k om "I'll choose Sayori."
        show sayori turned happ casual rup zorder 2 at r22
        show kotonoha cm at t21
        s om "How do you come up with the names of your characters?"
        show sayori cm
        k laug rhip om "I just give them all generic names, I don't really give it much thought."
        k ldown "I'm not that good of a name chooser."
    if koto_chosen == "natsuki":
        k om "I'll choose Natsuki."
        show natsuki turned happ casual rhip zorder 2 at r22
        show kotonoha cm at t21
        n om "What tips do you have to help people improve on their writing?"
        show natsuki cm
        k om "There's a lot, but here's the main one I can give:"
        k ldown rhip "Make sure you look back on past actions that the characters have done constantly."
        k lup "That way, you'll be able to form events that connect with what characters have done previously."
        k ldown "As opposed to events that have little to no connection at all."
    if koto_chosen == "yuri":
        k om "I'll choose Yuri."
        show yuri turned happ casual rup zorder 2 at r22
        show kotonoha cm at t21
        y om "What's your opinion on horror?"
        show yuri cm
        k laug ldown "Standalone horror tends to not work."
        k lup "It doesn't seem to scare me all that well."
        k ldown rhip "Personally I prefer psychological horror."
    if koto_chosen == "chat":
        k om "I'll choose Sayori's chat."
        show sayori turned happ casual rup zorder 2 at r22
        show kotonoha cm at t21

    hide kotonoha
    show monika forward casual happ rhip zorder 2 at t41
    show sayori turned casual happ rup zorder 2 at t42
    show natsuki turned casual happ rhip zorder 2 at t43
    show yuri turned casual happ rup zorder 2 at t44
    menu:
        "Next Question."
        
        "Monika" if last_chosen != "monika" and koto_chosen != "monika":
            $ last_chosen = "monika"
            m om "Have you ever done a collaboration project before?"
            show monika cm
            t "Besides with Koto-chan?  Only those writing assignments I was assigned with other classmates."
            t "Didn't have many to talk to."
        "Sayori" if last_chosen != "sayori" and koto_chosen != "sayori":
            $ last_chosen = "sayori"
            s om "Have you ever had to completely rewrite a story before release?"
            show sayori cm
            t "Yes actually, but only one."
            t "And that one would be Hollow."
            t "At some point during writing, there were so many lore inconsisties with the story that I had to rewrite the entire thing to fix the continuity."
            t "Not to mention how poorly written and cringey the first part of it was."
            t "That was certainly an endeavor."
        "Natsuki" if last_chosen != "natsuki" and koto_chosen != "natsuki":
            $ last_chosen = "natsuki"
            n om "Worst stereotype, go!"
            show natsuki cm
            t "Minority or race being weak."
            t "Enough said."
        "Yuri" if last_chosen != "yuri" and koto_chosen != "yuri":
            $ last_chosen = "yuri"
            y om "How do you get out of writer's block?"
            show yuri cm
            t "Take a break."
            t "That's it, it's that simple."
            t "A break really helps with things like that."
        "Sayori's chat" if last_chosen != "chat" and koto_chosen != "chat":
            $ last_chosen = "chat"

    hide yuri
    hide sayori
    hide monika
    hide natsuki
    show kotonoha turned casual happ lup zorder 2 at t11
    $ koto_chosen = renpy.random.choice([person_chosen for person_chosen in choice_list if person_chosen not in [koto_chosen, last_chosen, "chat"]])
    if koto_chosen == "monika":
        k om "I'll choose Monika."
        show monika forward happ casual rhip zorder 2 at r22
        show kotonoha cm at t21
        m om "Have you ever done a collaboration project before?"
        show monika cm
        k om "Besides with Tai-kun?  Only those writing assignments I was assigned with other classmates."
        k laug ldown rhip "Didn't have many to talk to."
    if koto_chosen == "sayori":
        k om "I'll choose Sayori."
        show sayori turned happ casual rup zorder 2 at r22
        show kotonoha cm at t21
        s om "Have you ever had to completely rewrite a story before release?"
        show sayori cm
        k om "Not really."
        k rhip "I know Tai-kun did."
        k laug ldown "He completely broke the lore, had to rewrite the entire first part."
        k rdown "It was certainly an endeavor."
    if koto_chosen == "natsuki":
        k om "I'll choose Natsuki."
        show natsuki turned happ casual rhip zorder 2 at r22
        show kotonoha cm at t21
        n om "Worst stereotype, go!"
        show natsuki cm
        k om "Minority or race being weak."
        k ldown rhip "Enough said."
    if koto_chosen == "yuri":
        k om "I'll choose Yuri."
        show yuri turned happ casual rup zorder 2 at r22
        show kotonoha cm at t21
        y om "How do you get out of writer's block?"
        show yuri cm
        k om "Take a break."
        k rhip "That's it, it's that simple."
        k ldown "A break really helps with things like that."
    if koto_chosen == "chat":
        k om "I'll choose Sayori's chat."
        show sayori turned happ casual rup zorder 2 at r22
        show kotonoha cm at t21

    hide kotonoha
    show monika forward casual happ rhip zorder 2 at t41
    show sayori turned casual happ rup zorder 2 at t42
    show natsuki turned casual happ rhip zorder 2 at t43
    show yuri turned casual happ rup zorder 2 at t44
    menu:
        "Next Question."
        
        "Monika" if last_chosen != "monika" and koto_chosen != "monika":
            $ last_chosen = "monika"
            m om "What's your least favorite genre?"
            show monika cm
            t "Comedy."
            t "Enough said."
        "Sayori" if last_chosen != "sayori" and koto_chosen != "sayori":
            $ last_chosen = "sayori"
            s om "What's the most common problem you see with stories and how do you wish to fix it?"
            show sayori cm
            t "Continuity errors, a sinner's favorite thing to call out."
            t "To avoid those, you want to look back on past events constantly to make sure everything lines up."
            t "Use your ability as the writer to look at the past as an advantage."
            t "It'll help connect things in the end."
        "Natsuki" if last_chosen != "natsuki" and koto_chosen != "natsuki":
            $ last_chosen = "natsuki"
            n om "What's your least favorite adaptation?"
            show natsuki cm
            t "That one where a demi-god tries to stop a war."
            t "That did not work as a movie."
            t "I'm glad they're fixing it and making it a TV series."
            t "I've seen the first season, it looks so much better now."
            t "Great improvement on last time!"
        "Yuri" if last_chosen != "yuri" and koto_chosen != "yuri":
            $ last_chosen = "yuri"
            y om "What's the general writing aspect that you focus the most on?"
            show yuri cm
            t "Continuity."
            t "Continuity errors often mess with a story's lore."
            t "So, I tend to make sure everything connects up properly."
            t "I'm sure Koto-chan would say the same."
        "Sayori's chat" if last_chosen != "chat" and koto_chosen != "chat":
            $ last_chosen = "chat"

    hide yuri
    hide sayori
    hide monika
    hide natsuki
    show kotonoha turned casual happ lup zorder 2 at t11
    $ koto_chosen = renpy.random.choice([person_chosen for person_chosen in choice_list if person_chosen not in [koto_chosen, last_chosen, "chat"]])
    if koto_chosen == "monika":
        k om "I'll choose Monika."
        show monika forward happ casual rhip zorder 2 at r22
        show kotonoha cm at t21
        m om "What's your least favorite genre?"
        show monika cm
        k om "Comedy."
        k ldown rhip "Enough said."
    if koto_chosen == "sayori":
        k om "I'll choose Sayori."
        show sayori turned happ casual rup zorder 2 at r22
        show kotonoha cm at t21
        s om "What's the most common problem you see with stories and how do you wish to fix it?"
        show sayori cm
        k anno ldown rhip ce om "Continuity errors, a sinner's favorite thing to call out."
        k happ lup rdown oe "To avoid those, you want to look back on past events constantly to make sure everything lines up."
        k rhip "Use your ability as the writer to look at the past as an advantage."
        k ldown "It'll help connect things in the end."
    if koto_chosen == "natsuki":
        k om "I'll choose Natsuki."
        show natsuki turned happ casual rhip zorder 2 at r22
        show kotonoha cm at t21
        n om "What's your least favorite adaptation?"
        show natsuki cm
        k anno om "That TV remake of the really good wizard boy story."
        k ldown rhip "I know it's not out yet, but that really doesn't need a TV remake."
        k ce "Seriously, people love the 8 movie series, we don't want a remake."
        k rdown "*Sigh*"
    if koto_chosen == "yuri":
        k om "I'll choose Yuri."
        show yuri turned happ casual rup zorder 2 at r22
        show kotonoha cm at t21
        y om "What's the general writing aspect that you focus the most on?"
        show yuri cm
        k om "Continuity."
        k rhip "Continuity errors often mess with a story's lore."
        k rdown "So, I tend to make sure everything connects up properly."
        k ldown rhip "I'm sure Tai-kun would say the same."
    if koto_chosen == "chat":
        k om "I'll choose Sayori's chat."
        show sayori turned happ casual rup zorder 2 at r22
        show kotonoha cm at t21

    hide kotonoha
    show monika forward casual happ rhip zorder 2 at t41
    show sayori turned casual happ rup zorder 2 at t42
    show natsuki turned casual happ rhip zorder 2 at t43
    show yuri turned casual happ rup zorder 2 at t44
    menu:
        "Next Question."
        
        "Monika" if last_chosen != "monika" and koto_chosen != "monika":
            $ last_chosen = "monika"
            m om "What's your least favorite story?"
            show monika cm
            t "I don't exactly have one to be honest."
            t "I've read so many good ones, it feels rude to pick a least favorite."
        "Sayori" if last_chosen != "sayori" and koto_chosen != "sayori":
            $ last_chosen = "sayori"
            s om "I know you don't like comedy, but what do you actually like about it?"
            show sayori cm
            t "I only like when it's just a gag that's done during a serious scene and manages to make you laugh."
            t "That's about it."
        "Natsuki" if last_chosen != "natsuki" and koto_chosen != "natsuki":
            $ last_chosen = "natsuki"
            n om "How do you feel about the deredere types?"
            show natsuki cm
            t "They're a very complicated bunch, I'll say that much."
            t "I think most people like the tsundere, and I must agree."
            n cross om "That's what I am!"
            show natsuki cm
            t "Never thought I'd hear an actual tsundere admit it."
            n laug om "Yeah, I gave up denying a long time ago..."
        "Yuri" if last_chosen != "yuri" and koto_chosen != "yuri":
            $ last_chosen = "yuri"
            y om "Who's your favorite character in any media?"
            show yuri cm
            t "An adorable golden girl from my favorite game of all time;"
            t "A gacha rhythm game with probably the best cast of characters in anything ever!"
            t "I'm not saying anything else, I want you all to have fun with this adorable cast yourself."
            t "Assuming you know what I'm talking about of course."
        "Sayori's chat" if last_chosen != "chat" and koto_chosen != "chat":
            $ last_chosen = "chat"

    hide yuri
    hide sayori
    hide monika
    hide natsuki
    show kotonoha turned casual happ lup zorder 2 at t11
    $ koto_chosen = renpy.random.choice([person_chosen for person_chosen in choice_list if person_chosen not in [koto_chosen, last_chosen, "chat"]])
    if koto_chosen == "monika":
        k om "I'll choose Monika."
        show monika forward happ casual rhip zorder 2 at r22
        show kotonoha cm at t21
        m om "What's your least favorite story?"
        show monika cm
        k om "Any nursery rhyme."
        k ldown rhip "Enough said."
    if koto_chosen == "sayori":
        k om "I'll choose Sayori."
        show sayori turned happ casual rup zorder 2 at r22
        show kotonoha cm at t21
        s om "I know you don't like comedy, but what do you actually like about it?"
        show sayori cm
        k om "I only like when it's just a gag that's done during a serious scene and manages to make you laugh."
        k ldown rhip "That's about it."
    if koto_chosen == "natsuki":
        k om "I'll choose Natsuki."
        show natsuki turned happ casual rhip zorder 2 at r22
        show kotonoha cm at t21
        n om "How do you feel about the deredere types?"
        show natsuki cm
        k om "They are quite a fun class of characters."
        k ldown rhip "And call me crazy, but my favorite type is the yandere."
        k laug "Even though in real life, they've tried to kill Tai-kun and I multiple times."
    if koto_chosen == "yuri":
        k om "I'll choose Yuri."
        show yuri turned happ casual rup zorder 2 at r22
        show kotonoha cm at t21
        y om "Who's your favorite character in any media?"
        show yuri cm
        k om "Hard to narrow it down."
        k ldown "There's so many good ones."
        k rhip "I'll probably need to break down every character I've ever liked to help me narrow things down." 
        k rdown "So that will be for later."
    if koto_chosen == "chat":
        k om "I'll choose Sayori's chat."
        show sayori turned happ casual rup zorder 2 at r22
        show kotonoha cm at t21

    hide kotonoha
    show monika forward casual happ rhip zorder 2 at t41
    show sayori turned casual happ rup zorder 2 at t42
    show natsuki turned casual happ rhip zorder 2 at t43
    show yuri turned casual happ rup zorder 2 at t44
    menu:
        t "Lastly..."
        
        "Monika" if last_chosen != "monika" and koto_chosen != "monika":
            $ last_chosen = "monika"
            m om "Alright!"
            m lpoint "I'm sure everyone's wondering this."
            m ldown "Are you joining the literature club?"
            show monika cm
        "Sayori" if last_chosen != "sayori" and koto_chosen != "sayori":
            $ last_chosen = "sayori"
            s om "Alright!"
            s "I'm sure everyone's wondering this."
            s lup "Are you joining the literature club?"
            show sayori cm
        "Natsuki" if last_chosen != "natsuki" and koto_chosen != "natsuki":
            $ last_chosen = "natsuki"
            n om "Well new guy, I would like to know if you are joining the literature club."
            show natsuki cm
        "Yuri" if last_chosen != "yuri" and koto_chosen != "yuri":
            $ last_chosen = "yuri"
            y om "Well my humble patient, I would like to know if you are joining the literature club."
            show yuri cm
        "Sayori's chat" if last_chosen != "chat" and koto_chosen != "chat":
            $ last_chosen = "chat"
            s "They would like to know if you're joining the literature club."
            show sayori cm
    t "Well, this club seems to be a lot of fun, even with only four members."
    show yuri at f44
    show sayori at f42
    t "Not to mention, some of my closest friends are here."
    show yuri at t44
    show sayori at t42
    t "So, final verdict:"
    t "I'm joining the literature club."
    hide yuri
    hide sayori
    hide monika
    hide natsuki
    show kotonoha turned casual happ lup rhip zorder 2 at t11
    k om "Before anyone asks, I am too."
    k ldown "Though I believe that still counts towards the quota."
    m "Yes it does."
    k rdown "Alright!"
    hide kotonoha
    "With the question quota met, we step down from the non-existent stage."
    stop music fadeout 1.0
    $ style.say_window = style.window
    $ nb = "namebox"
    scene bg park_01 with dissolve_scene_full
    play music confdep
    "I'm starting to wonder if I should really be here."
    "Everyone's so social here."
    "But me..."
    "I don't fit in."
    "I just don't fit in!"
    "I'm an observer from afar, not a socialist within reach."
    a "Damnit!"
    show akira 3bl zorder 2 at t11
    show akira at f11
    ak "You need a break?  You seem to be really out of it."
    show akira at t11
    a "Tell me about it."
    show akira at f11
    ak 4bc "You seemed interested in that boy over there."
    show akira at t11
    a "Not interested, just thought he sounded familiar."
    show akira at f11
    ak 2bl "Does the name 'Taiyen' ring a bell?"
    show akira at t11
    a "His name is what?"
    show akira at f11
    ak 1bl "Taiyen."
    show akira at t11
    a "No, it doesn't"
    show akira at f11
    ak 4bc "..."
    stop music fadeout 1.0
    $ style.say_window = style.window_fake
    $ nb = "namebox_fake"
    scene bg park_01 with dissolve_scene_full
    show monika forward casual happ lpoint rhip zorder 2 at t11
    play music t5
    m om "Okay, everyone!  We have one more activity planned for today, and it's a literature one!"
    m ldown "We do this every year, Let's all write a poem and show it to each other!"
    hide monika
    "With that, everyone goes off to write their poems seperately."
    "I'm actually not good at poems, but I might as well try while I can."
    scene bg park_01 with wipeleft_scene
    show monika forward casual happ lpoint rhip zorder 5 at t11
    m om "Alright!  If everyone has written their poems, then we can start sharing."
    show monika cm
    t "Can I go first?  I'm not good at poetry and I want to set a baseline for everybody."
    show kotonoha turned casual happ rhip zorder 1 at t41
    show yuri turned casual happ rup zorder 2 at t44
    show sayori turned casual happ rup zorder 3 at t21
    show natsuki turned casual happ rhip zorder 4 at t22
    m ldown om "Sure!"
    show monika cm
    call showpoem(poem_t, False)
    t "I think it speaks for itself."
    s laug ce om lup "Pfft!  That's hilarious!"
    t "Laugh at it all you want, it only promotes how bad it is."
    m  laug om "Taiyen, I know you're a drama writer, but I think you could go big as a comedy writer."
    t "I never liked comedy."
    t "Next, please."
    show sayori happ ldown cm oe
    m happ lpoint om "Well, while we're at it, let's have our other new member go next."
    show monika ldown cm at t41
    show kotonoha at t11
    k lup om "I'd love to."
    call showpoem(poem_k, False)
    k "What do you all think?"
    show kotonoha cm
    t "Koto-chan, when did you become a symbolistic writer?"
    k laug om ldown "I have absolutely no idea."
    y om "I love how your taking two completely different topics and seeing how they relate together."
    k happ lup "A lot of my inspiration came from how I've noticed that even if everything is different from each other, they still have a lot of similarities."
    k ldown rhip "Shows how things really go together."
    n curi "I never noticed."
    n lhip happ "Care to give us some more details?"
    k lup "When we have more time."
    show yuri cm
    k ldown "For now, who's next?"
    show monika at t11
    show kotonoha cm at t41
    m lpoint om "Good ol' me!"
    call showpoem(poem_m)
    show monika cm
    t "The hard truth of everything..."
    s e1b om "Yeah, it sucks to know that even you've made yourself the best you can be, there's still a lot of flaws that are just waiting to be pointed out."
    "I still don't even know your attribute."
    m dist ldown om "It doesn't help that everyone's been calling me 'perfect' when... I'm nowhere close."
    y anno om "You and everyone in the universe."
    n dist om "Perfection is boring."
    k lup om "Yeah, it's the flaws that makes someone beautiful."
    m happ "Thank you!"
    show natsuki happ cm
    show yuri happ cm
    show kotonoha ldown cm
    show sayori happ oe cm
    m lpoint "Yuri, want to go next?"
    show yuri at t11
    show monika ldown cm at t44
    y rup om "Sure!"
    call showpoem(poem_y)
    k curi om "What's this about?"
    t "She hasn't told you?"
    y curi "I thought I did.  Must've slipped my mind."
    k happ "It's fine."
    t "To give you the short version; Yuri-chan's past life wasn't the greatest."
    t "She can give you the details."
    t "Anyway, I'm glad you're getting through the past and fighting against it."
    show yuri happ cm
    show kotonoha cm
    t "It takes strength, but you'll get through it."
    t "On another note, what's with the classical language?  Seems kinda out of place."
    n curi om "Yeah, I was wondering that too."
    n lhip "You usually use certain language to imply time difference."
    n ldown "Did it really feel like it was that long ago?"
    y worr om "Yes, but it still haunts me."
    y neut "I'll tell you everything someday."
    show yuri happ cm
    n happ "Can I go next?"
    show yuri at t22
    show natsuki at t11
    m lpoint om "Go ahead!"
    show monika cm
    call showpoem(poem_n)
    y curi om "Who are you talking about now?"
    n cross dist "Someone whom I presume is dead; my sister."
    n neut "A lot happened and I really should talk about it."
    n dist "Just don't know when to."
    y happ "You'll find time, don't worry."
    n laug "Thanks."
    n happ turned rhip "Sayori's up last, right?"
    show natsuki cm at t21
    show sayori at t11
    s om "Sure am!"
    call showpoem(poem_s)
    t "Don't remind me.  WE WENT THROUGH HELL!"
    s laug "Yeah, but we survived in the end, didn't we?"
    s rdown "Besides, we're the only ones who remember that life, right?"
    t "As far as I know."
    m laug om lpoint "Seems like we have a lot of things that need talking about."
    k laug lup "Yep, we sure do."
    stop music fadeout 1.0
    $ style.say_window = style.window
    $ nb = "namebox"
    scene bg park_01 with dissolve_scene_full
    play music confdep
    ak "Aoruguri, where are you going?"
    a "I'm heading back, I can't do this anymore!"
    a "Everyone's having too much fun."
    ak "This is your oppurtunity to be social, you can't back out now!"
    a "Shut up!"
    a "I can't have any fun."
    a "You know that!"
    a "*Sigh*"
    a "I should never have come here..."
    stop music fadeout 1.0
    $ style.say_window = style.window_fake
    $ nb = "namebox_fake"
    scene bg park_01 with dissolve_scene_full
    play music t3
    show monika forward casual happ rhip zorder 2 at t11
    m om "Okay, everyone!  We are running out of time here, so let's decide on what we should write for this year."
    m lpoint "As some of you may know, this is a literature club.  And in this literature club, we are tasked to write about one topic for each year."
    m ldown "Last year, we agreed on drawing from a hat to decide on the topic."
    m rdown "So..."
    "She grabs the hat she mentioned."
    m "We still got a lot of suggestions in here."
    m lpoint "The topic of this year is..."
    show monika cm
    stop music fadeout 3.0
    $ pause(3.0)
    show monika dist
    $ pause(1.0)
    m ce ldown rhip om "*Sigh*\nOh boy..."
    m oe lpoint "'Write about a true experience, past or present, that has made a significant impact on your life.  Preferably, a dramatically long experience.'  *Sigh*"
    m neut "Does anyone want to reroll?"
    hide monika
    show kotonoha turned casual dist zorder 2 at t41
    show sayori turned casual dist rup zorder 2 at t42
    show natsuki turned casual dist rhip zorder 2 at t43
    show yuri turned casual dist rup zorder 2 at t44
    "..."
    t "I don't."
    y neut om "Me neither."
    show yuri cm
    n om rdown "I kinda do, but...  I know I shouldn't."
    show natsuki cm
    k worr n1 lup om "The problem with this topic is: it goes into subjects that can be really personal for the author."
    k ldown rhip e1d "But if everyone's in agreement, then I have nothing to say."
    show kotonoha cm
    t "Sayori?  Are you in on this?"
    s rdown ce "..."
    s neut oe om "I'll do it."
    hide kotonoha
    hide sayori
    hide natsuki
    hide yuri
    show monika forward casual dist rhip zorder 2 at t11
    m om "Seems like we have a majority..."
    m ce rdown "..."
    m neut oe "Honestly, I'm scared to write mine."
    m dist rhip "But I'm in a similar situation to Natsuki; I {i}should{/i} do this."
    m neut lpoint "Alright.  Let's come back on Monday with the first chapters of our stories complete."
    everyone "Got it."
    stop music fadeout 1.0
    scene black with dissolve_scene_full
    $ style.say_window = style.window
    $ nb = "namebox"
    play music ghostmenu
    $ akira = "Voice 4"
    $ hanato = "Voice 1"
    $ kirinani = "Voice 5"
    $ itsomi = "Voice 2"
    $ inari = "Voice 3"
    ha "Seems like your boyfriend has joined that club you despise."
    its "Well, how infuriating."
    ina "Seems like {i}we'll{/i} need to up our game a bit if we want to take over the school."
    ak "We sure will.  I hope your plan works, boss."
    kiri "Oh, don't worry.{w=1}  It will."
    achieve newfriends
    return