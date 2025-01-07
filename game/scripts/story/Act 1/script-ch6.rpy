label act1_ch6_main:
    stop music fadeout 2.0
    scene bg gym
    with dissolve_scene_full
    play ambience storm
    $ renpy.music.set_volume(0.3, delay=0, channel="ambience")
    $ style.say_window = style.window
    $ nb = "namebox"
    call showlocation("Sakura Academy Gym\n{size=25}桜学園高校のジム{/size}","October 4, 2023\n{size=15}2023年10月4日{/size}",6*60+0+0/60.0,"bg gym")
    t "If you thought I am about to fall in love..."
    t "I am not."
    t "If you thought I am about to make relationships..."
    t "I am not."
    t "If you thought I am about to find happiness..."
    t "I am not."
    t "The thing is, I will never be happy."
    t "Not with the failed experiment still asking for death..."
    t "In more ways than one, mind you."
    t "The past is not dead."
    t "The past will never be dead."
    t "Not like this."
    t "Sometimes I wonder who he would've been..."
    t "Sometimes I wonder how the times would've changed..."
    t "If the experiment never happened..."
    t "Things would've been better."
    t "But it wasn't meant to be."
    t "We tried... without knowing the inevitable consequences."
    t "The changes these once beloved friendly people would undergo!"
    t "Only one saw benefit from it..."
    t "And she's not even human..."
    t "...and we didn't know that at the time."
    t "The others..."
    t "The ones who weren't tested on..."
    t "They unfortunately have to suffer the consequences."
    t "And the ones who were never considered to participate..."
    t "They might be in danger as we speak."
    t "And it's all..."
    t "...our fault!"
    t "It is all..."
    t "...the fault of the Sakura family."
    t "The same family you all chose to idolize within this very school!"
    t "The same family who's oldest were murdered..."
    t "...by their own experiment."
    t "You all have probably heard this same dump of sudden information before."
    t "Certain confessions that lead up to certain incidents."
    t "Unlike the most referenced ones of those, I will not be comitting suicide to essentially 'avoid the problem'."
    t "You all can save your gently opened doors for another idol in your life."
    t "For I choose to slam those very doors open and try to fix the problem however I can."
    t "But I'm gonna need your help."
    t "He's grown to powerful for anyone to handle on they're own."
    t "And when he comes stomping..."
    t "You better be ready for a fight you can't escape."
    t "Your life is on the line whether you like it or not!"
    t "I hope you all understand that."
    t "I don't know what's going to happen..."
    t "But I do know this:"
    t "He is coming!"
    t "And he needs death!"
    stop ambience fadeout 1.0
    $ renpy.music.set_volume(1.0, delay=0, channel="ambience")
    achieve act1fin
    return