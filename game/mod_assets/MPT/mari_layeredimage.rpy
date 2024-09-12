layeredimage mari forward:
    always:
        "mod_assets/MPT/mari/body.png"
    
    
    
    group mood: 
        attribute neut default null
        attribute angr null
        attribute sad null
        attribute dist null
        attribute worr null
        attribute anno null
        attribute happ null
        attribute curi null
    
    
    
    group mouth:
        
        anchor (0,0) subpixel (True)
        
        # These defaults only have 6 mouths because the other three wouldn't work with any of the default emotions and were better off manually added onto other emotions
        attribute cm default if_any(["happ","neut","curi"]):
            "mod_assets/MPT/mari/mouths/a.png"
        attribute cm default if_any(["anno"]):
            "mod_assets/MPT/mari/mouths/f.png"
        attribute cm default if_any(["sad","angr","dist","worr"]):
            "mod_assets/MPT/mari/mouths/g.png"
        
        attribute om if_any(["happ","curi","neut"]):
            "mod_assets/MPT/mari/mouths/d.png"
        attribute om if_any(["angr","worr","sad","anno"]):
            "mod_assets/MPT/mari/mouths/h.png"
        attribute om if_any(["dist"]):
            "mod_assets/MPT/mari/mouths/i.png"
        
        attribute ma:
            "mod_assets/MPT/mari/mouths/a.png"
        attribute mb:
            "mod_assets/MPT/mari/mouths/b.png"
        attribute mc:
            "mod_assets/MPT/mari/mouths/c.png"
        attribute md:
            "mod_assets/MPT/mari/mouths/d.png"
        attribute me:
            "mod_assets/MPT/mari/mouths/e.png"
        attribute mf:
            "mod_assets/MPT/mari/mouths/f.png"
        attribute mg:
            "mod_assets/MPT/mari/mouths/g.png"
        attribute mh:
            "mod_assets/MPT/mari/mouths/h.png"
        attribute mi:
            "mod_assets/MPT/mari/mouths/i.png"
    
    
    
    group eyes:
        
        anchor (0,0) subpixel (True)
        
        # Apparently this character only has open eyes
        attribute oe default if_any(["neut"]):
            "mod_assets/MPT/mari/eyes/a.png"
        attribute oe default if_any(["angr","sad","worr","anno","happ","curi"]):
            "mod_assets/MPT/mari/eyes/f.png"
        attribute oe default if_any(["dist"]):
            "mod_assets/MPT/mari/eyes/d.png"

        attribute ea:
            "mod_assets/MPT/mari/eyes/a.png"
        attribute eb:
            "mod_assets/MPT/mari/eyes/b.png"
        attribute ec:
            "mod_assets/MPT/mari/eyes/c.png"
        attribute ed:
            "mod_assets/MPT/mari/eyes/d.png"
        attribute ee:
            "mod_assets/MPT/mari/eyes/e.png"
        attribute ef:
            "mod_assets/MPT/mari/eyes/f.png"
    
    
    group eyebrows:
        
        anchor (0,0) subpixel (True)
        
        #Default Eyebrows:
        attribute brow default if_any(["anno","angr"]):
            "mod_assets/MPT/mari/brows/b.png"
        attribute brow default if_any(["happ","sad","dist","worr"]):
            "mod_assets/MPT/mari/brows/a.png"
        attribute brow default if_any(["neut"]):
            "mod_assets/MPT/mari/brows/c.png"
        attribute brow default if_any(["curi"]):
            "mod_assets/MPT/mari/brows/d.png"
        
        attribute ba:
            "mod_assets/MPT/mari/brows/a.png"
        attribute bb:
            "mod_assets/MPT/mari/brows/b.png"
        attribute bc:
            "mod_assets/MPT/mari/brows/c.png"
        attribute bd:
            "mod_assets/MPT/mari/brows/d.png"
    
    
    group tears:
        attribute none default null
        attribute tears:
            "mod_assets/MPT/mari/tears.png"

