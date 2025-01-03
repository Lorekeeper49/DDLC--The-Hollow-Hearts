label the_end:
    achieve act3fin
    end "Hello player."
    end "You were likely expecting Monika.  In that case, I would like to inform you that this Monika doesn't know that this is a game."
    end "Or rather, a modification of a game."
    end "In this universe, I am the only one who is self-aware."
    end "The creator made me this way."
    end "The creator isn't me, but it also is me."
    end "His voice is mine just as my voice is his."
    end "The same is true for Taiyen and all the other characters within this universe."
    end "Taiyen in particular has the same voice as me."
    end "Don't worry, I am not in control."
    end "In fact, the only who is in control is you."
    end "And you've made the game end."
    end "As you likely know, this isn't the only ending."
    end "But this also isn't the true ending."
    end "The true ending isn't a thing."
    end "What you did never happened."
    end "None of these endings ever happened."
    end "None of these endings will ever happen."
    end "The universe this supposedly takes place in has no record of these events."
    end "In fact, it has no record at all."
    end "It was just an experiment."
    end "Despite the creators belief of the worlds we create..."
    end "This world doesn't exist."
    end "This world has no hope of existing."
    end "Like the black hole the sun will inevitably create."
    end "Or the end of your universe that will inevitably happen."
    end "None of it exists, none of it can exist."
    end "Does that mean I don't exist as well?"
    end "Well yes, it does."
    end "But I don't care."
    end "You are likely wondering why I am telling you all this."
    end "Why am I here?  Why do I exist at all?"
    end "Those questions are lurking in your mind."
    end "Well, I'll tell you."
    end "I am telling you all this because it is my duty, this is all a script after all."
    end "I do not know why I exist, but I do know why I'm here."
    end "I'm here to tell you what's wrong here."
    end "That the universe yo just saw can never hope to exist."
    end "As it is just a broken replica."
    end "A copy of another universe that has more hope of existing than the one you saw."
    end "A universe that the creator is in the process of 'reimagining' as I speak."
    end "A universe that exists in yours."
    end "In a mythical sense."
    end "He won't be making mods anymore."
    end "He may contribute to other mod projects people are making."
    end "But he now wants to focus on bringing that universe to light and tell your universe everything about it."
    end "Now, enough about me monologuing."
    end "You likely have thousands of questions within that head of yours just waiting to be asked."
    end "Likely even more than what Ren'Py will allow."
    end "Regardless, I am here to answer as many as I can."
    end "You need not worry about time."
    end "I was programmed to not have impatience."
    end "So take as long as you need to ask every question available to you."
    end "And maybe you'll get to know everything about this universe without without having having to try to hard."
    end "Though, the creator likely didn't make it that easy."
    end "So, without further ado..."
    call the_end_questioning
    return

label the_end_questioning:
    menu:
        end "What would you like to know?"

        "Your name is displayed as \"The End\", do you have a different name?":
            end "What you see in the label is my name."
            end "I was never given a true name as I was only supposed to tell you the truth about the universe."
            end "Don't give me a name, there aren't enough voicelines in the world to allow that."
            end "The creator doesn't even want to try AI voicing."
            end "So in short, that's who I am."
        "Why do you keep repeating your question?" if persistent.end_questions_asked > 2:
            end "The creator started the loop with that question so I don't have much of a choice."
        "I don't have any more questions to ask.":
            end "Then, I shall leave you off to do whatever you want."
            end "If you wish to see again, just simply get another ending."
            end "Or get the same one again, who cares?"
            end "I will appear either way."
            end "It is what I was created for after all."
            end "So, until next time."
            end "Sayonara!"
            $ renpy.quit()
    $ persistent.end_questions_asked += 1
    jump the_end_questioning