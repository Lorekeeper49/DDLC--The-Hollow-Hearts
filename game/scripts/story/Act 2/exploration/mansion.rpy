default wraith_beaten = False
image wraith_black = silhouetted("mod_assets/MPT/mari/body.png",0,0,0)
image wraith_black1 = silhouetted("mod_assets/MPT/mari/body.png",0,0,0)
image wraith_black2 = silhouetted("mod_assets/MPT/mari/body.png",0,0,0)
image wraith_black3 = silhouetted("mod_assets/MPT/mari/body.png",0,0,0)
image wraith_black4 = silhouetted("mod_assets/MPT/mari/body.png",0,0,0)
screen wraith:
    add "wraith_black"
    button xcenter 500 ycenter 200 xysize (200, 200) hovered SetVariable("wraith_beaten", True) unhovered SetVariable("wraith_beaten", False) action NullAction()
    timer 1.8 action Show("wraith_blink")
    timer 3.0 action [Hide("wraith_blink"), Hide("black_screen"), If(wraith_beaten, Hide("wraith"))]

screen black_screen:
    add Solid("#000", xsize=2000, ysize=2000)

screen wraith_blink:
    timer 0.1 repeat True action Show("black_screen", _zorder=200)
    timer 0.075 repeat True action Hide("black_screen")

screen first_room:
    style_prefix "explore"
    button xcenter 425 ycenter 250 xysize (75, 500) action [Play("sound", audio.door), Call("next_location", "bedroom1", w=True)]
    text "L\nE\nF\nT" xcenter 425 ycenter 250
    button xcenter 750 ycenter 200 xysize (300, 300) action [Play("sound", audio.footsteps), Call("next_location", "hall1", w=True)]
    text "FORWARD" xcenter 750 ycenter 200

screen bedroom1:
    style_prefix "explore"
    if "box open" in explored and not "spare key" in inventory:
        button xcenter 920 ycenter 300 xysize (100, 100) action AddToSet(inventory, "spare key")
        text "SPARE\nKEY" xcenter 920 ycenter 300
    elif not "spare key" in inventory:
        button xcenter 920 ycenter 300 xysize (100, 100) action Call("break_lock")
        text "LOCKED\nBOX" xcenter 920 ycenter 300
    button xcenter 640 ycenter 695 xysize (1280, 50) action [Play("sound", audio.door), Call("next_location", "first_room", w=True)]
    text "HALL" xcenter 640 ycenter 695

label break_lock:
    "That lock was easy to break."
    $ explored.append("box open")
    call screen bedroom1
    return

screen bedroom2:
    style_prefix "explore"
    button xcenter 640 ycenter 695 xysize (1280, 50) action [Play("sound", audio.door), Call("next_location", "hall3", w=True)]
    text "HALL" xcenter 640 ycenter 695

screen bedroom3:
    style_prefix "explore"
    button xcenter 640 ycenter 695 xysize (1280, 50) action [Play("sound", audio.door), Call("next_location", "hall6", w=True)]
    text "HALL" xcenter 640 ycenter 695

screen hall1:
    style_prefix "explore"
    button xcenter 640 ycenter 250 xysize (300, 300) action [Play("sound", audio.footsteps), Call("next_location", "hall2", w=True)]
    text "FORWARD" xcenter 640 ycenter 250
    button xcenter 640 ycenter 695 xysize (1280, 50) action [Play("sound", audio.footsteps), Call("next_location", "first_room", w=True)]
    text "BACK" xcenter 640 ycenter 695

screen hall2:
    style_prefix "explore"
    button xcenter 600 ycenter 250 xysize (300, 300) action [Play("sound", audio.footsteps), Call("next_location", "hall3", w=True)]
    text "FORWARD" xcenter 600 ycenter 250
    button xcenter 640 ycenter 695 xysize (1280, 50) action [Play("sound", audio.footsteps), Call("next_location", "hall1", w=True)]
    text "BACK" xcenter 640 ycenter 695

screen hall3:
    style_prefix "explore"
    button xcenter 600 ycenter 300 xysize (200, 300) action [Play("sound", audio.footsteps), Call("next_location", "hall4", w=True)]
    text "FORWARD" xcenter 600 ycenter 300
    button xcenter 640 ycenter 695 xysize (1280, 50) action [Play("sound", audio.footsteps), Call("next_location", "hall2", w=True)]
    text "BACK" xcenter 640 ycenter 695
    button xcenter 325 ycenter 300 xysize (75, 500) action [Play("sound", audio.footsteps), Call("next_location", "bedroom2", w=True)]
    text "B\nE\nD\nR\nO\nO\nM" xcenter 325 ycenter 300
    button xcenter 425 ycenter 300 xysize (75, 500) action If("spare key" in inventory, [Play("sound", audio.door), Call("next_location", "dark_kitchen", w=True)])
    text "K\nI\nT\nC\nH\nE\nN" xcenter 425 ycenter 300
    button xcenter 825 ycenter 300 xysize (75, 500) action [Play("sound", audio.footsteps), Call("next_location", "machine_room", w=True)]
    text "M\nA\nC\nH\nI\nN\nE\n \nR\nO\nO\nM" xcenter 825 ycenter 300
    button xcenter 950 ycenter 300 xysize (75, 500) action [Play("sound", audio.footsteps), Call("next_location", "home_office", w=True)]
    text "O\nF\nF\nI\nC\nE" xcenter 950 ycenter 300

screen hall4:
    style_prefix "explore"
    button xcenter 640 ycenter 300 xysize (200, 300) action [Play("sound", audio.footsteps), Call("next_location", "hall5", w=True)]
    text "FORWARD" xcenter 640 ycenter 300
    button xcenter 640 ycenter 695 xysize (1280, 50) action [Play("sound", audio.footsteps), Call("next_location", "hall3", w=True)]
    text "BACK" xcenter 640 ycenter 695
    button xcenter 850 ycenter 300 xysize (75, 500) action [Play("sound", audio.footsteps), Call("next_location", "storage1", w=True)]
    text "S\nT\nO\nR\nA\nG\nE" xcenter 850 ycenter 300

screen hall5:
    style_prefix "explore"
    button xcenter 640 ycenter 250 xysize (300, 300) action [Play("sound", audio.footsteps), Call("next_location", "hall6", w=True)]
    text "FORWARD" xcenter 640 ycenter 250
    button xcenter 640 ycenter 695 xysize (1280, 50) action [Play("sound", audio.footsteps), Call("next_location", "hall4", w=True)]
    text "BACK" xcenter 640 ycenter 695

screen hall6:
    style_prefix "explore"
    button xcenter 680 ycenter 250 xysize (200, 400) action Call("blocked", "hall6")
    text "FORWARD" xcenter 680 ycenter 250
    button xcenter 640 ycenter 695 xysize (1280, 50) action [Play("sound", audio.footsteps), Call("next_location", "hall4", w=True)]
    text "BACK" xcenter 640 ycenter 695
    button xcenter 900 ycenter 250 xysize (200, 400) action [Play("sound", audio.footsteps), Call("next_location", "storage6", w=True)]
    text "STORAGE" xcenter 900 ycenter 250
    button xcenter 375 ycenter 250 xysize (200, 400) action [Play("sound", audio.footsteps), Call("next_location", "bedroom3", w=True)]
    text "BEDROOM" xcenter 375 ycenter 250

screen hall7:
    style_prefix "explore"
    button xcenter 640 ycenter 250 xysize (300, 300) action [Play("sound", audio.footsteps), Call("next_location", "final_hall", w=True)]
    text "FORWARD" xcenter 640 ycenter 250
    button xcenter 640 ycenter 695 xysize (1280, 50) action [Play("sound", audio.door), Call("next_location", "storage6", w=True)]
    text "BACK" xcenter 640 ycenter 695

screen final_hall:
    style_prefix "explore"
    button xcenter 540 ycenter 350 xysize (300, 300) action If("broken key" in inventory, [Play("sound", audio.door), Call("mansion_end")]) 
    text "FAMILIAR ROOM" xcenter 540 ycenter 350
    button xcenter 640 ycenter 695 xysize (1280, 50) action [Play("sound", audio.footsteps), Call("next_location", "hall7", w=True)]
    text "BACK" xcenter 640 ycenter 695

screen machine_room:
    style_prefix "explore"
    button xcenter 640 ycenter 695 xysize (1280, 50) action [Play("sound", audio.door), Call("next_location", "hall3", w=True)]
    text "HALL" xcenter 640 ycenter 695

screen dark_kitchen:
    style_prefix "explore"
    button xcenter 935 ycenter 100 xysize (50, 200) action If("broken key" in inventory, Call("nothing", "dark_kitchen"), Call("something", "broken key", "dark_kitchen"))
    text "S\nE\nA\nR\nC\nH" xcenter 935 ycenter 100
    button xcenter 640 ycenter 695 xysize (1280, 50) action [Play("sound", audio.door), Call("next_location", "hall3", w=True)]
    text "HALL" xcenter 640 ycenter 695

screen home_office:
    style_prefix "explore"
    button xcenter 640 ycenter 695 xysize (1280, 50) action [Play("sound", audio.door), Call("next_location", "hall3", w=True)]
    text "HALL" xcenter 640 ycenter 695
    button xcenter 25 ycenter 360 xysize (50, 720) action [Play("sound", audio.door), Call("next_location", "lab", w=True)]
    text "L\nA\nB\nO\nR\nA\nT\nO\nR\nY" xcenter 25 ycenter 360

screen lab:
    style_prefix "explore"
    button xcenter 640 ycenter 695 xysize (1280, 50) action [Play("sound", audio.door), Call("next_location", "home_office", w=True)]
    text "OFFICE" xcenter 640 ycenter 695

screen storage1:
    style_prefix "explore"
    button xcenter 750 ycenter 250 xysize (300, 300) action [Play("sound", audio.footsteps), Call("next_location", "storage2", w=True)]
    text "FORWARD" xcenter 750 ycenter 250
    button xcenter 640 ycenter 695 xysize (1280, 50) action [Play("sound", audio.footsteps), Call("next_location", "hall4", w=True)]
    text "HALL" xcenter 640 ycenter 695

screen storage2:
    style_prefix "explore"
    button xcenter 750 ycenter 250 xysize (300, 300) action [Play("sound", audio.footsteps), Call("next_location", "storage3", w=True)]
    text "FORWARD" xcenter 750 ycenter 250
    button xcenter 640 ycenter 695 xysize (1280, 50) action [Play("sound", audio.footsteps), Call("next_location", "storage1", w=True)]
    text "BACK" xcenter 640 ycenter 695

screen storage3:
    style_prefix "explore"
    button xcenter 750 ycenter 250 xysize (300, 300) action [Play("sound", audio.footsteps), Call("next_location", "storage4", w=True)]
    text "FORWARD" xcenter 750 ycenter 250
    button xcenter 640 ycenter 695 xysize (1280, 50) action [Play("sound", audio.footsteps), Call("next_location", "storage2", w=True)]
    text "BACK" xcenter 640 ycenter 695
    button xcenter 300 ycenter 300 xysize (50, 300) action [Play("sound", audio.footsteps), Call("next_location", "room1", w=True)]
    text "ROOM" xcenter 300 ycenter 300

screen storage4:
    style_prefix "explore"
    button xcenter 640 ycenter 695 xysize (1280, 50) action [Play("sound", audio.footsteps), Call("next_location", "storage3", w=True)]
    text "BACK" xcenter 640 ycenter 695
    button xcenter 300 ycenter 300 xysize (50, 300) action [Play("sound", audio.footsteps), Call("next_location", "room2", w=True)]
    text "ROOM" xcenter 300 ycenter 300

screen storage5:
    style_prefix "explore"
    button xcenter 640 ycenter 695 xysize (1280, 50) action [Play("sound", audio.footsteps), Call("next_location", "storage6", w=True)]
    text "BACK" xcenter 640 ycenter 695

screen storage6:
    style_prefix "explore"
    button xcenter 1255 ycenter 360 xysize (50, 720) action [Play("sound", audio.footsteps), Call("next_location", "hall6", w=True)]
    text "B\nA\nC\nK" xcenter 1255 ycenter 360
    button xcenter 450 ycenter 300 xysize (200, 500) action [Play("sound", audio.footsteps), Call("next_location", "hall7", w=True)]
    text "HALL" xcenter 450 ycenter 300
    button xcenter 925 ycenter 200 xysize (200, 500) action [Play("sound", audio.footsteps), Call("next_location", "storage5", w=True)]
    text "FORWARD" xcenter 925 ycenter 200

screen room1:
    style_prefix "explore"
    button xcenter 640 ycenter 695 xysize (1280, 50) action [Play("sound", audio.door), Call("next_location", "storage3", w=True)]
    text "STORAGE" xcenter 640 ycenter 695

screen room2:
    style_prefix "explore"
    button xcenter 640 ycenter 695 xysize (1280, 50) action [Play("sound", audio.door), Call("next_location", "storage4", w=True)]
    text "STORAGE" xcenter 640 ycenter 695

label blocked(r):
    "BLOCKED"
    $ renpy.call_screen(r)
    return

label nothing(r):
    "Nothing here."
    $ renpy.call_screen(r)
    return

label something(i, r):
    "Found something."
    $ inventory.append(i)
    $ renpy.call_screen(r)
    return

label mansion_end:
    hide screen flashlight
    scene bg final_room
    with Fade(0.25, 0.0, 0.25)
    play ambience hb
    show veins zorder 10 at heartbeat
    play music jumpscare fadein 8.0
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
    $ pause()
    return

screen show_text:
    style_prefix "explore"
    text "YOU KNOW THIS PLACE" xcenter 640 ycenter 360