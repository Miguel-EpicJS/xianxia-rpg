class Colors:
    """
        Class to manage the colors used when styling the text ui
    """
    def __init__(self):
        pass 

    def Red(self, el):
        """
        Change string color to red
        """
        return f"\33[0;91m{el}\33[0m"

    def Green(self, el):
        """
        Change string color to green
        """
        return f"\33[0;92m{el}\33[0m"

    def Yellow(self, el):
        """
        Change string color to yellow
        """
        return f"\33[0;93m{el}\33[0m"

    def Blue(self, el):
        """
        Change string color to blue
        """
        return f"\33[0;49;34m{el}\33[0m"

    def Black(self, el):
        """
        Change string color to black
        """
        return f"\33[0;49;90m{el}\33[0m"

    def White(self, el):
        """
        Change string color to white
        """
        return f"\33[0;49;97m{el}\33[0m"


