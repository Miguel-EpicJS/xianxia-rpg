class Colors:
    def __init__(self):
        pass 

    def Red(self, el):
        return f"\33[0;91m{el}\33[0m"

    def Green(self, el):
        return f"\33[0;92m{el}\33[0m"

    def Yellow(self, el):
        return f"\33[0;93m{el}\33[0m"

    def Blue(self, el):
        return f"\33[0;49;34m{el}\33[0m"

    def Black(self, el):
        return f"\33[0;49;90m{el}\33[0m"

    def White(self, el):
        return f"\33[0;49;97m{el}\33[0m"


