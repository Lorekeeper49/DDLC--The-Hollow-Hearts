# Akira interviews CONTROLLER before the title screen shows up, prologue will not automatically start anymore, this will replace it.
# This will not be reviewable from the title screen, a new persistent variable will be created to ensure this plays for everyone.
#   - This note is because KaneMonger started from the title screen on his playthrough for some reason and had to start the prologue manually.

label start_inter:
    scene black
    $ window_style = ""
    $ nb = "namebox"
    $ akira = "神山秋羅\n{size=15}Kamiyama Akira{/size}"
    ak "Hello there CONTROLLER."
    ak "Sorry about the lights, no one's bothered to fix them for months."
    ak "So you unfortunately can't see me."
    ak "You also can't see this massive glass test tube looking thing behind me containing one of the many cores of this place."
    ak "The black and white oversized human hearts that I call..."
    ak "The Hollow Hearts."
    menu:
        "Roll Credits":
            ak "Wha-?"
            ak "Are you thinking this is some sort of fictional story you're sinning?"
            ak "Well, whatever."
        "The Hollow Hearts...":
            ak "Yes."
            ak "It's what I've codenamed this whole place."
    ak "What you are in operation of here is none other than my father's plan to bend the world to his will."
    ak "You are actually a tester, he plans to use that console himself once he knows it's working."
    ak "Now, be honest, do you think it's immoral to be controlling other people like this?"
    menu:
        "Yes":
            ak "Good, we have at least one thing in common."
            ak "So, here's the deal..."
        "No":
            ak "That's not the answer I wanted to hear, but I'll tell you the deal anyway."
        "I don't know":
            ak "That's fine, you'll learn soon enough."
            ak "Here's the deal..."
    ak "I'm not on my father's team."
    ak "I may be his descendant, but I'm not following his ways.  I'm following the ways of my mother."
    ak "Well, trying to at least."
    ak "I didn't get to know my mother that much before she was murdered by my father."
    ak "He calls it an accident, but I don't think it was."
    ak "And his lies only get worse."
    ak "I really don't like where this is going for him."
    menu:
        "So...  There might be a basement?":
            ak "Where are you hearing that from?"
    menu:
        "I hear crying...":
            ak "What do you...?"
    ak "Actually, now that you mention it..."
    ak "We don't have time to dwell on that now."
    ak "I need to talk about why I'm pissed off."
    ak "I'm pissed off because the person you're about to control is one of my close friends."
    ak "He is the brother of someone I really care about."
    ak "He is Sakura Taiyen."
    ak "I know it isn't really your job but..."
    ak "Take care of him... please."
    ak "Don't make him do anything irrational."
    ak "Remember the fate of this plan is based on what you do."
    ak "And the fate of this plan decides the fate of this world."
    ak "Don't doom it!"
    $ persistent.interviewed = True
    $ renpy.save_persistent()
    return