#engeki's turned blinking image
image en_blink_turned:
    alpha 0.0
    renpy.random.randint(2, 5)
    choice:
        alpha 1.0
        "mod_assets/MPT/engeki/expression/eyes/blink_a.png"
        alpha 0.015
        "mod_assets/MPT/engeki/expression/eyes/blink_b.png"
        0.035
        "mod_assets/MPT/engeki/expression/eyes/blink_a.png"
        0.015
    choice:
        alpha 1.0
        "mod_assets/MPT/engeki/expression/eyes/blink_a.png"
        0.015
        "mod_assets/MPT/engeki/expression/eyes/blink_b.png"
        0.065
        "mod_assets/MPT/engeki/expression/eyes/blink_a.png"
        0.015
    choice:
        alpha 1.0
        "mod_assets/MPT/engeki/expression/eyes/blink_a.png"
        0.015
        "mod_assets/MPT/engeki/expression/eyes/blink_b.png"
        0.095
        "mod_assets/MPT/engeki/expression/eyes/blink_a.png"
        0.015
    choice:
        alpha 1.0
        "mod_assets/MPT/engeki/expression/eyes/blink_a.png"
        0.015
        "mod_assets/MPT/engeki/expression/eyes/blink_b.png"
        0.035
        "mod_assets/MPT/engeki/expression/eyes/blink_a.png"
        0.015
        alpha 0.0
        0.015
        alpha 1.0
        "mod_assets/MPT/engeki/expression/eyes/blink_a.png"
        0.015
        "mod_assets/MPT/engeki/expression/eyes/blink_b.png"
        0.035
        "mod_assets/MPT/engeki/expression/eyes/blink_a.png"
        0.015
    repeat

#engeki's shy blinking image
image en_blink_shy:
    alpha 0.0
    renpy.random.randint(2, 5)
    choice:
        alpha 1.0
        "mod_assets/MPT/engeki/expression/shy_eyes/blink_a.png"
        alpha 0.015
        "mod_assets/MPT/engeki/expression/shy_eyes/blink_b.png"
        0.035
        "mod_assets/MPT/engeki/expression/shy_eyes/blink_a.png"
        0.015
    choice:
        alpha 1.0
        "mod_assets/MPT/engeki/expression/shy_eyes/blink_a.png"
        0.015
        "mod_assets/MPT/engeki/expression/shy_eyes/blink_b.png"
        0.065
        "mod_assets/MPT/engeki/expression/shy_eyes/blink_a.png"
        0.015
    choice:
        alpha 1.0
        "mod_assets/MPT/engeki/expression/shy_eyes/blink_a.png"
        0.015
        "mod_assets/MPT/engeki/expression/shy_eyes/blink_b.png"
        0.095
        "mod_assets/MPT/engeki/expression/shy_eyes/blink_a.png"
        0.015
    choice:
        alpha 1.0
        "mod_assets/MPT/engeki/expression/shy_eyes/blink_a.png"
        0.015
        "mod_assets/MPT/engeki/expression/shy_eyes/blink_b.png"
        0.035
        "mod_assets/MPT/engeki/expression/shy_eyes/blink_a.png"
        0.015
        alpha 0.0
        0.015
        alpha 1.0
        "mod_assets/MPT/engeki/expression/shy_eyes/blink_a.png"
        0.015
        "mod_assets/MPT/engeki/expression/shy_eyes/blink_b.png"
        0.035
        "mod_assets/MPT/engeki/expression/shy_eyes/blink_a.png"
        0.015
    repeat

#engeki turned layered image (a.k.a. normal pose)
layeredimage engeki turned:
    at AutofocusDisplayable(name="engeki")

    #at renpy.partial(Flatten, drawable_resolution=False)

    #Face base
    always "mod_assets/MPT/engeki/expression/base_turned.png"

    #Attributes for autofocus logic
    group af_logic multiple:
        attribute afm null
        attribute afz null

    #Outfits. In order: uniform, pink sweater, green shirt, white shirt(or singlet, idk)
    group outfit:
        attribute uniform default null
        attribute sweater null
        attribute green_shirt null
        attribute white_shirt null

    group blush:
        attribute nobl default null #No blush
        attribute awkw null #Awkward
        attribute blus null #Blushing
        attribute blaw null #Blushing AND awkward combined

    #Left part of the body
    group left:
        #Arm down
        attribute ldown default if_any(["uniform"]):
            "mod_assets/MPT/engeki/outfit/uniform/1l.png"
        attribute ldown default if_any(["sweater"]):
            "mod_assets/MPT/engeki/outfit/sweater/1dl.png"
        attribute ldown default if_any(["green_shirt"]):
            "mod_assets/MPT/engeki/outfit/green_shirt/1bl.png"
        attribute ldown default if_any(["white_shirt"]):
            "mod_assets/MPT/engeki/outfit/white_shirt/1cl.png"

        #Arm up
        attribute lup if_any(["uniform"]):
            "mod_assets/MPT/engeki/outfit/uniform/2l.png"
        attribute lup if_any(["sweater"]):
            "mod_assets/MPT/engeki/outfit/sweater/2dl.png"
        attribute lup if_any(["green_shirt"]):
            "mod_assets/MPT/engeki/outfit/green_shirt/2bl.png"
        attribute lup if_any(["white_shirt"]):
            "mod_assets/MPT/engeki/outfit/white_shirt/2cl.png"

        #Arm chest
        attribute lchest if_any(["uniform"]):
            "mod_assets/MPT/engeki/outfit/uniform/3l.png"
        attribute lchest if_any(["sweater"]):
            "mod_assets/MPT/engeki/outfit/sweater/3dl.png"
        attribute lchest if_any(["green_shirt"]):
            "mod_assets/MPT/engeki/outfit/green_shirt/3bl.png"
        attribute lchest if_any(["white_shirt"]):
            "mod_assets/MPT/engeki/outfit/white_shirt/3cl.png"

    #Right part of the body
    group right:
        #Arm down
        attribute rdown default if_any(["uniform"]):
            "mod_assets/MPT/engeki/outfit/uniform/1r.png"
        attribute rdown default if_any(["sweater"]):
            "mod_assets/MPT/engeki/outfit/sweater/1dr.png"
        attribute rdown default if_any(["green_shirt"]):
            "mod_assets/MPT/engeki/outfit/green_shirt/1br.png"
        attribute rdown default if_any(["white_shirt"]):
            "mod_assets/MPT/engeki/outfit/white_shirt/1cr.png"

        #Arm up
        attribute rup if_any(["uniform"]):
            "mod_assets/MPT/engeki/outfit/uniform/2r.png"
        attribute rup if_any(["sweater"]):
            "mod_assets/MPT/engeki/outfit/sweater/2dr.png"
        attribute rup if_any(["green_shirt"]):
            "mod_assets/MPT/engeki/outfit/green_shirt/2br.png"
        attribute rup if_any(["white_shirt"]):
            "mod_assets/MPT/engeki/outfit/white_shirt/2cr.png"

        #Arm chest
        attribute rchest if_any(["uniform"]):
            "mod_assets/MPT/engeki/outfit/uniform/3r.png"
        attribute rchest if_any(["sweater"]):
            "mod_assets/MPT/engeki/outfit/sweater/3dr.png"
        attribute rchest if_any(["green_shirt"]):
            "mod_assets/MPT/engeki/outfit/green_shiry/3br.png"
        attribute rchest if_any(["white_shirt"]):
            "mod_assets/MPT/engeki/outfit/white_shirt/3cr.png"

    #Blush group
    group nose:
        attribute nose default if_any(["nobl"]):
            "mod_assets/MPT/engeki/expression/nose/na.png"
        attribute nose default if_any(["awkw"]):
            "mod_assets/MPT/engeki/expression/nose/nb.png"
        attribute nose default if_any(["blus"]):
            "mod_assets/MPT/engeki/expression/nose/nc.png"
        attribute nose default if_any(["blaw"]):
            "mod_assets/MPT/engeki/expression/nose/nd.png"

        #All noses - truncated tags:
        attribute na:
            "mod_assets/MPT/engeki/expression/nose/na.png"
        attribute nb:
            "mod_assets/MPT/engeki/expression/nose/nb.png"
        attribute nc:
            "mod_assets/MPT/engeki/expression/nose/nc.png"
        attribute nd:
            "mod_assets/MPT/engeki/expression/nose/nd.png"

    #Eyes group
    group eyes:
        attribute ea default:
            "mod_assets/MPT/engeki/expression/eyes/ea.png"
        attribute eb:
            "mod_assets/MPT/engeki/expression/eyes/eb.png"
        attribute ec:
            "mod_assets/MPT/engeki/expression/eyes/ec.png"
        attribute ed:
            "mod_assets/MPT/engeki/expression/eyes/ed.png"
        attribute ee:
            "mod_assets/MPT/engeki/expression/eyes/ee.png"
        attribute ef:
            "mod_assets/MPT/engeki/expression/eyes/ef.png"
        attribute eg:
            "mod_assets/MPT/engeki/expression/eyes/eg.png"
        attribute eh:
            "mod_assets/MPT/engeki/expression/eyes/eh.png"
        attribute ei:
            "mod_assets/MPT/engeki/expression/eyes/ei.png"
        attribute ej:
            "mod_assets/MPT/engeki/expression/eyes/ej.png"

    #Blinking group. Disable by default
    group blink:
        attribute no_blink default null
        attribute blink if_not(["eh", "ei", "ej"]):
            "sy_blink_turned"
    
    #Mouths group
    group mouths:
        attribute ma default:
            "mod_assets/MPT/engeki/expression/mouths/ma.png"
        attribute mb:
            "mod_assets/MPT/engeki/expression/mouths/mb.png"
        attribute mc:
            "mod_assets/MPT/engeki/expression/mouths/mc.png"
        attribute md:
            "mod_assets/MPT/engeki/expression/mouths/md.png"
        attribute me:
            "mod_assets/MPT/engeki/expression/mouths/me.png"
        attribute mf:
            "mod_assets/MPT/engeki/expression/mouths/mf.png"
        attribute mg:
            "mod_assets/MPT/engeki/expression/mouths/mg.png"
        attribute mh:
            "mod_assets/MPT/engeki/expression/mouths/mh.png"
        attribute mi:
            "mod_assets/MPT/engeki/expression/mouths/mi.png"
        attribute mj:
            "mod_assets/MPT/engeki/expression/mouths/mj.png"
        attribute mk:
            "mod_assets/MPT/engeki/expression/mouths/mk.png"
        attribute ml:
            "mod_assets/MPT/engeki/expression/mouths/ml.png"
        attribute mm:
            "mod_assets/MPT/engeki/expression/mouths/mm.png"
        attribute mn:
            "mod_assets/MPT/engeki/expression/mouths/mn.png"
        attribute mo:
            "mod_assets/MPT/engeki/expression/mouths/mo.png"

    #Eyebrows group
    group eyebrows:
        attribute ba default:
            "mod_assets/MPT/engeki/expression/eyebrows/ba.png"
        attribute bb:
            "mod_assets/MPT/engeki/expression/eyebrows/bb.png"
        attribute bc:
            "mod_assets/MPT/engeki/expression/eyebrows/bc.png"
        attribute bd:
            "mod_assets/MPT/engeki/expression/eyebrows/bd.png"
        attribute be:
            "mod_assets/MPT/engeki/expression/eyebrows/be.png"
        attribute bf:
            "mod_assets/MPT/engeki/expression/eyebrows/bf.png"
        attribute bg:
            "mod_assets/MPT/engeki/expression/eyebrows/bg.png"

#engeki's shy layered image (looking away)
layeredimage engeki shy:
    at AutofocusDisplayable(name="engeki")

    #at renpy.partial(Flatten, drawable_resolution=False)

    #Face base
    always "mod_assets/MPT/engeki/expression/base_shy.png"

    #Attributes for autofocus logic
    group af_logic multiple:
        attribute afm null
        attribute afz null

    #Outfits. In order: uniform, pink sweater. Green shirt and white singlet are unavailable for this pose.
    group outfit:
        attribute uniform default null
        attribute sweater null


    group blush:
        attribute nobl default null #No blush
        attribute awkw null #Awkward
        attribute blus null #Blushing
        attribute blaw null #Blushing AND awkward combined
        attribute bhid null #The one that hide face

    #Left part of the body
    group left:

        #Arm down
        attribute ldown default if_any(["uniform"]):
            "mod_assets/MPT/engeki/outfit/uniform/1l2.png"
        attribute ldown default if_any(["sweater"]):
            "mod_assets/MPT/engeki/outfit/sweater/1dl2.png"

        #Arm up
        attribute lup if_any(["uniform"]):
            "mod_assets/MPT/engeki/outfit/uniform/2l2.png"
        attribute lup if_any(["sweater"]):
            "mod_assets/MPT/engeki/outfit/sweater/2dl2.png"

        #Arm chest
        attribute lchest if_any(["uniform"]):
            "mod_assets/MPT/engeki/outfit/uniform/3l2.png"
        attribute lchest if_any(["sweater"]):
            "mod_assets/MPT/engeki/outfit/sweater/3dl2.png"

    #Right part of the body
    group right:
        #Arm down
        attribute rdown default if_any(["uniform"]):
            "mod_assets/MPT/engeki/outfit/uniform/1r2.png"
        attribute rdown default if_any(["sweater"]):
            "mod_assets/MPT/engeki/outfit/sweater/1dr2.png"

        #Arm up
        attribute rup if_any(["uniform"]):
            "mod_assets/MPT/engeki/outfit/uniform/2r2.png"
        attribute rup if_any(["sweater"]):
            "mod_assets/MPT/engeki/outfit/sweater/2dr2.png"

        #Arm chest
        attribute rchest if_any(["uniform"]):
            "mod_assets/MPT/engeki/outfit/uniform/3r2.png"
        attribute rchest if_any(["sweater"]):
            "mod_assets/MPT/engeki/outfit/sweater/3dr2.png"

    #Blush group
    group nose:
        attribute nose default if_any(["nobl"]):
            "mod_assets/MPT/engeki/expression/shy_nose/na.png"
        attribute nose default if_any(["awkw"]):
            "mod_assets/MPT/engeki/expression/shy_nose/nb.png"
        attribute nose default if_any(["blus"]):
            "mod_assets/MPT/engeki/expression/shy_nose/nc.png"
        attribute nose default if_any(["blaw"]):
            "mod_assets/MPT/engeki/expression/shy_nose/nd.png"
        
        #All noses - truncated tags:
        attribute na:
            "mod_assets/MPT/engeki/expression/shy_nose/na.png"
        attribute nb:
            "mod_assets/MPT/engeki/expression/shy_nose/nb.png"
        attribute nc:
            "mod_assets/MPT/engeki/expression/shy_nose/nc.png"
        attribute nd:
            "mod_assets/MPT/engeki/expression/shy_nose/nd.png"

    #Eyes group
    group eyes:
        attribute ea default:
            "mod_assets/MPT/engeki/expression/shy_eyes/ea.png"
        attribute eb:
            "mod_assets/MPT/engeki/expression/shy_eyes/eb.png"
        attribute ec:
            "mod_assets/MPT/engeki/expression/shy_eyes/ec.png"
        attribute ed:
            "mod_assets/MPT/engeki/expression/shy_eyes/blink_b.png"
        attribute ee:
            "mod_assets/MPT/engeki/expression/shy_eyes/blink_a.png"

    #Blinking group. Disable by default
    group blink:
        attribute no_blink default null
        attribute blink if_not(["ed","ee","bhid","ne"]):
            "sy_blink_shy"

    #Mouths group
    group mouths:
        attribute ma default:
            "mod_assets/MPT/engeki/expression/shy_mouths/ma.png"
        attribute mb:
            "mod_assets/MPT/engeki/expression/shy_mouths/mb.png"
        attribute mc:
            "mod_assets/MPT/engeki/expression/shy_mouths/mc.png"
        attribute md:
            "mod_assets/MPT/engeki/expression/shy_mouths/md.png"
        attribute me:
            "mod_assets/MPT/engeki/expression/shy_mouths/me.png"

    #Eyebrows group
    group eyebrows:
        attribute ba default:
            "mod_assets/MPT/engeki/expression/shy_eyebrows/ba.png"
        attribute bb:
            "mod_assets/MPT/engeki/expression/shy_eyebrows/bb.png"
        attribute bc:
            "mod_assets/MPT/engeki/expression/shy_eyebrows/bc.png"

    #Blush that make it hide the eye one
    group nose:
        attribute nose default if_any(["bhid"]):
            "mod_assets/MPT/engeki/expression/shy_nose/ne.png"
        attribute ne:
            "mod_assets/MPT/engeki/expression/shy_nose/ne.png"