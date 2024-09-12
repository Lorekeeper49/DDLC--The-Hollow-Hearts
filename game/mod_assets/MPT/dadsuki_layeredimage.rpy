layeredimage dadsuki towards:

    always "mod_assets/MPT/dadsuki/base.png"

    group outfit:
        
        attribute casual default null
    
    group moods:

        attribute neut default null
        attribute angr null
        attribute cry null
        attribute curi null
        attribute happ null
        attribute nerv null
        attribute shoc null
        attribute sad null
        attribute vang null

    group eyes:

        attribute oe default if_any(["neut", "angr", "curi", "happ"]):
            "mod_assets/MPT/dadsuki/eyes/e1a.png"
        attribute oe default if_any(["cry"]):
            "mod_assets/MPT/dadsuki/eyes/e1d.png"
        attribute oe default if_any(["nerv", "sad"]):
            "mod_assets/MPT/dadsuki/eyes/e1b.png"
        attribute oe default if_any(["shoc", "vang"]):
            "mod_assets/MPT/dadsuki/eyes/e1c.png"

        attribute ce if_any(["neut", "angr", "curi", "happ", "sad", "vang", "nerv", "shoc"]):
            "mod_assets/MPT/dadsuki/eyes/e2a.png"
        attribute ce if_any(["cry"]):
            "mod_assets/MPT/dadsuki/eyes/e2b.png"

        attribute e1a:
            "mod_assets/MPT/dadsuki/eyes/e1a.png"
        attribute e1b:
            "mod_assets/MPT/dadsuki/eyes/e1b.png"
        attribute e1c:
            "mod_assets/MPT/dadsuki/eyes/e1c.png"
        attribute e1d:
            "mod_assets/MPT/dadsuki/eyes/e1d.png"
        attribute e2a:
            "mod_assets/MPT/dadsuki/eyes/e2a.png"
        attribute e2b:
            "mod_assets/MPT/dadsuki/eyes/e2b.png"

    group brows:

        attribute brows default if_any(["neut", "happ", "shoc"]) if_not(["ce"]):
            "mod_assets/MPT/dadsuki/brows/b1a.png"
        attribute brows default if_any(["neut", "happ", "shoc"]) if_not(["oe"]):
            "mod_assets/MPT/dadsuki/brows/b1aC.png"

        attribute brows default if_any(["angr", "vang"]) if_not(["ce"]):
            "mod_assets/MPT/dadsuki/brows/b1b.png"
        attribute brows default if_any(["angr", "vang"]) if_not(["oe"]):
            "mod_assets/MPT/dadsuki/brows/b1bC.png"

        attribute brows default if_any(["cry", "nerv", "sad"]) if_not(["ce"]):
            "mod_assets/MPT/dadsuki/brows/b1c.png"
        attribute brows default if_any(["cry", "sad", "nerv"]) if_not(["oe"]):
            "mod_assets/MPT/dadsuki/brows/b2a.png"

        attribute brows default if_any(["curi"]) if_not(["ce"]):
            "mod_assets/MPT/dadsuki/brows/b1d.png"
        attribute brows default if_any(["curi"]) if_not(["oe"]):
            "mod_assets/MPT/dadsuki/brows/b1dC.png"


        attribute b1a if_not(["b2a", "ce"]):
            "mod_assets/MPT/dadsuki/brows/b1a.png"
        attribute b1aC if_any(["b2a", "ce"]):
            "mod_assets/MPT/dadsuki/brows/b1aC.png"
        
        attribute b1b if_not(["b2a", "ce"]):
            "mod_assets/MPT/dadsuki/brows/b1b.png"
        attribute b1bC if_any(["b2a", "ce"]):
            "mod_assets/MPT/dadsuki/brows/b1bC.png"
        
        attribute b1c:
            "mod_assets/MPT/dadsuki/brows/b1c.png"
        
        attribute b1d if_not(["b2a", "ce"]):
            "mod_assets/MPT/dadsuki/brows/b1d.png"
        attribute b1dC if_any(["b2a", "ce"]):
            "mod_assets/MPT/dadsuki/brows/b1dC.png"

        attribute b2a:
            "mod_assets/MPT/dadsuki/brows/b2a.png"
    
    group mouths:

        attribute cm default if_any(["neut", "angr", "cry", "curi", "shoc", "sad"]):
            "mod_assets/MPT/dadsuki/mouths/ma.png"
        attribute cm default if_any(["happ", "nerv"]):
            "mod_assets/MPT/dadsuki/mouths/mb.png"
        attribute cm default if_any(["vang"]):
            "mod_assets/MPT/dadsuki/mouths/md.png"

        attribute om if_any(["neut", "angr", "cry", "curi", "nerv", "shoc", "sad", "happ"]):
            "mod_assets/MPT/dadsuki/mouths/mc.png"
        attribute om if_any(["vang"]):
            "mod_assets/MPT/dadsuki/mouths/me.png"

        attribute ma:
            "mod_assets/MPT/dadsuki/mouths/ma.png"
        attribute mb:
            "mod_assets/MPT/dadsuki/mouths/mb.png"
        attribute mc:
            "mod_assets/MPT/dadsuki/mouths/mc.png"
        attribute md:
            "mod_assets/MPT/dadsuki/mouths/md.png"
        attribute me:
            "mod_assets/MPT/dadsuki/mouths/me.png"
    
    group nose:
        
        attribute n1:
            "mod_assets/MPT/dadsuki/nose/n1.png"

    group right:
        anchor (0,0) subpixel (True)
        yoffset (-0.5) xoffset(-0.5)

        attribute rdown default if_not(["cross"]):
            "mod_assets/MPT/dadsuki/clothes/1r.png"
        attribute rup if_not(["cross"]):
            "mod_assets/MPT/dadsuki/clothes/2r.png"
        attribute cross:
            "mod_assets/MPT/dadsuki/clothes/3a.png"
    
    group left:
        anchor (0,0) subpixel (True)
        yoffset (-0.5) xoffset(-0.5)

        attribute ldown default if_not(["cross"]):
            "mod_assets/MPT/dadsuki/clothes/1l.png"
        attribute lup if_not(["cross"]):
            "mod_assets/MPT/dadsuki/clothes/2l.png"