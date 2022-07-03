class Data():

    def __init__(self):
        self.mCommands = []         # contains the name of commands used from the menu
        self.mDescriptions = {}     # contains the description of commands corresponding to
                                    # their names
        self.mFunctions = {}        # accomplishes the same thing as self.mDescriptions
                                    # but with regards callbacks to functionality rather than
                                    # the description.
    
    def add_action(self, name, function, description):
        self.mCommands.append(name)
        self.mDescrptions[name] = description
        self.mFunctions[name] = function

    def get_function(self, name):
        if name in self.mFunctions.keys():
            return self.mFunctions[name]
        return False

    def get_description(self, name):
        if name in self.mDescriptions.keys():
            return self.mDescriptions[name]
        return False
