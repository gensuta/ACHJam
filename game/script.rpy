# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define r = Character("Rose")
define j = Character("Jade")


# The game starts here.

#I'm using the ice-cream scene as a trial

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.


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
