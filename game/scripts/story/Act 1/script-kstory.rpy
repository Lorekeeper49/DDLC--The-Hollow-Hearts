label kstory(bgreturn="bg club_day"):
    scene black with dissolve_scene
    $ window_style = ""
    $ nb = "namebox"
    $ nextscene = "kstory_ch" + str(chapter)
    $ char_perspective = "Kotonoha"
    call expression nextscene 
    $ char_perspective = "Taiyen"
    stop music fadeout 2.0
    stop sound fadeout 2.0
    scene black with dissolve_scene
    $ window_style = "fake"
    $ nb = "namebox_fake"
    scene expression bgreturn with dissolve_scene_half
    return

label kstory_ch2:
    play music tears
    scene bg city_street_night with dissolve_scene_full
    call showlocation("Bustling Streets\n{size=25}賑やかな通り{/size}","September 29, 2023\n{size=15}2023年9月29日{/size}",20*60+4+57/60.0,"bg city_street_night")
    k "Ugh!  Why is that so difficult!?"
    "I look around after getting kicked out."
    "The game I was playing is hard as balls trapped in an air fryer!"
    "{cps=3}...{/cps}"
    "That is officially the weirdest thing I've ever said, especially in my head."
    k "*Sigh* Seiei?"
    "He comes out."
    show seiei turned casual anno ce zorder 2 at t11
    $ pause(0.5)
    call showintro(intro_sei) from _call_showintro_3
    sei om "*Sigh* That is an embarrassing death."
    show seiei cm
    k "They were swarming us!"
    sei oe om "Wanna do another attempt?"
    show seiei neut cm
    k "We can't, it's late and the club's probably worried."
    sei cross om "Right.  Let's head back to HQ."
    hide seiei
    "We walk for a bit."
    $ pause(3.0)
    "I stop."
    show seiei turned casual zorder 2 at t11
    k "It's...  It's not right!"
    sei curi om "What?  Me being here?"
    k "No-"
    sei cross neut "I get it.  There's no way an Ordinary man like me-"
    k "That's not what I'm talking about!"
    show seiei cm
    k "We're breaking into so many abandoned places..."
    k "going through so many dangers..."
    k "meeting so many fates...!"
    k "It's not right!  None of this is right!"
    k "So many people have died!"
    k "Mio...  Hime...  Himari...!"
    k "Not to mention all the people who went missing and never came back!"
    k "And for what?  To get at an overgrown mimic who's to powerful for his own good?"
    k "Face it, Seiei!"
    k "We're never gonna kill Kirinani!"
    k "It's impossible!"
    k "*Sob*"
    $ pause(1.0)
    sei ldown2 rdown2 om "Maybe so..."
    sei anno "{i}If{/i} we didn't have help from his own family."
    k "What?"
    sei ldown rdown "Follow me, I know where he is."
    scene bg shed_night with wipeleft_scene
    call showlocation("Shed Hideout\n{size=25}小屋の隠れ家{/size}","September 29, 2023\n{size=15}2023年9月29日{/size}",20*60+14+57/60.0,"bg shed_night")
    show akira uniform turned c zorder 2 at t11
    "...{w=1}Huh?"
    hide akira
    show seiei turned casual zorder 2 at t11
    k "Akira?  Why him?  He's like Kirinani's right hand man!"
    sei om "Well, why do {i}you{/i} like him?"
    show seiei cm
    k "Uh-?  *Flustered noise*\n...Fair point..."
    sei cross om "He's a spy, and a good one at that."
    sei ldown rdown anno om "Oi!  Akira!"
    k "Eh-W-Wait!"
    show akira uniform turned c zorder 2 at t22
    show seiei at t21
    "Akira comes over."
    k "I wanted you to at least explain things before calling him over!"
    "No one takes notice of me."
    ak cross "Seiei...  Did you do it again?"
    sei cross ce "*Sigh*"
    ak turned rout e "Ugh!  Seiei, I told you not to use STASIS to train!  It is unhealthy and doesn't actually do anything to the physical body."
    sei oe om "Yeah, yeah...  Listen, Kotonoha's here, say hi."
    show akira cross
    show seiei cm
    "He looks at me."
    ak g "So... we're finally telling {i}her{/i} about me, huh?"
    ak turned rout lout "Good, I don't have to hide anymore."
    hide seiei
    show akira at t11
    ak rpock lpock "Hi Kotonoha, it's me.  I spy on my family."
    k "You sound like you're tired of this job."
    ak cross k "I'm not tired of the job, I'm tired of staying up until midnight every day."
    "Right, he's like me; one of the unlucky ones that actually get tired."
    k "You can take a break at any time."
    ak g "Actually, I can't!"
    ak turned rout lpock "My father's doing so much evil, I can't take my eyes off him for a second!"
    k "That reminds me, why would a copycat who can give his comrades attributes not give them the ability to not get tired?"
    ak cross k "I've asked him that same question, and his answer was 'I wish it worked that way'.  And frankly, I agree."
    "Your telling me?  I wish {i}I{/i} could give people attributes, let alone the ability to not get tired."
    k "So, this is what you've been doing behind my back!"
    ak turned o "Yes... and it ain't easy."
    "If only we could make it easier."
    "Well at least I know I can trust him."
    "That is reassuring."
    return

label kstory_ch3:
    scene bg pasteur_night with dissolve_scene_half
    call showlocation("Kanzen Academy Ruins\n{size=25}完全学園高校の廃墟{/size}","September 30, 2023\n{size=15}2023年9月30日{/size}",60*23+59+57/60.0,"bg pasteur_night")
    k "You sure we'll be able find anything here?"
    k "The place is completely destroyed."
    show seiei turned casual cross zorder 2 at t11
    sei om "Yeah, Luna really did a number on this place."
    show seiei cm
    k "Not to mention the fact that they cleaned up the place so well it's almost like it never existed."
    sei ldown rdown om "Which means we're going underground!"
    scene bg sewer_hall with wipeleft_scene
    play ambience factory
    "Shit..."
    "I can barely see."
    "Don't like the sewers already, but {i}this{/i} is worse!"
    show seiei turned casual zorder 2 at t11
    sei om "We could get lost in here if we're not careful."
    "No need to state the obvious..."
    sei ldown rdown om "If I'm correct about this, there should be a factory nearby..."
    hide seiei
    "We look around."
    k "Found it!"
    "Convenient that the door's labeled."
    k "Locked!"
    sei "There's another door that leads to a business room, it might have a spare key they left behind."
    k "Okay, I'll stay here!"
    "{cps=1}...{/cps}"
    "It's so quiet..."
    $ pause(1.0)
    scene bg sewerwatched with dissolve_scene
    $ pause(1.0)
    k "Eh?"
    "Am I... being watched?"
    show seiei turned casual zorder 2 at r11
    sei "I'm back!"
    k "Ah!  Jesus Christ!"
    k "Ha...  Hi!"
    k "You scared the shit out of me!  Jesus!"
    sei laug ldown rdown2 om "Tehehe, sorry!"
    "Sure sounds like it!"
    sei neut cross "Anyway, let's get moving."
    show seiei cm at lhide 
    $ pause(1.0)
    hide seiei
    $ pause(1.0)
    scene bg sewer_hall with dissolve_scene
    $ pause(1.0)
    scene bg factory with wiperight_scene
    k "We're here."
    sei "Let's take a look around."
    "Kay, we got a lot stuff to work with here."
    "Some old parts, lots of old machinary..."
    "Whoa, hold on a second."
    "Is it just me or..."
    k "Uh Seiei..."
    k "Tell me you don't recognize this place."
    show seiei turned casual cross zorder 2 at t11
    sei om "Yeah I do not like the flashbacks I'm getting here."
    show seiei cm
    k "It's worse for me, you were cancelled."
    k "I'm one of the few who had to witness it all go wrong."
    k "*Sigh*...  And after I swore to never come back here..."
    sei ldown rdown om "I did the same."
    sei cross doub "Then again, all the leads led here."
    show seiei cm
    k "If that's the case then..."
    show seiei neut
    k "You stay here and keep looking for clues."
    k "I'm gonna head to the office."
    sei om "Got it."
    scene bg office with wiperight_scene
    "Oh, how I hate to see this place again after what happened."
    "However, this is probably the first time in ever since his calculations that anyone besides Kirinani has touched this PC."
    "Wait, wouldn't that mean...?"
    "Find stuff now, question him later."
    "One of the lesser known abilities of a telegraph is that they're able to tell the exact point in time when any object was last touched as well as who touched it."
    "Knowing this, I check and..."
    k "I knew it."
    "This was last touched by Kamiyama Kirinani on October 2nd, 2020 at 16:00."
    k "He used this for something, I know it."
    stop ambience fadeout 2.0
    return

label kstory_ch4:
    play ambience factory fadein 1.0
    scene bg office with dissolve_scene_half
    call showlocation("Abandoned Office\n{size=25}廃墟のオフィス{/size}","October 1, 2023\n{size=15}2023年10月1日{/size}",60*23+59+57/60.0,"bg office")
    k "These calcuations just don't make sense."
    "Decided to come back on my own, because something wasn't exactly clicking in my head."
    k "Why did it all go wrong when his data..."
    k "Hold on..."
    k "Take the samples and..."
    with wipeleft_scene
    k "And finally..."
    "I stab myself with a syringe and..."
    k "Okay, somethings out.  That's promising."
    "The syringe is glowing white."
    k "Now to test."
    "I try to use telekinesis to lift anything in this room."
    "{cps=3}...{/cps}"
    "Nothing."
    k "Nothing!"
    k "Yes, it worked!"
    k "Okay, now to put it back in."
    k "Just do the normal procedure..."
    with wipeleft_scene
    k "And..."
    "I again stab myself with a syringe and..."
    k "Okay, it's in."
    k "I hope this works, otherwise I just doomed myself."
    "I again try to use telekinesis to lift anything in this room."
    "The entire shelf beside me moves."
    k "Not my intention, but YES!"
    k "TRANSPLANT COMPLETE!"
    k "Wait, but that means..."
    k "Hold on, let me run a few more tests."
    with wipeleft_scene
    k "This...  No..."
    k "You can't be serious!"
    with wipeleft_scene
    k "No way..."
    k "We had it... all along..."
    k "It all went wrong because..."
    play sound footsteps
    k "!!!"
    "Getting out of here!"
    stop ambience fadeout 2.0
    return

label kstory_ch5:
    call showlocation("???","October 2, 2023",23,59,57)
    k "That son of a...!"
    k "Why didn't anyone tell me!?"
    k "I trusted him..."
    k "And all this time, he's been stealing for profit!?"

    return