import random           # random.randint
import data             # Data class

def display_menu(d):    # where d is a Data object
    """
    Displays each menu item corresponding with the following template:
    choiceCommand - Command description. Describes what the command does.
    should do nothing more than display in this manner.
    """
    for name in d.get_names():
        print(name + " - " + d.get_description(name))

def configure_menu(d):  # where d is a Data object
    """
    Adds choices and their corresponding functions and descriptions to the main Data object.
    use the following template:
    d.add_choice("choice-command", function_used, "Description to be displayed.")
    """
    d.add_choice("menu", display_menu, "Display menu.") # keep at list top

    # add all other options under this line
    d.add_choice("undefined-roll", roll_any_number, "Roll any number. Displays without cool ASCII art.")



    d.add_choice("quit", quit, "Quits the program.")    # keep at list bottom.

def quit(d):            # where d is a Data object
    # could be changed to used sys library to exit the program with sys.exit() or whatever
    d.set_done(True)

def roll_any_number(d): # where d is a Data object
    """
    Just gives the option to roll a dice with any side count.
    """
    n = get_integer("Roll up to and including what number? ")
    print(random.randint(1, n))

def get_integer(prompt):
    while True:
        n = input(prompt)
        try:
            n = int(n)
            break
        except ValueError:
            print("Please enter a valid integer.")
        except:
            print("Something else went wrong in our conversion. Please try again.")
    return n
