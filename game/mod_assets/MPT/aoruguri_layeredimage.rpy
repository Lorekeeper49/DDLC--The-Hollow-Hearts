layeredimage aoruguri turned:
    at AutofocusDisplayable(name="aoruguri")

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
    
    always:
        "mod_assets/MPT/aoruguri/Uniform/body.png" if_any(["uniform"])
    always:
        "mod_assets/MPT/aoruguri/Casual/body.png" if_any(["casual"])

    group left:
        subpixel (True)
        
        attribute ldown default if_any(["uniform"]):
            "mod_assets/MPT/aoruguri/Uniform/ldown.png"
        attribute lup if_any(["uniform"]):
            "mod_assets/MPT/aoruguri/Uniform/lup.png"
        attribute lhip if_any(["uniform"]):
            "mod_assets/MPT/aoruguri/Uniform/lhip.png"
        
        attribute ldown default if_any(["casual"]):
            "mod_assets/MPT/aoruguri/Casual/ldown.png"
        attribute lup if_any(["casual"]):
            "mod_assets/MPT/aoruguri/Casual/lup.png"
        attribute lhip if_any(["casual"]):
            "mod_assets/MPT/aoruguri/Casual/lhip.png"
    
    
    
    group right:
        subpixel (True)
        
        attribute rdown default if_any(["uniform"]):
            "mod_assets/MPT/aoruguri/Uniform/rdown.png"
        attribute rup if_any(["uniform"]):
            "mod_assets/MPT/aoruguri/Uniform/rup.png"
        attribute rhip if_any(["uniform"]):
            "mod_assets/MPT/aoruguri/Uniform/rhip.png"
        
        attribute rdown default if_any(["casual"]):
            "mod_assets/MPT/aoruguri/Casual/rdown.png"
        attribute rup if_any(["casual"]):
            "mod_assets/MPT/aoruguri/Casual/rup.png"
        attribute rhip if_any(["casual"]):
            "mod_assets/MPT/aoruguri/Casual/rhip.png"
    
    
    
    group mouth:
        
        anchor (0,0) subpixel (True)
        
        attribute cm default if_any(["neut","doub","curi"]):
            "mod_assets/MPT/aoruguri/mouth/c.png"
        attribute cm default if_any(["happ","laug"]):
            "mod_assets/MPT/aoruguri/mouth/a.png"
        attribute cm default if_any(["dist","sad","angr","vang","anno","cry","worr"]):
            "mod_assets/MPT/aoruguri/mouth/b.png"
        
        attribute om if_any(["neut","doub"]):
            "mod_assets/MPT/aoruguri/mouth/f.png"
        attribute om if_any(["happ","laugh"]):
            "mod_assets/MPT/aoruguri/mouth/d.png"
        attribute om if_any(["dist","sad","worr","curi","cry","angr","vang","anno"]):
            "mod_assets/MPT/aoruguri/mouth/e.png"
        
        attribute ma:
            "mod_assets/MPT/aoruguri/mouth/a.png"
        attribute mb:
            "mod_assets/MPT/aoruguri/mouth/b.png"
        attribute mc:
            "mod_assets/MPT/aoruguri/mouth/c.png"
        attribute md:
            "mod_assets/MPT/aoruguri/mouth/d.png"
        attribute me:
            "mod_assets/MPT/aoruguri/mouth/e.png"
        attribute mf:
            "mod_assets/MPT/aoruguri/mouth/f.png"
    
    
    
    group eyes:
        
        anchor (0,0) subpixel (True)
        
        attribute oe default if_any(["neut","happ","anno"]):
            "mod_assets/MPT/aoruguri/eyes/a.png"
        attribute oe default if_any(["angr"]):
            "mod_assets/MPT/aoruguri/eyes/d.png"
        attribute oe default if_any(["sad","worr","curi","laug"]):
            "mod_assets/MPT/aoruguri/eyes/e.png"
        attribute oe default if_any(["cry"]):
            "mod_assets/MPT/aoruguri/eyes/f.png"
        attribute oe default if_any(["doub"]):
            "mod_assets/MPT/aoruguri/eyes/h.png"
        attribute oe default if_any(["dist", "vang"]):
            "mod_assets/MPT/aoruguri/eyes/i.png"
        
        attribute ce if_any(["neut","angr","sad","doub","worr","anno","vang","dist"]):
            "mod_assets/MPT/aoruguri/eyes/b.png"
        attribute ce if_any(["happ","laug","curi"]):
            "mod_assets/MPT/aoruguri/eyes/c.png"
        attribute ce if_any(["cry"]):
            "mod_assets/MPT/aoruguri/eyes/g.png"
        
        attribute wink:
            "mod_assets/MPT/aoruguri/eyes/wink.png"

        attribute ea:
            "mod_assets/MPT/aoruguri/eyes/a.png"
        attribute eb:
            "mod_assets/MPT/aoruguri/eyes/b.png"
        attribute ec:
            "mod_assets/MPT/aoruguri/eyes/c.png"
        attribute ed:
            "mod_assets/MPT/aoruguri/eyes/d.png"
        attribute ee:
            "mod_assets/MPT/aoruguri/eyes/e.png"
        attribute ef:
            "mod_assets/MPT/aoruguri/eyes/f.png"
        attribute eg:
            "mod_assets/MPT/aoruguri/eyes/g.png"
        attribute eh:
            "mod_assets/MPT/aoruguri/eyes/h.png"
        attribute ei:
            "mod_assets/MPT/aoruguri/eyes/i.png"
    
    
    group eyebrows:
        
        anchor (0,0) subpixel (True)
        
        #Default Eyebrows:
        attribute brow default if_any(["neut","curi","doub"]):
            "mod_assets/MPT/aoruguri/brows/b.png"
        attribute brow default if_any(["happ","laug",]):
            "mod_assets/MPT/aoruguri/brows/a.png"
        attribute brow default if_any(["sad","cry","dist","worr"]):
            "mod_assets/MPT/aoruguri/brows/d.png"
        attribute brow default if_any(["angr","vang","anno"]):
            "mod_assets/MPT/aoruguri/brows/c.png"
        
        attribute ba:
            "mod_assets/MPT/aoruguri/brows/a.png"
        attribute bb:
            "mod_assets/MPT/aoruguri/brows/b.png"
        attribute bc:
            "mod_assets/MPT/aoruguri/brows/c.png"
        attribute bd:
            "mod_assets/MPT/aoruguri/brows/d.png"

    group blush:
        attribute na default null
        attribute nb:
            "mod_assets/MPT/aoruguri/blush.png"
    
    
    group hair:
        attribute plain default null
        attribute storm:
            "mod_assets/MPT/aoruguri/storm.png"

layeredimage aoruguri crossed:
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
    
    always:
        "mod_assets/MPT/aoruguri/Uniform/body.png" if_any(["uniform"])
    always:
        "mod_assets/MPT/aoruguri/Casual/body.png" if_any(["casual"])
    always:
        "mod_assets/MPT/aoruguri/Uniform/cross.png" if_any(["uniform"])
    always:
        "mod_assets/MPT/aoruguri/Casual/cross.png" if_any(["casual"])
    
    
    group mouth:
        
        anchor (0,0) subpixel (True)
        
        attribute cm default if_any(["neut","doub","curi"]):
            "mod_assets/MPT/aoruguri/mouth/c.png"
        attribute cm default if_any(["happ","laug"]):
            "mod_assets/MPT/aoruguri/mouth/a.png"
        attribute cm default if_any(["dist","sad","angr","vang","anno","cry","worr"]):
            "mod_assets/MPT/aoruguri/mouth/b.png"
        
        attribute om if_any(["neut","doub"]):
            "mod_assets/MPT/aoruguri/mouth/f.png"
        attribute om if_any(["happ","laugh"]):
            "mod_assets/MPT/aoruguri/mouth/d.png"
        attribute om if_any(["dist","sad","worr","curi","cry","angr","vang","anno"]):
            "mod_assets/MPT/aoruguri/mouth/e.png"
        
        attribute ma:
            "mod_assets/MPT/aoruguri/mouth/a.png"
        attribute mb:
            "mod_assets/MPT/aoruguri/mouth/b.png"
        attribute mc:
            "mod_assets/MPT/aoruguri/mouth/c.png"
        attribute md:
            "mod_assets/MPT/aoruguri/mouth/d.png"
        attribute me:
            "mod_assets/MPT/aoruguri/mouth/e.png"
        attribute mf:
            "mod_assets/MPT/aoruguri/mouth/f.png"
    
    
    
    group eyes:
        
        anchor (0,0) subpixel (True)
        
        attribute oe default if_any(["neut","happ","anno"]):
            "mod_assets/MPT/aoruguri/eyes/a.png"
        attribute oe default if_any(["angr"]):
            "mod_assets/MPT/aoruguri/eyes/d.png"
        attribute oe default if_any(["sad","worr","curi","laug"]):
            "mod_assets/MPT/aoruguri/eyes/e.png"
        attribute oe default if_any(["cry"]):
            "mod_assets/MPT/aoruguri/eyes/f.png"
        attribute oe default if_any(["doub"]):
            "mod_assets/MPT/aoruguri/eyes/h.png"
        attribute oe default if_any(["dist", "vang"]):
            "mod_assets/MPT/aoruguri/eyes/i.png"
        
        attribute ce if_any(["neut","angr","sad","doub","worr","anno","vang","dist"]):
            "mod_assets/MPT/aoruguri/eyes/b.png"
        attribute ce if_any(["happ","laug","curi"]):
            "mod_assets/MPT/aoruguri/eyes/c.png"
        attribute ce if_any(["cry"]):
            "mod_assets/MPT/aoruguri/eyes/g.png"
        
        attribute wink:
            "mod_assets/MPT/aoruguri/eyes/wink.png"

        attribute ea:
            "mod_assets/MPT/aoruguri/eyes/a.png"
        attribute eb:
            "mod_assets/MPT/aoruguri/eyes/b.png"
        attribute ec:
            "mod_assets/MPT/aoruguri/eyes/c.png"
        attribute ed:
            "mod_assets/MPT/aoruguri/eyes/d.png"
        attribute ee:
            "mod_assets/MPT/aoruguri/eyes/e.png"
        attribute ef:
            "mod_assets/MPT/aoruguri/eyes/f.png"
        attribute eg:
            "mod_assets/MPT/aoruguri/eyes/g.png"
        attribute eh:
            "mod_assets/MPT/aoruguri/eyes/h.png"
        attribute ei:
            "mod_assets/MPT/aoruguri/eyes/i.png"
    
    
    group eyebrows:
        
        anchor (0,0) subpixel (True)
        
        #Default Eyebrows:
        attribute brow default if_any(["neut","curi","doub"]):
            "mod_assets/MPT/aoruguri/brows/b.png"
        attribute brow default if_any(["happ","laug",]):
            "mod_assets/MPT/aoruguri/brows/a.png"
        attribute brow default if_any(["sad","cry","dist","worr"]):
            "mod_assets/MPT/aoruguri/brows/d.png"
        attribute brow default if_any(["angr","vang","anno"]):
            "mod_assets/MPT/aoruguri/brows/c.png"
        
        attribute ba:
            "mod_assets/MPT/aoruguri/brows/a.png"
        attribute bb:
            "mod_assets/MPT/aoruguri/brows/b.png"
        attribute bc:
            "mod_assets/MPT/aoruguri/brows/c.png"
        attribute bd:
            "mod_assets/MPT/aoruguri/brows/d.png"

    group blush:
        attribute na default null
        attribute nb:
            "mod_assets/MPT/aoruguri/blush.png"
    
    
    group hair:
        attribute plain default null
        attribute storm:
            "mod_assets/MPT/aoruguri/storm.png"