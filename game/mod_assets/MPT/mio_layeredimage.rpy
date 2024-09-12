layeredimage mio turned:

    always "mod_assets/MPT/mio/base.png"


    group outfit:

        attribute uniform default null
        attribute casual null

    
    group mood:

        attribute neut default null #neutral
        attribute angr null #angry
        attribute dist null #distant
        attribute happ null #happy
        attribute nerv null #nervous
        attribute pout null #pouting
        attribute sad null #sad
        attribute pani null #paniced
        attribute yand null #yandere

    group eyes:

        attribute oe default if_any(["neut", "happ", "pout", "sad"]):
            "mod_assets/MPT/mio/eyes/e1a.png"

        attribute oe default if_any(["angr", "pani"]):
            "mod_assets/MPT/mio/eyes/e1c.png"
        
        attribute oe default if_any(["dist", "nerv"]):
            "mod_assets/MPT/mio/eyes/e1b.png"
        
        attribute oe default if_any(["yand"]):
            "mod_assets/MPT/mio/eyes/e1d.png"
        
        
        attribute ce if_any(["neut", "angr", "dist", "sad", "pani"]):
            "mod_assets/MPT/mio/eyes/e2b.png"
        attribute ce if_any(["happ", "nerv", "pout", "yand"]):
            "mod_assets/MPT/mio/eyes/e2a.png"

        attribute e1a:
            "mod_assets/MPT/mio/eyes/e1a.png"
        attribute e1b:
            "mod_assets/MPT/mio/eyes/e1b.png"
        attribute e1c:
            "mod_assets/MPT/mio/eyes/e1c.png"
        attribute e1d:
            "mod_assets/MPT/mio/eyes/e1d.png"
        attribute e2a:
            "mod_assets/MPT/mio/eyes/e2a.png"
        attribute e2b:
            "mod_assets/MPT/mio/eyes/e2b.png"
        attribute e3a:
            "mod_assets/MPT/mio/eyes/e3a.png"
        attribute e3b:
            "mod_assets/MPT/mio/eyes/e3b.png"

    group brows:

        attribute brow default if_any(["neut", "happ", "pout", "yand"]):
            "mod_assets/MPT/mio/brows/b1a.png"
        attribute brow default if_any(["angr"]):
            "mod_assets/MPT/mio/brows/b1d.png"
        attribute brow default if_any(["dist", "nerv"]):
            "mod_assets/MPT/mio/brows/b1b.png"
        attribute brow default if_any(["sad", "pani"]):
            "mod_assets/MPT/mio/brows/b1c.png"

        attribute b1a:
            "mod_assets/MPT/mio/brows/b1a.png"
        attribute b1b:
            "mod_assets/MPT/mio/brows/b1b.png"
        attribute b1c:
            "mod_assets/MPT/mio/brows/b1c.png"
        attribute b1d:
            "mod_assets/MPT/mio/brows/b1d.png"

    group mouths:

        attribute cm default if_any(["neut", "dist", "sad"]):
            "mod_assets/MPT/mio/mouth/me.png"
        attribute cm default if_any(["angr", "pani"]):
            "mod_assets/MPT/mio/mouth/mh.png"
        attribute cm default if_any(["happ", "yand"]):
            "mod_assets/MPT/mio/mouth/mb.png"
        attribute cm default if_any(["nerv"]):
            "mod_assets/MPT/mio/mouth/ma.png"
        attribute cm default if_any(["pout"]):
            "mod_assets/MPT/mio/mouth/mi.png"
        
        attribute om if_any(["neut", "dist", "pout"]):
            "mod_assets/MPT/mio/mouth/md.png"
        attribute om if_any(["angr", "pani"]):
            "mod_assets/MPT/mio/mouth/mc.png"
        attribute om if_any(["happ", "nerv", "yand"]):
            "mod_assets/MPT/mio/mouth/mf.png"
        attribute om if_any(["sad"]):
            "mod_assets/MPT/mio/mouth/mg.png"

        attribute ma:
            "mod_assets/MPT/mio/mouth/ma.png"
        attribute mb:
            "mod_assets/MPT/mio/mouth/mb.png"
        attribute mc:
            "mod_assets/MPT/mio/mouth/mc.png"
        attribute md:
            "mod_assets/MPT/mio/mouth/md.png"
        attribute me:
            "mod_assets/MPT/mio/mouth/me.png"
        attribute mf:
            "mod_assets/MPT/mio/mouth/mf.png"
        attribute mg:
            "mod_assets/MPT/mio/mouth/mg.png"
        attribute mh:
            "mod_assets/MPT/mio/mouth/mh.png"
        attribute mi:
            "mod_assets/MPT/mio/mouth/mi.png"

    group nose:

        attribute nose default if_any(["neut", "angr", "dist", "happ", "pout", "sad", "pani", "yand"]):
            "mod_assets/MPT/mio/nose/n1.png"
        attribute nose default if_any(["nerv"]):
            "mod_assets/MPT/mio/nose/n2.png"

        attribute n1:
            "mod_assets/MPT/mio/nose/n1.png"
        attribute n2:
            "mod_assets/MPT/mio/nose/n2.png"
        attribute n3:
            "mod_assets/MPT/mio/nose/n3.png"
        attribute n4:
            "mod_assets/MPT/mio/nose/n4.png"

    
    group right:
        anchor (0,0) subpixel (True)
        yoffset (-0.5) xoffset(-0.5)

        attribute rup default if_any(["uniform"]) if_not(["cross"]):
            "mod_assets/MPT/mio/clothes/uniform/rup.png"
        attribute rup default if_any(["casual"]) if_not(["cross"]):
            "mod_assets/MPT/mio/clothes/casual/rup.png"

        attribute rdown if_any(["uniform"]) if_not(["cross"]):
            "mod_assets/MPT/mio/clothes/uniform/rdown.png"
        attribute rdown if_any(["casual"]) if_not(["cross"]):
            "mod_assets/MPT/mio/clothes/casual/rdown.png"

        attribute rchest if_any(["uniform"]) if_not(["cross"]):
            "mod_assets/MPT/mio/clothes/uniform/rchest.png"
        attribute rchest if_any(["casual"]) if_not(["cross"]):
            "mod_assets/MPT/mio/clothes/casual/rchest.png"

        attribute cross if_any(["uniform"]):
            "mod_assets/MPT/mio/clothes/uniform/cross.png"
        attribute cross if_any(["casual"]):
            "mod_assets/MPT/mio/clothes/casual/cross.png"

    group left:
        anchor (0,0) subpixel (True)
        yoffset (-0.5) xoffset(-0.5)

        attribute lup default if_any(["uniform"]) if_not(["cross"]):
            "mod_assets/MPT/mio/clothes/uniform/lup.png"
        attribute lup default if_any(["casual"]) if_not(["cross"]):
            "mod_assets/MPT/mio/clothes/casual/lup.png"

        attribute ldown if_any(["uniform"]) if_not(["cross"]):
            "mod_assets/MPT/mio/clothes/uniform/ldown.png"
        attribute ldown if_any(["casual"]) if_not(["cross"]):
            "mod_assets/MPT/mio/clothes/casual/ldown.png"

        attribute lchest if_any(["uniform"]) if_not(["cross"]):
            "mod_assets/MPT/mio/clothes/uniform/lchest.png"
        attribute lchest if_any(["casual"]) if_not(["cross"]):
            "mod_assets/MPT/mio/clothes/casual/lchest.png"
    

    group others:

        attribute fldown default if_any(["ldown"]) if_not(["rdown", "casual"]):
            "mod_assets/MPT/mio/others/uniform/fldown.png"
        attribute fldown default if_any(["ldown"])if_not(["rdown", "uniform"]):
            "mod_assets/MPT/mio/others/casual/fldown.png"

        attribute frdown default if_any(["rdown"]) if_not(["casual"]):
            "mod_assets/MPT/mio/others/uniform/frdown.png"
        attribute frdown default if_any(["rdown"]) if_not(["uniform"]):
            "mod_assets/MPT/mio/others/casual/frdown.png"

        attribute frchest default if_any(["rchest"]) if_not(["casual"]):
            "mod_assets/MPT/mio/others/uniform/frchest.png"
        attribute frchest default if_any[("rchest")] if_not(["uniform"]):
            "mod_assets/MPT/mio/others/casual/frchest.png"
        
