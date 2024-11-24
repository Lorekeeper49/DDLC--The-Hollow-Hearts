style location_text:
    font "mod_assets/fonts/AlexBrush-Regular.ttf"
    size 100
    color gui.text_color
    outlines [(2, "#000000aa", 0, 0)]
    text_align 0.5

style time_text:
    font "mod_assets/fonts/SevenSegment.ttf"
    size 75
    color "#FF0000"
    outlines [(2, "#000000aa", 0, 0)]
    text_align 0.5

style date_text:
    font "mod_assets/fonts/AlexBrush-Regular.ttf"
    size 25
    color gui.text_color
    outlines [(2, "#000000aa", 0, 0)]
    text_align 0.5

image location_text = ParameterizedText(style="location_text")

image time_text = ParameterizedText(style="time_text")
image date = ParameterizedText(style="date_text")

transform clock_transform:
    xcenter 640
    ycenter 360
    on show:
        alpha 0
        easeout 1 alpha 1 zoom 1 yoffset 0
    on replace:
        alpha 1
        yoffset 0
        zoom 1
    on hide:
        alpha 1
        easein 1 alpha 0 zoom 1 yoffset 0

transform text_transform:
    xcenter 640
    ycenter 50
    on show:
        alpha 0
        easeout 1 alpha 1 zoom 1 yoffset 0
    on replace:
        alpha 1
        yoffset 0
        zoom 1
    on hide:
        alpha 1
        easein 1 alpha 0 zoom 1 yoffset 0

# the code for the clock itself actually come from here: https://www.renpy.org/wiki/renpy/doc/cookbook/Adding_a_simple_Analog_Clock
image clock = "mod_assets/gui/clock_2.png" # Hour Clockhand
image clock_1 = "mod_assets/gui/clock_1.png" # Minute Clockhand
image clock_3 = "mod_assets/gui/clock_3.png" # Second Clockhand
image clock_2 = "mod_assets/gui/clock.png" # Clockface

transform rotateshort:
    xanchor 0.5
    yanchor 0.5
    xalign 0.5
    yalign 0.5
    rotate (minutes*6)
    
transform rotatelong:
    xanchor 0.5
    yanchor 0.5
    xalign 0.5
    yalign 0.5
    rotate (minutes*0.5)

transform face_trans:
    xanchor 0.5
    yanchor 0.5
    xalign 0.5
    yalign 0.5

transform rotatesecond:
    xanchor 0.5
    yanchor 0.5
    xalign 0.5
    yalign 0.5
    rotate (minutes/60)

transform timezone:
    xanchor 0.5
    yanchor 0.5
    xalign 0.5
    yalign 0.75

transform date_trans:
    xanchor 0.5
    yanchor 0.5
    xalign 0.5
    yalign 0.25

screen clock(bg="",date="",minutes=0.0):
    frame:
        at clock_transform
        xmaximum 250 # X size of clock graphic
        ymaximum 250 # Y size of clock graphic
        add bg:
            crop (1, 0, 240, 240)
        add "clock_2" at face_trans
        add "clock_1" at rotateshort
        add "clock" at rotatelong
        add "clock_3" at rotatesecond
        python:
            hour = int(minutes / 60)
            minu = int(minutes % 60)
            seco = int((minutes-int(minutes)) * 60)
            if seco < 10:
                sectext = "0" + str(seco)
            else:
                sectext = str(seco)
            if minu < 10:
                minutext = "0" + str(minu)
            else:
                minutext = str(minu)
            if hour < 10:
                hourtext = "0" + str(hour)
            else:
                hourtext = str(hour)
        text "[hourtext]:[minutext]:[sectext]" style "time_text" at face_trans
        text date style "date_text" at date_trans
        text "JST" style "date_text" at timezone


# Shows the clock
# place: The text indicating the location or time pass
# date: The date of the scene, example: "March 13, 2024"
# time: the time of the scene, it is recomended that you input the time as (hours*60+minutes+seconds/60.0)
# face: the defined image used for the clock face, could be a bg or something
label showlocation(place="",date="",time=0.0,face="#000000"):
    window hide
    $ pause(1)
    $ minutes = time
    show screen clock(face,date,minutes)
    show location_text "[place]" as ltext zorder 101 at text_transform
    $ pause(1)
    $ minutes += (1/60.0)
    $ pause(1)
    $ minutes += (1/60.0)
    $ pause(1)
    $ minutes += (1/60.0)
    $ pause(1)
    hide screen clock
    hide ltext
    return