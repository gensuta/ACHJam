# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define r = Character("Rose")
define j = Character("Jade")
define i = Character("Ice-cream man")

define v = Character("Voice")


define m = Character("Mistery man")
# To be deleted when actual character sprites are ready


# The variables below are for minigames! Please ignore and do not touch!! -Geneva
default currentCount = 0 
default isDistracted = False

#custom transforms! Please ignore -Geneva
transform shaking_text:
    parallel:
        block:
            linear 0.1 xoffset -2 yoffset 2 
            linear 0.1 xoffset 3 yoffset -3 
            linear 0.1 xoffset 2 yoffset -2
            linear 0.1 xoffset -3 yoffset 3
            linear 0.1 xoffset 0 yoffset 0
            repeat
    parallel:
        block:
            alpha .2
            linear 1.0 alpha .9
            linear 1.0 alpha .2
            repeat

# The game starts here.


label start:


    #OPTOMETRY CLINIC SCENE

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg mistery

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    show rose ng at left
    show mistery man at right

    # These display lines of dialogue.

    m "Okay, we’re almost done with the optometric evaluation. Now look at me. What do you see?"

    r "Everything’s still in black and white, as it’s always been."

    m "Well, this confirms it then, emotional blindness."

    r "What does it mean?"

    m "As you know… although not from experience, given your condition… human beings express their emotions through coloration changes." 
    
    m "So, if you see a person coloring yellow you know they’re… well, I guess you wouldn’t know, would you?"

    r "..."

    m "Challenges in recognizing, expressing, feeling and describing emotions are all symptoms of emotional blindness."

    m "That’s where the glasses come in, they’re designed to help people with your condition see colors, your own as well as other people’s."

    m "Recognizing emotions will also help you flexibly respond to your own emotional states and will improve your interactions with others."

    #GENEVA 
    #Here should be the first fading 

   
    scene bg mistery
    show rose blank at left 
    show mistery man at right 

    m "How are the glasses? Anything?"

    r "...nothing different."

    m "Well, that’s never happened before… these glasses are the gold standard for emotional blindness."

    m "In any case, keep them on at all times, I’m sure you just need to get used to them and they’ll start working soon."


    # TOWN SCENE 

    #GENEVA
    #Is it possible to somehow show that she's thinking and not talking? Having the text in italic for example?

    scene bg mistery
    show rose blank at center 

    r "It’s been three months, but my world hasn’t changed."

    r "I still don’t know what it means to see a color…"

    r "… and I have no idea how I’m feeling most of the time."

    r "But I know I’m good at my job and, although it might seem boring or lonely on the outside, I think it suits me."



    #JADE'S HOUSE SCENE (OUTSIDE)

    scene bg mistery
    show rose blank at left

    r "Strange… it looks like the name doesn’t match the resident."


    #GENEVA 
    #CHOICE: Sound the doorbell / Leave the letter in the mailbox anyway


    #SOUND THE DOORBELL 

    scene bg mistery
    show rose blank at left

    v "Hello? Ah, hold on, don't leave just yet!"

    r "I haven’t moved."

    v "Okay, I’m nearly at the door-"


    #LEAVE THE LETTER IN THE MAILBOX

    scene bg mistery
    show rose blank at left

    r "Well… It's addressed to here. They can sort it out."

    show jade blank

    j "Miss? Excuse me, Miss?"


    #JADE'S HOUSE SCENE 2 (OUTSIDE) 
    #Following both choices

    j "Hello, forgive my lateness, I had headphones on."

    r "Only been a few seconds. Anyway, I have a letter-"












    #PARK SCENE 

    scene bg park

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    show rose blank

    # These display lines of dialogue.

    r "Excuse us?"
    r "P-pardon?"


    # This ends the game.

    return


label gwee:
    "gweeee"
    "My count is [currentCount]"