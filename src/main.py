import choices

def main():
    # TODO: get continuous menu actions working.
    # might require moving this loop to a function of its own in choices.py
    while True:
        choice = input("What would you like to do? ")
        if choice == "menu":
            choices.display_menu()

if __name__ == "__main__":
    main()
