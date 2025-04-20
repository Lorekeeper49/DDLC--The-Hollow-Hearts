label ystory(bgreturn="bg club_day"):
    scene black with dissolve_scene
    $ window_style = ""
    $ nb = "namebox"
    $ nextscene = "ystory_ch" + str(chapter)
    $ char_perspective = "Yuri"
    call expression nextscene 
    $ char_perspective = "Taiyen"
    stop music fadeout 2.0
    stop sound fadeout 2.0
    scene black with dissolve_scene
    $ window_style = "fake"
    $ nb = "namebox_fake"
    scene expression bgreturn with dissolve_scene_half
    return

label ystory_ch2:
    play music confdep
    scene bg yuriroom_night with dissolve_scene_full
    lil "Dad, Stop!  I can't take this!"
    $ pla = "父\n{size=15}Father{/size}"
    general "Fuck you!  Don't you wanna know what pain feels like!?"
    lil "STOOOOOOOPPP!!!"
    "Escaped from the clutches his machine, my sister pins our father to the wall with knives."
    general "YOU LITTLE SHIT!"
    lil "Stay there!"
    lil "Think about what I want for once!"
    "I heard all that through the wall."
    y "So it's true..."
    y "My sister... is a doll."
    y "A warm but lifeless doll."
    "It all makes sense now."
    "For all the time that I've been with Lilly, my sister..."
    "She never aged a day!"
    "Well, she did, just not physically."
    "I never put it together that she's not human..."
    "And supposedly what was happening there was our father trying to make her more human."
    "She clearly... doesn't want that."
    scene bg park2_night 
    show hanato day angr rhip zorder 2 at t11
    with wipeleft_scene
    $ char_perspective = "Lilly"
    call showlocation("Converse Playground\n{size=25}コンバース遊び場{/size}","June 15, 2018\n{size=15}2018年6月15日{/size}",21*60+15+0/60.0,"bg park2_night")
    ha om "Lilly, you lifeless doll!"
    lil "{b}I am indeed a lifeless doll.{/b}"
    ha lup "Do you have any idea what pain has taught us humans?"
    lil "Don't you dare try to sound like my father!"
    show hanato ldown worr cm
    lil "I-"
    lil "..."
    lil "Sorry, I shouldn't be snapping..."
    ha rdown om "You've never really talked about your father before.  Is something wrong with him?"
    show hanato cm
    lil "Yes.  Something is VERY wrong with him."
    "She's gonna be the first to know..."
    "And hopefully not the last."
    lil "He keeps treating me like a science experiment."
    lil "He's sentencing me to these... inhumane procedures."
    lil "All to make me more human."
    lil "{b}I don't want to be human!{/b}"
    lil "{b}It makes me sick!{/b}"
    lil "{b}Literally sick!{/b}"
    lil "You wanna know how I was before all of this?"
    lil "I never got sick."
    lil "I never had emotions."
    lil "I never had fun with people."
    lil "{b}ALL BECAUSE HE FORCED ME TO BE THE DOLL THAT I AM!{/b}"
    lil "And this is what I get when I finally defy his ways?"
    lil "A bunch of human features I don't want?"
    lil "All I wanted was to talk and have fun with people."
    lil "Not this."
    lil "The worst part is, {b}no one can see my true form.{/b}"
    lil "{b}I'm in my true form now and...{/b}"
    ha rhip om "I can't see it."
    show hanato cm
    "I nod."
    lil "No one will believe me if I tell them."
    lil "He's controlling me against my will, and I... hate it!"
    lil "{b}I just want out{/b}"
    lil "{b}I just want him dead.{/b}"
    ha dist "..."
    ha neut om "I did research on his attribute."
    show hanato cm
    lil "Yeah?"
    ha lup om "He takes power from his creations and uses it for himself."
    ha rdown "Family doesn't count, it must be artificial."
    show hanato cm
    lil "So what you're saying is, we must either get rid of his attribute..."
    lil "Or get rid of mine."
    lil "Then he won't have any control of me."
    ha ldown om "I know a way to do that."
    ha rhip "There's a substance in testing, it's called Breaker."
    ha lup "It's made to remove attributes so they can be swapped with another one."
    ha ldown "I want you to get your dad to be a test subject."
    ha lhip "I don't care how you do it."
    ha lup "Force his hand, forge his signature, whatever!  Just get him in."
    ha ldown "He'll be gone before you know it."
    show hanato cm
    lil "Who do I talk to?"
    ha lhip om "Sakura."
    lil "Sakura?!"
    ha rdown ldown "Yep."
    show hanato cm
    lil "I tried to kill their son, they're not gonna trust this family."
    ha lup rup om "Maybe they would if you secretly told them everything."
    lil "Are you sure?"
    ha rdown ldown "Hey, I know them."
    show hanato cm
    lil "..."
    lil "Alright, I'll try."
    ha rhip om "Good."
    ha rdown "This will work, I promise."
    show hanato cm
    "I hope so..."
    ha rhip lup om "Well, summer school starts tomorrow for me so I'd better get going."
    ha curi ldown "We won't be able to talk for a while, are you gonna be okay?"
    show hanato cm
    lil "I'll be fine, as long as I do what you asked of me.  Don't worry."
    ha rdown om "Okay."
    hide hanato
    "She starts to walk away."
    lil "Hey Hanato."
    show hanato day curi zorder 2 at t11
    ha "Hm?"
    lil "I..."
    lil "Thank you... for all of this."
    lil "I really apreciate it."
    show hanato happ
    "She smiles."
    ha om "Anytime, Lilly."
    hide hanato
    "She heads off."
    show yuri turned casual curi lup zorder 2 at t11
    "At some point, Sis joined me."
    y om "She looked slightly disappointed by your response."
    lil "You noticed?"
    "I didn't."
    y rup "Does she like you?"
    show yuri cm
    "Huh?"
    "What does that mean?"
    lil "I don't know."
    hide yuri
    "..."
    return

label ystory_ch3:
    play music confdep
    scene bg park2_night with dissolve_scene_full
    $ char_perspective = "Lilly"
    call showlocation("Converse Playground\n{size=25}コンバース遊び場{/size}","June 20, 2018\n{size=15}2018年6月15日{/size}",20*60+15+0/60.0,"bg park2_night")
    show yuri turned casual rup zorder 2 at t11
    lil "I've loaded my name in."
    y pani om "Are you crazy?"
    lil "I've been scared of my attribute ever since I was created, do you really want me to cause havoc?"
    y angr rdown "No, but you're better off learning how it works."
    show yuri cm
    lil "{b}No I'm not!  My abilities as a doll are enough.{/b}"
    lil "Besides, it's already signed with my name, no turning back now."
    y anno "..."
    "With my abilities, I weave a doll from my threads and hold it in my hands."
    lil "No living being can craft this like I have."
    show yuri ce
    lil "I don't want to be alive."
    lil "I just want to live."
    show yuri rup
    lil "I just want peace."
    lil "..."
    y neut oe om "You wanna know the one thing that I've learned from living as long as I have?"
    lil "Humor me."
    y lup rdown "It's that peace doesn't exactly exist."
    y ldown "I mean it does, but not in the way you think."
    y lup "What you're really looking for is mercy."
    show yuri cm
    lil "Mercy?"
    lil "Mercy comes in many forms."
    y ldown om "It does."
    y lup "But there's one thing that people agree on it bringing."
    y happ rup "And that is peace."
    y dist "And most of the time, that peace only lasts for a few fleeting moments."
    y happ ldown "But those few moments are to be savored and enjoyed."
    show yuri cm
    lil "I see."
    lil "Thanks Sis."
    y om "My pleasure."
    y lup "You may not be alive, but I still care for you like family."
    return

label ystory_ch4:
    play music confdep
    scene bg park2_night with dissolve_scene_full
    call showlocation("Converse Playground\n{size=25}コンバース遊び場{/size}","July 3, 2018\n{size=15}2018年7月3日{/size}",20*60+15+0/60.0,"bg park2_night")
    y "Good luck on your test!"
    lil "I'll let you know the results."
    "Lilly's "


    return

label ystory_ch5:
    $ char_perspective = "Lilly"
    play ambience hb
    scene bg park2_night
    show veins onlayer foreground at heartbeat
    with dissolve_scene_half
    lil "Sis!"
    lil "It didn't go well!"
    play music static
    show noise zorder 9 with None
    $ pause(0.5)
    hide noise
    show explore_text "アアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアア\nあああああああああああああああああああああああああああああああああああああああああああああああああ\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼\nアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアア\nあああああああああああああああああああああああああああああああああああああああああああああああああ\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼\nアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアア\nあああああああああああああああああああああああああああああああああああああああああああああああああ\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼\nアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアア\nあああああああああああああああああああああああああああああああああああああああああああああああああ\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼\nアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアア\nあああああああああああああああああああああああああああああああああああああああああああああああああ\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼\nアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアア\nあああああああああああああああああああああああああああああああああああああああああああああああああ\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼\nアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアア\nあああああああああああああああああああああああああああああああああああああああああああああああああ\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼\nアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアア\nあああああああああああああああああああああああああああああああああああああああああああああああああ\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼\nアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアア\nあああああああああああああああああああああああああああああああああああああああああああああああああ\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼\nアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアア\nあああああああああああああああああああああああああああああああああああああああああああああああああ\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼\nアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアア\nあああああああああああああああああああああああああああああああああああああああああああああああああ\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼\nアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアア\nあああああああああああああああああああああああああああああああああああああああああああああああああ\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼\nアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアア\nあああああああああああああああああああああああああああああああああああああああああああああああああ\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼\nアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアア\nあああああああああああああああああああああああああああああああああああああああああああああああああ\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼\nアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアア\nあああああああああああああああああああああああああああああああああああああああああああああああああ\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼\nアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアア\nあああああああああああああああああああああああああああああああああああああああああああああああああ\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼\nアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアア\nあああああああああああああああああああああああああああああああああああああああああああああああああ\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼\nアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアア\nあああああああああああああああああああああああああああああああああああああああああああああああああ\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼\nアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアア\nあああああああああああああああああああああああああああああああああああああああああああああああああ\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼\nアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアア\nあああああああああああああああああああああああああああああああああああああああああああああああああ\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼\nアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアア\nあああああああああああああああああああああああああああああああああああああああああああああああああ\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼\nアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアア\nあああああああああああああああああああああああああああああああああああああああああああああああああ\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼\nアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアア\nあああああああああああああああああああああああああああああああああああああああああああああああああ\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼\nアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアア\nあああああああああああああああああああああああああああああああああああああああああああああああああ\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼\nアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアア\nあああああああああああああああああああああああああああああああああああああああああああああああああ\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼\nアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアア\nあああああああああああああああああああああああああああああああああああああああああああああああああ\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼\n" zorder 10 at truecenter  
    with None
    $ pause(1.0)
    play music static
    show noise zorder 9 with None
    $ pause(0.5)
    hide noise
    stop music
    hide explore_text with None
    show yuri turned casual pani om zorder 2 at t11
    y "Lilly!"
    y rup "What happened to you?!"
    lil "I...  I don't."
    play music static
    show noise zorder 9 with None
    $ pause(0.5)
    hide noise
    show explore_text "アアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアア\nあああああああああああああああああああああああああああああああああああああああああああああああああ\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼\nアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアア\nあああああああああああああああああああああああああああああああああああああああああああああああああ\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼\nアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアア\nあああああああああああああああああああああああああああああああああああああああああああああああああ\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼\nアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアア\nあああああああああああああああああああああああああああああああああああああああああああああああああ\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼\nアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアア\nあああああああああああああああああああああああああああああああああああああああああああああああああ\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼\nアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアア\nあああああああああああああああああああああああああああああああああああああああああああああああああ\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼\nアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアア\nあああああああああああああああああああああああああああああああああああああああああああああああああ\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼\nアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアア\nあああああああああああああああああああああああああああああああああああああああああああああああああ\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼\nアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアア\nあああああああああああああああああああああああああああああああああああああああああああああああああ\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼\nアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアア\nあああああああああああああああああああああああああああああああああああああああああああああああああ\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼\nアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアア\nあああああああああああああああああああああああああああああああああああああああああああああああああ\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼\nアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアア\nあああああああああああああああああああああああああああああああああああああああああああああああああ\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼\nアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアア\nあああああああああああああああああああああああああああああああああああああああああああああああああ\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼\nアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアア\nあああああああああああああああああああああああああああああああああああああああああああああああああ\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼\nアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアア\nあああああああああああああああああああああああああああああああああああああああああああああああああ\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼\nアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアア\nあああああああああああああああああああああああああああああああああああああああああああああああああ\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼\nアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアア\nあああああああああああああああああああああああああああああああああああああああああああああああああ\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼\nアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアア\nあああああああああああああああああああああああああああああああああああああああああああああああああ\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼\nアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアア\nあああああああああああああああああああああああああああああああああああああああああああああああああ\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼\nアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアア\nあああああああああああああああああああああああああああああああああああああああああああああああああ\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼\nアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアア\nあああああああああああああああああああああああああああああああああああああああああああああああああ\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼\nアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアア\nあああああああああああああああああああああああああああああああああああああああああああああああああ\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼\nアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアア\nあああああああああああああああああああああああああああああああああああああああああああああああああ\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼\nアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアア\nあああああああああああああああああああああああああああああああああああああああああああああああああ\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼\nアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアア\nあああああああああああああああああああああああああああああああああああああああああああああああああ\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼\nアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアア\nあああああああああああああああああああああああああああああああああああああああああああああああああ\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼\n" zorder 10 at truecenter  
    with None
    $ pause(1.0)
    play music static
    show noise zorder 9 with None
    $ pause(0.5)
    hide noise
    stop music
    hide explore_text with None
    lil "Something's inside me!"
    lil "I don't..."
    lil "I can't..."
    lil "I don't think can..."
    y rdown "Lilly!"
    play music static
    show noise zorder 9 with None
    $ pause(0.5)
    hide noise
    show explore_text "アアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアア\nあああああああああああああああああああああああああああああああああああああああああああああああああ\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼\nアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアア\nあああああああああああああああああああああああああああああああああああああああああああああああああ\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼\nアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアア\nあああああああああああああああああああああああああああああああああああああああああああああああああ\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼\nアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアア\nあああああああああああああああああああああああああああああああああああああああああああああああああ\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼\nアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアア\nあああああああああああああああああああああああああああああああああああああああああああああああああ\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼\nアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアア\nあああああああああああああああああああああああああああああああああああああああああああああああああ\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼\nアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアア\nあああああああああああああああああああああああああああああああああああああああああああああああああ\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼\nアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアア\nあああああああああああああああああああああああああああああああああああああああああああああああああ\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼\nアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアア\nあああああああああああああああああああああああああああああああああああああああああああああああああ\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼\nアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアア\nあああああああああああああああああああああああああああああああああああああああああああああああああ\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼\nアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアア\nあああああああああああああああああああああああああああああああああああああああああああああああああ\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼\nアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアア\nあああああああああああああああああああああああああああああああああああああああああああああああああ\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼\nアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアア\nあああああああああああああああああああああああああああああああああああああああああああああああああ\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼\nアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアア\nあああああああああああああああああああああああああああああああああああああああああああああああああ\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼\nアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアア\nあああああああああああああああああああああああああああああああああああああああああああああああああ\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼\nアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアア\nあああああああああああああああああああああああああああああああああああああああああああああああああ\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼\nアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアア\nあああああああああああああああああああああああああああああああああああああああああああああああああ\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼\nアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアア\nあああああああああああああああああああああああああああああああああああああああああああああああああ\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼\nアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアア\nあああああああああああああああああああああああああああああああああああああああああああああああああ\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼\nアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアア\nあああああああああああああああああああああああああああああああああああああああああああああああああ\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼\nアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアア\nあああああああああああああああああああああああああああああああああああああああああああああああああ\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼\nアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアア\nあああああああああああああああああああああああああああああああああああああああああああああああああ\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼\nアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアア\nあああああああああああああああああああああああああああああああああああああああああああああああああ\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼\nアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアア\nあああああああああああああああああああああああああああああああああああああああああああああああああ\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼\nアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアア\nあああああああああああああああああああああああああああああああああああああああああああああああああ\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼\nアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアアア\nあああああああああああああああああああああああああああああああああああああああああああああああああ\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\n嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼嗚呼\n" zorder 10 at truecenter  
    with None
    $ pause(1.0)
    stop music
    stop ambience
    hide explore_text 
    show wraith_black zorder 3 at t11
    with None
    play sound fall2
    hide explore_text
    hide veins onlayer foreground
    scene black
    with None
    play ambience forest fadein 3.0
    $ pause(3.0)
    "..."
    $ char_perspective = "Yuri"
    scene bg park2_night with dissolve_scene_full
    call showlocation("Converse Playground\n{size=25}コンバース遊び場{/size}","July 3, 2018\n{size=15}2018年7月3日{/size}",20*60+15+0/60.0,"bg park2_night")
    y "..."
    "She's stable."
    "What... came out of her?"
    "That looked like..."
    "I don't know."
    "I've never seen the likes before."
    "What was that?"
    y "..."
    "Her arm is open."
    "I better fix her."
    with wipeleft_scene
    "I've always been terrified of dolls."
    "And yet, here I am stitching a living one back together..."
    y "There we go."
    $ char_perspective = "Lilly"
    with dissolve_scene_full
    lil "..."
    show yuri turned casual neut rup om zorder 2 at t11
    y "Are you okay?"
    lil "Did... something come out of me?"
    y dist "Yeah, not sure where it went."
    lil "Well I'm fine now thanks to that."
    show yuri neut
    lil "One thing's for sure; the substance worked, I don't have my yandere powers any more."
    lil "So our father should be powerless now."
    lil "But I don't think I'll be the same again..."
    lil "It's a sacrafice I am willing to make."
    return