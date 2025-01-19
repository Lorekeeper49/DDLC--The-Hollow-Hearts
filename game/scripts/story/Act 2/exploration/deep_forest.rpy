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