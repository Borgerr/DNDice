import choices, data

def main():
    d = data.Data()
    choices.configure_menu(d)
    choices.display_menu(d)
    while not d.get_done():
        choice = input("What would you like to do? ")
        if choice not in d.get_names():
            print("Please enter a valid option.")
        else:
           d.do_the_thing(choice) 

if __name__ == "__main__":
    main()
