default wraith_beaten = False
image wraith_black = silhouetted("mod_assets/MPT/engeki/body.png",0,0,0)
image wraith_black1 = silhouetted("mod_assets/MPT/engeki/body.png",0,0,0)
image wraith_black2 = silhouetted("mod_assets/MPT/engeki/body.png",0,0,0)
image wraith_black3 = silhouetted("mod_assets/MPT/engeki/body.png",0,0,0)
image wraith_black4 = silhouetted("mod_assets/MPT/engeki/body.png",0,0,0)
screen wraith:
    zorder 200
    add "wraith_black"
    button xcenter 450 ycenter 200 xysize (200, 200) hovered SetVariable("wraith_beaten", True) unhovered SetVariable("wraith_beaten", False) action NullAction()
    timer 1.8 action Show("wraith_blink")
    timer 3.0 action [Hide("wraith_blink"), Hide("black_screen"), If(wraith_beaten, Hide("wraith"), Call("failure"))]

screen wraith_tut:
    add "wraith_black"
    button xcenter 450 ycenter 200 xysize (200, 200) hovered SetVariable("wraith_beaten", True) unhovered SetVariable("wraith_beaten", False) action NullAction()
    timer 1.8 action Show("wraith_blink")
    timer 3.0 action If(wraith_beaten, [Hide("wraith_blink"), Hide("black_screen"), Hide("wraith_tut"), SetVariable("wraith_beaten", False)]) repeat True

screen black_screen:
    add Solid("#000", xsize=2000, ysize=2000)

screen wraith_blink:
    timer 0.1 repeat True action Show("black_screen", _zorder=200)
    timer 0.075 repeat True action Hide("black_screen")

label failure:
    hide screen wraith
    hide screen flashlight
    play sound jumpscare
    show wraith_black zorder 1000 at face
    $ pause(0.25)
    scene black with None
    stop sound fadeout 3.0
    $ pause(3.0)
    return

screen first_room:
    style_prefix "explore"
    button xcenter 500 ycenter 300 xysize (200, 500) action [Play("sound", audio.door), Call("next_location", "bedroom1", w=True)]
    text "B\nE\nD\nR\nO\nO\nM" xcenter 500 ycenter 300
    button xcenter 1000 ycenter 300 xysize (300, 300) action [Play("sound", audio.footsteps), Call("next_location", "hall1", w=True)]
    text "FORWARD" xcenter 1000 ycenter 300

screen bedroom1:
    style_prefix "explore"
    button xcenter 640 ycenter 695 xysize (1280, 50) action [Play("sound", audio.door), Call("next_location", "first_room", w=True)]
    text "HALL" xcenter 640 ycenter 695

screen bedroom2:
    style_prefix "explore"
    button xcenter 500 ycenter 500 xysize (100, 150) action Call("nothing", "bedroom2")
    text "SEARCH" xcenter 500 ycenter 500
    button xcenter 640 ycenter 695 xysize (1280, 50) action [Play("sound", audio.door), Call("next_location", "hall1", w=True)]
    text "HALL" xcenter 640 ycenter 695

screen hall1:
    style_prefix "explore"
    button xcenter 1000 ycenter 300 xysize (300, 300) action [Play("sound", audio.footsteps), Call("next_location", "hall2", w=True)]
    text "FORWARD" xcenter 1000 ycenter 300
    button xcenter 640 ycenter 695 xysize (1280, 50) action [Play("sound", audio.footsteps), Call("next_location", "first_room", w=True)]
    text "BACK" xcenter 640 ycenter 695
    button xcenter 500 ycenter 300 xysize (200, 500) action [Play("sound", audio.door), Call("next_location", "bedroom2", w=True)]
    text "B\nE\nD\nR\nO\nO\nM" xcenter 500 ycenter 300
    button xcenter 700 ycenter 300 xysize (200, 500) action [Play("sound", audio.door), Call("next_location", "dark_kitchen", w=True)]
    text "K\nI\nT\nC\nH\nE\nN" xcenter 700 ycenter 300
    button xcenter 1200 ycenter 300 xysize (75, 500) action [Play("sound", audio.footsteps), Call("next_location", "storage", w=True)]
    text "S\nT\nO\nR\nA\nG\nE" xcenter 1200 ycenter 300

screen hall2:
    style_prefix "explore"
    button xcenter 150 ycenter 150 xysize (300, 300) action If("broken key" in inventory, [Play("sound", audio.door), Call("mansion_end")]) 
    text "FAMILIAR ROOM" xcenter 150 ycenter 150
    button xcenter 640 ycenter 695 xysize (1280, 50) action [Play("sound", audio.footsteps), Call("next_location", "hall1", w=True)]
    text "BACK" xcenter 640 ycenter 695

screen dark_kitchen:
    style_prefix "explore"
    button xcenter 450 ycenter 200 xysize (175, 400) action Call("nothing", "dark_kitchen")
    text "SEARCH" xcenter 450 ycenter 200
    button xcenter 650 ycenter 200 xysize (225, 400) action Call("nothing", "dark_kitchen")
    text "SEARCH" xcenter 650 ycenter 200
    button xcenter 915 ycenter 100 xysize (300, 200) action Call("nothing", "dark_kitchen")
    text "SEARCH" xcenter 915 ycenter 100
    button xcenter 300 ycenter 200 xysize (100, 400) action Call("nothing", "dark_kitchen")
    text "S\nE\nA\nR\nC\nH" xcenter 300 ycenter 200
    button xcenter 1175 ycenter 200 xysize (200, 350) action If("broken key" in inventory, Call("nothing", "dark_kitchen"), Call("something", "broken key", "dark_kitchen"))
    text "SEARCH" xcenter 1175 ycenter 200
    button xcenter 640 ycenter 695 xysize (1280, 50) action [Play("sound", audio.door), Call("next_location", "hall1", w=True)]
    text "HALL" xcenter 640 ycenter 695

screen storage:
    style_prefix "explore"
    button xcenter 640 ycenter 695 xysize (1280, 50) action [Play("sound", audio.footsteps), Call("next_location", "hall1", w=True)]
    text "BACK" xcenter 640 ycenter 695
    button xcenter 100 ycenter 400 xysize (100, 300) action [Play("sound", audio.footsteps), Call("next_location", "room", w=True)]
    text "R\nO\nO\nM" xcenter 100 ycenter 400

screen room:
    style_prefix "explore"
    button xcenter 640 ycenter 695 xysize (1280, 50) action [Play("sound", audio.door), Call("next_location", "storage", w=True)]
    text "STORAGE" xcenter 640 ycenter 695

label nothing(r):
    "Nothing here."
    call next_location(r, transition=False, w=True)
    return

label something(i, r):
    "Found something."
    $ inventory.append(i)
    call next_location(r, transition=False, w=True)
    return

label mansion_end:
    hide screen flashlight
    scene bg final_room
    with Fade(0.25, 0.0, 0.25)
    play ambience hb
    show veins zorder 10 at heartbeat
    play music jumpscare fadein 8.0
    show noise zorder 10 at noisefade(5.0)
    $ pause(0.144)
    show wraith_black at t11
    $ pause(1.479)
    $ pause(0.144)
    show wraith_black1 at t21
    $ pause(1.479)
    $ pause(0.144)
    show wraith_black2 at t22
    $ pause(1.479)
    $ pause(0.144)
    show wraith_black3 at t41
    $ pause(1.479)
    $ pause(0.144)
    show wraith_black4 at t44
    $ pause(1.479)
    scene black with None
    $ pause(1.0)
    show screen show_text with Dissolve(2.0)
    $ pause(1.0)
    hide screen show_text with Dissolve(2.0)
    $ pause(1.0)
    stop music
    stop ambience
    return

screen show_text:
    style_prefix "explore"
    text "YOU KNOW THIS PLACE" xcenter 640 ycenter 360