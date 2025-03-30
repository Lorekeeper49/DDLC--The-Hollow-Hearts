label shed:
    scene bg shed_night with Fade(0.25, 0.0, 0.25)
    $ renpy.music.set_volume(0.3, delay=0, channel="ambience")
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
            if not "Dominion Left Behind" in persistent.choices_made:
                $ persistent.choices_made.append("Dominion Left Behind")
            return
    if calm >= 3 and stress < calm:
        d "Okay, I'm calm.  I'm calm."
        a "You good?"
        d "Yeah, I'm good."
        d "I'll head back to the school in a bit."
        a "Okay."
        a "Whew."
        if not "Dominion Calm" in persistent.choices_made:
            $ persistent.choices_made.append("Dominion Calm")
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
            a "Your attribute seems dangerous."
            a "But we've all been through worse."
            a "We can help you out."
        "Be Stressful" if not Stressful:
            $ Stressful = True
            $ stress += 1
            a "This is probably pretty obvious."
            a "But you need to calm down."
            a "Things will look pretty bad here if you don't."
        "Be Direct" if not Direct:
            $ Direct = True
            $ calm += 1
            a "Your attribute may be scary."
            a "But it's only as dangerous as you make it."
            a "Lighten up a little."
        "Be Vague" if not Vague:
            $ Vague = True
            $ stress += 1
            a "It doesn't like emotion."
            a "Remove the emotion from the scene."
            a "We don't want distress."
        "Be Smart" if not Smart:
            $ Smart = True
            $ calm += 1
            a "Your attribute is powerful, and certainly dangerous."
            a "But it will only kill us if you let it."
            a "Don't let it."
        "Be Stupid" if not Stupid:
            $ Stupid = True
            $ stress += 1
            a "I don't know anything about your attribute."
            a "But it shouldn't be a problem."
            a "Just trust me."
        "Be Happy" if not Happy:
            $ Happy = True
            $ calm += 1
            a "I'm glad to know what your attribute is."
            a "I just need you to calm down."
            a "Okay?"
        "Be Angry" if not Angry:
            $ Angry = True
            $ stress += 1
            a "This is kind of cowardly."
            a "Hiding your attribute like this."
            a "You could've at least given a warning."
        "Stop convincing him":
            "Let's stop here."
            return
    d "..."
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
    show kotonoha turned casual rhip zorder 3 at l31
    a "Kotonoha?"
    a "Do the same thing you did to help train me to use storm."
    a "Clearly he's a rampant image, so use that as your reference."
    scene black with dissolve_scene
    "A rampant image has the ability to turn into a terrifying monster to rampage everywhere."
    "This monster has the same mass as the host and is controlled by the same mind."
    "It is a parasite that isn't... life-threatening."
    "...Couldn't think of a better word."
    scene bg shed_night
    show dominion zorder 2 at t11
    with dissolve_scene
    d "I think... I understand."
    d "I can use this... to fight."
    a "You calm?"
    d "I think so..."
    a "Good."
    d "Hey, can I come with you guys?"
    a "I think it's better if you get some rest."
    a "You've had a terrifying day."
    d "Right, I'll head home then."
    d "I'll text you tomorrow."
    a "Okay."
    hide dominion
    "He leaves."
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
    lil "{b}You got it!{/b}"
    play sound thunder
    scene bg storm
    show dominion zorder 2 at t11
    with flash
    play ambience epic_storm
    $ renpy.music.set_volume(1.0, delay=0, channel="ambience")
    "Come on Aoruguri, you can do this!"
    show lilly casual doll a0 zorder 2 at r44
    "Work with Lilly, and pull him out!"
    scene bg deep_forest with ZoomTransition
    "He's calling for help."
    scene black
    show dominion zorder 2 at t11
    with blink
    $ renpy.music.set_volume(0.3, delay=0, channel="ambience")
    d "I need your help."
    d "I can't fight this forever."
    a "Brother, I'm here for you."
    "Huh?"
    "What is...?"
    play sound thunder
    scene bg storm with flash
    $ renpy.music.set_volume(1.0, delay=0, channel="ambience")
    "What's happenning?"
    "I can't control what I'm doing!"
    a "Everyone!  Help me out!"
    show kotonoha turned casual angr zorder 2 at r22
    "What?"
    show kotonoha at lhide
    hide kotonoha
    "I don't need their help."
    show akira uniform cross g zorder 2 at l21
    "I just need Lilly's!"
    show akira at rhide
    hide akira
    "They don't need to be here."
    show akira uniform cross g zorder 2 at r22
    show kotonoha turned casual angr zorder 2 at l21
    "They're busy with..."
    show kotonoha at t11
    show akira at t11
    $ pause(0.01)
    hide akira
    hide kotonoha
    with flash
    d "AAAAAAAAAAAAAAAAHHHHH!!!"
    a "DOMINION!"
    "What am I doing?"
    "No stop!"
    a "STOP THIS!!"
    "Not that!"
    "That's gonna kill him!"
    a "WAKE UUUUUUUUUUUUPPPPPP!!!{nw}"
    show white onlayer foreground at noisefade(0.0, 1.0)
    "HOLD BAAAAAAAAAACCCKKK!!!{w=1}{nw}"
    hide white onlayer foreground
    stop ambience
    scene bg deep_forest with Shake((0, 0, 0, 0), 5.0, dist=50)
    $ pause(1.0)
    show dominion zorder 2 at t11
    $ pause(1.0)
    a "Shit!"
    "What did I just..."
    a "Is he okay?"
    show kotonoha turned casual neut zorder 2 at t22
    k "..."
    a "Kotonoha!"
    k worr ce om "No..."
    a "What...?"
    k rhip oe "He's not okay.  But at least he's alive."
    k rdown "I got him."
    hide kotonoha
    hide dominion
    a "What was I doing?"
    a "Partway through that fight, it felt like I had no control over myself."
    a "And... near the end..."
    a "I was about to release a blow that would've killed him."
    show akira uniform cross l zorder 2 at t11
    ak "You were under extreme stress."
    a "What?"
    ak turned rout lout "When people are under emotional distress, they tend to do things beyond their own control."
    a "I..."
    hide akira
    show mari forward happ zorder 2 at t11
    ma om "Hey, hey!  You're okay, you did great."
    ma "He's subdued."
    ma "You can calm down now."
    ma "I'm proud of you."
    show mari cm
    a "Yeah...  Thanks Mari."
    if not "Dominion Burst" in persistent.choices_made:
        $ persistent.choices_made.append("Dominion Burst")
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
    if not "Dominion Left Behind" in persistent.choices_made:
        $ persistent.choices_made.append("Dominion Left Behind")
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
    def randomize_blockages(start):
        while True:
            reset_blockages()
            for coords in blocked_directions:
                for direction in blocked_directions[coords]:
                    if not blocked_directions[coords][direction]:
                        blocked_directions[coords][direction] = random_chance(60)
            if path_valid(start):
                break
    def path_valid(start):
        from collections import deque
        directions = {
            "north": (0, 1),
            "south": (0, -1),
            "east": (1, 0),
            "west": (-1, 0)
        }
        start_pos = map(int, start.split("_"))
        queue = deque([start_pos])
        visited = set()
        while queue:
            x, y = queue.popleft()
            current = f"{x}_{y}"
            if current in visited:
                continue
            visited.add(current)
            if current == "9_9":
                return True
            for direction, (dx, dy) in directions.items():
                new_x, new_y = x + dx, y + dy
                new_coord = f"{new_x}_{new_y}"
                if new_coord in blocked_directions and not blocked_directions[current].get(direction, True) and new_coord not in visited:
                    queue.append((new_x, new_y))
        return False
    def reset_blockages():
        for coords in blocked_directions:
            for direction in blocked_directions[coords]:
                if (coords[0] == "9" and direction == "north") or (coords[0] == "0" and direction == "south") or (coords[2] == "9" and direction == "east") or (coords[2] == "0" and direction == "west"):
                    blocked_directions[coords][direction] = True
                else:
                    blocked_directions[coords][direction] = False

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