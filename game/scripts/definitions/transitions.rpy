init -10 python:
    renpy.register_shader("AnimGlitch", variables="""
        uniform sampler2D tex0; 
        uniform vec2 res0;
        attribute vec2 a_tex_coord; 
        varying vec2 v_tex_coord;

        uniform float u_rx; 
        uniform float u_ry;
        
        uniform float u_gx; 
        uniform float u_gy;
        
        uniform float u_bx;
        uniform float u_by;

    """, vertex_200="""
        v_tex_coord = a_tex_coord;
    """, fragment_300="""
        
        vec2 uv = v_tex_coord;
        vec3 o;

        o.r = texture2D(tex0, vec2(uv.x+u_rx/res0.x, uv.y+u_ry/res0.y)).r;
        o.g = texture2D(tex0, vec2(uv.x+u_gx/res0.x, uv.y+u_gy/res0.y)).g;
        o.b = texture2D(tex0, vec2(uv.x+u_bx/res0.x, uv.y+u_by/res0.y)).b;

        gl_FragColor = vec4(o, 1.0);
    """)

define blink = Fade(0.2, 0.0, 0.2)

transform ZoomTransition(new_widget, old_widget, t=.5, glitch_amt=1.0): 
    subpixel True mesh True shader "AnimGlitch"
    u_rx 0.0 u_ry 0.0
    u_gx 0.0 u_gy 0.0
    u_bx 0.0 u_by 0.0
    delay t*3.5
    xalign 0.5 yalign 0.5 zoom 1 blur 0 rotate 0
    matrixcolor BrightnessMatrix(0)

    old_widget
    easeout_circ t zoom 1.75 blur 20 matrixcolor BrightnessMatrix(.5) u_rx -1 * glitch_amt u_bx 1 * glitch_amt
    zoom 1
    new_widget
    easein_circ t * 1.75 zoom 1.1 blur 0 matrixcolor BrightnessMatrix(0) u_rx 0 u_bx 0
    ease_cubic t zoom 1

label deadfast(new_scene): 
    window hide
    $ audio.deadamb = "mod_assets/sounds/deadamb.ogg"
    play sound deadmantrans
    $ renpy.music.play(audio.deadamb, channel="ambience", fadein=0.5)
    show veins with blink
    scene expression new_scene
    show veins
    with ZoomTransition
    $ pause(0.1)
    play sound deadmantransout
    hide veins with blink
    $ renpy.music.stop(channel="ambience", fadeout=0.5)
    return

transform center_zoom(start=1.0, end=2.0, t=1.0):
    truecenter
    zoom start
    linear t zoom end

label chapter_trans(name):
    scene black with dissolve_scene_full
    window hide
    show location_text "Chapter [chapter]:\n[name]" zorder 10000 at center_zoom(0.5, 1.0, 5.0) with Dissolve(2.0)
    $ pause(1.0)
    hide location_text with Dissolve(2.0)
    return

image act1_logo = "mod_assets/Act1_logo.png"
image act2_logo = "mod_assets/Act2_logo.png"

label act_trans:
    scene black with dissolve_scene_full
    window hide
    show expression "act[act]_logo" as show_logo zorder 10000 at center_zoom(0.5, 1.0, 5.0) with Dissolve(2.0)
    $ pause(1.0)
    hide show_logo with Dissolve(2.0)
    return