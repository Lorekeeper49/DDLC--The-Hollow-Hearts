label shed:
    scene bg shed with Fade(0.25, 0.0, 0.25)
    show dominion zorder 2 at t11
    a "Dominion!"
    a "Found you!"
    scene bg shed with dissolve_scene_full
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
    show kotonoha anno rhip ce om zorder 2 at r22
    k "I can assure you, we are not-"
    a "Just face it.  With the amount of dangers you guys throw yourselves into, you might as well take the name."
    k lup "You say that as a member of us."
    show kotonoha cm
    a "I'll just shut my fucking mouth then!"
    k ldown om "No, you're the only one who can talk to him properly."
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

    return

label no_shed:
    a "Shit!"
    a "This is taking too long."
    a "We should head back."
    a "He's probably already gone anyway."
    return

default blocked_directions = { # randomized each run
    "0_0": {"north": False, "south": False, "east": False, "west": False},
    "1_0": {"north": False, "south": False, "east": False, "west": False},
    "2_0": {"north": False, "south": False, "east": False, "west": False},
    "3_0": {"north": False, "south": False, "east": False, "west": False},
    "4_0": {"north": False, "south": False, "east": False, "west": False},
    "5_0": {"north": False, "south": False, "east": False, "west": False},
    "6_0": {"north": False, "south": False, "east": False, "west": False},
    "7_0": {"north": False, "south": False, "east": False, "west": False},
    "8_0": {"north": False, "south": False, "east": False, "west": False},
    "9_0": {"north": False, "south": False, "east": False, "west": False},
    "0_1": {"north": False, "south": False, "east": False, "west": False},
    "1_1": {"north": False, "south": False, "east": False, "west": False},
    "2_1": {"north": False, "south": False, "east": False, "west": False},
    "3_1": {"north": False, "south": False, "east": False, "west": False},
    "4_1": {"north": False, "south": False, "east": False, "west": False},
    "5_1": {"north": False, "south": False, "east": False, "west": False},
    "6_1": {"north": False, "south": False, "east": False, "west": False},
    "7_1": {"north": False, "south": False, "east": False, "west": False},
    "8_1": {"north": False, "south": False, "east": False, "west": False},
    "9_1": {"north": False, "south": False, "east": False, "west": False},
    "0_2": {"north": False, "south": False, "east": False, "west": False},
    "1_2": {"north": False, "south": False, "east": False, "west": False},
    "2_2": {"north": False, "south": False, "east": False, "west": False},
    "3_2": {"north": False, "south": False, "east": False, "west": False},
    "4_2": {"north": False, "south": False, "east": False, "west": False},
    "5_2": {"north": False, "south": False, "east": False, "west": False},
    "6_2": {"north": False, "south": False, "east": False, "west": False},
    "7_2": {"north": False, "south": False, "east": False, "west": False},
    "8_2": {"north": False, "south": False, "east": False, "west": False},
    "9_2": {"north": False, "south": False, "east": False, "west": False},
    "0_3": {"north": False, "south": False, "east": False, "west": False},
    "1_3": {"north": False, "south": False, "east": False, "west": False},
    "2_3": {"north": False, "south": False, "east": False, "west": False},
    "3_3": {"north": False, "south": False, "east": False, "west": False},
    "4_3": {"north": False, "south": False, "east": False, "west": False},
    "5_3": {"north": False, "south": False, "east": False, "west": False},
    "6_3": {"north": False, "south": False, "east": False, "west": False},
    "7_3": {"north": False, "south": False, "east": False, "west": False},
    "8_3": {"north": False, "south": False, "east": False, "west": False},
    "9_3": {"north": False, "south": False, "east": False, "west": False},
    "0_4": {"north": False, "south": False, "east": False, "west": False},
    "1_4": {"north": False, "south": False, "east": False, "west": False},
    "2_4": {"north": False, "south": False, "east": False, "west": False},
    "3_4": {"north": False, "south": False, "east": False, "west": False},
    "4_4": {"north": False, "south": False, "east": False, "west": False},
    "5_4": {"north": False, "south": False, "east": False, "west": False},
    "6_4": {"north": False, "south": False, "east": False, "west": False},
    "7_4": {"north": False, "south": False, "east": False, "west": False},
    "8_4": {"north": False, "south": False, "east": False, "west": False},
    "9_4": {"north": False, "south": False, "east": False, "west": False},
    "0_5": {"north": False, "south": False, "east": False, "west": False},
    "1_5": {"north": False, "south": False, "east": False, "west": False},
    "2_5": {"north": False, "south": False, "east": False, "west": False},
    "3_5": {"north": False, "south": False, "east": False, "west": False},
    "4_5": {"north": False, "south": False, "east": False, "west": False},
    "5_5": {"north": False, "south": False, "east": False, "west": False},
    "6_5": {"north": False, "south": False, "east": False, "west": False},
    "7_5": {"north": False, "south": False, "east": False, "west": False},
    "8_5": {"north": False, "south": False, "east": False, "west": False},
    "9_5": {"north": False, "south": False, "east": False, "west": False},
    "0_6": {"north": False, "south": False, "east": False, "west": False},
    "1_6": {"north": False, "south": False, "east": False, "west": False},
    "2_6": {"north": False, "south": False, "east": False, "west": False},
    "3_6": {"north": False, "south": False, "east": False, "west": False},
    "4_6": {"north": False, "south": False, "east": False, "west": False},
    "5_6": {"north": False, "south": False, "east": False, "west": False},
    "6_6": {"north": False, "south": False, "east": False, "west": False},
    "7_6": {"north": False, "south": False, "east": False, "west": False},
    "8_6": {"north": False, "south": False, "east": False, "west": False},
    "9_6": {"north": False, "south": False, "east": False, "west": False},
    "0_7": {"north": False, "south": False, "east": False, "west": False},
    "1_7": {"north": False, "south": False, "east": False, "west": False},
    "2_7": {"north": False, "south": False, "east": False, "west": False},
    "3_7": {"north": False, "south": False, "east": False, "west": False},
    "4_7": {"north": False, "south": False, "east": False, "west": False},
    "5_7": {"north": False, "south": False, "east": False, "west": False},
    "6_7": {"north": False, "south": False, "east": False, "west": False},
    "7_7": {"north": False, "south": False, "east": False, "west": False},
    "8_7": {"north": False, "south": False, "east": False, "west": False},
    "9_7": {"north": False, "south": False, "east": False, "west": False},
    "0_8": {"north": False, "south": False, "east": False, "west": False},
    "1_8": {"north": False, "south": False, "east": False, "west": False},
    "2_8": {"north": False, "south": False, "east": False, "west": False},
    "3_8": {"north": False, "south": False, "east": False, "west": False},
    "4_8": {"north": False, "south": False, "east": False, "west": False},
    "5_8": {"north": False, "south": False, "east": False, "west": False},
    "6_8": {"north": False, "south": False, "east": False, "west": False},
    "7_8": {"north": False, "south": False, "east": False, "west": False},
    "8_8": {"north": False, "south": False, "east": False, "west": False},
    "9_8": {"north": False, "south": False, "east": False, "west": False},
    "0_9": {"north": False, "south": False, "east": False, "west": False},
    "1_9": {"north": False, "south": False, "east": False, "west": False},
    "2_9": {"north": False, "south": False, "east": False, "west": False},
    "3_9": {"north": False, "south": False, "east": False, "west": False},
    "4_9": {"north": False, "south": False, "east": False, "west": False},
    "5_9": {"north": False, "south": False, "east": False, "west": False},
    "6_9": {"north": False, "south": False, "east": False, "west": False},
    "7_9": {"north": False, "south": False, "east": False, "west": False},
    "8_9": {"north": False, "south": False, "east": False, "west": False},
    "9_9": {"north": False, "south": False, "east": False, "west": False}
}