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
    scene bg yuriroom_night with dissolve_scene_half
    #call showlocation("?????? House","Monday, August 1, 2020",23,59,57)
    lil "Dad, Stop!  I can't take this!"
    $ pla = "Father"
    general "Fuck you!  Don't you wanna know what pain feels like!?"
    lil "STOOOOOOOPPP!!!"
    "Escaped from the clutches his machine, my sister pins our father to the wall with knives."
    general "YOU LITTLE SHIT!"
    lil "Stay there!"
    lil "Think about what I want for once!"

    $ char_perspective = "Lilly"
    ha "Lilly, you lifeless doll!"
    lil "I am indeed a lifeless doll."
    ha "Do you have any idea what pain has taught us humans?"
    lil "Don't you dare try to sound like my father!"
    lil "I-"
    lil "..."
    lil "Sorry, I shouldn't be snapping..."
    ha "You've never really talked about your father before.  Is something wrong with him?"
    lil "Yes.  Something is VERY wrong with him."
    "She's gonna be the first to know..."
    "And hopefully not the last."
    lil "He keeps treating me like a science experiment."
    lil "He's sentencing me to these... inhumane procedures."
    lil "All to make me more human."
    lil "I don't want to be human!"
    lil "It makes me sick!"
    lil "Literally sick!"
    lil "You wanna know how I was before all of this?"
    lil "I never got sick."
    lil "I never had emotions."
    lil "I never had fun with people."
    lil "ALL BECAUSE HE FORCED ME TO ACT LIKE THE DOLL THAT I AM!"
    lil "And this is what I get when I finally defy his ways?"
    lil "A bunch of human features I don't want?"
    lil "All I wanted was to talk and have fun with people."
    lil "Not this."
    lil "The worst part is, no one can see my true form."
    lil "I'm in my true form right now and..."
    ha "I can't see it."
    "I nod."
    lil "No one will believe me if I tell them."
    lil "He's controlling me against my will, and I... hate it!"
    lil "I just want out."
    lil "I just want him dead."
    ha "..."
    ha "I did research on his attribute."
    lil "Yeah?"
    ha "He takes power from his creations and uses it for himself."
    ha "Family doesn't count, it must be artificial."
    lil "So what you're saying is, we must either get rid of his attribute..."
    lil "Or get rid of mine."
    lil "Then he won't have any control of me."
    ha "I know a way to do that."
    ha "There's a substance in testing, it's called Breaker."
    ha "It's made to remove attributes so they can be swapped with another one."
    ha "I want you to get your dad to be a test subject."
    ha "I don't care how you do it."
    ha "Force his hand, forge his signature, whatever!  Just get him in."
    ha "He'll be gone before you know it."
    lil "Who do I talk to?"
    ha "Sakura."
    lil "Sakura?!"
    ha "Yep."
    lil "I tried to kill their son, they're not gonna trust this family."
    ha "Maybe they would if you secretly told them everything."
    lil "Are you sure?"
    ha "Hey, I know them."
    lil "..."
    lil "Alright, I'll try."
    ha "Good."
    ha "This will work, I promise."
    "I hope so..."
    ha "Well, summer school starts tomorrow for me so I'd better get going."
    ha "We won't be able to talk for a while, are you gonna be okay?"
    lil "I'll be fine, as long as I do what you asked of me.  Don't worry."
    ha "Okay."
    "She starts to walk away."
    lil "Hey Hanato."
    ha "Hm?"
    lil "I..."
    lil "Thank you... for all of this."
    lil "I really apreciate it."
    "She smiles."
    ha "Anytime, Lilly."
    "She heads off."
    y "She looked slightly disappointed by your response."
    lil "You noticed?"
    "I didn't."
    y "Does she like you?"
    lil "I-"
    "Huh?"
    "What does that mean?"
    lil "I don't know."
    "..."
    return

label ystory_ch3:
    call showlocation("???","Monday, August 1, 2020",23,59,57)

    return

label ystory_ch4:
    call showlocation("???","Monday, August 1, 2020",23,59,57)

    return

label ystory_ch5:
    call showlocation("???","Monday, August 1, 2020",23,59,57)

    return