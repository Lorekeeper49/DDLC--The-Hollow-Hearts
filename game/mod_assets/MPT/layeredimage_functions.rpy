init python:
    def layeredimage_ref(i,target="master"):
        if not "[i]" in renpy.get_showing_tags(layer=target, sort=True):
            #If not currently showing this sprite, stop function.
            return
        pose = str(renpy.get_attributes("[i]",layer=target)[0])
        if pose == "":
            #Nope out if there's no actual pose here.
            return
        renpy.show("[i] " + pose + " refreshattribute",layer=target)
        renpy.show("[i]",layer=target)

screen layeredimagetool_stats():
    vbox:
        text "Current character is " + character + ", current position is " + position_displayable size 20
        text "Last input was " + posename size 20
        #text "Commands ('x' = first letter of character's name):" size 20
        #text "'menu' 'restart' 'clear' 'clear_x' 'xref'" size 20
        
