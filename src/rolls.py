def d6(side):
    """
    Gives ASCII output for the side given.
    Side input as an integer number between 1 and 6, inclusive.
    """
    if side == 1:
        # code for side 1 output
        """
        -----------
        |         |
        |         |
        |    O    |
        |         |
        |         |
        -----------
        """
        print("-----------") 
        print("|         |")
        print("|         |")
        print("|    O    |")
        print("|         |")
        print("|         |")
        print("-----------") 
    elif side == 2:
        # code for side 2 output
        print("-----------")
        print("|O        |")
        print("|         |")
        print("|         |")
        print("|         |")
        print("|        O|")
        print("-----------")
    elif side == 3:
        # code for side 3 output
        print("-----------")
        print("|O        |")
        print("|         |")
        print("|    O    |")
        print("|         |")
        print("|        O|")
        print("-----------")

    elif side == 4:
        # code for side 4 output
        print("-----------")
        print("|O       O|")
        print("|         |")
        print("|         |")
        print("|         |")
        print("|O       O|")
        print("-----------")
    elif side == 5:
        # code for side 5 output
        print("-----------")
        print("|O       O|")
        print("|         |")
        print("|    O    |")
        print("|         |")
        print("|O       O|")
        print("-----------")
    elif side == 6:
        # code for side 6 output
        print("-----------")
        print("|O       O|")
        print("|         |")
        print("|O       O|")
        print("|         |")
        print("|O       O|")
        print("-----------")
    else:
        print("d6 function somehow received an impossible roll for interpretation.")
