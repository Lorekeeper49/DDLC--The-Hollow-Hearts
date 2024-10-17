#Name: Dark Discoveries
label act2_ch2_main:
    if not known:
        jump act2_ch2_alt
    scene bg kamiclassnight
    show lilly c2e zorder 2 at t11
    with dissolve_scene_full
    lil "Hi..."
    "She scared the shit out of me!"
    lil c3 "Sorry, I had to find you."
    lil c1e "You saw it, right?"
    "So I'm not going crazy...?"
    a "Yes... I did."
    lil ebc2 "I'll just show you it."
    show lilly with Fade(0.0, 0.1, 0.0)
    $ pause(0.05)
    show lilly with Fade(0.0, 0.1, 0.0)
    $ pause(0.05)
    show lilly doll c0 with Fade(0.0, 0.3, 0.0)
    lil "You can see me, right?"
    show lilly a0
    a "Holy fuck!"
    lil c0 "This is what I truly look like."
    show lilly a0 with Fade(0.0, 0.05, 0.0)
    $ pause(0.05)
    show lilly with Fade(0.0, 0.05, 0.0)
    $ pause(0.05)
    show lilly with Fade(0.0, 0.05, 0.0)
    $ pause(0.05)
    show lilly with Fade(0.0, 0.05, 0.0)
    $ pause(0.05)
    show lilly with Fade(0.0, 0.05, 0.0)
    $ pause(0.05)
    play sound lightswitch
    show lilly norm dbc2 with Fade(0.0, 0.5, 0.0)
    $ pause(0.5)
    lil ebc2 "I'm not human, I'm a doll."
    "Fuck me."
    lil c3c2 "I am a horrible science experiment."
    lil c1e "I've known since I was born."
    lil c3 "or... created for that matter."
    lil c1e "But besides my creator, no one has ever seen it until..."
    a "...I did."
    "Well that's... something."
    a "H-hold on a second!"
    a "You flew into here, right?\nDolls don't fly."
    a "Actually more confusingly, Why do you look and feel like a human?"
    a "This isn't some android deal either, you actually feel like a human."
    "I refer back to when I shook her hand yesterday."
    lil c3 "Well...  I'm not sure how to put that."
    lil c1e "All I can say is... it wasn't initially intended."
    "How do you accidentally make an experiment human?"
    lil "Hey, you have something to do in a bit, right?"
    a "About that, hang on."
    "I pull out my phone since I think Akira told me to do something else this time."
    aktext "You're meeting up with Taiyen tomorrow, right?"
    "This text is from yesterday."
    aktext "Bring the club along, I want to show it to him."
    a "Akira suggested I'd invite the club to this."
    lil ee "I'll go get them then."
    show lilly with Fade(0.0, 0.1, 0.0)
    $ pause(0.05)
    show lilly with Fade(0.0, 0.1, 0.0)
    $ pause(0.05)
    show lilly doll a0 at i11 with Fade(0.0, 0.2, 0.0)
    $ pause(0.1)
    hide lilly with Fade(0.0, 0.1, 0.0)
    $ pause(0.05)
    scene bg kamiclassnight with Fade(0.0, 0.1, 0.0)
    "There she goes."
    "*Inhale*{w=2}\nI didn't expect any of that!"
    scene bg kamiclassday with None
    $ pause(0.1)
    scene bg kamiclassnight with None
    $ pause(0.5)
    scene bg kamiclassday with None
    $ pause(0.1)
    scene bg kamiclassnight with None
    $ pause(0.5)
    play sound lightswitch
    $ pause(0.5)
    scene bg kamiclassday with None
    a "Oh crap!  The system's broken, the lights aren't supposed to be on yet!"
    scene bg kamiroofs with wipeleft_scene
    "On the roof, I see the culprit;"
    show hanato day anno zorder 2 at t11
    a "HANATO!"
    a "How many times do I have to tell you?!  Don't mess with the illusion mainframe!"
    a "This is the 15th time you've done it!  What are you even trying to do here?"
    show hanato lhip at rhide 
    $ pause(1.0)
    hide hanato
    "No response?"
    "Maybe she's just fed up."
    "I go over to the mainframe and fix it up, while also noticing a little note left inside.\nIt reads..."
    ha "Meet me up here during lunch, come alone."
    "It says that in Chinese, not many people speak that language here."
    a "I accept."
    "Usually I don't talk with the Kamiyamas often (besides Akira) but since she's sending an encrypted message asking to talk alone, I need to see what she has to say."
    "Besides, if it turns out to be a trap, I know how to defend myself now."
    "I close the mainframe."
    "..."
    "I will never understand this school and it's design choices."
    "They literally blew a giant hole in a big hill just to build this place."
    "...And they kept this top part."
    "Wow."
    a "Heh, look at me rambling to myself!"
    a "I've really changed, huh?"
    a "..."
    a "I'm running out of time."
    scene bg tree with flash
    play ambience forest
    a "Guys, you here?"
    show tina turned anno zorder 2 at t11
    ti "You're late!"
    show akira 1ab zorder 1 at t21
    ak "Actually, you're right on time.\nYour boyfriend's not here yet."
    a "He's not my..."
    "I'm not even blushing and I cut myself off."
    hide akira
    hide tina
    show kotonoha turned rhip neut zorder 2 at t11
    k "Okay, calm down people!"
    "Already done."
    k happ e1c "Oh!  He's here!"
    hide kotonoha
    play music t2
    show sayori turned happ zorder 4 at l21
    show natsuki turned happ zorder 3 at l22
    show yuri turned happ zorder 2 at l44
    show taiyen zorder 1 at l41
    show monika forward happ zorder 5 at l11
    t "Good Morning, everyone."
    a "Good morning{nw}"
    stop music
    extend "-"
    "I don't know half of these people, but..."
    show vignette zorder 100 with dissolve
    "Why does it feel like...?"
    a "Ugh.{nw}"
    stop ambience fadeout 1.0
    scene black with dissolve
    play sound fall
    everyone "Aoruguri!"
    $ pause(1.0)
    scene bg wilderness with dissolve_scene
    play ambience forest
    a "Nngh!"
    show taiyen zorder 2 at t11
    t "Ah!  You're awake!"
    a "Taiyen?"
    a "How long was I out?"
    t "An hour."
    a "Why am I not in the hospital."
    t "Thank Yuri-chan."
    "He shows what I assume is his phone with a knife in the center of it."
    a "That's... a little extreme."
    t "She's a yangire, extreme's kind of her middle name."
    "I attempt to get up."
    t "Uh- do that slowly."
    a "I got it."
    hide taiyen
    "Ugh...  What was that dream I had?"
    "I remember it clearly like I usually do, this isn't the first time I've been knocked out.  But it felt so... familiar..."
    "I stand up wearily."
    show kotonoha turned worr om zorder 2 at t11
    k "Hate to burst your bubble but you struck yourself with lightning about 12 times while you were asleep."
    a "Why did I-\nWait, I know exactly why."
    a "My body likes to go crazy while I'm asleep, even attempt to kill itself."
    show taiyen zorder 2 at t21
    show kotonoha at t22
    t "Jesus!"
    "I notice my body's not scratched up at all, it's really gotten used to this."
    a "But it isn't that bad anymore, I know how to keep myself from danger."
    t "That's good."
    hide taiyen
    hide kotonoha
    show yuri turned neut rup om zorder 2 at t21
    show lilly a2e zorder 2 at t22
    y "We've been making aquaintance since you've been asleep."
    y e1c "I didn't expect my sister to work with the infamous Night Club."
    y lup "It's kinda scary."
    lil c3e "I'm fine, sis!"
    "Yuri..."
    hide yuri
    hide lilly
    show natsuki turned neut om zorder 2 at t11
    n "I'm wondering about you though."
    n rhip "How long has it been?  5 years?"
    "Natsuki..."
    hide natsuki
    show sayori turned rup neut om zorder 2 at t11
    s "I worry about you, you know?"
    s worr "I don't want the events from years ago to happen twice."
    "Sayori..."
    hide sayori
    show monika forward neut om zorder 2 at t11
    m "You need to start taking better care of yourself."
    m rhip worr "You nearly killed yourself at that old school."
    "Monika..."
    hide monika
    show yuri turned neut rup zorder 2 at t21
    show sayori turned rup neut zorder 2 at t22
    a "Sayori?  Yuri?  Why do I feel like I know you even though I have no memory of what happened?"
    show sayori lsur rdown
    y lsur lup om "That's alarming!"
    s om "Lots of stuff happened that I still remember!"
    show natsuki turned curi om zorder 3 at t11
    n "Did you develop some sort of amnesia or something?"
    show natsuki cm
    a "No?"
    "No matter how much I rack my brain, nothing comes up."
    a "*Sigh* I don't know."
    hide natsuki
    "Suddenly, my class alarm goes off."
    a "Shit!  I'm gonna be late for class."
    show taiyen zorder 2 at t11
    t "Us too!  We better get going."
    hide taiyen
    show sayori turned happ zorder 4 at t21
    show natsuki turned happ zorder 3 at t22
    show yuri turned happ zorder 2 at t44
    show kotonoha turned happ zorder 1 at t41
    show monika forward happ zorder 5 at t11
    everyone "We'll see you later"
    hide sayori 
    hide natsuki 
    hide yuri 
    hide kotonoha 
    hide monika 
    show taiyen zorder 2 at t11
    t "Take care, Aoruguri."
    a "You too."
    "With that, I raise my hand and..."
    scene bg kamiclassday with flash
    stop ambience
    "...zap back to school."
    play sound kamibell
    "Right in time for the bell."
    "...Yes, that's our bell."
    scene bg kamiroofd with wipeleft_scene
    call showlocation("Kamiyama Academy Roof","October 9, 2023",724.95,"bg kamiroofd") from _call_showlocation_40
    show hanato day zorder 2 at t11
    $ pause(1.0)
    a "Hanato."
    a "You wanted to talk?  Let's talk."
    ha lhip rhip angr om "Yes, let's!"
    ha lup "First of all, elephant in the room, I'm working with the guy who killed your friend's parents."
    ha ce "Well actually, I'm his sister."
    show hanato cm
    "That's a surprise!"
    "Wait, does that mean...?"
    "I guess that would make sense."
    ha ldown oe om "That's not the whole point though."
    ha rdown "He's planning something, and I don't like what I'm reading off of him."
    ha rup lhip "You won't understand this, but..."
    ha rdown "He plans to attack and destroy the school your friend goes to.\n{{Said normally but editted to sound backwards}" # Ot seog rouy loohcs eht yortsed dna kcatta ot snalp eh.
    show hanato cm    
    a "De-"
    "What? {{confused}"
    ha ce om "Yeah, that's what he's done to keep the plan secret."
    ha rup oe "And before you try making it sound normal, I already have to no avail."
    show hanato:
        time 3
        tcommon(x=-100)
    a "Okay...  What do you think he's say...\nEh?"
    hide hanato
    a "Do you... hear that?"
    window hide 
    with Shake((0, 0, 0, 0), 5.0, dist=50)
    "Both" "*Screaming*{w=2}{nw}"
    scene bg sewer_hall with wipeleft_scene
    stop ambience
    a "*Huff* *Puff*\nWhere are we?"
    a "Hanato?"
    "No sign of her!"
    "Shit!"
    "Well, first order of business: find a way out of here!"
    "Sewer's have been equipped with dampeners since a historic incident so I won't be able to use my abilities."
    a "Son of a bitch!"
    call explore("sewer_hall") from _call_explore
    play ambience forest
    scene bg tree with wipeleft_scene
    a "Well, that was fun.  {{said sarcastically}"
    show hanato day anno rhip lhip om zorder 2 at t11
    ha "You said it!  I don't know if I want to go there again."
    a "We should head back to school, we've been gone for over two hours, no doubt we missed classes."
    "I don't even acknowledge the fact that this is the park Taiyen and I usually meet at."
    scene bg kamiroofn with flash
    show mari forward worr zorder 2 at t11
    ma "Aoruguri!?"
    ma angr om "Where have you been!?  We've been looking for you for hours!"
    show mari cm
    a "In the sewer..."
    "I relay everything that happened."
    ma worr om "Jesus!"
    ma happ bc "Well, you better get to the Headquarters, everyone's worried sick about you!"
    a "Copy that!"
    scene black with wipeleft_scene
    stop ambience fadeout 1.0
    "I returned back to the club..."
    "Nothing else happened after that besides having to change schedules with going to the mansion, but I imagine this won't be the last time I must go through a place like that."
    return

label act2_ch2_alt:
    stop music fadeout 2.0
    play ambience forest
    scene bg tree
    with dissolve_scene_full
    a "*Sigh*"
    "I don't know why I keep coming back here..."
    scene bg pasteur_day with wiperight
    t "Hey..."
    a "Hello...?"
    a "You don't sound too good..."
    t "..."
    a "Something wrong?"
    t "Something bad happened last night..."
    t "She's dead."
    t "My sister's dead!"
    t "He killed her..."
    t "He fucking killed her!"
    a "fuck... fuck... fuck... FUCK... FUCK..."
    t "Doesn't exactly help, but you said it."
    a "Sorry..."
    a "I've never been good at these types of things."
    a "I don't even know why I come here anymore..."
    t "You and me both."
    t "But..."
    t "..."
    t "Damn it!"
    t "Sorry, I'm ruining our usual."
    t "I should've cancelled for today."
    "..."
    scene bg wilderness with wipeleft
    "Without knowing why, I go to the other side and give him a hug."
    "If I can't even communicate with people, I might as well comfort the only person I've ever been able to regularly talk with."
    scene black with dissolve
    t "..."
    a "..."
    $ pause(1.0)
    scene wilderness with dissolve
    "We release..."
    show taiyen zorder 2 at t11
    t "Thank you, I really needed that."
    a "You shouldn't go to school today."
    t "I actually cancelled school today thanks to the incident."
    a "Right, you and your family own that school."
    t "Yeah..."
    t "But you've still got school, right?"
    a "Hm..."
    "I'm considering something."
    a "Call me crazy, but..."
    "What am I doing?"
    a "I don't think you should be alone today."
    "?"
    t "Huh?  You sure?"
    "Confused, I snap out of whatever trance I was in."
    a "Sorry.  I have no idea what the fuck I am doing!"
    t "No no, it's fine!  You just surprised me is all."
    a "No I truly have no idea what I'm-"
    t "If you're truly sure about this, then follow me home.  I trust you with my location."
    a "But don't blame me if this ends up hurting your grade!"
    "He starts walking away."
    a "Ah! Fuck it!"
    "I begin following him."
    
    return