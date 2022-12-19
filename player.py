class Player:

    def __init__(self, name, age = 240, qi = 0, rank = 0):
        
        self.name = name
        self.age = age  # in months
        self.qi = qi
        self.rank = rank
        self.qiNext = 2**rank * 100

        self.ranksMajor = ["Qi Gathering", "Foundation Building", "Golden Core", "Nascent Soul"]
        self.ranksMinor = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]

        self.grades = ["Mortal", "Earth", "Heaven", "Immortal"]  # for future updates

    def levelUp(self):
        if self.qi >= self.qiNext:

            self.qi -= self.qiNext
            self.rank += 1
            self.qiNext = 2**self.rank * 100

            return True

        return False

    def gather(self, amount):
        self.qi += amount
        self.age += 1

    def getRank(self):
        return f"{self.ranksMinor[ self.rank % 10 ]} {self.ranksMajor[ self.rank // 10 ]}"

    def getAge(self):
        return { "value": self.age, "result": f"{self.age//12}y {self.age%12}m" }
