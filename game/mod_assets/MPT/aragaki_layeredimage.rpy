layeredimage aragaki turned:
    at AutofocusDisplayable(name="aragaki")

    group outfit:
        attribute uniform default null
        attribute casual null
    
    group left if_any(["uniform"]) if_not(["crossed"]): # had to make two dofferent groups for the left part
        attribute ldown default:
            "mod_assets/MPT/aragaki/outfits/uniform_ldown.png"
        
        attribute lup:
            "mod_assets/MPT/aragaki/outfits/uniform_lup.png"
        
        attribute lscratch:
            "mod_assets/MPT/aragaki/outfits/uniform_lscratch.png"
        
    group left if_any(["casual"]) if_not(["crossed"]): # since this one is a bit off centered
        subpixel True
        anchor (0.0, 0.0)
        xoffset 0.3

        attribute ldown default:
            "mod_assets/MPT/aragaki/outfits/casual_ldown.png"

        attribute lup:
            "mod_assets/MPT/aragaki/outfits/casual_lup.png"

        attribute lscratch:
            "mod_assets/MPT/aragaki/outfits/casual_lscratch.png"

    group right:
        attribute rdown default if_any(["uniform"]) if_not(["crossed"]):
            "mod_assets/MPT/aragaki/outfits/uniform_rdown.png"
        attribute rdown default if_any(["casual"]) if_not(["crossed"]):
            "mod_assets/MPT/aragaki/outfits/casual_rdown.png"
        
        attribute rpocket if_any(["uniform"]) if_not(["crossed"]):
            "mod_assets/MPT/aragaki/outfits/uniform_rpocket.png"
        attribute rpocket if_any(["casual"]) if_not(["crossed"]):
            "mod_assets/MPT/aragaki/outfits/casual_rpocket.png"

    group center:
        attribute not_crossed default null
        attribute crossed if_any(["uniform"]):
            "mod_assets/MPT/aragaki/outfits/uniform_crossed.png"
        attribute crossed if_any(["casual"]):
            "mod_assets/MPT/aragaki/outfits/casual_crossed.png"
    
    always: # render the head above the body, otherwise the back of the sweater overlaps
        subpixel True
        anchor (0.0, 0.0)
        yoffset -0.1
        
        "mod_assets/MPT/aragaki/facebase.png"

    group nose:
        attribute na default null                         # nothing
        attribute nb:
            "mod_assets/MPT/aragaki/nose_b.png"     # sweat drop
        attribute nc:
            "mod_assets/MPT/aragaki/nose_c.png"     # blush

    group mouth:
        attribute ma default:
            "mod_assets/MPT/aragaki/mouth_a.png"    # smiling
        attribute mb:
            "mod_assets/MPT/aragaki/mouth_b.png"    # smiling + talking
        attribute mc:
            "mod_assets/MPT/aragaki/mouth_c.png"    # big ass smile
        attribute md:
            "mod_assets/MPT/aragaki/mouth_d.png"    # closed mouth
        attribute me:
            "mod_assets/MPT/aragaki/mouth_e.png"    # closed mouth but it's a bit open
        attribute mf:
            "mod_assets/MPT/aragaki/mouth_f.png"    # talking
        attribute mg:
            "mod_assets/MPT/aragaki/mouth_g.png"    # closed mouth, "yeah no shit!" style
        attribute mh:
            "mod_assets/MPT/aragaki/mouth_h.png"    # surprised
        attribute mi:
            "mod_assets/MPT/aragaki/mouth_i.png"    # awkward laugh
        attribute mj:
            "mod_assets/MPT/aragaki/mouth_j.png"    # anger

    group eyes:
        attribute ea default:
            "mod_assets/MPT/aragaki/eyes_a.png"     # neutral
        attribute eb:
            "mod_assets/MPT/aragaki/eyes_b.png"     # serious
        attribute ec:
            "mod_assets/MPT/aragaki/eyes_c.png"     # surprised
        attribute ed:
            "mod_assets/MPT/aragaki/eyes_d.png"     # closed
        attribute ee:
            "mod_assets/MPT/aragaki/eyes_e.png"     # closed + happy
        
    group eyebrows:
        attribute ba default:
            "mod_assets/MPT/aragaki/eyebrows_a.png" # neutral
        attribute bb:
            "mod_assets/MPT/aragaki/eyebrows_b.png" # serious
        attribute bc:
            "mod_assets/MPT/aragaki/eyebrows_c.png" # surprised
        attribute bd:
            "mod_assets/MPT/aragaki/eyebrows_d.png" # anger
        attribute be:
            "mod_assets/MPT/aragaki/eyebrows_e.png" # worried
