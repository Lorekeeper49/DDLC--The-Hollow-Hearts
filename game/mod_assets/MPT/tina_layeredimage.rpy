


init python:
    #Layered image refreshes
    def tref(target="master"):
        if not "tina" in renpy.get_showing_tags(layer=target, sort=True):
            #If not currently showing this sprite, stop function.
            return
        pose = str(renpy.get_attributes("tina",layer=target)[0])
        if pose == "":
            #Nope out if there's no actual pose here.
            return
        renpy.show("tina " + pose + " refreshattribute",layer=target)
        renpy.show("tina",layer=target)


# With "$ tref()", you can refresh all attibutes to default.


layeredimage tina turned: #turned definitions.
    
    always "mod_assets/MPT/tina/tina_turned_facebase.png" #Always need this face.
    
    group outfit: #These attributes are here only to determine which set of "body" sprites to use later.  "null" is what lets us just use these attributes as logic and nothing else.
        attribute uniform null
        attribute suit default null
    

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
        #attribute xxxx null #xxxx #Do you want to define a new mood?  Here, have a template!
    

    group blush: #Have to separate these out, they can't share moods.
        attribute nobl null #No blush.
        attribute awkw null #awkward.  defaults for n
        attribute blus null #blushing.  defaults for n
        attribute blaw null #blushing and awkward.  defaults for n
    

    group crossed: #Controls whether arms are crossed. Used to hide left and right sides when they are.
        attribute uncross default null #Not crossed.
        attribute cross null #Crossed.
        

    group cigarette: #Controls whenever Tina has a cigarette in her mouth. 
        attribute nocig default null #Doesn't have a cigarette.
        attribute cig null #Does have a cigarette, but isn't lighted up.
        attribute ciglight null #Does have a lighted up cigarette.
        attribute pcig null #Has an unlit cigarette in her hand.
        attribute pciglight null #Has an lit cigarette in her hand.


    group mark: #Controls, whenever Tina has the "angry mark"
        attribute nomark default null
        attribute mark null


    #Left arm variants - Uniform outfit
    group left if_any(["uniform"]) if_not(["cross"]):
        attribute ldown default:
            "mod_assets/MPT/tina/tina_turned_uniform_left_down.png"
        attribute lpistol:
            "mod_assets/MPT/tina/tina_turned_uniform_left_pistol.png"
        attribute lhip:
            "mod_assets/MPT/tina/tina_turned_uniform_left_hip.png"
    #Suit outfit
    group left if_any(["suit"]) if_not(["cross"]):
        attribute ldown default:
            "mod_assets/MPT/tina/tina_turned_suit_left_down.png"
        attribute lpistol:
            "mod_assets/MPT/tina/tina_turned_suit_left_pistol.png"
        attribute lhip:
            "mod_assets/MPT/tina/tina_turned_suit_left_hip.png"
    
    

    #Right arm variants - Uniform outfit
    group right if_any(["uniform"]) if_not(["cross","pcig","pciglight"]):
        attribute rdown default:
            "mod_assets/MPT/tina/tina_turned_uniform_right_down.png"
        attribute rside:
            "mod_assets/MPT/tina/tina_turned_uniform_right_side.png"
        attribute rhip:
            "mod_assets/MPT/tina/tina_turned_uniform_right_hip.png"
        attribute rup:
            "mod_assets/MPT/tina/tina_turned_uniform_right_up.png"
        attribute rmiddle:
            "mod_assets/MPT/tina/tina_turned_uniform_right_middle.png"
    #Suit outfit
    group right if_any(["suit"]) if_not(["cross","pcig","pciglight"]):
        attribute rdown default:
            "mod_assets/MPT/tina/tina_turned_suit_right_down.png"
        attribute rside:
            "mod_assets/MPT/tina/tina_turned_suit_right_side.png"
        attribute rhip:
            "mod_assets/MPT/tina/tina_turned_suit_right_hip.png"
        attribute rup:
            "mod_assets/MPT/tina/tina_turned_suit_right_up.png"
        attribute rmiddle:
            "mod_assets/MPT/tina/tina_turned_suit_right_middle.png"
    

    #Uniform - pcig
    group right if_any(["uniform"]) if_all(["pcig"]) if_not(["cross","pciglight"]):
        attribute rdown default:
            "mod_assets/MPT/tina/tina_turned_uniform_right_down.png"
        attribute rup:
            "mod_assets/MPT/tina/tina_turned_uniform_right_up_cig.png"
        attribute rside:
            "mod_assets/MPT/tina/tina_turned_uniform_right_side_cig.png"
        attribute rhip:
            "mod_assets/MPT/tina/tina_turned_uniform_right_hip.png"
        attribute rmiddle:
            "mod_assets/MPT/tina/tina_turned_uniform_right_middle.png"
    #Suit - pcig
    #group right if_any(["suit"]) if_all(["pcig"]) if_not(["cross","pciglight"]):
        attribute rdown default:
            "mod_assets/MPT/tina/tina_turned_suit_right_down.png"
        attribute rup:
            "mod_assets/MPT/tina/tina_turned_suit_right_up_cig.png"
        attribute rside:
            "mod_assets/MPT/tina/tina_turned_suit_right_side_cig.png"
        attribute rhip:
            "mod_assets/MPT/tina/tina_turned_suit_right_hip.png"
        attribute rmiddle:
            "mod_assets/MPT/tina/tina_turned_suit_right_middle.png"
    

    #Uniform - pciglight
    group right if_any(["uniform"]) if_all(["pciglight"]) if_not(["cross","pcig"]):
        attribute rdown default:
            "mod_assets/MPT/tina/tina_turned_uniform_right_down.png"
        attribute rup:
            "mod_assets/MPT/tina/tina_turned_uniform_right_up_ciglight.png"
        attribute rside:
            "mod_assets/MPT/tina/tina_turned_uniform_right_side_ciglight.png"
        attribute rhip:
            "mod_assets/MPT/tina/tina_turned_uniform_right_hip.png"
        attribute rmiddle:
            "mod_assets/MPT/tina/tina_turned_uniform_right_middle.png"
    #Suit - pciglight
    #group right if_any(["suit"]) if_all(["pciglight"]) if_not(["cross","pcig"]):
        attribute rdown default:
            "mod_assets/MPT/tina/tina_turned_suit_right_down.png"
        attribute rup:
            "mod_assets/MPT/tina/tina_turned_suit_right_up_ciglight.png"
        attribute rside:
            "mod_assets/MPT/tina/tina_turned_suit_right_side_ciglight.png"
        attribute rhip:
            "mod_assets/MPT/tina/tina_turned_suit_right_hip.png"
        attribute rmiddle:
            "mod_assets/MPT/tina/tina_turned_suit_right_middle.png"

    

    #Crossed arm variants
    group center if_any(["uniform"]) if_all(["cross"]):
        attribute crossnocig default:
            "mod_assets/MPT/tina/tina_crossed_uniform.png"
        attribute crosscig:
            "mod_assets/MPT/tina/tina_crossed_uniform_cig.png"
        attribute crossciglight:
            "mod_assets/MPT/tina/tina_crossed_uniform_ciglight.png"
        attribute crossmiddle:
            "mod_assets/MPT/tina/tina_crossed_uniform_middle.png"

    group center if_any(["suit"]) if_all(["cross"]):
        attribute crossnocig default:
            "mod_assets/MPT/tina/tina_crossed_suit.png"
        attribute crosscig:
            "mod_assets/MPT/tina/tina_crossed_suit_cig.png"
        attribute crossciglight:
            "mod_assets/MPT/tina/tina_crossed_suit_ciglight.png"
        attribute crossmiddle:
            "mod_assets/MPT/tina/tina_crossed_suit_middle.png"


    group nose:
        
        #Default nose/blush.
        attribute nose default if_any(["nobl"]):#default nose
            "mod_assets/MPT/tina/tina_turned_nose_n1.png"
        attribute nose default if_any(["awkw"]):#default nose when "awkward"
            "mod_assets/MPT/tina/tina_turned_nose_n2.png"
        attribute nose default if_any(["blus"]):#default nose when "blushing"
            "mod_assets/MPT/tina/tina_turned_nose_n3.png"
        attribute nose default if_any(["blaw"]):#default nose when "blushing and awkward"
            "mod_assets/MPT/tina/tina_turned_nose_n4.png"
        
        
        #All noses - truncated tags:
        attribute n1:
            "mod_assets/MPT/tina/tina_turned_nose_n1.png"
        attribute n2:
            "mod_assets/MPT/tina/tina_turned_nose_n2.png"
        attribute n3:
            "mod_assets/MPT/tina/tina_turned_nose_n3.png"
        attribute n4:
            "mod_assets/MPT/tina/tina_turned_nose_n4.png"
    
    
    
    group mouth:
        
        #Default Closed Mouths:
        attribute cm default if_any(["happ","nerv",]) if_not (["cig","ciglight"]):
            "mod_assets/MPT/tina/tina_turned_mouth_ma.png"
        attribute cm default if_any(["happ","nerv",]) if_not (["ciglight"]) if_all (["cig"]):
            "mod_assets/MPT/tina/tina_turned_mouth_ma_cig.png"
        attribute cm default if_any(["happ","nerv",]) if_not (["cig"]) if_all (["ciglight"]):
            "mod_assets/MPT/tina/tina_turned_mouth_ma_ciglight.png"
        attribute cm default if_any(["sedu"]) if_not (["cig","ciglight"]):
            "mod_assets/MPT/tina/tina_turned_mouth_mb.png"
        attribute cm default if_any(["sedu"]) if_not (["ciglight"]) if_all (["cmig"]):
            "mod_assets/MPT/tina/tina_turned_mouth_mb_cig.png"
        attribute cm default if_any(["sedu"]) if_not (["cig"]) if_all (["ciglight"]):
            "mod_assets/MPT/tina/tina_turned_mouth_mb_ciglight.png"
        attribute cm default if_any(["neut","anno","curi"]) if_not (["cig","ciglight"]):
            "mod_assets/MPT/tina/tina_turned_mouth_me.png"
        attribute cm default if_any(["neut","anno","curi"]) if_not (["ciglight"]) if_all (["cig"]):
            "mod_assets/MPT/tina/tina_turned_mouth_me_cig.png"
        attribute cm default if_any(["neut","anno","curi"]) if_not (["cig"]) if_all (["ciglight"]):
            "mod_assets/MPT/tina/tina_turned_mouth_me_ciglight.png"
        attribute cm default if_any(["dist","flus","worr"]) if_not (["cig","ciglight"]):
            "mod_assets/MPT/tina/tina_turned_mouth_mf.png"
        attribute cm default if_any(["dist","flus","worr"]) if_not (["ciglight"]) if_all (["cig"]):
            "mod_assets/MPT/tina/tina_turned_mouth_mf_cig.png"
        attribute cm default if_any(["dist","flus","worr"]) if_not (["cig"]) if_all (["ciglight"]):
            "mod_assets/MPT/tina/tina_turned_mouth_mf_ciglight.png"
        attribute cm default if_any(["vsur","shoc"]) if_not (["cig","ciglight"]):
            "mod_assets/MPT/tina/tina_turned_mouth_mi.png"
        attribute cm default if_any(["vsur","shoc"]) if_not (["ciglight"]) if_all (["cig"]):
            "mod_assets/MPT/tina/tina_turned_mouth_mi_cig.png"
        attribute cm default if_any(["vsur","shoc"]) if_not (["cig"]) if_all (["ciglight"]):
            "mod_assets/MPT/tina/tina_turned_mouth_mi_ciglight.png"
        attribute cm default if_any(["lsur","sad"]):
            "mod_assets/MPT/tina/tina_turned_mouth_mh.png"
        attribute cm default if_any(["angr","pout","doub"]) if_not (["cig","ciglight"]):
            "mod_assets/MPT/tina/tina_turned_mouth_mg.png"
        attribute cm default if_any(["angr","pout","doub"]) if_not (["ciglight"]) if_all (["cig"]):
            "mod_assets/MPT/tina/tina_turned_mouth_mg_cig.png"
        attribute cm default if_any(["angr","pout","doub"]) if_not (["cig"]) if_all (["ciglight"]):
            "mod_assets/MPT/tina/tina_turned_mouth_mg_ciglight.png"
        attribute cm default if_any(["cry","pani"]) if_not (["cig","ciglight"]):
            "mod_assets/MPT/tina/tina_turned_mouth_mn.png"
        attribute cm default if_any(["cry","pani"]) if_not (["ciglight"]) if_all (["cig"]):
            "mod_assets/MPT/tina/tina_turned_mouth_mn_cig.png"
        attribute cm default if_any(["cry","pani"]) if_not (["cig"]) if_all (["ciglight"]):
            "mod_assets/MPT/tina/tina_turned_mouth_mn_ciglight.png"
        attribute cm default if_any(["vang"]):
            "mod_assets/MPT/tina/tina_turned_mouth_ml.png"
        attribute cm default if_any(["laug"]) if_not (["cig","ciglight"]):
            "mod_assets/MPT/tina/tina_turned_mouth_mp.png"
        attribute cm default if_any(["laug"]) if_not (["ciglight"]) if_all (["cig"]):
            "mod_assets/MPT/tina/tina_turned_mouth_mp_cig.png"
        attribute cm default if_any(["laug"]) if_not (["cig"]) if_all (["ciglight"]):
            "mod_assets/MPT/tina/tina_turned_mouth_mp_ciglight.png"
        attribute cm default if_any(["yand"]):
            "mod_assets/MPT/tina/tina_turned_mouth_mq.png"
        
        #Open Mouths:
        attribute om if_any(["happ","laug"]) if_not (["cig","ciglight"]):
            "mod_assets/MPT/tina/tina_turned_mouth_md.png"
        attribute om if_any(["happ","laug"]) if_not (["ciglight"]) if_all (["cig"]):
            "mod_assets/MPT/tina/tina_turned_mouth_md_cig.png"
        attribute om if_any(["happ","laug"]) if_not (["cig"]) if_all (["ciglight"]):
            "mod_assets/MPT/tina/tina_turned_mouth_md_ciglight.png"
        attribute om if_any(["nerv","sedu"]) if_not (["cig","ciglight"]):
            "mod_assets/MPT/tina/tina_turned_mouth_mc.png"
        attribute om if_any(["nerv","sedu"]) if_not (["ciglight"]) if_all (["cig"]):
            "mod_assets/MPT/tina/tina_turned_mouth_mc_cig.png"
        attribute om if_any(["nerv","sedu"]) if_not (["cig"]) if_all (["ciglight"]):
            "mod_assets/MPT/tina/tina_turned_mouth_mc_ciglight.png"
        attribute om if_any(["sad","lsur","dist","yand"]):
            "mod_assets/MPT/tina/tina_turned_mouth_mj.png"
        attribute om if_any(["neut","anno","shoc","worr","doub","curi","pout"]) if_not (["cig","ciglight"]):
            "mod_assets/MPT/tina/tina_turned_mouth_mk.png"
        attribute om if_any(["neut","anno","shoc","worr","doub","curi","pout"]) if_not (["ciglight"]) if_all (["cig"]):
            "mod_assets/MPT/tina/tina_turned_mouth_mk_cig.png"
        attribute om if_any(["neut","anno","shoc","worr","doub","curi","pout"]) if_not (["cig"]) if_all (["ciglight"]):
            "mod_assets/MPT/tina/tina_turned_mouth_mk_ciglight.png"
        attribute om if_any(["cry","vsur","pani","flus","angr"]):
            "mod_assets/MPT/tina/tina_turned_mouth_mo.png"
        attribute om if_any(["vang"]):
            "mod_assets/MPT/tina/tina_turned_mouth_mm.png"
        
        
        ###All mouths - truncated tags
        ### Without cigarette
        attribute ma if_not (["cig","ciglight"]):
            "mod_assets/MPT/tina/tina_turned_mouth_ma.png"
        attribute mb if_not (["cig","ciglight"]):
            "mod_assets/MPT/tina/tina_turned_mouth_mb.png"
        attribute mc if_not (["cig","ciglight"]):
            "mod_assets/MPT/tina/tina_turned_mouth_mc.png"
        attribute md if_not (["cig","ciglight"]):
            "mod_assets/MPT/tina/tina_turned_mouth_md.png"
        attribute me if_not (["cig","ciglight"]):
            "mod_assets/MPT/tina/tina_turned_mouth_me.png"
        attribute mf if_not (["cig","ciglight"]):
            "mod_assets/MPT/tina/tina_turned_mouth_mf.png"
        attribute mg if_not (["cig","ciglight"]):
            "mod_assets/MPT/tina/tina_turned_mouth_mg.png"
        attribute mh:
            "mod_assets/MPT/tina/tina_turned_mouth_mh.png"
        attribute mi if_not (["cig","ciglight"]):
            "mod_assets/MPT/tina/tina_turned_mouth_mi.png"
        attribute mj:
            "mod_assets/MPT/tina/tina_turned_mouth_mj.png"
        attribute mk if_not (["cig","ciglight"]):
            "mod_assets/MPT/tina/tina_turned_mouth_mk.png"
        attribute ml:
            "mod_assets/MPT/tina/tina_turned_mouth_ml.png"
        attribute mm:
            "mod_assets/MPT/tina/tina_turned_mouth_mm.png"
        attribute mn if_not (["cig","ciglight"]):
            "mod_assets/MPT/tina/tina_turned_mouth_mn.png"
        attribute mo:
            "mod_assets/MPT/tina/tina_turned_mouth_mo.png"
        attribute mp if_not (["cig","ciglight"]):
            "mod_assets/MPT/tina/tina_turned_mouth_mp.png"
        attribute mq:
            "mod_assets/MPT/tina/tina_turned_mouth_mq.png"
        attribute mr:
            "mod_assets/MPT/tina/tina_turned_mouth_mr.png"
        attribute ms:
            "mod_assets/MPT/tina/tina_turned_mouth_ms.png"
        attribute ms2:
            "mod_assets/MPT/tina/tina_turned_mouth_ms2.png"

        #With a non-lit cigarette
        attribute ma if_not (["ciglight"]) if_all (["cig"]):
            "mod_assets/MPT/tina/tina_turned_mouth_ma_cig.png"
        attribute mb if_not (["ciglight"]) if_all (["cig"]):
            "mod_assets/MPT/tina/tina_turned_mouth_mb_cig.png"
        attribute mc if_not (["ciglight"]) if_all (["cig"]):
            "mod_assets/MPT/tina/tina_turned_mouth_mc_cig.png"
        attribute md if_not (["ciglight"]) if_all (["cig"]):
            "mod_assets/MPT/tina/tina_turned_mouth_md_cig.png"
        attribute me if_not (["ciglight"]) if_all (["cig"]):
            "mod_assets/MPT/tina/tina_turned_mouth_me_cig.png"
        attribute mf if_not (["ciglight"]) if_all (["cig"]):
            "mod_assets/MPT/tina/tina_turned_mouth_mf_cig.png"
        attribute mg if_not (["ciglight"]) if_all (["cig"]):
            "mod_assets/MPT/tina/tina_turned_mouth_mg_cig.png"
        attribute mi if_not (["ciglight"]) if_all (["cig"]):
            "mod_assets/MPT/tina/tina_turned_mouth_mi_cig.png"
        attribute mk if_not (["ciglight"]) if_all (["cig"]):
            "mod_assets/MPT/tina/tina_turned_mouth_mk_cig.png"
        attribute mn if_not (["ciglight"]) if_all (["cig"]):
            "mod_assets/MPT/tina/tina_turned_mouth_mn_cig.png"
        attribute mp if_not (["ciglight"]) if_all (["cig"]):
            "mod_assets/MPT/tina/tina_turned_mouth_mp_cig.png"
    
        #With a lit cigarette
        attribute ma if_not (["cig"]) if_all (["ciglight"]):
            "mod_assets/MPT/tina/tina_turned_mouth_ma_ciglight.png"
        attribute mb if_not (["cig"]) if_all (["ciglight"]):
            "mod_assets/MPT/tina/tina_turned_mouth_mb_ciglight.png"
        attribute mc if_not (["cig"]) if_all (["ciglight"]):
            "mod_assets/MPT/tina/tina_turned_mouth_mc_ciglight.png"
        attribute md if_not (["cig"]) if_all (["ciglight"]):
            "mod_assets/MPT/tina/tina_turned_mouth_md_ciglight.png"
        attribute me if_not (["cig"]) if_all (["ciglight"]):
            "mod_assets/MPT/tina/tina_turned_mouth_me_ciglight.png"
        attribute mf if_not (["cig"]) if_all (["ciglight"]):
            "mod_assets/MPT/tina/tina_turned_mouth_mf_ciglight.png"
        attribute mg if_not (["cig"]) if_all (["ciglight"]):
            "mod_assets/MPT/tina/tina_turned_mouth_mg_ciglight.png"
        attribute mi if_not (["cig"]) if_all (["ciglight"]):
            "mod_assets/MPT/tina/tina_turned_mouth_mi_ciglight.png"
        attribute mk if_not (["cig"]) if_all (["ciglight"]):
            "mod_assets/MPT/tina/tina_turned_mouth_mk_ciglight.png"
        attribute mn if_not (["cig"]) if_all (["ciglight"]):
            "mod_assets/MPT/tina/tina_turned_mouth_mn_ciglight.png"
        attribute mp if_not (["cig"]) if_all (["ciglight"]):
            "mod_assets/MPT/tina/tina_turned_mouth_mp_ciglight.png"
    
    group eyes:
        
        #Default Opened eyes:
        attribute oe default if_any(["neut","happ","laug","sad"]):
            "mod_assets/MPT/tina/tina_turned_eyes_e1a.png"
        attribute oe default if_any(["dist","worr","pout","nerv"]):
            "mod_assets/MPT/tina/tina_turned_eyes_e1b.png"
        attribute oe default if_any(["anno","sedu","doub","angr"]):
            "mod_assets/MPT/tina/tina_turned_eyes_e1c.png"
        attribute oe default if_any(["cry"]):
            "mod_assets/MPT/tina/tina_turned_eyes_e1g.png"
        attribute oe default if_any(["lsur","flus","curi","nerv"]):
            "mod_assets/MPT/tina/tina_turned_eyes_e2a.png"
        attribute oe default if_any(["pani","vang","shoc","vsur"]):
            "mod_assets/MPT/tina/tina_turned_eyes_e2b.png"
        attribute oe default if_any(["yand"]):
            "mod_assets/MPT/tina/tina_turned_eyes_e3a.png"
        
        #Default Closed eyes:
        attribute ce if_any(["sad","anno","angr","vang","vsur","dist","shoc","worr","nerv","curi","doub","neut"]):
            "mod_assets/MPT/tina/tina_turned_eyes_e4b.png"
        attribute ce if_any(["happ","laug","lsur","yand","pout","sedu"]):
            "mod_assets/MPT/tina/tina_turned_eyes_e4a.png"
        attribute ce if_any(["flus","pani"]):
            "mod_assets/MPT/tina/tina_turned_eyes_e4c.png"
        attribute ce if_any(["cry"]):
            "mod_assets/MPT/tina/tina_turned_eyes_e4d.png"
        
        
        ###All eyes - truncated tags:
        attribute e1a:
            "mod_assets/MPT/tina/tina_turned_eyes_e1a.png"
        attribute e1b:
            "mod_assets/MPT/tina/tina_turned_eyes_e1b.png"
        attribute e1c:
            "mod_assets/MPT/tina/tina_turned_eyes_e1c.png"
        attribute e1d:
            "mod_assets/MPT/tina/tina_turned_eyes_e1d.png"
        attribute e1e:
            "mod_assets/MPT/tina/tina_turned_eyes_e1e.png"
        attribute e1f:
            "mod_assets/MPT/tina/tina_turned_eyes_e1f.png"
        attribute e1g:
            "mod_assets/MPT/tina/tina_turned_eyes_e1g.png"
        attribute e1h:
            "mod_assets/MPT/tina/tina_turned_eyes_e1h.png"
        attribute e2a:
            "mod_assets/MPT/tina/tina_turned_eyes_e2a.png"
        attribute e2b:
            "mod_assets/MPT/tina/tina_turned_eyes_e2b.png"
        attribute e2c:
            "mod_assets/MPT/tina/tina_turned_eyes_e2c.png"
        attribute e2d:
            "mod_assets/MPT/tina/tina_turned_eyes_e2d.png"
        attribute e3a:
            "mod_assets/MPT/tina/tina_turned_eyes_e3a.png"
        attribute e3b:
            "mod_assets/MPT/tina/tina_turned_eyes_e3b.png"
        attribute e4a:
            "mod_assets/MPT/tina/tina_turned_eyes_e4a.png"
        attribute e4b:
            "mod_assets/MPT/tina/tina_turned_eyes_e4b.png"
        attribute e4c:
            "mod_assets/MPT/tina/tina_turned_eyes_e4c.png"
        attribute e4d:
            "mod_assets/MPT/tina/tina_turned_eyes_e4d.png"
        attribute e0a:
            "mod_assets/MPT/tina/tina_turned_eyes_e0a.png"
        attribute e0b:
            "mod_assets/MPT/tina/tina_turned_eyes_e0b.png"
        attribute e0c:
            "mod_assets/MPT/tina/tina_turned_eyes_e0c.png"
    
    
    
    
    
    group eyebrows:
        
        #Default Eyebrows:
        attribute brow default if_any(["neut","happ","dist"]):
            "mod_assets/MPT/tina/tina_turned_eyebrows_b1.png"
        attribute brow default if_any(["sad","cry","yand","nerv"]):
            "mod_assets/MPT/tina/tina_turned_eyebrows_b4.png"
        attribute brow default if_any(["laug","vsur","worr","lsur","pani","shoc","flus"]):
            "mod_assets/MPT/tina/tina_turned_eyebrows_b2.png"
        attribute brow default if_any(["anno","pout"]) if_all (["nomark"]) if_not (["mark"]):
            "mod_assets/MPT/tina/tina_turned_eyebrows_b5.png"
        attribute brow default if_any(["anno","pout"]) if_all (["mark"]) if_not (["nomark"]):
            "mod_assets/MPT/tina/tina_turned_eyebrows_b5m.png"
        attribute brow default if_any(["angr","vang"]) if_all (["nomark"]) if_not (["mark"]):
            "mod_assets/MPT/tina/tina_turned_eyebrows_b6.png"
        attribute brow default if_any(["angr","vang"]) if_all (["mark"]) if_not (["nomark"]):
            "mod_assets/MPT/tina/tina_turned_eyebrows_b6m.png"
        attribute brow default if_any(["curi","doub","sedu"]):
            "mod_assets/MPT/tina/tina_turned_eyebrows_b3.png"
        
        
        ###All eyebrows - truncated tags:
        attribute b1:
            "mod_assets/MPT/tina/tina_turned_eyebrows_b1.png"
        attribute b2:
            "mod_assets/MPT/tina/tina_turned_eyebrows_b2.png"
        attribute b3:
            "mod_assets/MPT/tina/tina_turned_eyebrows_b3.png"
        attribute b4:
            "mod_assets/MPT/tina/tina_turned_eyebrows_b4.png"
        attribute b5 if_all (["nomark"]) if_not (["mark"]):
            "mod_assets/MPT/tina/tina_turned_eyebrows_b5.png"
        attribute b5 if_all (["mark"]) if_not (["nomark"]):
            "mod_assets/MPT/tina/tina_turned_eyebrows_b5m.png"
        attribute b6 if_all (["nomark"]) if_not (["mark"]):
            "mod_assets/MPT/tina/tina_turned_eyebrows_b6.png"
        attribute b6 if_all (["mark"]) if_not (["nomark"]):
            "mod_assets/MPT/tina/tina_turned_eyebrows_b6m.png"





    #This group is intentionally last on this list, so it will render over top of every other thing on the face.
    group special:
        
        attribute t_horny:
            "mod_assets/MPT/tina/tina_turned_special_horny.png"

