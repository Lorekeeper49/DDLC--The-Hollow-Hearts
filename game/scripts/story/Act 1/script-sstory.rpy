label sstory(bgreturn="bg club_day"):
    scene black with dissolve_scene
    $ window_style = ""
    $ nb = "namebox"
    $ nextscene = "sstory_ch" + str(chapter)
    $ char_perspective = "Sayori"
    call expression nextscene 
    $ char_perspective = "Taiyen"
    stop music fadeout 2.0
    stop sound fadeout 2.0
    scene black with dissolve_scene
    $ window_style = "fake"
    $ nb = "namebox_fake"
    scene expression bgreturn with dissolve_scene_half
    return

label sstory_ch2:
    play music confdep
    scene bg shouse_day with dissolve_scene_half
    t "So that's who you are..."
    s "You're pretty interesting too."
    t "Thanks?"
    t "You know, you picked up words pretty well."
    s "So did you."
    t "..."
    s "..."
    t "Do you know why we keep coming to these locations?"
    s "Beats me."
    s "There's a lot I don't know."
    s "Am I even... alive?  If that's what that word means..."
    t "I don't know.  We're not normal so..."
    t "Hm..."
    "We ponder for a while."
    "This place is very strange."
    "I don't know where I am or... {i}what{/i} I am for that matter."
    "I can't see myself."
    "Nor can I see this man standing right next to me."
    "It doesn't even make sense how we can hear each other."
    "I'm not sure if I'm smart enough to question it though."
    "Maybe when I learn more."
    "..."
    show vignette with dissolve_scene
    s "Hey, do you hear something?"
    return

label sstory_ch3:
    play music confdep
    scene bg shouse_day 
    show vignette
    with dissolve_scene_half
    t "Are you okay?"
    s "Sort of..."
    s "Hey, you know that move you told me about?"
    t "Way ahead of you!"
    "His form..."
    "I can see his form!"
    play sound thunder
    with Shake((0, 0, 0, 0), 0.1, dist=50)
    t "SHUT UUUUP!"
    play sound thunder2
    hide vignette with Fade(1.0, 0.0, 1.0)
    t "It's gone."
    s "Do you know what that was?"
    t "No."
    t "But I don't think that this will be the last time we have to deal with that."
    s "Why's that?"
    t "I don't know, just something in my gut."
    t "But I'll protect you, don't worry."
    s "Promise?"
    t "Promise."
    s "Good."
    "I smile."
    s "By the way..."
    s "Earlier, you weren't formless."
    s "What was that?"
    t "I... don't know."
    t "I just... have a form doing that."
    s "Well, whatever it is...  Let's keep it up for next time."
    t "Yeah."
    return

label sstory_ch4:
    play music confdep
    scene bg shouse_night with dissolve_scene_half
    "He's gone."
    "That's it.  I'm on my own."
    "Guess I know now why I keep coming back here."
    "This is where I'm gonna be born."
    s "Heh.  It's been a long time coming."
    s "Soon, I'll get my one chance to live."
    s "I better make it count."
    s "..."
    show vignette with dissolve_scene
    "Ah crap."
    s "Again?"
    s "Alright, fine."
    s "I'm on my own now though."
    s "So I'll be easier."
    s "That said, I'm not going down without a fight."
    s "Bring it on!"
    return

label sstory_ch5:
    play music confdep
    scene bg shouse_night with dissolve_scene_half
    "The fog fades and the dust settles."
    s "Did I... win?"
    "Doing this alone is hell."
    "I'd ask where he is when you need him, but I think I already know the answer to that question."
    "I'm on my own now that he's out."
    "My question though is why this storm keeps going beserk."
    s "Who are you?"
    "She doesn't respond, as expected."
    "I'm not even sure if she's still there."
    s "..."
    s "There's one location you keep coming from..."
    "Following my instincts, I head to that location."
    show bg mansion with wipeleft_scene
    s "What is this place?"
    "There's a pregnant woman sitting on the stairs at the front, looks like she's almost due."
    s "I hope for my sake that that's the storm in there."
    "I point to the woman's belly."
    "Suddenly, she reacts to her stomach, hard."
    "I think her water's about to break."
    "I decide to watch this unfold."
    with wipeleft_scene
    "She had twins."
    s "I knew it."
    s "One of those is the storm."
    s "..."
    "..."
    "I'm due in a few weeks."
    "I better go."
    return