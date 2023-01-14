class Character:
    def __init__(self, name, age = 240):
            self.name = name
            self.age = age

    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age

    def getFormatedAge(self):
        return { 'years': self.age // 12, 'months': self.age % 12}

    def printStatus(self):
        print(f"{'*' * 33}")
        print(f"* Name: { self.name } | Age: { self.getFormatedAge()['years'] }y { self.getFormatedAge()['months'] }m  *")
        print(f"{'*' * 33}")

