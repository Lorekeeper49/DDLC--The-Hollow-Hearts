#Name: The Aftermath
label act2_ch3_main:
    if not known:
        jump act2_ch3_alt
    if config.developer:
        $ found_breaker = True
    stop music fadeout 2.0
    play ambience forest
    scene bg park_night
    with dissolve_scene_full
    call showlocation("Converse Park","October 10, 2023",23*60+14+57/60.0,"bg tree") from _call_showlocation_41
    a "What are we doing here?"
    a "This is the same park that I..."
    show kotonoha turned casual neut om zorder 2 at t11
    k "We're looking into a lead."
    a "If this about that sewer, I've already been down there!"
    k rhip "It's not about the sewer."
    stop ambience
    hide kotonoha
    a "Hold!"
    "Is that...?"
    ak "Aoruguri, what are you doing?"
    a "Guys!"
    ak "I wouldn't go out there on your own!"
    "Ignoring them, I walk up to find..."
    show dominion zorder 2 at t11
    a "Dominion?"
    d "Eh?"
    show dominion monster0 with blink
    $ pause(1)
    show dominion monster1 with blink
    $ pause(1)
    show dominion monster2 with blink
    $ pause(1)
    show dominion monster3 with blink
    $ pause(1)
    scene black with blink
    $ pause(1)
    scene park_night
    show taiyen zorder 2 at face
    with dissolve_scene_half
    $ pla = "Sakura Taiyen?"
    general "Are you okay?"
    a "Yeah, thanks Taiyen..."
    general "Okay, you're not exactly okay."
    a "Huh?"
    hide taiyen
    show kotonoha turned casual worr zorder 2 at face
    with blink
    a "Ah!"
    show kotonoha lsur om at t11
    "I push myself off her."
    a "huff... puff..."
    a "Ahem!  I'm so sorry, Kotonoha!"
    a "I don't know what happened, I just..."
    k rhip "No, you're fine."
    k curi "About this Dominion, you sure you saw him?"
    show akira 4ao zorder 1 at t22
    ak "I did."
    ak 1ao "He's been presumed dead for years.  Didn't think he'd turn up here."
    hide kotonoha
    hide akira
    show mari forward worr zorder 2 at t11
    a "Mari, do you happen to know whatever happened to him?"
    ma om "Maybe I shouldn't burden you with the details while the tension's high..."
    a "Fair enough."
    hide mari
    show kotonoha turned casual anno rhip lup zorder 2 at t11
    k om "Okay.  We need to figure out where to find this Dominion.  Anyone have any ideas?"
    show kotonoha cm
    a "I believe I read somewhere that there is a small storage shack south of here, but were gonna have to search deep in the forest to find it."
    k ldown "Then we'll search there.  Everyone, use your GPSes to find your way to each other if you're lost."
    everyone "Got it!"
    $ start_loc = random_list(["0_0", "1_0", "2_0", "3_0", "4_0", "5_0", "6_0", "7_0", "8_0", "9_0"])
    call explore("deep_forest_" + start_loc[0], True) from _call_explore_1
    scene bg kamiclassnight with dissolve_scene_full
    call showlocation("HEADQUARTERS","October 10, 2023",2*60+59+57/60.0,"bg kamiclassnight") from _call_showlocation_42
    "We're back."
    show mari forward anno zorder 2 at t11
    a "Mari, about Dominion..."
    ma mi "I already know what you're about to ask."
    ma dist "*Sigh*"
    ma anno mi "Has Sakura-kun told you about Breaker?"
    show mari cm
    a "Yes, but he didn't tell me what it looked like."
    ma mi "Well, it's a black substance, I can say that much."
    if found_breaker:
        show mari cm
        "A black substance...?"
        "Wait."
        a "Is there a chance you could be talking about this?"
        "I show Mari the vials I had in my pocket."
        ma eb "!!!"
        ma om "Yes!  Yes!  That's exactly what I'm talking about!  How the hell did you find that!?"
        a "It was in an abandoned underground factory just a few meters from where we were tonight."
        ma "Please tell me you haven't used those on anybody..."
        a "I didn't, these were the only 2 vials in there and their both half full like how vials are usually filled."
        ma anno "...Good."
        ma dist "Make sure you keep those safe, you don't want them to end up in the wrong hands."
        a "I will."
        show mari oe
        ma anno mi "Anyway..."
    ma "I'll tell you that I was one of the cancelled test subjects during production."
    ma "And because of that, I know of the other test subjects."
    ma dist "And, as you might have guessed, Dominion was one of the three that actually went through."
    ma anno "Someone was assigned with putting the three processed test subjects out of their misery...  But I guess they didn't have the strength to kill them."
    ma dist "Either that, or they escaped before it happened."
    show mari cm
    a "Jesus..."
    a "Who were the others?"
    ma anno "Settou Seiei was the other cancelled one, he was our old leader."
    ma "The other processed ones were Kamiyama Kirinani..."
    ma dist "And... Yandere Lilly..."
    show mari cm
    a  "!!!"
    hide mari
    show lilly norm be zorder 2 at t11
    "..."
    lil "I have full memory of this..."
    lil l2bc2 "It was horrible..."
    lil l2eb "I don't even remember what happened before that anymore..."
    lil l2bc2 "I just know... that I was never the same again..."
    lil l2eb "I never did get my attribute back."
    "..."
    a "How old were you?"
    lil "Twelve..."
    a "What the fuck was wrong with you?  Why would you agree to that when you don't even know the side effects?"
    a "Wah?"
    "Why did I...?"
    a "Sorry, I don't know what that was..."
    hide lilly
    show vignette zorder 100 with None
    a "NGH!"
    lil "Aoruguri?"
    scene bg secret_room
    show vignette
    with None
    $ pause(0.05)
    scene bg kamiclassnight
    show vignette
    with None
    $ pause(0.05)
    scene bg secret_room
    show vignette
    with None
    $ pause(0.05)
    scene bg kamiclassnight
    show vignette
    with None
    $ pause(0.05)
    scene bg secret_room
    show vignette
    with None
    $ pause(0.05)
    scene bg kamiclassnight
    show vignette
    with None
    $ pause(0.05)
    scene bg secret_room
    show vignette
    with None
    $ pause(0.05)
    scene bg kamiclassnight
    show vignette
    with None
    $ pause(0.05)
    scene bg secret_room
    show vignette
    with None
    $ pause(0.05)
    scene bg kamiclassnight
    show vignette
    with None
    $ pause(0.05)
    play ambience creepy
    scene bg secret_room
    show vignette zorder 100
    with None
    $ pause(0.5)
    "Not again!"
    "Where am I now?"
    $ mari = "Woman"
    $ pla = "Man"
    ma "She has to take the substance, it's the only way!"
    general "Well how about you take it then?  Do your test early!"
    ma "FUCK YOU!  She is my daughter and I'd rather see the effects on her before taking it myself!"
    "Someone's gotta get their priorities straight."
    general "You saw the other two tests, you know how those went!"
    ma "This one's gonna be different, I know it!"
    general "SHUT UP!  She is my daughter too and I don't want her personality to change!"
    ma "YOU ABUSED HER!  You don't have a right to call her your daughter!"
    general "She took my name-"
    ma "Because we didn't have a choice but to give her your family name!"
    general "WHAT'D YOU SAY, BITCH!?"
    ma "FUCK YOU LUNA!"
    general "Oh you did not just-"
    ma "SHUT UP!  You don't even know how to properly take care of a child!"
    ma "I can't believe I had sex with you!"
    general "MARI-"
    ma "Don't call me that!"
    ma "In fact, just get the fuck out of my life!"
    "..."
    show mari forward sad zorder 2 at t11
    ma "Hey baby."
    $ mari = "Kusanoki Mari"
    ma "Hey, Aoruguri!"
    stop ambience fadeout 1.0
    scene bg kamiclassnight
    show mari forward worr zorder 2 at t11
    with blink
    ma "Hey, you're okay.  You're okay."
    a "Mari?"
    a "Or should I say..."
    a "Mom?"
    ma neut "..."
    a "You're my mother, right?"
    a "I finally understand what I've been seeing these past few months...!"
    ma "..."
    ma happ tears om "You finally remember!"
    show mari cm
    "I've been looking for you forever!"
    a "Mom!"
    show mari at face
    $ pause()
    $ pla = "Luna Aoruguri & Kusanoki Mari"
    show mari om
    general "*Sigh*"
    show mari at t11
    a "If that test actually went through and it went the way you wanted it to, what attribute would you have replaced my storm with?"
    ma om "Mine."
    a "Why didn't it go through then?"
    ma anno "You resisted, makes sense."
    ma cm "Your father abused you but you never got to see what I would do to you, I should've expected you to be scared."
    a "I see."
    hide mari
    "Something's still bothering me..."
    "Right, Lilly!"
    show lilly zorder 1 at t21
    show hanato day anno rhip zorder 2 at t22
    ha "LILLY!"
    "Someone had the same mind."
    "Wait, what's Hanato doing here?"
    ha om "Why didn't you tell me anything?"
    lil c2e "I'm sorry, I didn't know you were involved..."
    show lilly a1e
    ha rdown "Of course I was involved!"
    ha "I have been here protecting the Yanderes with my life and you just want to throw that away and put yourself in danger!?"
    ha sad "How could you do this to me?"
    "Guess she was listening in."
    "Though, how far away was she that she just now got here?"
    lil c2e "Hanato, I didn't want..."
    lil c2c2 "I didn't want to be a Yandere anymore."
    ha anno ej cm "*Scoff*"
    lil c3e "You don't get it, okay?"
    lil "I've killed so many innocents!"
    lil "I almost killed Taiyen-"
    $ layeredimage_ref("hanato")
    ha vang om "Taiyen and your kills have nothing to do with this!"
    ha angr rhip "You...  You matter!"
    show lilly h2e
    "Hanato looks away from Lilly."
    ha cry rdown "You're the weakest one of them all."
    ha "Without your attribute... even if you somehow have other abilities..."
    ha ce "You're in danger."
    ha "I... I don't..."
    ha "I don't know what...  I don't want to..."
    ha cm "..."
    lil "I don't understa-"
    show hanato sad at t11
    lil cat h1eb "Mmph!"
    "Huh?"
    "Is she...?"
    ha oe "..."
    show hanato at t22
    ha om "I'm sorry..."
    ha ej "I don't know why I..."
    show hanato at t33
    show lilly at t22
    lil norm n4eb "Wait, Hanato!{w=1}{nw}"
    show hanato at rhide
    show lilly cat at t33
    hide hanato
    extend "  Hanato!"
    a "Leave her be."
    lil norm "But..."
    a "She did that on impulse, this happens a lot with first kisses like that."
    a "Just let her process what she just did before you go after her, okay?"
    lil n2bc2 "...{w=1}{nw}"
    show lilly n2eb2
    extend "Okay."
    show lilly at lhide
    hide lilly
    show mari forward happ zorder 2 at t11
    ma om "You should get some rest, give you some time to process everything that's been going on for you too."
    show mari cm
    a "Right..."
    return

label act2_ch3_alt:
    stop music fadeout 2.0
    play ambience forest
    scene bg park_night
    with dissolve_scene_full
    call showlocation("Converse Park","October 10, 2023",19*60+14+57/60.0,"bg tree")
    "I have absolutely no idea why I'm going to the exact place an 'unkown' number has told me to go."
    "Even said they know me?"
    "Ah well, it's not like I've got anything left to lose anyway."
    show natsuki turned casual dist rhip zorder 2 at t11
    n "..."
    a "Hello?"
    a "Are you Natsuki?"
    n ce "..."
    n cross neut oe om "Hey Sis..."
    stop ambience
    show bg vision_background zorder 1
    play ambience creepy
    n "Do you... remember me?"
    show natsuki cm
    "Something doesn't feel right..."
    a "No?"
    n om "Of course..."
    n dist "Hello amnesia, how are you?"
    n turned neut rhip "Mom not able to find you?"
    "'Mom'?"
    a "I don't know my mother."
    n dist "Of course you don't!"
    n anno rdown ce "Damnit!"
    n oe "You know Taiyen, right?"
    a "Sort of..."
    n neut "I know what you're thinking about."
    n anno rhip lhip "It's fuck him or dump him!  I say fuck him!"
    n dist "That is a sentence I just said." 
    n ldown neut "But in all seriousness, he exists in most of those memories of yours."
    n dist "The others, well..."
    n cross neut "There's an old mansion on the west side of town about 50 blocks from your school."
    hide bg vision_background
    play sound static
    show noise zorder 1
    n "{w=0.15}{nw}"
    stop sound
    stop ambience
    hide noise 
    show bg park_night zorder 1
    play ambience forest fadein 5.0
    n "I suggest you start there."
    "Is she crazy?"
    hide natsuki
    "She begins walking away."
    a "Wait!"
    show natsuki cross casual neut zorder 2 at t11
    "She stops."
    a "You said my mother can't find me, can you find her?"
    "I'm just assuming what she's saying is true without a second thought."
    "If this girl really is my sister, then she'd know how to find mother."
    n om "I don't need to."
    n "You already have."
    "The fuck is that supposed to mean?"
    hide natsuki
    "She walks away."
    a "I should consult Mari."
    scene bg mari_office with wipeleft_scene
    call showlocation("Principal's Office", "October 10, 2023",19*60+59+57/60.0,"bg mari_office")
    a "Mari?"
    show mari forward curi zorder 2 at t11
    ma om "Yes, honey?"
    show mari cm
    a "Well..."
    "Fuck it, let's test this."
    a "Mother..."
    ma happ "!!!"
    a "(Holy fuck!)"
    "I got her?"
    ma tears om "Daughter?  You remember?!"
    "She's always been right in front of me!"
    a "Mother!"
    show mari ce cm at face
    "..."
    ma oe om "I finally found you!"
    show mari cm
    "She kisses my forehead lovingly."
    show mari at t11
    a "I wouldn't say you've found me per se, I think I've still got amnesia."
    ma om "Well, it's a start, is it not?"
    show mari none
    "She wipes her tears."
    a "So, why didn't you tell me about all this before?  I feel like things would've been the same, if not a lot happier."
    ma dist "They would not have been..."
    ma om "It's a lot of things to take in."
    ma ee "Not to mention how little I actually want to recall."

    return