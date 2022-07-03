class Data():

    def __init__(self):
        self.mCommands = []         # contains the name of commands used from the menu.
        self.mDescriptions = {}     # contains the description of commands corresponding to
                                    # their names.
        self.mFunctions = {}        # accomplishes the same thing as self.mDescriptions
                                    # but with regards callbacks to functionality rather than
                                    # the description.
        self.mDone = False          # relates to the main loop of the program.
    
    def add_choice(self, name, function, description):
        self.mCommands.append(name)
        self.mDescriptions[name] = description
        self.mFunctions[name] = function

    def get_function(self, name):
        if name in self.mFunctions.keys():
            return self.mFunctions[name]
        return False

    def get_description(self, name):
        if name in self.mDescriptions.keys():
            return self.mDescriptions[name]
        return False

    def get_names(self):
        return self.mCommands

    def get_done(self):
        return self.mDone

    def set_done(self, boolian):
        self.mDone = boolian

    def do_the_thing(self, name):
        """
        all the values stored in self.mFunctions take data objects as parameters,
        so we use this method as a kind of shortcut instead of going through get_function.
        """
        function = self.get_function(name)
        if function:
            function(self)
