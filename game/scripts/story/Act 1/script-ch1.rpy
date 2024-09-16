label act1_ch1_main:
    stop music fadeout 2.0
    scene bg tlivingroom
    with dissolve_scene_full
    $ style.say_window = style.window
    $ nb = "namebox"
    call showlocation("Sakura Household","September 29, 2023",7*60+0+0/60.0,"bg tlivingroom")
    t "Agh!  I can't focus!"
    "Been trying to play my favorite game to get my mind off it, but it's bothering me so much!"
    "What were those voices I heard last night?"
    "And why did one of them sound like Akira-kun?"
    show kotonoha turned casual rhip neut zorder 2 at t11
    k om "Because it was."
    show kotonoha cm
    t "A-"
    t "Were you listening?"
    t "Actually, more importantly, you heard them too?"
    k ce om "Yes."
    k oe lup "I know his voice like no other."
    t "Because of your crush on him, right?"
    k surp cm "!!!"
    k nerv om ldown "Well- yes, but that's not the point!"
    show kotonoha cm
    "Don't think you should be smiling."
    kmind neut "Don't think you should be internally monologing."
    t "Touchè."
    k rdown "Anyway..."
    k lup "Remember that experiment we did years ago?"
    t "Yes."
    k ldown rhip "Well, he's alive."
    t "...{w=1}{cps=10}Which subject?{/cps}"
    "FOUR's at school..."
    "ONE and TWO are presumed dead."
    k rdown "ONE."
    show kotonoha cm
    t "...{w=1}{cps=5}ONE?{/cps}"
    play ambience hb
    show veins zorder 10 at heartbeat
    t "ONE!  ONE!  Why ONE?"
    t "THREE's fine, she's at school..."
    t "TWO would be questionable, but fine..."
    t "but ONE's...!"
    t "No..."
    t "That's who..."
    t "Damn it!  They were right!"
    t "It was my fault!"
    k worr om "Tai-kun?"
    t "I... I need some fresh air!"
    stop ambience fadeout 1.0
    scene bg house with wipeleft_scene
    t "*Deep breath*"
    show kotonoha turned casual worr zorder 2 at t11
    k om "Are you okay?"
    show kotonoha cm
    t "...{w=2}I'll be fine."
    t "I just need to process all this."
    t "ONE was a great man, capable of many accomplishments..."
    t "However, scans of his brain revealed he was once fond of corruption."
    t "If the expriment destroyed his mind then..."
    t "..."
    t "Sorry, I need a distraction, I just can't fathom the impact of this."
    show kotonoha neut
    "Koto-chan silently accepts."
    hide kotonoha
    s "We're going somewhere new today, the old location is compromised for unknown reasons."
    s "So, we're heading East instead of West."
    t "That'll help."
    "I follow her."
    $ style.say_window = style.window_fake
    $ nb = "namebox_fake"
    call deadfast("bg park_day")
    play music t2
    call showlocation("Converse Park","September 29, 2023",7*60+15+0/60.0,"bg tree")
    t "Ohayou Sayori!"
    show sayori turned casual happ zorder 2 at t11
    s om "I thought someone was following me!"
    s rup oe "Ohayou Taiyen!"
    t "Streaming today?"
    s oe "Mhm, feel free to join!"
    show sayori cm
    t "I think I will!"
    "I sit down next to her."
    s om rdown "So, what brings you here on this fine day?"
    show sayori cm
    menu(time=5,force=2):
        "You do.":
            pass
        "What about you?":
            t "You first."
            s rup om "Well my usual spot is under construction for some reason so I'm using this place as my backup."
            show sayori cm
            t "I see."
            "Didn't have to use this spot but, I won't judge."
            t "As for me..."
        "Why so formal?":
            t "Uh, there's no need to be so formal!"
            s rup ce om "Ahaha!  I'm just kidding with you!"
            s oe "Jeez, you need to learn to take a joke."
            show sayori cm
            t "You're one to talk."
            s laug om "Oh, shut up!"
            show sayori cm
            t "But, to answer the question..."
    show sayori happ cm
    "Well, I saw you starting your stream how you usually do and since I had nothing to do today I thought, why not?  I'll come by and join the stream!"
    s rup "Ah!  Well it's nice to have you here!"
    "As usual, her chat is shipping us."
    "It's like a Vtuber's chat."
    s laug om "Guys, you don't need to keep shipping us like this, there's other boys in my life and there's other girls in Taiyen's life."
    t "You say that as if you know about other girls I talk to."
    s happ rdown "But I do!"
    s rup "Over there, right?"
    "She points to our left."
    s "You talk to a girl every week over there."
    s "I'm almost jealous."
    show sayori cm
    menu(time=5,force=1):
        t "That's because..."

        "She's hidden":
            t "Look, I don't actually know her, okay?"
        "You win.":
            t "You know what, you can have this win, I'm not fighting back against this!"
    s ce "Hehehehehe!"
    "*Sigh* I swear, I can't win with this girl sometimes!"
    stop music fadeout 2.0
    $ pause(1.0)
    show sayori dist om oe rdown ldown 
    $ pause(1.0)
    s "I'm sorry... everyone...  I can't..."
    s sad rup "My mind just keeps going back the experiment!"
    "Wha-"
    s lup "All the terrible things that happened to them!"
    "Why is she not pausing the stream?"
    s "I just can't!"
    s cry "I can't do anything people want me to do!"
    show sayori ce cm
    "Given how the chats reacting, I assume they know about what she's talking about.\nAnd I do too."
    t "There's my request-"
    s oe ldown "No!  There isn't!"
    s om "I lied to you Taiyen!"
    s "I didn't do it..."
    s lup "I didn't kill any of them!!!"
    s ce cm "I couldn't do it!"
    s ldown om "I'm not a killer!"
    s rdown oe "I don't know how you expect me to do anything like that!"
    t "*Faded gasp*"
    "..."
    show sayori cm
    t "I-"
    "How do I respond?"
    "My emotions are handling this the worst right now."
    "I don't know if I should feel mad that she lied or if I should feel ashamed of myself for thinking she could put suffering ones out of their misery."
    "Well, one of them's happy."
    t "Well, think about THREE."
    s sad oe "Can you please call her by her real name for once?"
    show sayori cm
    t "Right, sorry."
    t "But seriously, think of Lilly."
    t "She's attending school, thriving, and having fun."
    t "And best of all, she's not trying to kill me!"
    s nerv e1a om rup "Are you sure that's the best?  She took the shot {i}because{/i} she didn't want to kill you."
    show sayori cm
    t "Point taken."
    $ layeredimage_ref("sayori")
    s dist rdown om "But she's not the one I'm worried about."
    s neut "I'm worried about the others."
    s rup "ONE and TWO..."
    s nerv "I forget their names."
    t "Well I'm too occupied to remember them right now."
    t "But they were both intrigued by pretty dark things."
    t "Can't imagine what the experiment did to them."
    t "..."
    "Her chat is not confused at all; I don't think this is the first time she's said anything."
    s neut "I'm probably gonna ruin my reputation if I keep talking."
    t "Yeah, let's just take this on a date later."
    "No one ask what that means, please."
    scene bg deep_forest with wipeleft_scene

    return