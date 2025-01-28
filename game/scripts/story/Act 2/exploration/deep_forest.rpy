label shed:
    scene bg shed_night with Fade(0.25, 0.0, 0.25)
    show dominion zorder 2 at t11
    a "Dominion!"
    a "Found you!"
    stop jump0 fadeout 1.0
    stop jump1 fadeout 1.0
    stop jump2 fadeout 1.0
    stop jump3 fadeout 1.0
    stop jump4 fadeout 1.0
    stop jump5 fadeout 1.0
    stop jump6 fadeout 1.0
    stop jump7 fadeout 1.0
    stop jump8 fadeout 1.0
    stop jump9 fadeout 1.0
    stop jump10 fadeout 1.0
    stop jump11 fadeout 1.0
    stop jump12 fadeout 1.0
    stop jump13 fadeout 1.0
    stop jump14 fadeout 1.0
    stop jump15 fadeout 1.0
    scene bg shed_night with dissolve_scene_full
    call showlocation("Abandoned Shed\n{size=25}放置された小屋{/size}","October 10, 2023\n{size=15}2023年10月10日{/size}",1*60+59+57/60.0,"bg shed")
    show dominion zorder 2 at t11
    call showintro(intro_d)
    d "..."
    d "!!!"
    d "Who are you people?"
    a "Dominion!  Dominion!  Calm down!  These are my new friends."
    d "Aoruguri?"
    d "Get away from me!  I'm not safe!"
    a "We saw.  You're okay."
    a "These people live for danger."
    d "Tch!  Some daredevils, huh?"
    show dominion at t21
    show kotonoha turned casual anno rhip ce om zorder 2 at r22
    k "I can assure you, we are not-"
    a "Just face it.  With the amount of dangers you guys throw yourselves into, you might as well take the name."
    k oe lup "You say that as a member of us."
    show kotonoha cm
    a "I'll just shut my fucking mouth then!"
    k angr ldown om "No, you're the only one who can talk to him properly."
    show kotonoha cm
    a "Then keep him from getting out!"
    k rdown om "Copy that."
    show kotonoha cm at rhide
    hide kotonoha
    show dominion at t11
    d "Seriously!  You should get out of here!  I could end up killing you!"
    "Hm.  Seems like talking to him will be more difficult than usual."
    "How should I go about this?"
    call dominion_loop
    a "Let's get out of here!"
    return

default dom_calm = False
default dom_stress = False
default dom_rage = False
default calm = 0
default stress = 0
label dominion_loop:
    menu:
        "Convince him to calm down" if not dom_calm:
            $ dom_calm = True
            call dom_com
        "Stress him to face it" if not dom_stress:
            $ dom_stress = True
            call dom_stress
        "Tell him his abilities straight":
            jump dom_ab
        "Give up on him":
            a "I give up!"
            return
    if calm >= 3 and stress < calm:
        d "Okay, I'm calm.  I'm calm."
        a "You good?"
        d "Yeah, I'm good."
        d "I'll head back to the school in a bit."
        a "Okay."
        a "Whew."
        return
    elif stress >= 3 and calm > stress:
        d "*Stuttered Breath*"
        d monstertrans "AAAAAAAAAAAAAAAAHHHHH!!!"
        a "Shit!"
        jump dom_burst
    elif dom_rage:
        return
    jump dominion_loop

default Comforting = False
default Stressful = False
default Direct = False
default Vague = False
default Smart = False
default Stupid = False
default Angry = False
default Happy = False
label dom_com:
    menu:
        "Be Comforting" if not Comforting:
            $ Comforting = True
            $ calm += 1

        "Be Stressful" if not Stressful:
            $ Stressful = True
            $ stress += 1

        "Be Direct" if not Direct:
            $ Direct = True
            $ calm += 1

        "Be Vague" if not Vague:
            $ Vague = True
            $ stress += 1

        "Be Smart" if not Smart:
            $ Smart = True
            $ calm += 1

        "Be Stupid" if not Stupid:
            $ Stupid = True
            $ stress += 1

        "Be Angry" if not Angry:
            $ Angry = True
            $ stress += 1

        "Be Happy" if not Happy:
            $ Happy = True
            $ calm += 1

        "Stop convincing him":
            "Let's stop here."
            return
    jump dom_com

label dom_stress:
    $ stress += 2
    a "How about you just face it?"
    d "Huh?"
    a "What?  You could learn how it works."
    a "Or are you gonna be a fucking crybaby about potentially killing us?"
    menu:
        "Stress him to face it":
            pass
        "Stop":
            a "Sorry, I'll stop."
            "Let's try something else."
            return
    a "I'm being serious here!"
    a "You won't be able to fight if you don't face it!"
    d "You can't hold back that power!"
    a "You really sure about that?"
    a "We can prove you wrong."
    menu:
        "Stress him!":
            pass
        "Stop":
            a "Sorry, I'll stop."
            "Let's try something else."
            return
    d "I don't know what to-"
    a "You're already a dick."
    a "BUT YOU'LL BE EVEN MORE OF A DICK IF YOU DON'T FUCK THAT POWER!"
    menu:
        "Face it!":
            pass
        "Stop":
            a "Sorry, I'll stop."
            "Let's try something else."
            return
    a "Just ass up and face it!"
    a "Or are you gonna be a coward like me?"
    d "I can't-"
    a "JUST FUCKING SHOW IT TO US!!"
    menu:
        "FACE IT!":
            pass
        "Stop":
            a "Sorry, I'll stop."
            "Let's try something else."
            return
    a "SHOW IT TO US!!!"
    d monstertrans "AAAAAAAAAAAAAAAAHHHHH!!!"
    a "Well that worked."
    jump dom_burst

label dom_ab:

    return

label dom_burst:
    $ dom_rage = True
    #INSERT EPIC BATTLE CUTSCENE ANIMATED TO My Demons BY Starset
    show kotonoha turned casual angr zorder 3 at l31
    a "Kotonoha!  Lock on his mind!"
    k om "Got it!"
    show kotonoha cm
    show akira uniform cross d zorder 3 at r33
    a "Akira!  Weaken him!"
    ak "On it!"
    show kotonoha at t31
    show akira at t33
    hide kotonoha
    hide akira
    show tina turned angr lhip rhip zorder 3 at t11
    ti om "Who put you in charge?!"
    show tina cm
    a "We don't have time for aggresive chatter!  This is life or death!  Make sure no one gets near!"
    ti cross "..."
    hide tina
    show lilly casual norm se zorder 3 at t11
    a "Lilly?"
    lil "Yes?"
    a "Use your true form and help me out!"
    show lilly doll a0 with blink
    lil "You got it!"

    return

label no_shed:
    a "Shit!"
    a "This is taking too long."
    a "We should head back."
    a "He's probably already gone anyway."
    stop jump0 fadeout 1.0
    stop jump1 fadeout 1.0
    stop jump2 fadeout 1.0
    stop jump3 fadeout 1.0
    stop jump4 fadeout 1.0
    stop jump5 fadeout 1.0
    stop jump6 fadeout 1.0
    stop jump7 fadeout 1.0
    stop jump8 fadeout 1.0
    stop jump9 fadeout 1.0
    stop jump10 fadeout 1.0
    stop jump11 fadeout 1.0
    stop jump12 fadeout 1.0
    stop jump13 fadeout 1.0
    stop jump14 fadeout 1.0
    stop jump15 fadeout 1.0
    return

default blocked_directions = { # randomized each run
    "0_0": {"north": False, "south": True, "east": False, "west": True},
    "1_0": {"north": False, "south": True, "east": False, "west": False},
    "2_0": {"north": False, "south": True, "east": False, "west": False},
    "3_0": {"north": False, "south": True, "east": False, "west": False},
    "4_0": {"north": False, "south": True, "east": False, "west": False},
    "5_0": {"north": False, "south": True, "east": False, "west": False},
    "6_0": {"north": False, "south": True, "east": False, "west": False},
    "7_0": {"north": False, "south": True, "east": False, "west": False},
    "8_0": {"north": False, "south": True, "east": False, "west": False},
    "9_0": {"north": False, "south": True, "east": True, "west": False},
    "0_1": {"north": False, "south": False, "east": False, "west": True},
    "1_1": {"north": False, "south": False, "east": False, "west": False},
    "2_1": {"north": False, "south": False, "east": False, "west": False},
    "3_1": {"north": False, "south": False, "east": False, "west": False},
    "4_1": {"north": False, "south": False, "east": False, "west": False},
    "5_1": {"north": False, "south": False, "east": False, "west": False},
    "6_1": {"north": False, "south": False, "east": False, "west": False},
    "7_1": {"north": False, "south": False, "east": False, "west": False},
    "8_1": {"north": False, "south": False, "east": False, "west": False},
    "9_1": {"north": False, "south": False, "east": True, "west": False},
    "0_2": {"north": False, "south": False, "east": False, "west": True},
    "1_2": {"north": False, "south": False, "east": False, "west": False},
    "2_2": {"north": False, "south": False, "east": False, "west": False},
    "3_2": {"north": False, "south": False, "east": False, "west": False},
    "4_2": {"north": False, "south": False, "east": False, "west": False},
    "5_2": {"north": False, "south": False, "east": False, "west": False},
    "6_2": {"north": False, "south": False, "east": False, "west": False},
    "7_2": {"north": False, "south": False, "east": False, "west": False},
    "8_2": {"north": False, "south": False, "east": False, "west": False},
    "9_2": {"north": False, "south": False, "east": True, "west": False},
    "0_3": {"north": False, "south": False, "east": False, "west": True},
    "1_3": {"north": False, "south": False, "east": False, "west": False},
    "2_3": {"north": False, "south": False, "east": False, "west": False},
    "3_3": {"north": False, "south": False, "east": False, "west": False},
    "4_3": {"north": False, "south": False, "east": False, "west": False},
    "5_3": {"north": False, "south": False, "east": False, "west": False},
    "6_3": {"north": False, "south": False, "east": False, "west": False},
    "7_3": {"north": False, "south": False, "east": False, "west": False},
    "8_3": {"north": False, "south": False, "east": False, "west": False},
    "9_3": {"north": False, "south": False, "east": True, "west": False},
    "0_4": {"north": False, "south": False, "east": False, "west": True},
    "1_4": {"north": False, "south": False, "east": False, "west": False},
    "2_4": {"north": False, "south": False, "east": False, "west": False},
    "3_4": {"north": False, "south": False, "east": False, "west": False},
    "4_4": {"north": False, "south": False, "east": False, "west": False},
    "5_4": {"north": False, "south": False, "east": False, "west": False},
    "6_4": {"north": False, "south": False, "east": False, "west": False},
    "7_4": {"north": False, "south": False, "east": False, "west": False},
    "8_4": {"north": False, "south": False, "east": False, "west": False},
    "9_4": {"north": False, "south": False, "east": True, "west": False},
    "0_5": {"north": False, "south": False, "east": False, "west": True},
    "1_5": {"north": False, "south": False, "east": False, "west": False},
    "2_5": {"north": False, "south": False, "east": False, "west": False},
    "3_5": {"north": False, "south": False, "east": False, "west": False},
    "4_5": {"north": False, "south": False, "east": False, "west": False},
    "5_5": {"north": False, "south": False, "east": False, "west": False},
    "6_5": {"north": False, "south": False, "east": False, "west": False},
    "7_5": {"north": False, "south": False, "east": False, "west": False},
    "8_5": {"north": False, "south": False, "east": False, "west": False},
    "9_5": {"north": False, "south": False, "east": True, "west": False},
    "0_6": {"north": False, "south": False, "east": False, "west": True},
    "1_6": {"north": False, "south": False, "east": False, "west": False},
    "2_6": {"north": False, "south": False, "east": False, "west": False},
    "3_6": {"north": False, "south": False, "east": False, "west": False},
    "4_6": {"north": False, "south": False, "east": False, "west": False},
    "5_6": {"north": False, "south": False, "east": False, "west": False},
    "6_6": {"north": False, "south": False, "east": False, "west": False},
    "7_6": {"north": False, "south": False, "east": False, "west": False},
    "8_6": {"north": False, "south": False, "east": False, "west": False},
    "9_6": {"north": False, "south": False, "east": True, "west": False},
    "0_7": {"north": False, "south": False, "east": False, "west": True},
    "1_7": {"north": False, "south": False, "east": False, "west": False},
    "2_7": {"north": False, "south": False, "east": False, "west": False},
    "3_7": {"north": False, "south": False, "east": False, "west": False},
    "4_7": {"north": False, "south": False, "east": False, "west": False},
    "5_7": {"north": False, "south": False, "east": False, "west": False},
    "6_7": {"north": False, "south": False, "east": False, "west": False},
    "7_7": {"north": False, "south": False, "east": False, "west": False},
    "8_7": {"north": False, "south": False, "east": False, "west": False},
    "9_7": {"north": False, "south": False, "east": True, "west": False},
    "0_8": {"north": False, "south": False, "east": False, "west": True},
    "1_8": {"north": False, "south": False, "east": False, "west": False},
    "2_8": {"north": False, "south": False, "east": False, "west": False},
    "3_8": {"north": False, "south": False, "east": False, "west": False},
    "4_8": {"north": False, "south": False, "east": False, "west": False},
    "5_8": {"north": False, "south": False, "east": False, "west": False},
    "6_8": {"north": False, "south": False, "east": False, "west": False},
    "7_8": {"north": False, "south": False, "east": False, "west": False},
    "8_8": {"north": False, "south": False, "east": False, "west": False},
    "9_8": {"north": False, "south": False, "east": True, "west": False},
    "0_9": {"north": True, "south": False, "east": False, "west": True},
    "1_9": {"north": True, "south": False, "east": False, "west": False},
    "2_9": {"north": True, "south": False, "east": False, "west": False},
    "3_9": {"north": True, "south": False, "east": False, "west": False},
    "4_9": {"north": True, "south": False, "east": False, "west": False},
    "5_9": {"north": True, "south": False, "east": False, "west": False},
    "6_9": {"north": True, "south": False, "east": False, "west": False},
    "7_9": {"north": True, "south": False, "east": False, "west": False},
    "8_9": {"north": True, "south": False, "east": False, "west": False},
    "9_9": {"north": True, "south": False, "east": True, "west": False}
}

init python:
    def randomize_blockages():
        for coords in blocked_directions:
            for direction in blocked_directions[coords]:
                if not blocked_directions[coords][direction]:
                    blocked_directions[coords][direction] = random_chance(25)
    def reset_blockages():
        blocked_directions = {
            "0_0": {"north": False, "south": True, "east": False, "west": True},
            "1_0": {"north": False, "south": True, "east": False, "west": False},
            "2_0": {"north": False, "south": True, "east": False, "west": False},
            "3_0": {"north": False, "south": True, "east": False, "west": False},
            "4_0": {"north": False, "south": True, "east": False, "west": False},
            "5_0": {"north": False, "south": True, "east": False, "west": False},
            "6_0": {"north": False, "south": True, "east": False, "west": False},
            "7_0": {"north": False, "south": True, "east": False, "west": False},
            "8_0": {"north": False, "south": True, "east": False, "west": False},
            "9_0": {"north": False, "south": True, "east": True, "west": False},
            "0_1": {"north": False, "south": False, "east": False, "west": True},
            "1_1": {"north": False, "south": False, "east": False, "west": False},
            "2_1": {"north": False, "south": False, "east": False, "west": False},
            "3_1": {"north": False, "south": False, "east": False, "west": False},
            "4_1": {"north": False, "south": False, "east": False, "west": False},
            "5_1": {"north": False, "south": False, "east": False, "west": False},
            "6_1": {"north": False, "south": False, "east": False, "west": False},
            "7_1": {"north": False, "south": False, "east": False, "west": False},
            "8_1": {"north": False, "south": False, "east": False, "west": False},
            "9_1": {"north": False, "south": False, "east": True, "west": False},
            "0_2": {"north": False, "south": False, "east": False, "west": True},
            "1_2": {"north": False, "south": False, "east": False, "west": False},
            "2_2": {"north": False, "south": False, "east": False, "west": False},
            "3_2": {"north": False, "south": False, "east": False, "west": False},
            "4_2": {"north": False, "south": False, "east": False, "west": False},
            "5_2": {"north": False, "south": False, "east": False, "west": False},
            "6_2": {"north": False, "south": False, "east": False, "west": False},
            "7_2": {"north": False, "south": False, "east": False, "west": False},
            "8_2": {"north": False, "south": False, "east": False, "west": False},
            "9_2": {"north": False, "south": False, "east": True, "west": False},
            "0_3": {"north": False, "south": False, "east": False, "west": True},
            "1_3": {"north": False, "south": False, "east": False, "west": False},
            "2_3": {"north": False, "south": False, "east": False, "west": False},
            "3_3": {"north": False, "south": False, "east": False, "west": False},
            "4_3": {"north": False, "south": False, "east": False, "west": False},
            "5_3": {"north": False, "south": False, "east": False, "west": False},
            "6_3": {"north": False, "south": False, "east": False, "west": False},
            "7_3": {"north": False, "south": False, "east": False, "west": False},
            "8_3": {"north": False, "south": False, "east": False, "west": False},
            "9_3": {"north": False, "south": False, "east": True, "west": False},
            "0_4": {"north": False, "south": False, "east": False, "west": True},
            "1_4": {"north": False, "south": False, "east": False, "west": False},
            "2_4": {"north": False, "south": False, "east": False, "west": False},
            "3_4": {"north": False, "south": False, "east": False, "west": False},
            "4_4": {"north": False, "south": False, "east": False, "west": False},
            "5_4": {"north": False, "south": False, "east": False, "west": False},
            "6_4": {"north": False, "south": False, "east": False, "west": False},
            "7_4": {"north": False, "south": False, "east": False, "west": False},
            "8_4": {"north": False, "south": False, "east": False, "west": False},
            "9_4": {"north": False, "south": False, "east": True, "west": False},
            "0_5": {"north": False, "south": False, "east": False, "west": True},
            "1_5": {"north": False, "south": False, "east": False, "west": False},
            "2_5": {"north": False, "south": False, "east": False, "west": False},
            "3_5": {"north": False, "south": False, "east": False, "west": False},
            "4_5": {"north": False, "south": False, "east": False, "west": False},
            "5_5": {"north": False, "south": False, "east": False, "west": False},
            "6_5": {"north": False, "south": False, "east": False, "west": False},
            "7_5": {"north": False, "south": False, "east": False, "west": False},
            "8_5": {"north": False, "south": False, "east": False, "west": False},
            "9_5": {"north": False, "south": False, "east": True, "west": False},
            "0_6": {"north": False, "south": False, "east": False, "west": True},
            "1_6": {"north": False, "south": False, "east": False, "west": False},
            "2_6": {"north": False, "south": False, "east": False, "west": False},
            "3_6": {"north": False, "south": False, "east": False, "west": False},
            "4_6": {"north": False, "south": False, "east": False, "west": False},
            "5_6": {"north": False, "south": False, "east": False, "west": False},
            "6_6": {"north": False, "south": False, "east": False, "west": False},
            "7_6": {"north": False, "south": False, "east": False, "west": False},
            "8_6": {"north": False, "south": False, "east": False, "west": False},
            "9_6": {"north": False, "south": False, "east": True, "west": False},
            "0_7": {"north": False, "south": False, "east": False, "west": True},
            "1_7": {"north": False, "south": False, "east": False, "west": False},
            "2_7": {"north": False, "south": False, "east": False, "west": False},
            "3_7": {"north": False, "south": False, "east": False, "west": False},
            "4_7": {"north": False, "south": False, "east": False, "west": False},
            "5_7": {"north": False, "south": False, "east": False, "west": False},
            "6_7": {"north": False, "south": False, "east": False, "west": False},
            "7_7": {"north": False, "south": False, "east": False, "west": False},
            "8_7": {"north": False, "south": False, "east": False, "west": False},
            "9_7": {"north": False, "south": False, "east": True, "west": False},
            "0_8": {"north": False, "south": False, "east": False, "west": True},
            "1_8": {"north": False, "south": False, "east": False, "west": False},
            "2_8": {"north": False, "south": False, "east": False, "west": False},
            "3_8": {"north": False, "south": False, "east": False, "west": False},
            "4_8": {"north": False, "south": False, "east": False, "west": False},
            "5_8": {"north": False, "south": False, "east": False, "west": False},
            "6_8": {"north": False, "south": False, "east": False, "west": False},
            "7_8": {"north": False, "south": False, "east": False, "west": False},
            "8_8": {"north": False, "south": False, "east": False, "west": False},
            "9_8": {"north": False, "south": False, "east": True, "west": False},
            "0_9": {"north": True, "south": False, "east": False, "west": True},
            "1_9": {"north": True, "south": False, "east": False, "west": False},
            "2_9": {"north": True, "south": False, "east": False, "west": False},
            "3_9": {"north": True, "south": False, "east": False, "west": False},
            "4_9": {"north": True, "south": False, "east": False, "west": False},
            "5_9": {"north": True, "south": False, "east": False, "west": False},
            "6_9": {"north": True, "south": False, "east": False, "west": False},
            "7_9": {"north": True, "south": False, "east": False, "west": False},
            "8_9": {"north": True, "south": False, "east": False, "west": False},
            "9_9": {"north": True, "south": False, "east": True, "west": False}
        }

screen deep_forest_coords:
    style_prefix "explore"
    if not blocked_directions["1_1"]["north"]:
        button xcenter 740 ycenter 360 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_next", j=True)]
        text "北\nNORTH" xcenter 740 ycenter 360
    if not blocked_directions["1_1"]["west"]:
        button xcenter 240 ycenter 260 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_next", j=True)]
        text "西\nWEST" xcenter 240 ycenter 260
    if not blocked_directions["1_1"]["east"]:
        button xcenter 1140 ycenter 460 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_next", j=True)]
        text "東\nEAST" xcenter 1140 ycenter 460
    if not blocked_directions["1_1"]["south"]:
        button xcenter 640 ycenter 680 xysize (1280, 100) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_next", j=True)]
        text "南\nSOUTH" xcenter 640 ycenter 680

screen deep_forest_0_0:
    style_prefix "explore"
    if not blocked_directions["0_0"]["north"]:
        button xcenter 740 ycenter 360 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_0_1", j=True)]
        text "北\nNORTH" xcenter 740 ycenter 360
    if not blocked_directions["0_0"]["west"]:
        button xcenter 240 ycenter 260 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_-1_0", j=True)]
        text "西\nWEST" xcenter 240 ycenter 260
    if not blocked_directions["0_0"]["east"]:
        button xcenter 1140 ycenter 460 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_1_0", j=True)]
        text "東\nEAST" xcenter 1140 ycenter 460
    if not blocked_directions["0_0"]["south"]:
        button xcenter 640 ycenter 680 xysize (1280, 100) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_0_-1", j=True)]
        text "南\nSOUTH" xcenter 640 ycenter 680

screen deep_forest_0_1:
    style_prefix "explore"
    if not blocked_directions["0_1"]["north"]:
        button xcenter 740 ycenter 360 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_0_2", j=True)]
        text "北\nNORTH" xcenter 740 ycenter 360
    if not blocked_directions["0_1"]["west"]:
        button xcenter 240 ycenter 260 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_-1_1", j=True)]
        text "西\nWEST" xcenter 240 ycenter 260
    if not blocked_directions["0_1"]["east"]:
        button xcenter 1140 ycenter 460 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_1_1", j=True)]
        text "東\nEAST" xcenter 1140 ycenter 460
    if not blocked_directions["0_1"]["south"]:
        button xcenter 640 ycenter 680 xysize (1280, 100) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_0_0", j=True)]
        text "南\nSOUTH" xcenter 640 ycenter 680

screen deep_forest_0_2:
    style_prefix "explore"
    if not blocked_directions["0_2"]["north"]:
        button xcenter 740 ycenter 360 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_0_3", j=True)]
        text "北\nNORTH" xcenter 740 ycenter 360
    if not blocked_directions["0_2"]["west"]:
        button xcenter 240 ycenter 260 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_-1_2", j=True)]
        text "西\nWEST" xcenter 240 ycenter 260
    if not blocked_directions["0_2"]["east"]:
        button xcenter 1140 ycenter 460 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_1_2", j=True)]
        text "東\nEAST" xcenter 1140 ycenter 460
    if not blocked_directions["0_2"]["south"]:
        button xcenter 640 ycenter 680 xysize (1280, 100) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_0_1", j=True)]
        text "南\nSOUTH" xcenter 640 ycenter 680

screen deep_forest_0_3:
    style_prefix "explore"
    if not blocked_directions["0_3"]["north"]:
        button xcenter 740 ycenter 360 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_0_4", j=True)]
        text "北\nNORTH" xcenter 740 ycenter 360
    if not blocked_directions["0_3"]["west"]:
        button xcenter 240 ycenter 260 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_-1_3", j=True)]
        text "西\nWEST" xcenter 240 ycenter 260
    if not blocked_directions["0_3"]["east"]:
        button xcenter 1140 ycenter 460 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_1_3", j=True)]
        text "東\nEAST" xcenter 1140 ycenter 460
    if not blocked_directions["0_3"]["south"]:
        button xcenter 640 ycenter 680 xysize (1280, 100) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_0_2", j=True)]
        text "南\nSOUTH" xcenter 640 ycenter 680

screen deep_forest_0_4:
    style_prefix "explore"
    if not blocked_directions["0_4"]["north"]:
        button xcenter 740 ycenter 360 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_0_5", j=True)]
        text "北\nNORTH" xcenter 740 ycenter 360
    if not blocked_directions["0_4"]["west"]:
        button xcenter 240 ycenter 260 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_-1_4", j=True)]
        text "西\nWEST" xcenter 240 ycenter 260
    if not blocked_directions["0_4"]["east"]:
        button xcenter 1140 ycenter 460 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_1_4", j=True)]
        text "東\nEAST" xcenter 1140 ycenter 460
    if not blocked_directions["0_4"]["south"]:
        button xcenter 640 ycenter 680 xysize (1280, 100) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_0_3", j=True)]
        text "南\nSOUTH" xcenter 640 ycenter 680

screen deep_forest_0_5:
    style_prefix "explore"
    if not blocked_directions["0_5"]["north"]:
        button xcenter 740 ycenter 360 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_0_6", j=True)]
        text "北\nNORTH" xcenter 740 ycenter 360
    if not blocked_directions["0_5"]["west"]:
        button xcenter 240 ycenter 260 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_-1_5", j=True)]
        text "西\nWEST" xcenter 240 ycenter 260
    if not blocked_directions["0_5"]["east"]:
        button xcenter 1140 ycenter 460 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_1_5", j=True)]
        text "東\nEAST" xcenter 1140 ycenter 460
    if not blocked_directions["0_5"]["south"]:
        button xcenter 640 ycenter 680 xysize (1280, 100) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_0_4", j=True)]
        text "南\nSOUTH" xcenter 640 ycenter 680

screen deep_forest_0_6:
    style_prefix "explore"
    if not blocked_directions["0_6"]["north"]:
        button xcenter 740 ycenter 360 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_0_7", j=True)]
        text "北\nNORTH" xcenter 740 ycenter 360
    if not blocked_directions["0_6"]["west"]:
        button xcenter 240 ycenter 260 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_-1_6", j=True)]
        text "西\nWEST" xcenter 240 ycenter 260
    if not blocked_directions["0_6"]["east"]:
        button xcenter 1140 ycenter 460 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_1_6", j=True)]
        text "東\nEAST" xcenter 1140 ycenter 460
    if not blocked_directions["0_6"]["south"]:
        button xcenter 640 ycenter 680 xysize (1280, 100) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_0_5", j=True)]
        text "南\nSOUTH" xcenter 640 ycenter 680

screen deep_forest_0_7:
    style_prefix "explore"
    if not blocked_directions["0_7"]["north"]:
        button xcenter 740 ycenter 360 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_0_8", j=True)]
        text "北\nNORTH" xcenter 740 ycenter 360
    if not blocked_directions["0_7"]["west"]:
        button xcenter 240 ycenter 260 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_-1_7", j=True)]
        text "西\nWEST" xcenter 240 ycenter 260
    if not blocked_directions["0_7"]["east"]:
        button xcenter 1140 ycenter 460 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_1_7", j=True)]
        text "東\nEAST" xcenter 1140 ycenter 460
    if not blocked_directions["0_7"]["south"]:
        button xcenter 640 ycenter 680 xysize (1280, 100) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_0_6", j=True)]
        text "南\nSOUTH" xcenter 640 ycenter 680

screen deep_forest_0_8:
    style_prefix "explore"
    if not blocked_directions["0_8"]["north"]:
        button xcenter 740 ycenter 360 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_0_9", j=True)]
        text "北\nNORTH" xcenter 740 ycenter 360
    if not blocked_directions["0_8"]["west"]:
        button xcenter 240 ycenter 260 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_-1_8", j=True)]
        text "西\nWEST" xcenter 240 ycenter 260
    if not blocked_directions["0_8"]["east"]:
        button xcenter 1140 ycenter 460 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_1_8", j=True)]
        text "東\nEAST" xcenter 1140 ycenter 460
    if not blocked_directions["0_8"]["south"]:
        button xcenter 640 ycenter 680 xysize (1280, 100) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_0_7", j=True)]
        text "南\nSOUTH" xcenter 640 ycenter 680

screen deep_forest_0_9:
    style_prefix "explore"
    if not blocked_directions["0_9"]["north"]:
        button xcenter 740 ycenter 360 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_0_10", j=True)]
        text "北\nNORTH" xcenter 740 ycenter 360
    if not blocked_directions["0_9"]["west"]:
        button xcenter 240 ycenter 260 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_-1_9", j=True)]
        text "西\nWEST" xcenter 240 ycenter 260
    if not blocked_directions["0_9"]["east"]:
        button xcenter 1140 ycenter 460 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_1_9", j=True)]
        text "東\nEAST" xcenter 1140 ycenter 460
    if not blocked_directions["0_9"]["south"]:
        button xcenter 640 ycenter 680 xysize (1280, 100) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_0_8", j=True)]
        text "南\nSOUTH" xcenter 640 ycenter 680

screen deep_forest_1_0:
    style_prefix "explore"
    if not blocked_directions["1_0"]["north"]:
        button xcenter 740 ycenter 360 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_1_1", j=True)]
        text "北\nNORTH" xcenter 740 ycenter 360
    if not blocked_directions["1_0"]["west"]:
        button xcenter 240 ycenter 260 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_0_0", j=True)]
        text "西\nWEST" xcenter 240 ycenter 260
    if not blocked_directions["1_0"]["east"]:
        button xcenter 1140 ycenter 460 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_2_0", j=True)]
        text "東\nEAST" xcenter 1140 ycenter 460
    if not blocked_directions["1_0"]["south"]:
        button xcenter 640 ycenter 680 xysize (1280, 100) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_1_-1", j=True)]
        text "南\nSOUTH" xcenter 640 ycenter 680

screen deep_forest_1_1:
    style_prefix "explore"
    if not blocked_directions["1_1"]["north"]:
        button xcenter 740 ycenter 360 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_1_2", j=True)]
        text "北\nNORTH" xcenter 740 ycenter 360
    if not blocked_directions["1_1"]["west"]:
        button xcenter 240 ycenter 260 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_0_1", j=True)]
        text "西\nWEST" xcenter 240 ycenter 260
    if not blocked_directions["1_1"]["east"]:
        button xcenter 1140 ycenter 460 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_2_1", j=True)]
        text "東\nEAST" xcenter 1140 ycenter 460
    if not blocked_directions["1_1"]["south"]:
        button xcenter 640 ycenter 680 xysize (1280, 100) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_1_0", j=True)]
        text "南\nSOUTH" xcenter 640 ycenter 680

screen deep_forest_1_2:
    style_prefix "explore"
    if not blocked_directions["1_2"]["north"]:
        button xcenter 740 ycenter 360 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_1_3", j=True)]
        text "北\nNORTH" xcenter 740 ycenter 360
    if not blocked_directions["1_2"]["west"]:
        button xcenter 240 ycenter 260 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_0_2", j=True)]
        text "西\nWEST" xcenter 240 ycenter 260
    if not blocked_directions["1_2"]["east"]:
        button xcenter 1140 ycenter 460 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_2_2", j=True)]
        text "東\nEAST" xcenter 1140 ycenter 460
    if not blocked_directions["1_2"]["south"]:
        button xcenter 640 ycenter 680 xysize (1280, 100) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_1_1", j=True)]
        text "南\nSOUTH" xcenter 640 ycenter 680

screen deep_forest_1_3:
    style_prefix "explore"
    if not blocked_directions["1_3"]["north"]:
        button xcenter 740 ycenter 360 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_1_4", j=True)]
        text "北\nNORTH" xcenter 740 ycenter 360
    if not blocked_directions["1_3"]["west"]:
        button xcenter 240 ycenter 260 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_0_3", j=True)]
        text "西\nWEST" xcenter 240 ycenter 260
    if not blocked_directions["1_3"]["east"]:
        button xcenter 1140 ycenter 460 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_2_3", j=True)]
        text "東\nEAST" xcenter 1140 ycenter 460
    if not blocked_directions["1_3"]["south"]:
        button xcenter 640 ycenter 680 xysize (1280, 100) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_1_2", j=True)]
        text "南\nSOUTH" xcenter 640 ycenter 680

screen deep_forest_1_4:
    style_prefix "explore"
    if not blocked_directions["1_4"]["north"]:
        button xcenter 740 ycenter 360 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_1_5", j=True)]
        text "北\nNORTH" xcenter 740 ycenter 360
    if not blocked_directions["1_4"]["west"]:
        button xcenter 240 ycenter 260 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_0_4", j=True)]
        text "西\nWEST" xcenter 240 ycenter 260
    if not blocked_directions["1_4"]["east"]:
        button xcenter 1140 ycenter 460 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_2_4", j=True)]
        text "東\nEAST" xcenter 1140 ycenter 460
    if not blocked_directions["1_4"]["south"]:
        button xcenter 640 ycenter 680 xysize (1280, 100) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_1_3", j=True)]
        text "南\nSOUTH" xcenter 640 ycenter 680

screen deep_forest_1_5:
    style_prefix "explore"
    if not blocked_directions["1_5"]["north"]:
        button xcenter 740 ycenter 360 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_1_6", j=True)]
        text "北\nNORTH" xcenter 740 ycenter 360
    if not blocked_directions["1_5"]["west"]:
        button xcenter 240 ycenter 260 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_0_5", j=True)]
        text "西\nWEST" xcenter 240 ycenter 260
    if not blocked_directions["1_5"]["east"]:
        button xcenter 1140 ycenter 460 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_2_5", j=True)]
        text "東\nEAST" xcenter 1140 ycenter 460
    if not blocked_directions["1_5"]["south"]:
        button xcenter 640 ycenter 680 xysize (1280, 100) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_1_4", j=True)]
        text "南\nSOUTH" xcenter 640 ycenter 680

screen deep_forest_1_6:
    style_prefix "explore"
    if not blocked_directions["1_6"]["north"]:
        button xcenter 740 ycenter 360 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_1_7", j=True)]
        text "北\nNORTH" xcenter 740 ycenter 360
    if not blocked_directions["1_6"]["west"]:
        button xcenter 240 ycenter 260 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_0_6", j=True)]
        text "西\nWEST" xcenter 240 ycenter 260
    if not blocked_directions["1_6"]["east"]:
        button xcenter 1140 ycenter 460 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_2_6", j=True)]
        text "東\nEAST" xcenter 1140 ycenter 460
    if not blocked_directions["1_6"]["south"]:
        button xcenter 640 ycenter 680 xysize (1280, 100) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_1_5", j=True)]
        text "南\nSOUTH" xcenter 640 ycenter 680

screen deep_forest_1_7:
    style_prefix "explore"
    if not blocked_directions["1_7"]["north"]:
        button xcenter 740 ycenter 360 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_1_8", j=True)]
        text "北\nNORTH" xcenter 740 ycenter 360
    if not blocked_directions["1_7"]["west"]:
        button xcenter 240 ycenter 260 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_0_7", j=True)]
        text "西\nWEST" xcenter 240 ycenter 260
    if not blocked_directions["1_7"]["east"]:
        button xcenter 1140 ycenter 460 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_2_7", j=True)]
        text "東\nEAST" xcenter 1140 ycenter 460
    if not blocked_directions["1_7"]["south"]:
        button xcenter 640 ycenter 680 xysize (1280, 100) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_1_6", j=True)]
        text "南\nSOUTH" xcenter 640 ycenter 680

screen deep_forest_1_8:
    style_prefix "explore"
    if not blocked_directions["1_8"]["north"]:
        button xcenter 740 ycenter 360 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_1_9", j=True)]
        text "北\nNORTH" xcenter 740 ycenter 360
    if not blocked_directions["1_8"]["west"]:
        button xcenter 240 ycenter 260 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_0_8", j=True)]
        text "西\nWEST" xcenter 240 ycenter 260
    if not blocked_directions["1_8"]["east"]:
        button xcenter 1140 ycenter 460 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_2_8", j=True)]
        text "東\nEAST" xcenter 1140 ycenter 460
    if not blocked_directions["1_8"]["south"]:
        button xcenter 640 ycenter 680 xysize (1280, 100) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_1_7", j=True)]
        text "南\nSOUTH" xcenter 640 ycenter 680

screen deep_forest_1_9:
    style_prefix "explore"
    if not blocked_directions["1_9"]["north"]:
        button xcenter 740 ycenter 360 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_1_10", j=True)]
        text "北\nNORTH" xcenter 740 ycenter 360
    if not blocked_directions["1_9"]["west"]:
        button xcenter 240 ycenter 260 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_0_9", j=True)]
        text "西\nWEST" xcenter 240 ycenter 260
    if not blocked_directions["1_9"]["east"]:
        button xcenter 1140 ycenter 460 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_2_9", j=True)]
        text "東\nEAST" xcenter 1140 ycenter 460
    if not blocked_directions["1_9"]["south"]:
        button xcenter 640 ycenter 680 xysize (1280, 100) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_1_8", j=True)]
        text "南\nSOUTH" xcenter 640 ycenter 680

screen deep_forest_2_0:
    style_prefix "explore"
    if not blocked_directions["2_0"]["north"]:
        button xcenter 740 ycenter 360 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_2_1", j=True)]
        text "北\nNORTH" xcenter 740 ycenter 360
    if not blocked_directions["2_0"]["west"]:
        button xcenter 240 ycenter 260 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_1_0", j=True)]
        text "西\nWEST" xcenter 240 ycenter 260
    if not blocked_directions["2_0"]["east"]:
        button xcenter 1140 ycenter 460 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_3_0", j=True)]
        text "東\nEAST" xcenter 1140 ycenter 460
    if not blocked_directions["2_0"]["south"]:
        button xcenter 640 ycenter 680 xysize (1280, 100) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_2_-1", j=True)]
        text "南\nSOUTH" xcenter 640 ycenter 680

screen deep_forest_2_1:
    style_prefix "explore"
    if not blocked_directions["2_1"]["north"]:
        button xcenter 740 ycenter 360 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_2_2", j=True)]
        text "北\nNORTH" xcenter 740 ycenter 360
    if not blocked_directions["2_1"]["west"]:
        button xcenter 240 ycenter 260 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_1_1", j=True)]
        text "西\nWEST" xcenter 240 ycenter 260
    if not blocked_directions["2_1"]["east"]:
        button xcenter 1140 ycenter 460 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_3_1", j=True)]
        text "東\nEAST" xcenter 1140 ycenter 460
    if not blocked_directions["2_1"]["south"]:
        button xcenter 640 ycenter 680 xysize (1280, 100) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_2_0", j=True)]
        text "南\nSOUTH" xcenter 640 ycenter 680

screen deep_forest_2_2:
    style_prefix "explore"
    if not blocked_directions["2_2"]["north"]:
        button xcenter 740 ycenter 360 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_2_3", j=True)]
        text "北\nNORTH" xcenter 740 ycenter 360
    if not blocked_directions["2_2"]["west"]:
        button xcenter 240 ycenter 260 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_1_2", j=True)]
        text "西\nWEST" xcenter 240 ycenter 260
    if not blocked_directions["2_2"]["east"]:
        button xcenter 1140 ycenter 460 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_3_2", j=True)]
        text "東\nEAST" xcenter 1140 ycenter 460
    if not blocked_directions["2_2"]["south"]:
        button xcenter 640 ycenter 680 xysize (1280, 100) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_2_1", j=True)]
        text "南\nSOUTH" xcenter 640 ycenter 680

screen deep_forest_2_3:
    style_prefix "explore"
    if not blocked_directions["2_3"]["north"]:
        button xcenter 740 ycenter 360 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_2_4", j=True)]
        text "北\nNORTH" xcenter 740 ycenter 360
    if not blocked_directions["2_3"]["west"]:
        button xcenter 240 ycenter 260 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_1_3", j=True)]
        text "西\nWEST" xcenter 240 ycenter 260
    if not blocked_directions["2_3"]["east"]:
        button xcenter 1140 ycenter 460 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_3_3", j=True)]
        text "東\nEAST" xcenter 1140 ycenter 460
    if not blocked_directions["2_3"]["south"]:
        button xcenter 640 ycenter 680 xysize (1280, 100) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_2_2", j=True)]
        text "南\nSOUTH" xcenter 640 ycenter 680

screen deep_forest_2_4:
    style_prefix "explore"
    if not blocked_directions["2_4"]["north"]:
        button xcenter 740 ycenter 360 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_2_5", j=True)]
        text "北\nNORTH" xcenter 740 ycenter 360
    if not blocked_directions["2_4"]["west"]:
        button xcenter 240 ycenter 260 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_1_4", j=True)]
        text "西\nWEST" xcenter 240 ycenter 260
    if not blocked_directions["2_4"]["east"]:
        button xcenter 1140 ycenter 460 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_3_4", j=True)]
        text "東\nEAST" xcenter 1140 ycenter 460
    if not blocked_directions["2_4"]["south"]:
        button xcenter 640 ycenter 680 xysize (1280, 100) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_2_3", j=True)]
        text "南\nSOUTH" xcenter 640 ycenter 680

screen deep_forest_2_5:
    style_prefix "explore"
    if not blocked_directions["2_5"]["north"]:
        button xcenter 740 ycenter 360 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_2_6", j=True)]
        text "北\nNORTH" xcenter 740 ycenter 360
    if not blocked_directions["2_5"]["west"]:
        button xcenter 240 ycenter 260 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_1_5", j=True)]
        text "西\nWEST" xcenter 240 ycenter 260
    if not blocked_directions["2_5"]["east"]:
        button xcenter 1140 ycenter 460 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_3_5", j=True)]
        text "東\nEAST" xcenter 1140 ycenter 460
    if not blocked_directions["2_5"]["south"]:
        button xcenter 640 ycenter 680 xysize (1280, 100) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_2_4", j=True)]
        text "南\nSOUTH" xcenter 640 ycenter 680

screen deep_forest_2_6:
    style_prefix "explore"
    if not blocked_directions["2_6"]["north"]:
        button xcenter 740 ycenter 360 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_2_7", j=True)]
        text "北\nNORTH" xcenter 740 ycenter 360
    if not blocked_directions["2_6"]["west"]:
        button xcenter 240 ycenter 260 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_1_6", j=True)]
        text "西\nWEST" xcenter 240 ycenter 260
    if not blocked_directions["2_6"]["east"]:
        button xcenter 1140 ycenter 460 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_3_6", j=True)]
        text "東\nEAST" xcenter 1140 ycenter 460
    if not blocked_directions["2_6"]["south"]:
        button xcenter 640 ycenter 680 xysize (1280, 100) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_2_5", j=True)]
        text "南\nSOUTH" xcenter 640 ycenter 680

screen deep_forest_2_7:
    style_prefix "explore"
    if not blocked_directions["2_7"]["north"]:
        button xcenter 740 ycenter 360 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_2_8", j=True)]
        text "北\nNORTH" xcenter 740 ycenter 360
    if not blocked_directions["2_7"]["west"]:
        button xcenter 240 ycenter 260 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_1_7", j=True)]
        text "西\nWEST" xcenter 240 ycenter 260
    if not blocked_directions["2_7"]["east"]:
        button xcenter 1140 ycenter 460 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_3_7", j=True)]
        text "東\nEAST" xcenter 1140 ycenter 460
    if not blocked_directions["2_7"]["south"]:
        button xcenter 640 ycenter 680 xysize (1280, 100) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_2_6", j=True)]
        text "南\nSOUTH" xcenter 640 ycenter 680

screen deep_forest_2_8:
    style_prefix "explore"
    if not blocked_directions["2_8"]["north"]:
        button xcenter 740 ycenter 360 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_2_9", j=True)]
        text "北\nNORTH" xcenter 740 ycenter 360
    if not blocked_directions["2_8"]["west"]:
        button xcenter 240 ycenter 260 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_1_8", j=True)]
        text "西\nWEST" xcenter 240 ycenter 260
    if not blocked_directions["2_8"]["east"]:
        button xcenter 1140 ycenter 460 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_3_8", j=True)]
        text "東\nEAST" xcenter 1140 ycenter 460
    if not blocked_directions["2_8"]["south"]:
        button xcenter 640 ycenter 680 xysize (1280, 100) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_2_7", j=True)]
        text "南\nSOUTH" xcenter 640 ycenter 680

screen deep_forest_2_9:
    style_prefix "explore"
    if not blocked_directions["2_9"]["north"]:
        button xcenter 740 ycenter 360 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_2_10", j=True)]
        text "北\nNORTH" xcenter 740 ycenter 360
    if not blocked_directions["2_9"]["west"]:
        button xcenter 240 ycenter 260 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_1_9", j=True)]
        text "西\nWEST" xcenter 240 ycenter 260
    if not blocked_directions["2_9"]["east"]:
        button xcenter 1140 ycenter 460 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_3_9", j=True)]
        text "東\nEAST" xcenter 1140 ycenter 460
    if not blocked_directions["2_9"]["south"]:
        button xcenter 640 ycenter 680 xysize (1280, 100) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_2_8", j=True)]
        text "南\nSOUTH" xcenter 640 ycenter 680

screen deep_forest_3_0:
    style_prefix "explore"
    if not blocked_directions["3_0"]["north"]:
        button xcenter 740 ycenter 360 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_3_1", j=True)]
        text "北\nNORTH" xcenter 740 ycenter 360
    if not blocked_directions["3_0"]["west"]:
        button xcenter 240 ycenter 260 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_2_0", j=True)]
        text "西\nWEST" xcenter 240 ycenter 260
    if not blocked_directions["3_0"]["east"]:
        button xcenter 1140 ycenter 460 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_4_0", j=True)]
        text "東\nEAST" xcenter 1140 ycenter 460
    if not blocked_directions["3_0"]["south"]:
        button xcenter 640 ycenter 680 xysize (1280, 100) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_3_-1", j=True)]
        text "南\nSOUTH" xcenter 640 ycenter 680

screen deep_forest_3_1:
    style_prefix "explore"
    if not blocked_directions["3_1"]["north"]:
        button xcenter 740 ycenter 360 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_3_2", j=True)]
        text "北\nNORTH" xcenter 740 ycenter 360
    if not blocked_directions["3_1"]["west"]:
        button xcenter 240 ycenter 260 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_2_1", j=True)]
        text "西\nWEST" xcenter 240 ycenter 260
    if not blocked_directions["3_1"]["east"]:
        button xcenter 1140 ycenter 460 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_4_1", j=True)]
        text "東\nEAST" xcenter 1140 ycenter 460
    if not blocked_directions["3_1"]["south"]:
        button xcenter 640 ycenter 680 xysize (1280, 100) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_3_0", j=True)]
        text "南\nSOUTH" xcenter 640 ycenter 680

screen deep_forest_3_2:
    style_prefix "explore"
    if not blocked_directions["3_2"]["north"]:
        button xcenter 740 ycenter 360 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_3_3", j=True)]
        text "北\nNORTH" xcenter 740 ycenter 360
    if not blocked_directions["3_2"]["west"]:
        button xcenter 240 ycenter 260 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_2_2", j=True)]
        text "西\nWEST" xcenter 240 ycenter 260
    if not blocked_directions["3_2"]["east"]:
        button xcenter 1140 ycenter 460 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_4_2", j=True)]
        text "東\nEAST" xcenter 1140 ycenter 460
    if not blocked_directions["3_2"]["south"]:
        button xcenter 640 ycenter 680 xysize (1280, 100) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_3_1", j=True)]
        text "南\nSOUTH" xcenter 640 ycenter 680

screen deep_forest_3_3:
    style_prefix "explore"
    if not blocked_directions["3_3"]["north"]:
        button xcenter 740 ycenter 360 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_3_4", j=True)]
        text "北\nNORTH" xcenter 740 ycenter 360
    if not blocked_directions["3_3"]["west"]:
        button xcenter 240 ycenter 260 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_2_3", j=True)]
        text "西\nWEST" xcenter 240 ycenter 260
    if not blocked_directions["3_3"]["east"]:
        button xcenter 1140 ycenter 460 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_4_3", j=True)]
        text "東\nEAST" xcenter 1140 ycenter 460
    if not blocked_directions["3_3"]["south"]:
        button xcenter 640 ycenter 680 xysize (1280, 100) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_3_2", j=True)]
        text "南\nSOUTH" xcenter 640 ycenter 680

screen deep_forest_3_4:
    style_prefix "explore"
    if not blocked_directions["3_4"]["north"]:
        button xcenter 740 ycenter 360 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_3_5", j=True)]
        text "北\nNORTH" xcenter 740 ycenter 360
    if not blocked_directions["3_4"]["west"]:
        button xcenter 240 ycenter 260 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_2_4", j=True)]
        text "西\nWEST" xcenter 240 ycenter 260
    if not blocked_directions["3_4"]["east"]:
        button xcenter 1140 ycenter 460 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_4_4", j=True)]
        text "東\nEAST" xcenter 1140 ycenter 460
    if not blocked_directions["3_4"]["south"]:
        button xcenter 640 ycenter 680 xysize (1280, 100) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_3_3", j=True)]
        text "南\nSOUTH" xcenter 640 ycenter 680

screen deep_forest_3_5:
    style_prefix "explore"
    if not blocked_directions["3_5"]["north"]:
        button xcenter 740 ycenter 360 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_3_6", j=True)]
        text "北\nNORTH" xcenter 740 ycenter 360
    if not blocked_directions["3_5"]["west"]:
        button xcenter 240 ycenter 260 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_2_5", j=True)]
        text "西\nWEST" xcenter 240 ycenter 260
    if not blocked_directions["3_5"]["east"]:
        button xcenter 1140 ycenter 460 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_4_5", j=True)]
        text "東\nEAST" xcenter 1140 ycenter 460
    if not blocked_directions["3_5"]["south"]:
        button xcenter 640 ycenter 680 xysize (1280, 100) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_3_4", j=True)]
        text "南\nSOUTH" xcenter 640 ycenter 680

screen deep_forest_3_6:
    style_prefix "explore"
    if not blocked_directions["3_6"]["north"]:
        button xcenter 740 ycenter 360 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_3_7", j=True)]
        text "北\nNORTH" xcenter 740 ycenter 360
    if not blocked_directions["3_6"]["west"]:
        button xcenter 240 ycenter 260 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_2_6", j=True)]
        text "西\nWEST" xcenter 240 ycenter 260
    if not blocked_directions["3_6"]["east"]:
        button xcenter 1140 ycenter 460 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_4_6", j=True)]
        text "東\nEAST" xcenter 1140 ycenter 460
    if not blocked_directions["3_6"]["south"]:
        button xcenter 640 ycenter 680 xysize (1280, 100) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_3_5", j=True)]
        text "南\nSOUTH" xcenter 640 ycenter 680

screen deep_forest_3_7:
    style_prefix "explore"
    if not blocked_directions["3_7"]["north"]:
        button xcenter 740 ycenter 360 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_3_8", j=True)]
        text "北\nNORTH" xcenter 740 ycenter 360
    if not blocked_directions["3_7"]["west"]:
        button xcenter 240 ycenter 260 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_2_7", j=True)]
        text "西\nWEST" xcenter 240 ycenter 260
    if not blocked_directions["3_7"]["east"]:
        button xcenter 1140 ycenter 460 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_4_7", j=True)]
        text "東\nEAST" xcenter 1140 ycenter 460
    if not blocked_directions["3_7"]["south"]:
        button xcenter 640 ycenter 680 xysize (1280, 100) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_3_6", j=True)]
        text "南\nSOUTH" xcenter 640 ycenter 680

screen deep_forest_3_8:
    style_prefix "explore"
    if not blocked_directions["3_8"]["north"]:
        button xcenter 740 ycenter 360 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_3_9", j=True)]
        text "北\nNORTH" xcenter 740 ycenter 360
    if not blocked_directions["3_8"]["west"]:
        button xcenter 240 ycenter 260 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_2_8", j=True)]
        text "西\nWEST" xcenter 240 ycenter 260
    if not blocked_directions["3_8"]["east"]:
        button xcenter 1140 ycenter 460 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_4_8", j=True)]
        text "東\nEAST" xcenter 1140 ycenter 460
    if not blocked_directions["3_8"]["south"]:
        button xcenter 640 ycenter 680 xysize (1280, 100) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_3_7", j=True)]
        text "南\nSOUTH" xcenter 640 ycenter 680

screen deep_forest_3_9:
    style_prefix "explore"
    if not blocked_directions["3_9"]["north"]:
        button xcenter 740 ycenter 360 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_3_10", j=True)]
        text "北\nNORTH" xcenter 740 ycenter 360
    if not blocked_directions["3_9"]["west"]:
        button xcenter 240 ycenter 260 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_2_9", j=True)]
        text "西\nWEST" xcenter 240 ycenter 260
    if not blocked_directions["3_9"]["east"]:
        button xcenter 1140 ycenter 460 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_4_9", j=True)]
        text "東\nEAST" xcenter 1140 ycenter 460
    if not blocked_directions["3_9"]["south"]:
        button xcenter 640 ycenter 680 xysize (1280, 100) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_3_8", j=True)]
        text "南\nSOUTH" xcenter 640 ycenter 680

screen deep_forest_4_0:
    style_prefix "explore"
    if not blocked_directions["4_0"]["north"]:
        button xcenter 740 ycenter 360 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_4_1", j=True)]
        text "北\nNORTH" xcenter 740 ycenter 360
    if not blocked_directions["4_0"]["west"]:
        button xcenter 240 ycenter 260 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_3_0", j=True)]
        text "西\nWEST" xcenter 240 ycenter 260
    if not blocked_directions["4_0"]["east"]:
        button xcenter 1140 ycenter 460 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_5_0", j=True)]
        text "東\nEAST" xcenter 1140 ycenter 460
    if not blocked_directions["4_0"]["south"]:
        button xcenter 640 ycenter 680 xysize (1280, 100) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_4_-1", j=True)]
        text "南\nSOUTH" xcenter 640 ycenter 680

screen deep_forest_4_1:
    style_prefix "explore"
    if not blocked_directions["4_1"]["north"]:
        button xcenter 740 ycenter 360 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_4_2", j=True)]
        text "北\nNORTH" xcenter 740 ycenter 360
    if not blocked_directions["4_1"]["west"]:
        button xcenter 240 ycenter 260 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_3_1", j=True)]
        text "西\nWEST" xcenter 240 ycenter 260
    if not blocked_directions["4_1"]["east"]:
        button xcenter 1140 ycenter 460 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_5_1", j=True)]
        text "東\nEAST" xcenter 1140 ycenter 460
    if not blocked_directions["4_1"]["south"]:
        button xcenter 640 ycenter 680 xysize (1280, 100) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_4_0", j=True)]
        text "南\nSOUTH" xcenter 640 ycenter 680

screen deep_forest_4_2:
    style_prefix "explore"
    if not blocked_directions["4_2"]["north"]:
        button xcenter 740 ycenter 360 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_4_3", j=True)]
        text "北\nNORTH" xcenter 740 ycenter 360
    if not blocked_directions["4_2"]["west"]:
        button xcenter 240 ycenter 260 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_3_2", j=True)]
        text "西\nWEST" xcenter 240 ycenter 260
    if not blocked_directions["4_2"]["east"]:
        button xcenter 1140 ycenter 460 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_5_2", j=True)]
        text "東\nEAST" xcenter 1140 ycenter 460
    if not blocked_directions["4_2"]["south"]:
        button xcenter 640 ycenter 680 xysize (1280, 100) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_4_1", j=True)]
        text "南\nSOUTH" xcenter 640 ycenter 680

screen deep_forest_4_3:
    style_prefix "explore"
    if not blocked_directions["4_3"]["north"]:
        button xcenter 740 ycenter 360 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_4_4", j=True)]
        text "北\nNORTH" xcenter 740 ycenter 360
    if not blocked_directions["4_3"]["west"]:
        button xcenter 240 ycenter 260 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_3_3", j=True)]
        text "西\nWEST" xcenter 240 ycenter 260
    if not blocked_directions["4_3"]["east"]:
        button xcenter 1140 ycenter 460 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_5_3", j=True)]
        text "東\nEAST" xcenter 1140 ycenter 460
    if not blocked_directions["4_3"]["south"]:
        button xcenter 640 ycenter 680 xysize (1280, 100) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_4_2", j=True)]
        text "南\nSOUTH" xcenter 640 ycenter 680

screen deep_forest_4_4:
    style_prefix "explore"
    if not blocked_directions["4_4"]["north"]:
        button xcenter 740 ycenter 360 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_4_5", j=True)]
        text "北\nNORTH" xcenter 740 ycenter 360
    if not blocked_directions["4_4"]["west"]:
        button xcenter 240 ycenter 260 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_3_4", j=True)]
        text "西\nWEST" xcenter 240 ycenter 260
    if not blocked_directions["4_4"]["east"]:
        button xcenter 1140 ycenter 460 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_5_4", j=True)]
        text "東\nEAST" xcenter 1140 ycenter 460
    if not blocked_directions["4_4"]["south"]:
        button xcenter 640 ycenter 680 xysize (1280, 100) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_4_3", j=True)]
        text "南\nSOUTH" xcenter 640 ycenter 680

screen deep_forest_4_5:
    style_prefix "explore"
    if not blocked_directions["4_5"]["north"]:
        button xcenter 740 ycenter 360 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_4_6", j=True)]
        text "北\nNORTH" xcenter 740 ycenter 360
    if not blocked_directions["4_5"]["west"]:
        button xcenter 240 ycenter 260 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_3_5", j=True)]
        text "西\nWEST" xcenter 240 ycenter 260
    if not blocked_directions["4_5"]["east"]:
        button xcenter 1140 ycenter 460 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_5_5", j=True)]
        text "東\nEAST" xcenter 1140 ycenter 460
    if not blocked_directions["4_5"]["south"]:
        button xcenter 640 ycenter 680 xysize (1280, 100) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_4_4", j=True)]
        text "南\nSOUTH" xcenter 640 ycenter 680

screen deep_forest_4_6:
    style_prefix "explore"
    if not blocked_directions["4_6"]["north"]:
        button xcenter 740 ycenter 360 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_4_7", j=True)]
        text "北\nNORTH" xcenter 740 ycenter 360
    if not blocked_directions["4_6"]["west"]:
        button xcenter 240 ycenter 260 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_3_6", j=True)]
        text "西\nWEST" xcenter 240 ycenter 260
    if not blocked_directions["4_6"]["east"]:
        button xcenter 1140 ycenter 460 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_5_6", j=True)]
        text "東\nEAST" xcenter 1140 ycenter 460
    if not blocked_directions["4_6"]["south"]:
        button xcenter 640 ycenter 680 xysize (1280, 100) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_4_5", j=True)]
        text "南\nSOUTH" xcenter 640 ycenter 680

screen deep_forest_4_7:
    style_prefix "explore"
    if not blocked_directions["4_7"]["north"]:
        button xcenter 740 ycenter 360 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_4_8", j=True)]
        text "北\nNORTH" xcenter 740 ycenter 360
    if not blocked_directions["4_7"]["west"]:
        button xcenter 240 ycenter 260 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_3_7", j=True)]
        text "西\nWEST" xcenter 240 ycenter 260
    if not blocked_directions["4_7"]["east"]:
        button xcenter 1140 ycenter 460 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_5_7", j=True)]
        text "東\nEAST" xcenter 1140 ycenter 460
    if not blocked_directions["4_7"]["south"]:
        button xcenter 640 ycenter 680 xysize (1280, 100) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_4_6", j=True)]
        text "南\nSOUTH" xcenter 640 ycenter 680

screen deep_forest_4_8:
    style_prefix "explore"
    if not blocked_directions["4_8"]["north"]:
        button xcenter 740 ycenter 360 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_4_9", j=True)]
        text "北\nNORTH" xcenter 740 ycenter 360
    if not blocked_directions["4_8"]["west"]:
        button xcenter 240 ycenter 260 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_3_8", j=True)]
        text "西\nWEST" xcenter 240 ycenter 260
    if not blocked_directions["4_8"]["east"]:
        button xcenter 1140 ycenter 460 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_5_8", j=True)]
        text "東\nEAST" xcenter 1140 ycenter 460
    if not blocked_directions["4_8"]["south"]:
        button xcenter 640 ycenter 680 xysize (1280, 100) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_4_7", j=True)]
        text "南\nSOUTH" xcenter 640 ycenter 680

screen deep_forest_4_9:
    style_prefix "explore"
    if not blocked_directions["4_9"]["north"]:
        button xcenter 740 ycenter 360 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_4_10", j=True)]
        text "北\nNORTH" xcenter 740 ycenter 360
    if not blocked_directions["4_9"]["west"]:
        button xcenter 240 ycenter 260 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_3_9", j=True)]
        text "西\nWEST" xcenter 240 ycenter 260
    if not blocked_directions["4_9"]["east"]:
        button xcenter 1140 ycenter 460 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_5_9", j=True)]
        text "東\nEAST" xcenter 1140 ycenter 460
    if not blocked_directions["4_9"]["south"]:
        button xcenter 640 ycenter 680 xysize (1280, 100) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_4_8", j=True)]
        text "南\nSOUTH" xcenter 640 ycenter 680

screen deep_forest_5_0:
    style_prefix "explore"
    if not blocked_directions["5_0"]["north"]:
        button xcenter 740 ycenter 360 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_5_1", j=True)]
        text "北\nNORTH" xcenter 740 ycenter 360
    if not blocked_directions["5_0"]["west"]:
        button xcenter 240 ycenter 260 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_4_0", j=True)]
        text "西\nWEST" xcenter 240 ycenter 260
    if not blocked_directions["5_0"]["east"]:
        button xcenter 1140 ycenter 460 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_6_0", j=True)]
        text "東\nEAST" xcenter 1140 ycenter 460
    if not blocked_directions["5_0"]["south"]:
        button xcenter 640 ycenter 680 xysize (1280, 100) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_5_-1", j=True)]
        text "南\nSOUTH" xcenter 640 ycenter 680

screen deep_forest_5_1:
    style_prefix "explore"
    if not blocked_directions["5_1"]["north"]:
        button xcenter 740 ycenter 360 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_5_2", j=True)]
        text "北\nNORTH" xcenter 740 ycenter 360
    if not blocked_directions["5_1"]["west"]:
        button xcenter 240 ycenter 260 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_4_1", j=True)]
        text "西\nWEST" xcenter 240 ycenter 260
    if not blocked_directions["5_1"]["east"]:
        button xcenter 1140 ycenter 460 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_6_1", j=True)]
        text "東\nEAST" xcenter 1140 ycenter 460
    if not blocked_directions["5_1"]["south"]:
        button xcenter 640 ycenter 680 xysize (1280, 100) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_5_0", j=True)]
        text "南\nSOUTH" xcenter 640 ycenter 680

screen deep_forest_5_2:
    style_prefix "explore"
    if not blocked_directions["5_2"]["north"]:
        button xcenter 740 ycenter 360 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_5_3", j=True)]
        text "北\nNORTH" xcenter 740 ycenter 360
    if not blocked_directions["5_2"]["west"]:
        button xcenter 240 ycenter 260 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_4_2", j=True)]
        text "西\nWEST" xcenter 240 ycenter 260
    if not blocked_directions["5_2"]["east"]:
        button xcenter 1140 ycenter 460 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_6_2", j=True)]
        text "東\nEAST" xcenter 1140 ycenter 460
    if not blocked_directions["5_2"]["south"]:
        button xcenter 640 ycenter 680 xysize (1280, 100) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_5_1", j=True)]
        text "南\nSOUTH" xcenter 640 ycenter 680

screen deep_forest_5_3:
    style_prefix "explore"
    if not blocked_directions["5_3"]["north"]:
        button xcenter 740 ycenter 360 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_5_4", j=True)]
        text "北\nNORTH" xcenter 740 ycenter 360
    if not blocked_directions["5_3"]["west"]:
        button xcenter 240 ycenter 260 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_4_3", j=True)]
        text "西\nWEST" xcenter 240 ycenter 260
    if not blocked_directions["5_3"]["east"]:
        button xcenter 1140 ycenter 460 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_6_3", j=True)]
        text "東\nEAST" xcenter 1140 ycenter 460
    if not blocked_directions["5_3"]["south"]:
        button xcenter 640 ycenter 680 xysize (1280, 100) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_5_2", j=True)]
        text "南\nSOUTH" xcenter 640 ycenter 680

screen deep_forest_5_4:
    style_prefix "explore"
    if not blocked_directions["5_4"]["north"]:
        button xcenter 740 ycenter 360 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_5_5", j=True)]
        text "北\nNORTH" xcenter 740 ycenter 360
    if not blocked_directions["5_4"]["west"]:
        button xcenter 240 ycenter 260 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_4_4", j=True)]
        text "西\nWEST" xcenter 240 ycenter 260
    if not blocked_directions["5_4"]["east"]:
        button xcenter 1140 ycenter 460 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_6_4", j=True)]
        text "東\nEAST" xcenter 1140 ycenter 460
    if not blocked_directions["5_4"]["south"]:
        button xcenter 640 ycenter 680 xysize (1280, 100) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_5_3", j=True)]
        text "南\nSOUTH" xcenter 640 ycenter 680

screen deep_forest_5_5:
    style_prefix "explore"
    if not blocked_directions["5_5"]["north"]:
        button xcenter 740 ycenter 360 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_5_6", j=True)]
        text "北\nNORTH" xcenter 740 ycenter 360
    if not blocked_directions["5_5"]["west"]:
        button xcenter 240 ycenter 260 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_4_5", j=True)]
        text "西\nWEST" xcenter 240 ycenter 260
    if not blocked_directions["5_5"]["east"]:
        button xcenter 1140 ycenter 460 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_6_5", j=True)]
        text "東\nEAST" xcenter 1140 ycenter 460
    if not blocked_directions["5_5"]["south"]:
        button xcenter 640 ycenter 680 xysize (1280, 100) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_5_4", j=True)]
        text "南\nSOUTH" xcenter 640 ycenter 680

screen deep_forest_5_6:
    style_prefix "explore"
    if not blocked_directions["5_6"]["north"]:
        button xcenter 740 ycenter 360 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_5_7", j=True)]
        text "北\nNORTH" xcenter 740 ycenter 360
    if not blocked_directions["5_6"]["west"]:
        button xcenter 240 ycenter 260 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_4_6", j=True)]
        text "西\nWEST" xcenter 240 ycenter 260
    if not blocked_directions["5_6"]["east"]:
        button xcenter 1140 ycenter 460 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_6_6", j=True)]
        text "東\nEAST" xcenter 1140 ycenter 460
    if not blocked_directions["5_6"]["south"]:
        button xcenter 640 ycenter 680 xysize (1280, 100) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_5_5", j=True)]
        text "南\nSOUTH" xcenter 640 ycenter 680

screen deep_forest_5_7:
    style_prefix "explore"
    if not blocked_directions["5_7"]["north"]:
        button xcenter 740 ycenter 360 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_5_8", j=True)]
        text "北\nNORTH" xcenter 740 ycenter 360
    if not blocked_directions["5_7"]["west"]:
        button xcenter 240 ycenter 260 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_4_7", j=True)]
        text "西\nWEST" xcenter 240 ycenter 260
    if not blocked_directions["5_7"]["east"]:
        button xcenter 1140 ycenter 460 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_6_7", j=True)]
        text "東\nEAST" xcenter 1140 ycenter 460
    if not blocked_directions["5_7"]["south"]:
        button xcenter 640 ycenter 680 xysize (1280, 100) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_5_6", j=True)]
        text "南\nSOUTH" xcenter 640 ycenter 680

screen deep_forest_5_8:
    style_prefix "explore"
    if not blocked_directions["5_8"]["north"]:
        button xcenter 740 ycenter 360 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_5_9", j=True)]
        text "北\nNORTH" xcenter 740 ycenter 360
    if not blocked_directions["5_8"]["west"]:
        button xcenter 240 ycenter 260 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_4_8", j=True)]
        text "西\nWEST" xcenter 240 ycenter 260
    if not blocked_directions["5_8"]["east"]:
        button xcenter 1140 ycenter 460 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_6_8", j=True)]
        text "東\nEAST" xcenter 1140 ycenter 460
    if not blocked_directions["5_8"]["south"]:
        button xcenter 640 ycenter 680 xysize (1280, 100) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_5_7", j=True)]
        text "南\nSOUTH" xcenter 640 ycenter 680

screen deep_forest_5_9:
    style_prefix "explore"
    if not blocked_directions["5_9"]["north"]:
        button xcenter 740 ycenter 360 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_5_10", j=True)]
        text "北\nNORTH" xcenter 740 ycenter 360
    if not blocked_directions["5_9"]["west"]:
        button xcenter 240 ycenter 260 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_4_9", j=True)]
        text "西\nWEST" xcenter 240 ycenter 260
    if not blocked_directions["5_9"]["east"]:
        button xcenter 1140 ycenter 460 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_6_9", j=True)]
        text "東\nEAST" xcenter 1140 ycenter 460
    if not blocked_directions["5_9"]["south"]:
        button xcenter 640 ycenter 680 xysize (1280, 100) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_5_8", j=True)]
        text "南\nSOUTH" xcenter 640 ycenter 680

screen deep_forest_6_0:
    style_prefix "explore"
    if not blocked_directions["6_0"]["north"]:
        button xcenter 740 ycenter 360 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_6_1", j=True)]
        text "北\nNORTH" xcenter 740 ycenter 360
    if not blocked_directions["6_0"]["west"]:
        button xcenter 240 ycenter 260 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_5_0", j=True)]
        text "西\nWEST" xcenter 240 ycenter 260
    if not blocked_directions["6_0"]["east"]:
        button xcenter 1140 ycenter 460 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_7_0", j=True)]
        text "東\nEAST" xcenter 1140 ycenter 460
    if not blocked_directions["6_0"]["south"]:
        button xcenter 640 ycenter 680 xysize (1280, 100) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_6_-1", j=True)]
        text "南\nSOUTH" xcenter 640 ycenter 680

screen deep_forest_6_1:
    style_prefix "explore"
    if not blocked_directions["6_1"]["north"]:
        button xcenter 740 ycenter 360 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_6_2", j=True)]
        text "北\nNORTH" xcenter 740 ycenter 360
    if not blocked_directions["6_1"]["west"]:
        button xcenter 240 ycenter 260 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_5_1", j=True)]
        text "西\nWEST" xcenter 240 ycenter 260
    if not blocked_directions["6_1"]["east"]:
        button xcenter 1140 ycenter 460 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_7_1", j=True)]
        text "東\nEAST" xcenter 1140 ycenter 460
    if not blocked_directions["6_1"]["south"]:
        button xcenter 640 ycenter 680 xysize (1280, 100) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_6_0", j=True)]
        text "南\nSOUTH" xcenter 640 ycenter 680

screen deep_forest_6_2:
    style_prefix "explore"
    if not blocked_directions["6_2"]["north"]:
        button xcenter 740 ycenter 360 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_6_3", j=True)]
        text "北\nNORTH" xcenter 740 ycenter 360
    if not blocked_directions["6_2"]["west"]:
        button xcenter 240 ycenter 260 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_5_2", j=True)]
        text "西\nWEST" xcenter 240 ycenter 260
    if not blocked_directions["6_2"]["east"]:
        button xcenter 1140 ycenter 460 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_7_2", j=True)]
        text "東\nEAST" xcenter 1140 ycenter 460
    if not blocked_directions["6_2"]["south"]:
        button xcenter 640 ycenter 680 xysize (1280, 100) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_6_1", j=True)]
        text "南\nSOUTH" xcenter 640 ycenter 680

screen deep_forest_6_3:
    style_prefix "explore"
    if not blocked_directions["6_3"]["north"]:
        button xcenter 740 ycenter 360 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_6_4", j=True)]
        text "北\nNORTH" xcenter 740 ycenter 360
    if not blocked_directions["6_3"]["west"]:
        button xcenter 240 ycenter 260 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_5_3", j=True)]
        text "西\nWEST" xcenter 240 ycenter 260
    if not blocked_directions["6_3"]["east"]:
        button xcenter 1140 ycenter 460 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_7_3", j=True)]
        text "東\nEAST" xcenter 1140 ycenter 460
    if not blocked_directions["6_3"]["south"]:
        button xcenter 640 ycenter 680 xysize (1280, 100) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_6_2", j=True)]
        text "南\nSOUTH" xcenter 640 ycenter 680

screen deep_forest_6_4:
    style_prefix "explore"
    if not blocked_directions["6_4"]["north"]:
        button xcenter 740 ycenter 360 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_6_5", j=True)]
        text "北\nNORTH" xcenter 740 ycenter 360
    if not blocked_directions["6_4"]["west"]:
        button xcenter 240 ycenter 260 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_5_4", j=True)]
        text "西\nWEST" xcenter 240 ycenter 260
    if not blocked_directions["6_4"]["east"]:
        button xcenter 1140 ycenter 460 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_7_4", j=True)]
        text "東\nEAST" xcenter 1140 ycenter 460
    if not blocked_directions["6_4"]["south"]:
        button xcenter 640 ycenter 680 xysize (1280, 100) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_6_3", j=True)]
        text "南\nSOUTH" xcenter 640 ycenter 680

screen deep_forest_6_5:
    style_prefix "explore"
    if not blocked_directions["6_5"]["north"]:
        button xcenter 740 ycenter 360 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_6_6", j=True)]
        text "北\nNORTH" xcenter 740 ycenter 360
    if not blocked_directions["6_5"]["west"]:
        button xcenter 240 ycenter 260 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_5_5", j=True)]
        text "西\nWEST" xcenter 240 ycenter 260
    if not blocked_directions["6_5"]["east"]:
        button xcenter 1140 ycenter 460 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_7_5", j=True)]
        text "東\nEAST" xcenter 1140 ycenter 460
    if not blocked_directions["6_5"]["south"]:
        button xcenter 640 ycenter 680 xysize (1280, 100) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_6_4", j=True)]
        text "南\nSOUTH" xcenter 640 ycenter 680

screen deep_forest_6_6:
    style_prefix "explore"
    if not blocked_directions["6_6"]["north"]:
        button xcenter 740 ycenter 360 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_6_7", j=True)]
        text "北\nNORTH" xcenter 740 ycenter 360
    if not blocked_directions["6_6"]["west"]:
        button xcenter 240 ycenter 260 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_5_6", j=True)]
        text "西\nWEST" xcenter 240 ycenter 260
    if not blocked_directions["6_6"]["east"]:
        button xcenter 1140 ycenter 460 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_7_6", j=True)]
        text "東\nEAST" xcenter 1140 ycenter 460
    if not blocked_directions["6_6"]["south"]:
        button xcenter 640 ycenter 680 xysize (1280, 100) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_6_5", j=True)]
        text "南\nSOUTH" xcenter 640 ycenter 680

screen deep_forest_6_7:
    style_prefix "explore"
    if not blocked_directions["6_7"]["north"]:
        button xcenter 740 ycenter 360 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_6_8", j=True)]
        text "北\nNORTH" xcenter 740 ycenter 360
    if not blocked_directions["6_7"]["west"]:
        button xcenter 240 ycenter 260 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_5_7", j=True)]
        text "西\nWEST" xcenter 240 ycenter 260
    if not blocked_directions["6_7"]["east"]:
        button xcenter 1140 ycenter 460 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_7_7", j=True)]
        text "東\nEAST" xcenter 1140 ycenter 460
    if not blocked_directions["6_7"]["south"]:
        button xcenter 640 ycenter 680 xysize (1280, 100) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_6_6", j=True)]
        text "南\nSOUTH" xcenter 640 ycenter 680

screen deep_forest_6_8:
    style_prefix "explore"
    if not blocked_directions["6_8"]["north"]:
        button xcenter 740 ycenter 360 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_6_9", j=True)]
        text "北\nNORTH" xcenter 740 ycenter 360
    if not blocked_directions["6_8"]["west"]:
        button xcenter 240 ycenter 260 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_5_8", j=True)]
        text "西\nWEST" xcenter 240 ycenter 260
    if not blocked_directions["6_8"]["east"]:
        button xcenter 1140 ycenter 460 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_7_8", j=True)]
        text "東\nEAST" xcenter 1140 ycenter 460
    if not blocked_directions["6_8"]["south"]:
        button xcenter 640 ycenter 680 xysize (1280, 100) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_6_7", j=True)]
        text "南\nSOUTH" xcenter 640 ycenter 680

screen deep_forest_6_9:
    style_prefix "explore"
    if not blocked_directions["6_9"]["north"]:
        button xcenter 740 ycenter 360 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_6_10", j=True)]
        text "北\nNORTH" xcenter 740 ycenter 360
    if not blocked_directions["6_9"]["west"]:
        button xcenter 240 ycenter 260 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_5_9", j=True)]
        text "西\nWEST" xcenter 240 ycenter 260
    if not blocked_directions["6_9"]["east"]:
        button xcenter 1140 ycenter 460 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_7_9", j=True)]
        text "東\nEAST" xcenter 1140 ycenter 460
    if not blocked_directions["6_9"]["south"]:
        button xcenter 640 ycenter 680 xysize (1280, 100) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_6_8", j=True)]
        text "南\nSOUTH" xcenter 640 ycenter 680

screen deep_forest_7_0:
    style_prefix "explore"
    if not blocked_directions["7_0"]["north"]:
        button xcenter 740 ycenter 360 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_7_1", j=True)]
        text "北\nNORTH" xcenter 740 ycenter 360
    if not blocked_directions["7_0"]["west"]:
        button xcenter 240 ycenter 260 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_6_0", j=True)]
        text "西\nWEST" xcenter 240 ycenter 260
    if not blocked_directions["7_0"]["east"]:
        button xcenter 1140 ycenter 460 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_8_0", j=True)]
        text "東\nEAST" xcenter 1140 ycenter 460
    if not blocked_directions["7_0"]["south"]:
        button xcenter 640 ycenter 680 xysize (1280, 100) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_7_-1", j=True)]
        text "南\nSOUTH" xcenter 640 ycenter 680

screen deep_forest_7_1:
    style_prefix "explore"
    if not blocked_directions["7_1"]["north"]:
        button xcenter 740 ycenter 360 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_7_2", j=True)]
        text "北\nNORTH" xcenter 740 ycenter 360
    if not blocked_directions["7_1"]["west"]:
        button xcenter 240 ycenter 260 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_6_1", j=True)]
        text "西\nWEST" xcenter 240 ycenter 260
    if not blocked_directions["7_1"]["east"]:
        button xcenter 1140 ycenter 460 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_8_1", j=True)]
        text "東\nEAST" xcenter 1140 ycenter 460
    if not blocked_directions["7_1"]["south"]:
        button xcenter 640 ycenter 680 xysize (1280, 100) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_7_0", j=True)]
        text "南\nSOUTH" xcenter 640 ycenter 680

screen deep_forest_7_2:
    style_prefix "explore"
    if not blocked_directions["7_2"]["north"]:
        button xcenter 740 ycenter 360 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_7_3", j=True)]
        text "北\nNORTH" xcenter 740 ycenter 360
    if not blocked_directions["7_2"]["west"]:
        button xcenter 240 ycenter 260 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_6_2", j=True)]
        text "西\nWEST" xcenter 240 ycenter 260
    if not blocked_directions["7_2"]["east"]:
        button xcenter 1140 ycenter 460 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_8_2", j=True)]
        text "東\nEAST" xcenter 1140 ycenter 460
    if not blocked_directions["7_2"]["south"]:
        button xcenter 640 ycenter 680 xysize (1280, 100) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_7_1", j=True)]
        text "南\nSOUTH" xcenter 640 ycenter 680

screen deep_forest_7_3:
    style_prefix "explore"
    if not blocked_directions["7_3"]["north"]:
        button xcenter 740 ycenter 360 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_7_4", j=True)]
        text "北\nNORTH" xcenter 740 ycenter 360
    if not blocked_directions["7_3"]["west"]:
        button xcenter 240 ycenter 260 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_6_3", j=True)]
        text "西\nWEST" xcenter 240 ycenter 260
    if not blocked_directions["7_3"]["east"]:
        button xcenter 1140 ycenter 460 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_8_3", j=True)]
        text "東\nEAST" xcenter 1140 ycenter 460
    if not blocked_directions["7_3"]["south"]:
        button xcenter 640 ycenter 680 xysize (1280, 100) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_7_2", j=True)]
        text "南\nSOUTH" xcenter 640 ycenter 680

screen deep_forest_7_4:
    style_prefix "explore"
    if not blocked_directions["7_4"]["north"]:
        button xcenter 740 ycenter 360 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_7_5", j=True)]
        text "北\nNORTH" xcenter 740 ycenter 360
    if not blocked_directions["7_4"]["west"]:
        button xcenter 240 ycenter 260 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_6_4", j=True)]
        text "西\nWEST" xcenter 240 ycenter 260
    if not blocked_directions["7_4"]["east"]:
        button xcenter 1140 ycenter 460 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_8_4", j=True)]
        text "東\nEAST" xcenter 1140 ycenter 460
    if not blocked_directions["7_4"]["south"]:
        button xcenter 640 ycenter 680 xysize (1280, 100) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_7_3", j=True)]
        text "南\nSOUTH" xcenter 640 ycenter 680

screen deep_forest_7_5:
    style_prefix "explore"
    if not blocked_directions["7_5"]["north"]:
        button xcenter 740 ycenter 360 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_7_6", j=True)]
        text "北\nNORTH" xcenter 740 ycenter 360
    if not blocked_directions["7_5"]["west"]:
        button xcenter 240 ycenter 260 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_6_5", j=True)]
        text "西\nWEST" xcenter 240 ycenter 260
    if not blocked_directions["7_5"]["east"]:
        button xcenter 1140 ycenter 460 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_8_5", j=True)]
        text "東\nEAST" xcenter 1140 ycenter 460
    if not blocked_directions["7_5"]["south"]:
        button xcenter 640 ycenter 680 xysize (1280, 100) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_7_4", j=True)]
        text "南\nSOUTH" xcenter 640 ycenter 680

screen deep_forest_7_6:
    style_prefix "explore"
    if not blocked_directions["7_6"]["north"]:
        button xcenter 740 ycenter 360 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_7_7", j=True)]
        text "北\nNORTH" xcenter 740 ycenter 360
    if not blocked_directions["7_6"]["west"]:
        button xcenter 240 ycenter 260 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_6_6", j=True)]
        text "西\nWEST" xcenter 240 ycenter 260
    if not blocked_directions["7_6"]["east"]:
        button xcenter 1140 ycenter 460 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_8_6", j=True)]
        text "東\nEAST" xcenter 1140 ycenter 460
    if not blocked_directions["7_6"]["south"]:
        button xcenter 640 ycenter 680 xysize (1280, 100) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_7_5", j=True)]
        text "南\nSOUTH" xcenter 640 ycenter 680

screen deep_forest_7_7:
    style_prefix "explore"
    if not blocked_directions["7_7"]["north"]:
        button xcenter 740 ycenter 360 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_7_8", j=True)]
        text "北\nNORTH" xcenter 740 ycenter 360
    if not blocked_directions["7_7"]["west"]:
        button xcenter 240 ycenter 260 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_6_7", j=True)]
        text "西\nWEST" xcenter 240 ycenter 260
    if not blocked_directions["7_7"]["east"]:
        button xcenter 1140 ycenter 460 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_8_7", j=True)]
        text "東\nEAST" xcenter 1140 ycenter 460
    if not blocked_directions["7_7"]["south"]:
        button xcenter 640 ycenter 680 xysize (1280, 100) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_7_6", j=True)]
        text "南\nSOUTH" xcenter 640 ycenter 680

screen deep_forest_7_8:
    style_prefix "explore"
    if not blocked_directions["7_8"]["north"]:
        button xcenter 740 ycenter 360 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_7_9", j=True)]
        text "北\nNORTH" xcenter 740 ycenter 360
    if not blocked_directions["7_8"]["west"]:
        button xcenter 240 ycenter 260 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_6_8", j=True)]
        text "西\nWEST" xcenter 240 ycenter 260
    if not blocked_directions["7_8"]["east"]:
        button xcenter 1140 ycenter 460 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_8_8", j=True)]
        text "東\nEAST" xcenter 1140 ycenter 460
    if not blocked_directions["7_8"]["south"]:
        button xcenter 640 ycenter 680 xysize (1280, 100) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_7_7", j=True)]
        text "南\nSOUTH" xcenter 640 ycenter 680

screen deep_forest_7_9:
    style_prefix "explore"
    if not blocked_directions["7_9"]["north"]:
        button xcenter 740 ycenter 360 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_7_10", j=True)]
        text "北\nNORTH" xcenter 740 ycenter 360
    if not blocked_directions["7_9"]["west"]:
        button xcenter 240 ycenter 260 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_6_9", j=True)]
        text "西\nWEST" xcenter 240 ycenter 260
    if not blocked_directions["7_9"]["east"]:
        button xcenter 1140 ycenter 460 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_8_9", j=True)]
        text "東\nEAST" xcenter 1140 ycenter 460
    if not blocked_directions["7_9"]["south"]:
        button xcenter 640 ycenter 680 xysize (1280, 100) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_7_8", j=True)]
        text "南\nSOUTH" xcenter 640 ycenter 680

screen deep_forest_8_0:
    style_prefix "explore"
    if not blocked_directions["8_0"]["north"]:
        button xcenter 740 ycenter 360 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_8_1", j=True)]
        text "北\nNORTH" xcenter 740 ycenter 360
    if not blocked_directions["8_0"]["west"]:
        button xcenter 240 ycenter 260 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_7_0", j=True)]
        text "西\nWEST" xcenter 240 ycenter 260
    if not blocked_directions["8_0"]["east"]:
        button xcenter 1140 ycenter 460 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_9_0", j=True)]
        text "東\nEAST" xcenter 1140 ycenter 460
    if not blocked_directions["8_0"]["south"]:
        button xcenter 640 ycenter 680 xysize (1280, 100) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_8_-1", j=True)]
        text "南\nSOUTH" xcenter 640 ycenter 680

screen deep_forest_8_1:
    style_prefix "explore"
    if not blocked_directions["8_1"]["north"]:
        button xcenter 740 ycenter 360 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_8_2", j=True)]
        text "北\nNORTH" xcenter 740 ycenter 360
    if not blocked_directions["8_1"]["west"]:
        button xcenter 240 ycenter 260 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_7_1", j=True)]
        text "西\nWEST" xcenter 240 ycenter 260
    if not blocked_directions["8_1"]["east"]:
        button xcenter 1140 ycenter 460 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_9_1", j=True)]
        text "東\nEAST" xcenter 1140 ycenter 460
    if not blocked_directions["8_1"]["south"]:
        button xcenter 640 ycenter 680 xysize (1280, 100) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_8_0", j=True)]
        text "南\nSOUTH" xcenter 640 ycenter 680

screen deep_forest_8_2:
    style_prefix "explore"
    if not blocked_directions["8_2"]["north"]:
        button xcenter 740 ycenter 360 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_8_3", j=True)]
        text "北\nNORTH" xcenter 740 ycenter 360
    if not blocked_directions["8_2"]["west"]:
        button xcenter 240 ycenter 260 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_7_2", j=True)]
        text "西\nWEST" xcenter 240 ycenter 260
    if not blocked_directions["8_2"]["east"]:
        button xcenter 1140 ycenter 460 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_9_2", j=True)]
        text "東\nEAST" xcenter 1140 ycenter 460
    if not blocked_directions["8_2"]["south"]:
        button xcenter 640 ycenter 680 xysize (1280, 100) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_8_1", j=True)]
        text "南\nSOUTH" xcenter 640 ycenter 680

screen deep_forest_8_3:
    style_prefix "explore"
    if not blocked_directions["8_3"]["north"]:
        button xcenter 740 ycenter 360 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_8_4", j=True)]
        text "北\nNORTH" xcenter 740 ycenter 360
    if not blocked_directions["8_3"]["west"]:
        button xcenter 240 ycenter 260 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_7_3", j=True)]
        text "西\nWEST" xcenter 240 ycenter 260
    if not blocked_directions["8_3"]["east"]:
        button xcenter 1140 ycenter 460 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_9_3", j=True)]
        text "東\nEAST" xcenter 1140 ycenter 460
    if not blocked_directions["8_3"]["south"]:
        button xcenter 640 ycenter 680 xysize (1280, 100) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_8_2", j=True)]
        text "南\nSOUTH" xcenter 640 ycenter 680

screen deep_forest_8_4:
    style_prefix "explore"
    if not blocked_directions["8_4"]["north"]:
        button xcenter 740 ycenter 360 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_8_5", j=True)]
        text "北\nNORTH" xcenter 740 ycenter 360
    if not blocked_directions["8_4"]["west"]:
        button xcenter 240 ycenter 260 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_7_4", j=True)]
        text "西\nWEST" xcenter 240 ycenter 260
    if not blocked_directions["8_4"]["east"]:
        button xcenter 1140 ycenter 460 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_9_4", j=True)]
        text "東\nEAST" xcenter 1140 ycenter 460
    if not blocked_directions["8_4"]["south"]:
        button xcenter 640 ycenter 680 xysize (1280, 100) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_8_3", j=True)]
        text "南\nSOUTH" xcenter 640 ycenter 680

screen deep_forest_8_5:
    style_prefix "explore"
    if not blocked_directions["8_5"]["north"]:
        button xcenter 740 ycenter 360 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_8_6", j=True)]
        text "北\nNORTH" xcenter 740 ycenter 360
    if not blocked_directions["8_5"]["west"]:
        button xcenter 240 ycenter 260 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_7_5", j=True)]
        text "西\nWEST" xcenter 240 ycenter 260
    if not blocked_directions["8_5"]["east"]:
        button xcenter 1140 ycenter 460 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_9_5", j=True)]
        text "東\nEAST" xcenter 1140 ycenter 460
    if not blocked_directions["8_5"]["south"]:
        button xcenter 640 ycenter 680 xysize (1280, 100) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_8_4", j=True)]
        text "南\nSOUTH" xcenter 640 ycenter 680

screen deep_forest_8_6:
    style_prefix "explore"
    if not blocked_directions["8_6"]["north"]:
        button xcenter 740 ycenter 360 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_8_7", j=True)]
        text "北\nNORTH" xcenter 740 ycenter 360
    if not blocked_directions["8_6"]["west"]:
        button xcenter 240 ycenter 260 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_7_6", j=True)]
        text "西\nWEST" xcenter 240 ycenter 260
    if not blocked_directions["8_6"]["east"]:
        button xcenter 1140 ycenter 460 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_9_6", j=True)]
        text "東\nEAST" xcenter 1140 ycenter 460
    if not blocked_directions["8_6"]["south"]:
        button xcenter 640 ycenter 680 xysize (1280, 100) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_8_5", j=True)]
        text "南\nSOUTH" xcenter 640 ycenter 680

screen deep_forest_8_7:
    style_prefix "explore"
    if not blocked_directions["8_7"]["north"]:
        button xcenter 740 ycenter 360 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_8_8", j=True)]
        text "北\nNORTH" xcenter 740 ycenter 360
    if not blocked_directions["8_7"]["west"]:
        button xcenter 240 ycenter 260 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_7_7", j=True)]
        text "西\nWEST" xcenter 240 ycenter 260
    if not blocked_directions["8_7"]["east"]:
        button xcenter 1140 ycenter 460 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_9_7", j=True)]
        text "東\nEAST" xcenter 1140 ycenter 460
    if not blocked_directions["8_7"]["south"]:
        button xcenter 640 ycenter 680 xysize (1280, 100) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_8_6", j=True)]
        text "南\nSOUTH" xcenter 640 ycenter 680

screen deep_forest_8_8:
    style_prefix "explore"
    if not blocked_directions["8_8"]["north"]:
        button xcenter 740 ycenter 360 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_8_9", j=True)]
        text "北\nNORTH" xcenter 740 ycenter 360
    if not blocked_directions["8_8"]["west"]:
        button xcenter 240 ycenter 260 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_7_8", j=True)]
        text "西\nWEST" xcenter 240 ycenter 260
    if not blocked_directions["8_8"]["east"]:
        button xcenter 1140 ycenter 460 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_9_8", j=True)]
        text "東\nEAST" xcenter 1140 ycenter 460
    if not blocked_directions["8_8"]["south"]:
        button xcenter 640 ycenter 680 xysize (1280, 100) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_8_7", j=True)]
        text "南\nSOUTH" xcenter 640 ycenter 680

screen deep_forest_8_9:
    style_prefix "explore"
    if not blocked_directions["8_9"]["north"]:
        button xcenter 740 ycenter 360 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_8_10", j=True)]
        text "北\nNORTH" xcenter 740 ycenter 360
    if not blocked_directions["8_9"]["west"]:
        button xcenter 240 ycenter 260 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_7_9", j=True)]
        text "西\nWEST" xcenter 240 ycenter 260
    if not blocked_directions["8_9"]["east"]:
        button xcenter 1140 ycenter 460 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_9_9", j=True)]
        text "東\nEAST" xcenter 1140 ycenter 460
    if not blocked_directions["8_9"]["south"]:
        button xcenter 640 ycenter 680 xysize (1280, 100) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_8_8", j=True)]
        text "南\nSOUTH" xcenter 640 ycenter 680

screen deep_forest_9_0:
    style_prefix "explore"
    if not blocked_directions["9_0"]["north"]:
        button xcenter 740 ycenter 360 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_9_1", j=True)]
        text "北\nNORTH" xcenter 740 ycenter 360
    if not blocked_directions["9_0"]["west"]:
        button xcenter 240 ycenter 260 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_8_0", j=True)]
        text "西\nWEST" xcenter 240 ycenter 260
    if not blocked_directions["9_0"]["east"]:
        button xcenter 1140 ycenter 460 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_10_0", j=True)]
        text "東\nEAST" xcenter 1140 ycenter 460
    if not blocked_directions["9_0"]["south"]:
        button xcenter 640 ycenter 680 xysize (1280, 100) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_9_-1", j=True)]
        text "南\nSOUTH" xcenter 640 ycenter 680

screen deep_forest_9_1:
    style_prefix "explore"
    if not blocked_directions["9_1"]["north"]:
        button xcenter 740 ycenter 360 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_9_2", j=True)]
        text "北\nNORTH" xcenter 740 ycenter 360
    if not blocked_directions["9_1"]["west"]:
        button xcenter 240 ycenter 260 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_8_1", j=True)]
        text "西\nWEST" xcenter 240 ycenter 260
    if not blocked_directions["9_1"]["east"]:
        button xcenter 1140 ycenter 460 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_10_1", j=True)]
        text "東\nEAST" xcenter 1140 ycenter 460
    if not blocked_directions["9_1"]["south"]:
        button xcenter 640 ycenter 680 xysize (1280, 100) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_9_0", j=True)]
        text "南\nSOUTH" xcenter 640 ycenter 680

screen deep_forest_9_2:
    style_prefix "explore"
    if not blocked_directions["9_2"]["north"]:
        button xcenter 740 ycenter 360 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_9_3", j=True)]
        text "北\nNORTH" xcenter 740 ycenter 360
    if not blocked_directions["9_2"]["west"]:
        button xcenter 240 ycenter 260 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_8_2", j=True)]
        text "西\nWEST" xcenter 240 ycenter 260
    if not blocked_directions["9_2"]["east"]:
        button xcenter 1140 ycenter 460 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_10_2", j=True)]
        text "東\nEAST" xcenter 1140 ycenter 460
    if not blocked_directions["9_2"]["south"]:
        button xcenter 640 ycenter 680 xysize (1280, 100) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_9_1", j=True)]
        text "南\nSOUTH" xcenter 640 ycenter 680

screen deep_forest_9_3:
    style_prefix "explore"
    if not blocked_directions["9_3"]["north"]:
        button xcenter 740 ycenter 360 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_9_4", j=True)]
        text "北\nNORTH" xcenter 740 ycenter 360
    if not blocked_directions["9_3"]["west"]:
        button xcenter 240 ycenter 260 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_8_3", j=True)]
        text "西\nWEST" xcenter 240 ycenter 260
    if not blocked_directions["9_3"]["east"]:
        button xcenter 1140 ycenter 460 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_10_3", j=True)]
        text "東\nEAST" xcenter 1140 ycenter 460
    if not blocked_directions["9_3"]["south"]:
        button xcenter 640 ycenter 680 xysize (1280, 100) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_9_2", j=True)]
        text "南\nSOUTH" xcenter 640 ycenter 680

screen deep_forest_9_4:
    style_prefix "explore"
    if not blocked_directions["9_4"]["north"]:
        button xcenter 740 ycenter 360 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_9_5", j=True)]
        text "北\nNORTH" xcenter 740 ycenter 360
    if not blocked_directions["9_4"]["west"]:
        button xcenter 240 ycenter 260 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_8_4", j=True)]
        text "西\nWEST" xcenter 240 ycenter 260
    if not blocked_directions["9_4"]["east"]:
        button xcenter 1140 ycenter 460 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_10_4", j=True)]
        text "東\nEAST" xcenter 1140 ycenter 460
    if not blocked_directions["9_4"]["south"]:
        button xcenter 640 ycenter 680 xysize (1280, 100) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_9_3", j=True)]
        text "南\nSOUTH" xcenter 640 ycenter 680

screen deep_forest_9_5:
    style_prefix "explore"
    if not blocked_directions["9_5"]["north"]:
        button xcenter 740 ycenter 360 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_9_6", j=True)]
        text "北\nNORTH" xcenter 740 ycenter 360
    if not blocked_directions["9_5"]["west"]:
        button xcenter 240 ycenter 260 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_8_5", j=True)]
        text "西\nWEST" xcenter 240 ycenter 260
    if not blocked_directions["9_5"]["east"]:
        button xcenter 1140 ycenter 460 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_10_5", j=True)]
        text "東\nEAST" xcenter 1140 ycenter 460
    if not blocked_directions["9_5"]["south"]:
        button xcenter 640 ycenter 680 xysize (1280, 100) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_9_4", j=True)]
        text "南\nSOUTH" xcenter 640 ycenter 680

screen deep_forest_9_6:
    style_prefix "explore"
    if not blocked_directions["9_6"]["north"]:
        button xcenter 740 ycenter 360 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_9_7", j=True)]
        text "北\nNORTH" xcenter 740 ycenter 360
    if not blocked_directions["9_6"]["west"]:
        button xcenter 240 ycenter 260 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_8_6", j=True)]
        text "西\nWEST" xcenter 240 ycenter 260
    if not blocked_directions["9_6"]["east"]:
        button xcenter 1140 ycenter 460 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_10_6", j=True)]
        text "東\nEAST" xcenter 1140 ycenter 460
    if not blocked_directions["9_6"]["south"]:
        button xcenter 640 ycenter 680 xysize (1280, 100) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_9_5", j=True)]
        text "南\nSOUTH" xcenter 640 ycenter 680

screen deep_forest_9_7:
    style_prefix "explore"
    if not blocked_directions["9_7"]["north"]:
        button xcenter 740 ycenter 360 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_9_8", j=True)]
        text "北\nNORTH" xcenter 740 ycenter 360
    if not blocked_directions["9_7"]["west"]:
        button xcenter 240 ycenter 260 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_8_7", j=True)]
        text "西\nWEST" xcenter 240 ycenter 260
    if not blocked_directions["9_7"]["east"]:
        button xcenter 1140 ycenter 460 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_10_7", j=True)]
        text "東\nEAST" xcenter 1140 ycenter 460
    if not blocked_directions["9_7"]["south"]:
        button xcenter 640 ycenter 680 xysize (1280, 100) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_9_6", j=True)]
        text "南\nSOUTH" xcenter 640 ycenter 680

screen deep_forest_9_8:
    style_prefix "explore"
    if not blocked_directions["9_8"]["north"]:
        button xcenter 740 ycenter 360 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_9_9", j=True)]
        text "北\nNORTH" xcenter 740 ycenter 360
    if not blocked_directions["9_8"]["west"]:
        button xcenter 240 ycenter 260 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_8_8", j=True)]
        text "西\nWEST" xcenter 240 ycenter 260
    if not blocked_directions["9_8"]["east"]:
        button xcenter 1140 ycenter 460 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_10_8", j=True)]
        text "東\nEAST" xcenter 1140 ycenter 460
    if not blocked_directions["9_8"]["south"]:
        button xcenter 640 ycenter 680 xysize (1280, 100) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_9_7", j=True)]
        text "南\nSOUTH" xcenter 640 ycenter 680

screen deep_forest_9_9:
    style_prefix "explore"
    if blocked_directions["9_9"]["north"]:
        button xcenter 740 ycenter 360 xysize (200, 300) action [Play("sound", audio.door), Call("shed")]
        text "北\nNORTH" xcenter 740 ycenter 360
    if not blocked_directions["9_9"]["west"]:
        button xcenter 240 ycenter 260 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_8_9", j=True)]
        text "西\nWEST" xcenter 240 ycenter 260
    if not blocked_directions["9_9"]["east"]:
        button xcenter 1140 ycenter 460 xysize (200, 300) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_10_9", j=True)]
        text "東\nEAST" xcenter 1140 ycenter 460
    if not blocked_directions["9_9"]["south"]:
        button xcenter 640 ycenter 680 xysize (1280, 100) action [Play("sound", audio.grass_move), Call("next_location", "deep_forest_9_8", j=True)]
        text "南\nSOUTH" xcenter 640 ycenter 680