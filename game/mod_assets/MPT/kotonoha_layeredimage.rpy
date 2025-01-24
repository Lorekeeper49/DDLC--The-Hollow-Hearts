image _koko_blink_a:
    alpha 0.0
    renpy.random.randint(20, 100)*0.1
    choice:
        alpha 1.0
        "mod_assets/MPT/kotonoha/blink/blink1.png"
        0.015
        "mod_assets/MPT/kotonoha/blink/blink2.png"
        0.035
        "mod_assets/MPT/kotonoha/blink/blink1.png"
        0.015
    choice:
        alpha 1.0
        "mod_assets/MPT/kotonoha/blink/blink1.png"
        0.015
        "mod_assets/MPT/kotonoha/blink/blink2.png"
        0.065
        "mod_assets/MPT/kotonoha/blink/blink1.png"
        0.015
    choice:
        alpha 1.0
        "mod_assets/MPT/kotonoha/blink/blink1.png"
        0.015
        "mod_assets/MPT/kotonoha/blink/blink2.png"
        0.095
        "mod_assets/MPT/kotonoha/blink/blink1.png"
        0.015
    choice:
        alpha 1.0
        "mod_assets/MPT/kotonoha/blink/blink1.png"
        0.015
        "mod_assets/MPT/kotonoha/blink/blink2.png"
        0.035
        "mod_assets/MPT/kotonoha/blink/blink1.png"
        0.015
        alpha 0.0
        0.15
        alpha 1.0
        "mod_assets/MPT/kotonoha/blink/blink1.png"
        0.015
        "mod_assets/MPT/kotonoha/blink/blink2.png"
        0.035
        "mod_assets/MPT/kotonoha/blink/blink1.png"
        0.015
    repeat

layeredimage kotonoha turned:
    at AutofocusDisplayable(name="kotonoha")
    always if_any(["uniform"]) if_not(["casual", "bikini"]):
        "mod_assets/MPT/kotonoha/bases/base1.png"

    always if_any(["bikini"]) if_not(["casual", "uniform"]):
        "mod_assets/MPT/kotonoha/bases/base3.png"

    always if_any(["casual"]) if_not(["uniform", "bikini"]):
        "mod_assets/MPT/kotonoha/bases/base2.png"

    group outfit:

        attribute uniform default null
        attribute casual null
        attribute bikini null

    group mood:

        attribute neut default null #neutral
        attribute angr null #angry
        attribute anno null #annoyed
        attribute cry null #crying
        attribute curi null #curious
        attribute dist null #distant
        attribute doub null #doubtful
        attribute flus null #flustered
        attribute happ null #happy
        attribute laug null #laughing
        attribute lsur null #surprised (lightly)
        attribute nerv null #nervous
        attribute pani null #panicked
        attribute pout null #pouting
        attribute sad null #sad
        attribute sedu null #seductive
        attribute shoc null #shocked
        attribute vang null #very angry
        attribute vsur null #very surprised
        attribute worr null #worried
        attribute yand null #yandere



    
    group eyes:

        attribute oe default if_any(["neut", "curi", "happ", "laug", "cry", "pout", "sad"]):
            "mod_assets/MPT/kotonoha/eyes/e1a.png"
        attribute oe default if_any(["angr", "anno"]):
            "mod_assets/MPT/kotonoha/eyes/e1d.png"
        attribute oe default if_any(["flus", "nerv", "worr", "dist"]):
            "mod_assets/MPT/kotonoha/eyes/e1b.png"
        attribute oe default if_any(["doub", "sedu"]):
            "mod_assets/MPT/kotonoha/eyes/e1d.png"
        attribute oe default if_any(["lsur", "vang", "vsur"]):
            "mod_assets/MPT/kotonoha/eyes/e2a.png"
        attribute oe default if_any(["pani", "shoc"]):
            "mod_assets/MPT/kotonoha/eyes/e2d.png"
        attribute oe default if_any(["yand"]):
            "mod_assets/MPT/kotonoha/eyes/e3a.png"

        attribute ce if_any(["neut", "angr", "doub", "sad", "worr", "anno", "shoc", "vang", "cry", "dist", "pani", "vsur"]):
            "mod_assets/MPT/kotonoha/eyes/e4a.png"
        attribute ce if_any(["curi", "flus", "happ", "laug", "lsur", "nerv", "pout", "sedu", "yand"]):
            "mod_assets/MPT/kotonoha/eyes/e4b.png"

        attribute e1a:
            "mod_assets/MPT/kotonoha/eyes/e1a.png"
        attribute e1b:
            "mod_assets/MPT/kotonoha/eyes/e1b.png"
        attribute e1c:
            "mod_assets/MPT/kotonoha/eyes/e1c.png"
        attribute e1d:
            "mod_assets/MPT/kotonoha/eyes/e1d.png"
        attribute e1e:
            "mod_assets/MPT/kotonoha/eyes/e1e.png"
        attribute e1f:
            "mod_assets/MPT/kotonoha/eyes/e1f.png"
        attribute e2a:
            "mod_assets/MPT/kotonoha/eyes/e2a.png"
        attribute e2b:
            "mod_assets/MPT/kotonoha/eyes/e2b.png"
        attribute e2c:
            "mod_assets/MPT/kotonoha/eyes/e2c.png"
        attribute e2d:
            "mod_assets/MPT/kotonoha/eyes/e2d.png"
        attribute e3a:
            "mod_assets/MPT/kotonoha/eyes/e3a.png"
        attribute e3b:
            "mod_assets/MPT/kotonoha/eyes/e3b.png"
        attribute e3c:
            "mod_assets/MPT/kotonoha/eyes/e3c.png"
        attribute e3d:
            "mod_assets/MPT/kotonoha/eyes/e3d.png"
        attribute e4a:
            "mod_assets/MPT/kotonoha/eyes/e4a.png"
        attribute e4b:
            "mod_assets/MPT/kotonoha/eyes/e4b.png"
        attribute e0a:
            "mod_assets/MPT/kotonoha/eyes/e0a.png"
        attribute e0b:
            "mod_assets/MPT/kotonoha/eyes/e0b.png"

    group blink:

        anchor (0,0) subpixel (True)

        attribute blink_a default if_not(["ce", "e2b", "e4a","e4b","e4c", "e4d", "e4f", "e4e", "e1e", "e1f"]):
            "_koko_blink_a"
        attribute no_blink:
            "sprite_blank"

    group brows:

        attribute brow default if_any(["neut", "happ", "yand"]):
            "mod_assets/MPT/kotonoha/brows/b1a.png"
        attribute brow default if_any(["anno", "pout", "sedu", "dist"]):
            "mod_assets/MPT/kotonoha/brows/b1c.png"
        attribute brow default if_any(["angr", "vang"]):
            "mod_assets/MPT/kotonoha/brows/b1e.png"
        attribute brow default if_any(["curi", "doub"]):
            "mod_assets/MPT/kotonoha/brows/b1f.png"
        attribute brow default if_any(["flus", "laug", "nerv", "sad", "worr", "cry", "pani", "shoc"]):
            "mod_assets/MPT/kotonoha/brows/b1b.png"
        attribute brow default if_any(["lsur"]):
            "mod_assets/MPT/kotonoha/brows/b2b.png"
        attribute brow default if_any(["vsur"]):
            "mod_assets/MPT/kotonoha/brows/b2a.png"

        attribute b1a:
            "mod_assets/MPT/kotonoha/brows/b1a.png"
        attribute b1b:
            "mod_assets/MPT/kotonoha/brows/b1b.png"
        attribute b1c:
            "mod_assets/MPT/kotonoha/brows/b1c.png"
        attribute b1e:
            "mod_assets/MPT/kotonoha/brows/b1e.png"
        attribute b1f:
            "mod_assets/MPT/kotonoha/brows/b1f.png"
        attribute b2a:
            "mod_assets/MPT/kotonoha/brows/b2a.png"
        attribute b2b:
            "mod_assets/MPT/kotonoha/brows/b2b.png"

    group mouths:

        attribute cm default if_any(["neut", "angr", "flus", "doub", "sad", "worr", "anno", "dist"]):
            "mod_assets/MPT/kotonoha/mouths/md.png"
        attribute cm default if_any(["curi", "lsur"]):
            "mod_assets/MPT/kotonoha/mouths/me.png"
        attribute cm default if_any(["happ", "nerv"]):
            "mod_assets/MPT/kotonoha/mouths/ma.png"
        attribute cm default if_any(["laug", "sedu"]):
            "mod_assets/MPT/kotonoha/mouths/mn.png"
        attribute cm default if_any(["cry", "sad"]):
            "mod_assets/MPT/kotonoha/mouths/mj.png"
        attribute cm default if_any(["pani", "vang"]):
            "mod_assets/MPT/kotonoha/mouths/mm.png"
        attribute cm default if_any(["pout", "vsur"]):
            "mod_assets/MPT/kotonoha/mouths/mf.png"
        attribute cm default if_any(["shoc"]):
            "mod_assets/MPT/kotonoha/mouths/mi.png"
        attribute cm default if_any(["yand"]):
            "mod_assets/MPT/kotonoha/mouths/mo.png"
        
        attribute om if_any(["worr"]):
            "mod_assets/MPT/kotonoha/mouths/mf.png"
        attribute om if_any(["curi", "flus", "lsur", "pout"]):
            "mod_assets/MPT/kotonoha/mouths/mh.png"
        attribute om if_any(["happ", "sedu"]):
            "mod_assets/MPT/kotonoha/mouths/mb.png"
        attribute om if_any(["laug", "nerv", "yand"]):
            "mod_assets/MPT/kotonoha/mouths/mc.png"
        attribute om if_any(["neut", "dist"]):
            "mod_assets/MPT/kotonoha/mouths/me.png"
        attribute om if_any(["angr", "cry", "pani", "shoc", "vang"]):
            "mod_assets/MPT/kotonoha/mouths/ml.png"
        attribute om if_any(["anno", "vsur"]):
            "mod_assets/MPT/kotonoha/mouths/mh.png"
        attribute om if_any(["doub"]):
            "mod_assets/MPT/kotonoha/mouths/ml.png"
        attribute om if_any(["sad"]):
            "mod_assets/MPT/kotonoha/mouths/mk.png"

        attribute ma:
            "mod_assets/MPT/kotonoha/mouths/ma.png"
        attribute mb:
            "mod_assets/MPT/kotonoha/mouths/mb.png"
        attribute mc:
            "mod_assets/MPT/kotonoha/mouths/mc.png"
        attribute md:
            "mod_assets/MPT/kotonoha/mouths/md.png"
        attribute me:
            "mod_assets/MPT/kotonoha/mouths/me.png"
        attribute mf:
            "mod_assets/MPT/kotonoha/mouths/mf.png"
        attribute mg:
            "mod_assets/MPT/kotonoha/mouths/mg.png"
        attribute mh:
            "mod_assets/MPT/kotonoha/mouths/mh.png"
        attribute mi:
            "mod_assets/MPT/kotonoha/mouths/mi.png"
        attribute mj:
            "mod_assets/MPT/kotonoha/mouths/mj.png"
        attribute mk:
            "mod_assets/MPT/kotonoha/mouths/mk.png"
        attribute ml:
            "mod_assets/MPT/kotonoha/mouths/ml.png"
        attribute mm:
            "mod_assets/MPT/kotonoha/mouths/mm.png"
        attribute mn:
            "mod_assets/MPT/kotonoha/mouths/mn.png"
        attribute mo:
            "mod_assets/MPT/kotonoha/mouths/mo.png"
        attribute mp:
            "mod_assets/MPT/kotonoha/mouths/mp.png"
        attribute mq:
            "mod_assets/MPT/kotonoha/mouths/mq.png"
        attribute mr:
            "mod_assets/MPT/kotonoha/mouths/mr.png"
        attribute ms:
            "mod_assets/MPT/kotonoha/mouths/ms.png"

    group noses:
        
        attribute n1 null
        attribute n2:
            "mod_assets/MPT/kotonoha/noses/n2.png"
        attribute n3:
            "mod_assets/MPT/kotonoha/noses/n3.png"
        attribute n4:
            "mod_assets/MPT/kotonoha/noses/n4.png"

    group tears:

        attribute tce default if_any(["cry"]):
            "mod_assets/MPT/kotonoha/tears/t3.png"

        attribute toe if_any(["cry"]):
            "mod_assets/MPT/kotonoha/tears/t1.png"

        # Open-eyed Tears
        attribute t1 if_not(["e4a", "e4b", "e4c", "e4d", "e1e", "e1f", "e1g"]):
            "mod_assets/MPT/kotonoha/tears/t1.png"
        attribute t2 if_not(["e4a", "e4b", "e4c", "e4d", "e1e", "e1f", "e1g"]):
            "mod_assets/MPT/kotonoha/tears/t2.png"

        # Close-eyed Tears
        attribute t3 if_not(["e1a", "e1b", "e1c", "e1d", "e1e", "e1f", "e1g", "e2a", "e2b", "e2c", "e2d", "e3a", "e3b", "e3c", "e4c", "e4d"]):
            "mod_assets/MPT/kotonoha/tears/t3.png"

        attribute tno null

    group left:

        attribute ldown default if_any(["uniform"]):
            "mod_assets/MPT/kotonoha/clothes/uniform/ldown.png"
        attribute ldown default if_any(["casual"]):
            "mod_assets/MPT/kotonoha/clothes/casual/ldown.png"
        attribute ldown default if_any(["bikini"]):
            "mod_assets/MPT/kotonoha/clothes/bikini/ldown.png"

        attribute lchest if_any(["uniform"]):
            "mod_assets/MPT/kotonoha/clothes/uniform/lchest.png"
        attribute lchest if_any(["casual"]):
            "mod_assets/MPT/kotonoha/clothes/casual/lchest.png"
        attribute lchest if_any(["bikini"]):
            "mod_assets/MPT/kotonoha/clothes/bikini/lchest.png"

        attribute lup if_any(["uniform"]):
            "mod_assets/MPT/kotonoha/clothes/uniform/lup.png"
        attribute lup if_any(["casual"]):
            "mod_assets/MPT/kotonoha/clothes/casual/lup.png"
        attribute lup if_any(["bikini"]):
            "mod_assets/MPT/kotonoha/clothes/bikini/lup.png"

    group right:

        attribute rdown default if_any("uniform"):
            "mod_assets/MPT/kotonoha/clothes/uniform/rdown.png"
        attribute rdown default if_any("casual"):
            "mod_assets/MPT/kotonoha/clothes/casual/rdown.png"
        attribute rdown default if_any("bikini"):
            "mod_assets/MPT/kotonoha/clothes/bikini/rdown.png"

        attribute rbehind if_any(["uniform"]):
            "mod_assets/MPT/kotonoha/clothes/uniform/rbehind.png"
        attribute rbehind if_any(["casual"]):
            "mod_assets/MPT/kotonoha/clothes/casual/rbehind.png"
        attribute rbehind if_any(["bikini"]):
            "mod_assets/MPT/kotonoha/clothes/bikini/rbehind.png"

        attribute rhip if_any(["uniform"]):
            "mod_assets/MPT/kotonoha/clothes/uniform/rhip.png"
        attribute rhip if_any(["casual"]):
            "mod_assets/MPT/kotonoha/clothes/casual/rhip.png"
        attribute rhip if_any(["bikini"]):
            "mod_assets/MPT/kotonoha/clothes/bikini/rhip.png"

    