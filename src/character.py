class Character:
    def __init__(self, name, age = 240):
            self.name = name
            self.age = age

            self.rank = 1

            self.qi = 0
            self.qiForNextRank = 2 ** self.rank * 100

    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age

    def getFormatedAge(self):
        return { 'years': self.age // 12, 'months': self.age % 12}

    def rankUp(self):
        if self.qi >= self.qiForNextRank:

            self.qi -= self.qiForNextRank
            self.rank += 1

            self.calculateNextRankQi()
            return True

        return False

    def calculateNextRankQi(self):
        self.qiForNextRank = 2 ** self.rank * 100

    def printStatus(self):
        print(f"{'*' * 33}")
        print(f"* Name: { self.name } | Age: { self.getFormatedAge()['years'] }y { self.getFormatedAge()['months'] }m  *")
        print(f"{'*' * 33}")

