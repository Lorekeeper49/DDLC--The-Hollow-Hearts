layeredimage hanato day:
    
    always "mod_assets/MPT/hanato/Day/face_base.png"
    
    
    
    group outfit: 
        attribute uniform default null
        attribute casual null
    
    
    
    group mood: 
        attribute neut default null
        attribute angr null
        attribute vang null
        attribute sad null
        attribute cry null
        attribute doub null
        attribute dist null
        attribute worr null
        attribute anno null
        attribute happ null
        attribute laug null
        attribute curi null
    
    
    group left:
        subpixel (True)

        attribute ldown default if_any(["uniform"]):
            "mod_assets/MPT/hanato/Day/Uniform/ldown.png"
        attribute lup if_any(["uniform"]):
            "mod_assets/MPT/hanato/Day/Uniform/lup.png"
        attribute lhip if_any(["uniform"]):
            "mod_assets/MPT/hanato/Day/Uniform/lhip.png"
        
        attribute ldown default if_any(["casual"]):
            "mod_assets/MPT/hanato/Day/Casual/ldown.png"
        attribute lup if_any(["casual"]):
            "mod_assets/MPT/hanato/Day/Casual/lup.png"
        attribute lhip if_any(["casual"]):
            "mod_assets/MPT/hanato/Day/Casual/lhip.png"
    
    
    
    group right:
        subpixel (True)
        attribute rdown default if_any(["uniform"]):
            "mod_assets/MPT/hanato/Day/Uniform/rdown.png"
        attribute rup if_any(["uniform"]):
            "mod_assets/MPT/hanato/Day/Uniform/rup.png"
        attribute rhip if_any(["uniform"]):
            "mod_assets/MPT/hanato/Day/Uniform/rhip.png"
        
        attribute rdown default if_any(["casual"]):
            "mod_assets/MPT/hanato/Day/Casual/rdown.png"
        attribute rup if_any(["casual"]):
            "mod_assets/MPT/hanato/Day/Casual/rup.png"
        attribute rhip if_any(["casual"]):
            "mod_assets/MPT/hanato/Day/Casual/rhip.png"
    
    
    
    group mouth:
        
        anchor (0,0) subpixel (True)
        
        attribute cm default if_any(["neut","doub"]):
            "mod_assets/MPT/hanato/Day/mouth/a.png"
        attribute cm default if_any(["happ","laug"]):
            "mod_assets/MPT/hanato/Day/mouth/d.png"
        attribute cm default if_any(["curi","dist"]):
            "mod_assets/MPT/hanato/Day/mouth/f.png"
        attribute cm default if_any(["sad","angr","vang","anno","cry","worr"]):
            "mod_assets/MPT/hanato/Day/mouth/h.png"
        
        attribute om if_any(["neut","doub"]):
            "mod_assets/MPT/hanato/Day/mouth/a.png"
        attribute om if_any(["happ","laugh"]):
            "mod_assets/MPT/hanato/Day/mouth/c.png"
        attribute om if_any(["dist"]):
            "mod_assets/MPT/hanato/Day/mouth/e.png"
        attribute om if_any(["sad","worr","curi","cry"]):
            "mod_assets/MPT/hanato/Day/mouth/g.png"
        attribute om if_any(["angr","vang","anno"]):
            "mod_assets/MPT/hanato/Day/mouth/i.png"
        
        
        attribute ma:
            "mod_assets/MPT/hanato/Day/mouth/a.png"
        attribute mb:
            "mod_assets/MPT/hanato/Day/mouth/b.png"
        attribute mc:
            "mod_assets/MPT/hanato/Day/mouth/c.png"
        attribute md:
            "mod_assets/MPT/hanato/Day/mouth/d.png"
        attribute me:
            "mod_assets/MPT/hanato/Day/mouth/e.png"
        attribute mf:
            "mod_assets/MPT/hanato/Day/mouth/f.png"
        attribute mg:
            "mod_assets/MPT/hanato/Day/mouth/g.png"
        attribute mh:
            "mod_assets/MPT/hanato/Day/mouth/h.png"
        attribute mi:
            "mod_assets/MPT/hanato/Day/mouth/i.png"
    
    
    
    group eyes:
        
        anchor (0,0) subpixel (True)
        
        attribute oe default if_any(["neut","happ","anno"]):
            "mod_assets/MPT/hanato/Day/eyes/a.png"
        attribute oe default if_any(["angr"]):
            "mod_assets/MPT/hanato/Day/eyes/d.png"
        attribute oe default if_any(["sad","worr"]):
            "mod_assets/MPT/hanato/Day/eyes/e.png"
        attribute oe default if_any(["curi","laug"]):
            "mod_assets/MPT/hanato/Day/eyes/f.png"
        attribute oe default if_any(["cry"]):
            "mod_assets/MPT/hanato/Day/eyes/g.png"
        attribute oe default if_any(["doub"]):
            "mod_assets/MPT/hanato/Day/eyes/i.png"
        attribute oe default if_any(["dist"]):
            "mod_assets/MPT/hanato/Day/eyes/j.png"
        attribute oe default if_any(["vang"]):
            "mod_assets/MPT/hanato/Day/eyes/j.png"

        attribute ce if_any(["neut","angr","sad","doub","worr","anno","vang","dist"]):
            "mod_assets/MPT/hanato/Day/eyes/b"
        attribute ce if_any(["happ","laug","curi"]):
            "mod_assets/MPT/hanato/Day/eyes/c"
        attribute ce if_any(["cry"]):
            "mod_assets/MPT/hanato/Day/eyes/h.png"
        
        attribute wink:
            "mod_assets/MPT/hanato/Day/eyes/wink.png"
        
        attribute ea:
            "mod_assets/MPT/hanato/Day/eyes/a.png"
        attribute eb:
            "mod_assets/MPT/hanato/Day/eyes/b.png"
        attribute ec:
            "mod_assets/MPT/hanato/Day/eyes/c.png"
        attribute ed:
            "mod_assets/MPT/hanato/Day/eyes/d.png"
        attribute ee:
            "mod_assets/MPT/hanato/Day/eyes/e.png"
        attribute ef:
            "mod_assets/MPT/hanato/Day/eyes/f.png"
        attribute eg:
            "mod_assets/MPT/hanato/Day/eyes/g.png"
        attribute eh:
            "mod_assets/MPT/hanato/Day/eyes/h.png"
        attribute ei:
            "mod_assets/MPT/hanato/Day/eyes/i.png"
        attribute ej:
            "mod_assets/MPT/hanato/Day/eyes/j.png"
        attribute ek:
            "mod_assets/MPT/hanato/Day/eyes/k.png"
    
    
    group blush:
        attribute na default null
        attribute nb:
            "mod_assets/MPT/hanato/Day/blush/a.png"
        attribute nc:
            "mod_assets/MPT/hanato/Day/blush/b.png"
    
    
    group eyebrows:
        
        anchor (0,0) subpixel (True)
        
        #Default Eyebrows:
        attribute brow default if_any(["neut","happ","laug"]):
            "mod_assets/MPT/hanato/Day/brows/a.png"
        attribute brow default if_any(["angr","vang","anno"]):
            "mod_assets/MPT/hanato/Day/brows/b.png"
        attribute brow default if_any(["sad","cry","dist","worr"]):
            "mod_assets/MPT/hanato/Day/brows/c.png"
        attribute brow default if_any(["curi","doub"]):
            "mod_assets/MPT/hanato/Day/brows/d.png"
        
        attribute ba:
            "mod_assets/MPT/hanato/Day/brows/a.png"
        attribute bb:
            "mod_assets/MPT/hanato/Day/brows/b.png"
        attribute bc:
            "mod_assets/MPT/hanato/Day/brows/c.png"
        attribute bd:
            "mod_assets/MPT/hanato/Day/brows/d.png"

layeredimage hanato night:
    
    always "mod_assets/MPT/hanato/Night/face_base.png"
    
    
    
    group outfit: 
        attribute uniform default null
        attribute casual null
    
    
    
    group mood: 
        attribute neut default null
        attribute angr null
        attribute vang null
        attribute sad null
        attribute cry null
        attribute doub null
        attribute dist null
        attribute worr null
        attribute anno null
        attribute happ null
        attribute laug null
        attribute curi null
    
    
    group left:
        subpixel (True)

        attribute ldown default if_any(["uniform"]):
            "mod_assets/MPT/hanato/Night/Uniform/ldown.png"
        attribute lup if_any(["uniform"]):
            "mod_assets/MPT/hanato/Night/Uniform/lup.png"
        attribute lhip if_any(["uniform"]):
            "mod_assets/MPT/hanato/Night/Uniform/lhip.png"
        
        attribute ldown default if_any(["casual"]):
            "mod_assets/MPT/hanato/Night/Casual/ldown.png"
        attribute lup if_any(["casual"]):
            "mod_assets/MPT/hanato/Night/Casual/lup.png"
        attribute lhip if_any(["casual"]):
            "mod_assets/MPT/hanato/Night/Casual/lhip.png"
    
    
    
    group right:
        subpixel (True)

        attribute rdown default if_any(["uniform"]):
            "mod_assets/MPT/hanato/Night/Uniform/rdown.png"
        attribute rup if_any(["uniform"]):
            "mod_assets/MPT/hanato/Night/Uniform/rup.png"
        attribute rhip if_any(["uniform"]):
            "mod_assets/MPT/hanato/Night/Uniform/rhip.png"
        
        attribute rdown default if_any(["casual"]):
            "mod_assets/MPT/hanato/Night/Casual/rdown.png"
        attribute rup if_any(["casual"]):
            "mod_assets/MPT/hanato/Night/Casual/rup.png"
        attribute rhip if_any(["casual"]):
            "mod_assets/MPT/hanato/Night/Casual/rhip.png"
    
    
    
    group mouth:
        
        anchor (0,0) subpixel (True)
        
        attribute cm default if_any(["neut","doub"]):
            "mod_assets/MPT/hanato/Night/mouth/a.png"
        attribute cm default if_any(["happ","laug"]):
            "mod_assets/MPT/hanato/Night/mouth/d.png"
        attribute cm default if_any(["curi","dist"]):
            "mod_assets/MPT/hanato/Night/mouth/f.png"
        attribute cm default if_any(["sad","angr","vang","anno","cry","worr"]):
            "mod_assets/MPT/hanato/Night/mouth/h.png"
        
        attribute om if_any(["neut","doub"]):
            "mod_assets/MPT/hanato/Night/mouth/a.png"
        attribute om if_any(["happ","laugh"]):
            "mod_assets/MPT/hanato/Night/mouth/c.png"
        attribute om if_any(["dist"]):
            "mod_assets/MPT/hanato/Night/mouth/e.png"
        attribute om if_any(["sad","worr","curi","cry"]):
            "mod_assets/MPT/hanato/Night/mouth/g.png"
        attribute om if_any(["angr","vang","anno"]):
            "mod_assets/MPT/hanato/Night/mouth/i.png"
        
        
        attribute ma:
            "mod_assets/MPT/hanato/Night/mouth/a.png"
        attribute mb:
            "mod_assets/MPT/hanato/Night/mouth/b.png"
        attribute mc:
            "mod_assets/MPT/hanato/Night/mouth/c.png"
        attribute md:
            "mod_assets/MPT/hanato/Night/mouth/d.png"
        attribute me:
            "mod_assets/MPT/hanato/Night/mouth/e.png"
        attribute mf:
            "mod_assets/MPT/hanato/Night/mouth/f.png"
        attribute mg:
            "mod_assets/MPT/hanato/Night/mouth/g.png"
        attribute mh:
            "mod_assets/MPT/hanato/Night/mouth/h.png"
        attribute mi:
            "mod_assets/MPT/hanato/Night/mouth/i.png"
    
    
    
    group eyes:
        
        anchor (0,0) subpixel (True)
        
        attribute oe default if_any(["neut","happ","anno"]):
            "mod_assets/MPT/hanato/Night/eyes/a.png"
        attribute oe default if_any(["angr"]):
            "mod_assets/MPT/hanato/Night/eyes/d.png"
        attribute oe default if_any(["sad","worr"]):
            "mod_assets/MPT/hanato/Night/eyes/e.png"
        attribute oe default if_any(["curi","laug"]):
            "mod_assets/MPT/hanato/Night/eyes/f.png"
        attribute oe default if_any(["cry"]):
            "mod_assets/MPT/hanato/Night/eyes/g.png"
        attribute oe default if_any(["doub"]):
            "mod_assets/MPT/hanato/Night/eyes/i.png"
        attribute oe default if_any(["dist"]):
            "mod_assets/MPT/hanato/Night/eyes/j.png"
        attribute oe default if_any(["vang"]):
            "mod_assets/MPT/hanato/Night/eyes/j.png"
        
        attribute ce if_any(["neut","angr","sad","doub","worr","anno","vang","dist"]):
            "mod_assets/MPT/hanato/Night/eyes/b"
        attribute ce if_any(["happ","laug","curi"]):
            "mod_assets/MPT/hanato/Night/eyes/c"
        attribute ce if_any(["cry"]):
            "mod_assets/MPT/hanato/Night/eyes/h.png"
        
        attribute wink:
            "mod_assets/MPT/hanato/Night/eyes/wink.png"
        
        attribute ea:
            "mod_assets/MPT/hanato/Night/eyes/a.png"
        attribute eb:
            "mod_assets/MPT/hanato/Night/eyes/b.png"
        attribute ec:
            "mod_assets/MPT/hanato/Night/eyes/c.png"
        attribute ed:
            "mod_assets/MPT/hanato/Night/eyes/d.png"
        attribute ee:
            "mod_assets/MPT/hanato/Night/eyes/e.png"
        attribute ef:
            "mod_assets/MPT/hanato/Night/eyes/f.png"
        attribute eg:
            "mod_assets/MPT/hanato/Night/eyes/g.png"
        attribute eh:
            "mod_assets/MPT/hanato/Night/eyes/h.png"
        attribute ei:
            "mod_assets/MPT/hanato/Night/eyes/i.png"
        attribute ej:
            "mod_assets/MPT/hanato/Night/eyes/j.png"
        attribute ek:
            "mod_assets/MPT/hanato/Night/eyes/k.png"
    
    
    group blush:
        attribute na default null
        attribute nb:
            "mod_assets/MPT/hanato/Night/blush/a.png"
        attribute nc:
            "mod_assets/MPT/hanato/Night/blush/b.png"
    
    
    group eyebrows:
        
        anchor (0,0) subpixel (True)
        
        #Default Eyebrows:
        attribute brow default if_any(["neut","happ","laug"]):
            "mod_assets/MPT/hanato/Night/brows/a.png"
        attribute brow default if_any(["angr","vang","anno"]):
            "mod_assets/MPT/hanato/Night/brows/b.png"
        attribute brow default if_any(["sad","cry","dist","worr"]):
            "mod_assets/MPT/hanato/Night/brows/c.png"
        attribute brow default if_any(["curi","doub"]):
            "mod_assets/MPT/hanato/Night/brows/d.png"
        
        attribute ba:
            "mod_assets/MPT/hanato/Night/brows/a.png"
        attribute bb:
            "mod_assets/MPT/hanato/Night/brows/b.png"
        attribute bc:
            "mod_assets/MPT/hanato/Night/brows/c.png"
        attribute bd:
            "mod_assets/MPT/hanato/Night/brows/d.png"