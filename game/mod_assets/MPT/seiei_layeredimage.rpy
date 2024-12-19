init python:

    #base folder of the MPT. If you need to change the path for
    #whatever reason, just change the one below!
    base_path = "mod_assets/MPT/seiei/"
    outfits_path = base_path + "body/"
    blink_a = base_path + "eyes/blink/_blink_am.png"
    blink_b = base_path + "eyes/blink/_blink_af.png"

## Blinking Images
image seiei_blink_a:
    Null()
    renpy.random.randint(20, 100)*0.1
    choice:
        blink_a
        0.015
        blink_b
        0.035
        blink_a
        0.015
    choice:
        blink_a
        0.015
        blink_b
        0.065
        blink_a
        0.015
    choice:
        blink_a
        0.015
        blink_b
        0.095
        blink_a
        0.015
    choice:
        blink_a
        0.015
        blink_b
        0.035
        blink_a
        0.015
        alpha 0
        0.15
        alpha 1
        blink_a
        0.015
        blink_b
        0.035
        blink_a
        0.015
    repeat

image seiei_blink_b:
    choice:
        blink_a
        0.015
        blink_b
        0.035
        blink_a
        0.015
    choice:
        blink_a
        0.015
        blink_b
        0.065
        blink_a
        0.015
    choice:
        blink_a
        0.015
        blink_b
        0.095
        blink_a
        0.015
    choice:
        blink_a
        0.015
        blink_b
        0.035
        blink_a
        0.015
        alpha 0
        0.15
        alpha 1
        blink_a
        0.015
        blink_b
        0.035
        blink_a
        0.015
    Null()
    renpy.random.randint(3, 6)
    repeat


layeredimage seiei turned: #turned definitions.
    at AutofocusDisplayable(name="seiei")

    always base_path + "facebase.png" #Always need this face.

    group outfit: #These attributes are here only to determine which set of "body" sprites to use later.  "null" is what lets us just use these attributes as logic and nothing else.
        attribute uniform default null
        attribute casual null


    group mood: #Mood determines what the defaults images are for the following attributes:
        #"oe", "ce", "om", "cm", "brow".
        #By changing what the "mood" attribute is, you can easily switch between premade sets of expressions that work well together, speeding up your workflow.
        #Additionally, you can add in any new ones as you like.
        attribute neut default null #neutral
        attribute angr null #angry
        attribute anno null #annoyed
        attribute cry null  #crying
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
        attribute sad null  #sad
        attribute sedu null #seductive
        attribute shoc null #shocked
        attribute vang null #VERY angry
        attribute vsur null #surprised (very)
        attribute worr null #worried
        attribute yand null #yandere
        attribute scream null #screaming



    group blush: #Have to separate these out, they can't share moods.
        attribute nobl default null #No blush.
        attribute awkw null #awkward.  defaults for n
        attribute blus null #blushing.  defaults for n
        attribute blaw null #blushing and awkward.  defaults for n
        attribute empty null #blushing and awkward.  defaults for n



    group eye_color: #These attributes control which eye color the MC uses between Brown, Gold, and Red.
        attribute eyes_brown default null
        attribute eyes_gold null
        attribute eyes_red null


    #Turned arm variants
    group left:
        attribute ldown default if_any ["uniform"]:
            outfits_path + "uniform_ldown.png"
        attribute ldown default if_any ["casual"]:
            outfits_path + "casual_ldown.png"
        attribute ldown2 if_any ["uniform"]:
            outfits_path + "uniform_ldown2.png"
        attribute ldown2 if_any ["casual"]:
            outfits_path + "casual_ldown2.png"
        attribute lup if_any ["uniform"]:
            outfits_path + "uniform_lup.png"
        attribute lup if_any ["casual"]:
            outfits_path + "casual_lup.png"
    #Crossed arm variants
        attribute cross if_any ["uniform"]:
            outfits_path + "uniform_crossed.png"
        attribute cross if_any ["casual"]:
            outfits_path + "casual_crossed.png"
    
    #Turned arm variants
    group right:
        attribute rdown default if_any ["uniform"]:
            outfits_path + "uniform_rdown.png"
        attribute rdown default if_any ["casual"]:
            outfits_path + "casual_rdown.png"
        attribute rdown2 if_any ["uniform"]:
            outfits_path + "uniform_rdown2.png"
        attribute rdown2 if_any ["casual"]:
            outfits_path + "casual_rdown2.png"
        attribute cross null



    group nose:

        #Default nose/blush.
        attribute nose default if_any ["nobl"]:#default nose
            base_path + "noses/n1.png"
        attribute nose default if_any ["awkw"]:#default nose when "awkward"
            base_path + "noses/n2.png"
        attribute nose default if_any ["blus"]:#default nose when "blushing"
            base_path + "noses/n3.png"
        attribute nose default if_any ["blaw","scream"]:#default nose when "blushing and awkward"
            base_path + "noses/n4.png"
        attribute nose default if_any ["empty"] null#default nose when "blushing and awkward"


        #All noses - truncated tags:
        attribute n1:
            base_path + "noses/n1.png"
        attribute n2:
            base_path + "noses/n2.png"
        attribute n3:
            base_path + "noses/n3.png"
        attribute n4:
            base_path + "noses/n4.png"


    group face_gradient:

        attribute nogr default null
        attribute g_blue:
            base_path + "special/blue_gloom.png"
        attribute g_green:
            base_path + "special/green_gloom.png"
        attribute g_grey:
            base_path + "special/grey_gloom.png"
        attribute g_red:
            base_path + "special/red_gloom.png"


    group mouth:

        #Default Closed Mouths:
        attribute cm default if_any ["happ","sedu","nerv"]:
            base_path + "mouth/ma.png"
        attribute cm default if_any ["neut","anno","worr","curi"]:
            base_path + "mouth/md.png"
        attribute cm default if_any ["dist","flus"]:
            base_path + "mouth/me.png"
        attribute cm default if_any ["lsur","shoc"]:
            base_path + "mouth/mf.png"
        attribute cm default if_any ["sad","angr","pout","doub"]:
            base_path + "mouth/mj.png"
        attribute cm default if_any ["cry","pani","vsur","scream"]:
            base_path + "mouth/mk.png"
        attribute cm default if_any ["vang"]:
            base_path + "mouth/mm.png"
        attribute cm default if_any ["laug"]:
            base_path + "mouth/mn.png"
        attribute cm default if_any ["yand"]:
            base_path + "mouth/mo.png"
        
        #Open Mouths:
        attribute om if_any ["happ","laug"]:
            base_path + "mouth/mb.png"
        attribute om if_any ["yand","nerv"]:
            base_path + "mouth/mc.png"
        attribute om if_any ["pout","sedu"]:
            base_path + "mouth/mf.png"
        attribute om if_any ["sad","lsur","dist"]:
            base_path + "mouth/mg.png"
        attribute om if_any ["neut","anno","shoc","worr"]:
            base_path + "mouth/mh.png"
        attribute om if_any ["curi","doub"]:
            base_path + "mouth/mi.png"
        attribute om if_any ["flus"]:
            base_path + "mouth/mk.png"
        attribute om if_any ["cry","vsur"]:
            base_path + "mouth/ml.png"
        attribute om if_any ["scream"]:
            base_path + "mouth/mp.png"
        attribute om if_any ["angr","pani","vang"]:
            base_path + "mouth/mq.png"


        ###All mouths - truncated tags:
        attribute ma:
            base_path + "mouth/ma.png"
        attribute mb:
            base_path + "mouth/mb.png"
        attribute mc:
            base_path + "mouth/mc.png"
        attribute md:
            base_path + "mouth/md.png"
        attribute me:
            base_path + "mouth/me.png"
        attribute mf:
            base_path + "mouth/mf.png"
        attribute mg:
            base_path + "mouth/mg.png"
        attribute mh:
            base_path + "mouth/mh.png"
        attribute mi:
            base_path + "mouth/mi.png"
        attribute mj:
            base_path + "mouth/mj.png"
        attribute mk:
            base_path + "mouth/mk.png"
        attribute ml:
            base_path + "mouth/ml.png"
        attribute mm:
            base_path + "mouth/mm.png"
        attribute mn:
            base_path + "mouth/mn.png"
        attribute mo:
            base_path + "mouth/mo.png"
        attribute mp:
            base_path + "mouth/mp.png"
        attribute mq:
            base_path + "mouth/mq.png"
        attribute mr:
            base_path + "mouth/mr.png"

    group eyes:

        #Default Opened eyes: - Brown
        attribute oe default if_any ["scream"] if_all ["eyes_brown"]:
            base_path + "eyes/e0b.png"
        attribute oe default if_any ["neut","anno","sedu","doub","sad"] if_all ["eyes_brown"]:
            base_path + "eyes/e1a.png"
        attribute oe default if_any ["dist","worr","pout"] if_all ["eyes_brown"]:
            base_path + "eyes/e1b.png"
        attribute oe default if_any ["angr","happ","laug"] if_all ["eyes_brown"]:
            base_path + "eyes/e1d.png"
        attribute oe default if_any ["cry"] if_all ["eyes_brown"]:
            base_path + "eyes/e1g.png"
        attribute oe default if_any ["lsur","flus","vsur","curi"] if_all ["eyes_brown"]:
            base_path + "eyes/e2a.png"
        attribute oe default if_any ["nerv"] if_all ["eyes_brown"]:
            base_path + "eyes/e2b.png"
        attribute oe default if_any ["pani","vang","shoc"] if_all ["eyes_brown"]:
            base_path + "eyes/e2d.png"
        attribute oe default if_any ["yand"] if_all ["eyes_brown"]:
            base_path + "eyes/e3a.png"
        
        #Default Opened eyes: - Gold
        attribute oe default if_any ["scream"] if_all ["eyes_gold"]:
            base_path + "eyes/e0b_g.png"
        attribute oe default if_any ["neut","anno","sedu","doub"] if_all ["eyes_gold"]:
            base_path + "eyes/e1a_g.png"
        attribute oe default if_any ["dist","worr","pout"] if_all ["eyes_gold"]:
            base_path + "eyes/e1b_g.png"
        attribute oe default if_any ["angr","happ","laug","sad"] if_all ["eyes_gold"]:
            base_path + "eyes/e1d_g.png"
        attribute oe default if_any ["cry"] if_all ["eyes_gold"]:
            base_path + "eyes/e1g_g.png"
        attribute oe default if_any ["lsur","flus","vsur","curi"] if_all ["eyes_gold"]:
            base_path + "eyes/e2a_g.png"
        attribute oe default if_any ["nerv"] if_all ["eyes_gold"]:
            base_path + "eyes/e2b_g.png"
        attribute oe default if_any ["pani","vang","shoc"] if_all ["eyes_gold"]:
            base_path + "eyes/e2d_g.png"
        attribute oe default if_any ["yand"] if_all ["eyes_gold"]:
            base_path + "eyes/e3a_g.png"
        
        #Default Opened eyes: - Red
        attribute oe default if_any ["scream"] if_all ["eyes_red"]:
            base_path + "eyes/e0b_r.png"
        attribute oe default if_any ["neut","anno","sedu","doub"] if_all ["eyes_red"]:
            base_path + "eyes/e1a_r.png"
        attribute oe default if_any ["dist","worr","pout"] if_all ["eyes_red"]:
            base_path + "eyes/e1b_r.png"
        attribute oe default if_any ["angr","happ","laug","sad"] if_all ["eyes_red"]:
            base_path + "eyes/e1d_r.png"
        attribute oe default if_any ["cry"] if_all ["eyes_red"]:
            base_path + "eyes/e1g_r.png"
        attribute oe default if_any ["lsur","flus","vsur","curi"] if_all ["eyes_red"]:
            base_path + "eyes/e2a_r.png"
        attribute oe default if_any ["nerv"] if_all ["eyes_red"]:
            base_path + "eyes/e2b_r.png"
        attribute oe default if_any ["pani","vang","shoc"] if_all ["eyes_red"]:
            base_path + "eyes/e2d_r.png"
        attribute oe default if_any ["yand"] if_all ["eyes_red"]:
            base_path + "eyes/e3a_r.png"
        
        #Default Closed eyes:
        attribute ce if_any ["sad","anno","angr","dist","shoc","worr","nerv","curi","doub"]:
            base_path + "eyes/e4a.png"
        attribute ce if_any ["neut","happ","lsur","laug","vsur","yand","pout","sedu"]:
            base_path + "eyes/e4b.png"
        attribute ce if_any ["vang","flus","pani","scream"]:
            base_path + "eyes/e4c.png"
        attribute ce if_any ["cry"]:
            base_path + "eyes/e4d.png"


        ###All eyes w/ Brown-Gold-Red variants - truncated tags:
        # Brown Eyes - Default
        attribute e0a if_all ["eyes_brown"]:
            base_path + "eyes/e0a.png"
        attribute e0b if_all ["eyes_brown"]:
            base_path + "eyes/e0b.png"
        attribute e1a if_all ["eyes_brown"]:
            base_path + "eyes/e1a.png"
        attribute e1b if_all ["eyes_brown"]:
            base_path + "eyes/e1b.png"
        attribute e1c if_all ["eyes_brown"]:
            base_path + "eyes/e1c.png"
        attribute e1d if_all ["eyes_brown"]:
            base_path + "eyes/e1d.png"
        attribute e1e if_all ["eyes_brown"]:
            base_path + "eyes/e1e.png"
        attribute e1f if_all ["eyes_brown"]:
            base_path + "eyes/e1f.png"
        attribute e1g if_all ["eyes_brown"]:
            base_path + "eyes/e1g.png"
        attribute e1h if_all ["eyes_brown"]:
            base_path + "eyes/e1h.png"
        attribute e2a if_all ["eyes_brown"]:
            base_path + "eyes/e2a.png"
        attribute e2b if_all ["eyes_brown"]:
            base_path + "eyes/e2b.png"
        attribute e2c if_all ["eyes_brown"]:
            base_path + "eyes/e2c.png"
        attribute e2d if_all ["eyes_brown"]:
            base_path + "eyes/e2d.png"
        attribute e2e if_all ["eyes_brown"]:
            base_path + "eyes/e2e.png"
        attribute e3a if_all ["eyes_brown"]:
            base_path + "eyes/e3a.png"
        attribute e3b if_all ["eyes_brown"]:
            base_path + "eyes/e3b.png"
        attribute e3c if_all ["eyes_brown"]:
            base_path + "eyes/e3c.png"
        attribute e4a:
            base_path + "eyes/e4a.png"
        attribute e4b:
            base_path + "eyes/e4b.png"
        attribute e4c:
            base_path + "eyes/e4c.png"
        attribute e4d:
            base_path + "eyes/e4d.png"
        attribute e4e:
            base_path + "eyes/e4e.png"
        attribute e0c:
            base_path + "eyes/e0c.png"

        # Gold Eyes
        attribute e0a if_all ["eyes_gold"]:
            base_path + "eyes/e0a_g.png"
        attribute e0b if_all ["eyes_gold"]:
            base_path + "eyes/e0b_g.png"
        attribute e1a if_all ["eyes_gold"]:
            base_path + "eyes/e1a_g.png"
        attribute e1b if_all ["eyes_gold"]:
            base_path + "eyes/e1b_g.png"
        attribute e1c if_all ["eyes_gold"]:
            base_path + "eyes/e1c_g.png"
        attribute e1d if_all ["eyes_gold"]:
            base_path + "eyes/e1d_g.png"
        attribute e1e if_all ["eyes_gold"]:
            base_path + "eyes/e1e_g.png"
        attribute e1f if_all ["eyes_gold"]:
            base_path + "eyes/e1f_g.png"
        attribute e1g if_all ["eyes_gold"]:
            base_path + "eyes/e1g_g.png"
        attribute e1h if_all ["eyes_gold"]:
            base_path + "eyes/e1h_g.png"
        attribute e2a if_all ["eyes_gold"]:
            base_path + "eyes/e2a_g.png"
        attribute e2b if_all ["eyes_gold"]:
            base_path + "eyes/e2b_g.png"
        attribute e2c if_all ["eyes_gold"]:
            base_path + "eyes/e2c_g.png"
        attribute e2d if_all ["eyes_gold"]:
            base_path + "eyes/e2d_g.png"
        attribute e2e if_all ["eyes_gold"]:
            base_path + "eyes/e2e_g.png"
        attribute e3a if_all ["eyes_gold"]:
            base_path + "eyes/e3a_g.png"
        attribute e3b if_all ["eyes_gold"]:
            base_path + "eyes/e3b_g.png"
        attribute e3c if_all ["eyes_gold"]:
            base_path + "eyes/e3c_g.png"

        # Red Eyes
        attribute e0a if_all ["eyes_red"]:
            base_path + "eyes/e0a_r.png"
        attribute e0b if_all ["eyes_red"]:
            base_path + "eyes/e0b_r.png"
        attribute e1a if_all ["eyes_red"]:
            base_path + "eyes/e1a_r.png"
        attribute e1b if_all ["eyes_red"]:
            base_path + "eyes/e1b_r.png"
        attribute e1c if_all ["eyes_red"]:
            base_path + "eyes/e1c_r.png"
        attribute e1d if_all ["eyes_red"]:
            base_path + "eyes/e1d_r.png"
        attribute e1e if_all ["eyes_red"]:
            base_path + "eyes/e1e_r.png"
        attribute e1f if_all ["eyes_red"]:
            base_path + "eyes/e1f_r.png"
        attribute e1g if_all ["eyes_red"]:
            base_path + "eyes/e1g_r.png"
        attribute e1h if_all ["eyes_red"]:
            base_path + "eyes/e1h_r.png"
        attribute e2a if_all ["eyes_red"]:
            base_path + "eyes/e2a_r.png"
        attribute e2b if_all ["eyes_red"]:
            base_path + "eyes/e2b_r.png"
        attribute e2c if_all ["eyes_red"]:
            base_path + "eyes/e2c_r.png"
        attribute e2d if_all ["eyes_red"]:
            base_path + "eyes/e2d_r.png"
        attribute e2e if_all ["eyes_red"]:
            base_path + "eyes/e2e_r.png"
        attribute e3a if_all ["eyes_red"]:
            base_path + "eyes/e3a_r.png"
        attribute e3b if_all ["eyes_red"]:
            base_path + "eyes/e3b_r.png"
        attribute e3c if_all ["eyes_red"]:
            base_path + "eyes/e3c_r.png"

    #Blinking group. You can disable the blinking using the 'no_blink' attribute in your 'show' statement.
    group blink:

        attribute noblink default null
        # Blink at random intervals
        attribute blink_a if_not ["ce","e4a","e4b","e4c", "e4d", "e4f", "e4e", "e1e", "e1f", "g_blue", "g_green", "g_grey", "g_red"]:
            "mc_blink_a"
        # Blink immediately after use, then random intervals
        attribute blink_b if_not ["ce","e4a","e4b","e4c", "e4d", "e4f", "e4e", "e1e", "e1f", "g_blue", "g_green", "g_grey", "g_red"]:
            "mc_blink_b"

    group eyebrows:

        #Default Eyebrows:
        attribute brow default if_any ["neut","happ","lsur","flus","shoc","dist"]:
            base_path + "eyebrows/b1a.png"
        attribute brow default if_any ["sad","cry","worr"]:
            base_path + "eyebrows/b1b.png"
        attribute brow default if_any ["pani","yand","nerv","scream"]:
            base_path + "eyebrows/b1b_h.png"
        attribute brow default if_any ["laug","vsur","sedu"]:
            base_path + "eyebrows/b1c.png"
        attribute brow default if_any ["anno","pout"]:
            base_path + "eyebrows/b1d.png"
        attribute brow default if_any ["angr","vang"]:
            base_path + "eyebrows/b1e.png"
        attribute brow default if_any ["curi","doub"]:
            base_path + "eyebrows/b1f.png"


        ###All eyebrows - truncated tags:
        attribute b1a:
            base_path + "eyebrows/b1a.png"
        attribute b1b:
            base_path + "eyebrows/b1b.png"
        attribute b1b_h:
            base_path + "eyebrows/b1b_h.png"
        attribute b1c:
            base_path + "eyebrows/b1c.png"
        attribute b1d:
            base_path + "eyebrows/b1d.png"
        attribute b1e:
            base_path + "eyebrows/b1e.png"
        attribute b1f:
            base_path + "eyebrows/b1f.png"
    
    group extra multiple:
        
        attribute sweat:
            base_path + "noses/sweat.png"
        attribute sweatdrop:
            base_path + "noses/sweatdrop.png"
        attribute sobbing:
            base_path + "eyes/sobbing.png"
        attribute tears:
            base_path + "eyes/tears.png"