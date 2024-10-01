screen sewer_hall:
    style_prefix "explore"
    button xcenter 750 ycenter 350 xysize (100, 100) action If("factory key" in inventory, [Play("sound", audio.door), Call("next_location", "factory")]) 
    text "FACTORY" xcenter 750 ycenter 350
    button xcenter 640 ycenter 695 xysize (1280, 50) action [Play("sound", audio.door), Call("next_location", "hideout")]
    text "BUSINESS ROOM" xcenter 640 ycenter 695

screen hideout:
    style_prefix "explore"
    if not "factory key" in inventory:
        button xcenter 550 ycenter 500 xysize (100, 100) action AddToSet(inventory, "factory key")
        text "KEY" xcenter 550 ycenter 500
    button xcenter 640 ycenter 695 xysize (1280, 50) action [Play("sound", audio.door), Call("next_location", "sewer_hall")]
    text "HALL" xcenter 640 ycenter 695
    button xcenter 1015 ycenter 285 xysize (200, 425) action If("hanato" in party, [Play("sound", audio.door), Return()], Call("not_leaving"))
    text "EXIT" xcenter 1015 ycenter 285

label not_leaving:
    "That's the exit, but I'm not leaving here without Hanato!"
    call screen hideout
    return

screen factory:
    style_prefix "explore"
    button xcenter 640 ycenter 695 xysize (1280, 50) action [Play("sound", audio.door), Call("next_location", "sewer_hall")]
    text "HALL" xcenter 640 ycenter 695
    button xcenter 25 ycenter 360 xysize (50, 720) action [Play("sound", audio.footsteps), Call("next_location", "stairs")]
    text "S\nT\nA\nI\nR\nS" xcenter 25 ycenter 360
    button xcenter 635 ycenter 430 xysize (100, 75) action Call("sewer_notice")
    text "NOTICE\nBOARD" xcenter 635 ycenter 430

label sewer_notice:
    "NOTICE FROM MANAGER" "Apologies for the inconvenience but I'm shutting this place down!  We've had far too many incidents and lawsuits over the past 5 years and it's put us into bankruptcy."
    "NOTICE FROM MANAGER" "I am really sorry that all of our hard work is going to waste, but that's just how the situation is..."
    "NOTICE FROM MANAGER" "Unfortunately, this means that the entrance to the secret room in the basement that you all know about by now will eventually be found by unwanted people.  I never hid that place well anyway."
    "NOTICE FROM MANAGER" "I'd grab what's in there, but I don't trust myself enough to keep it safe."
    "NOTICE FROM MANAGER" "I just hope that either one of you did or it doesn't end up in the wrong hands."
    "NOTICE FROM MANAGER" "With that, goodbye Palace Factories Inc."
    "NOTICE FROM MANAGER" "P.S. Here's that poem that never made sense for one final time..."
    "NOTICE FROM MANAGER" "If I die today, I am for one.  If I died yesterday, I am for two.  Let's make tomorrow better for seven so that we can add the last two."
    $ explored.append("notice board")
    call screen factory
    return

screen stairs:
    style_prefix "explore"
    button xcenter 1255 ycenter 360 xysize (50, 720) action [Play("sound", audio.footsteps), Call("next_location", "factory")]
    text "F\nA\nC\nT\nO\nR\nY" xcenter 1255 ycenter 360
    button xcenter 740 ycenter 400 xysize (600, 270) action [Play("sound", audio.footsteps), If("basement" in explored, Call("next_location", "basement"), Call("to_basement"))]
    text "BASEMENT" xcenter 740 ycenter 400

label to_basement:
    $ explored.append("basement")
    scene bg basement with Fade(0.25, 0.0, 0.25)
    "This place is more run down here than up there..."
    "Better be careful."
    call screen basement
    return

screen basement:
    style_prefix "explore"
    button xcenter 472 ycenter 365 xysize (175, 175) action [Play("sound", audio.footsteps), Call("next_location", "stairs")]
    text "UPSTAIRS" xcenter 472 ycenter 365
    button xcenter 620 ycenter 365 xysize (75, 150) action [Play("sound", audio.footsteps), Call("next_location", "power_room")]
    text "POWER\nROOM" xcenter 620 ycenter 365
    button xcenter 720 ycenter 350 xysize (75, 175) action [Play("sound", audio.door), Call("next_location", "office")]
    text "O\nF\nF\nI\nC\nE" xcenter 720 ycenter 350

screen power_room:
    style_prefix "explore"
    if not "hanato" in party:
        button xcenter 1000 ycenter 450 xysize (100, 100) action Call("hanato_found")
        text "SOMEONE\nHIDING" xcenter 1000 ycenter 450
    button xcenter 640 ycenter 695 xysize (1280, 50) action [Play("sound", audio.footsteps), Call("next_location", "basement")]
    text "BACK" xcenter 640 ycenter 695

label hanato_found:
    show hanato day zorder 2 at t11
    a "There you are!"
    ha lhip rhip angr om "I'm glad I decided to stay in one place after running away from that!  Whatever it was."
    show hanato cm
    a "Probably wraiths."
    a "Anyway, we need to get out of here!"
    ha lup om "Yeah, I don't want to stay here any longer than we have to!"
    show hanato cm
    if "notice board" in explored:
        a "There's also this secret room down here that it seems the old company knew about."
        a "The place looks like it was shut down years ago, so it's probably already found."
        ha ldown om "Who told you about it?"
        show hanato cm
        a "The old manager, thanks to a notice on a bulletin."
        a "It also had this strange poem that looks to be a riddle to a code..."
        ha rdown "I'll see what I can find."
    hide hanato
    $ party.append("hanato")
    call screen power_room
    return

screen office:
    style_prefix "explore"
    if "hanato" in party and "notice board" in explored:
        button xcenter 935 ycenter 550 xysize (100, 200) action If("secret" in codes, [Play("sound", audio.footsteps), Call("next_location", "secret_room")], Call("dialpad", "2179", "office", "secret"))
        text "SECRET\nROOM" xcenter 935 ycenter 550
    button xcenter 640 ycenter 695 xysize (1280, 50) action [Play("sound", audio.door), Call("next_location", "basement")]
    text "BACK" xcenter 640 ycenter 695

screen secret_room:
    style_prefix "explore"
    button xcenter 930 ycenter 115 xysize (300, 150) action [Play("sound", audio.footsteps), Call("next_location", "office")]
    text "OFFICE" xcenter 930 ycenter 115
    if not found_breaker:
        button xcenter 450 ycenter 530 xysize (600, 200) action Call("found_something")
        text "SEARCH" xcenter 450 ycenter 530

label found_something:
    ha "I'll keep watch."
    "Alright, what do we got?"
    "Old boxes...  Nope."
    "Money!"
    "I could take it, I've stolen a couple things."
    "From somewhere..."
    "I don't remember."
    "But I should stop that."
    "What I'm getting from the school's enough."
    "Let's just get what the manager hopes is in a more secure location and get it there."
    "There's a lidless crate here with lots of vials..."
    "What the fuck's this substance?"
    ha "Shit!  I hear something!"
    a "I think I got what the manager was talking about."
    ha "Well good, 'cause we better get the hell out of here!"
    a "Right behind you!"
    $ found_breaker = True
    $ persistent.choices_made.append("")
    call screen secret_room
    return