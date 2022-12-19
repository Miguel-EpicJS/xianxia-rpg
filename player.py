from random import choice

class Player:

    def __init__(self, name, age = 240, qi = 0, rank = 0):
        
        self.name = name
        self.age = age  # in months
        self.qi = qi
        self.rank = rank
        self.qiNext = 2**rank * 100

        self.amount = 10

        self.ranksMajor = ["Qi Gathering", "Foundation Building", "Golden Core", "Nascent Soul"]
        self.ranksMinor = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]

        self.grades = [ 
            { "grade": "Mortal", "multiplier": 1 }, 
            { "grade": "Earth", "multiplier": 2 },  
            { "grade": "Heaven", "multiplier": 3 },  
            { "grade": "Immortal", "multiplier": 5 }
        ]

        self.talent = choice(self.grades)

    def levelUp(self):
        if self.qi >= self.qiNext:

            self.qi -= self.qiNext
            self.rank += 1
            self.qiNext = 2**self.rank * 100

            return True

        return False

    def gather(self):
        self.qi += self.amount * self.talent["multiplier"]
        self.age += 1
        return self.amount

    def getAmount(self):
        return self.amount

    def getTalent(self):
        return self.talent["grade"]

    def getRank(self):
        return f"{self.ranksMinor[ self.rank % 10 ]} {self.ranksMajor[ self.rank // 10 ]}"

    def getAge(self):
        return { "value": self.age, "result": f"{self.age//12}y {self.age%12}m" }

    def stats(self):
        print(f"Name: {self.name} # ", end='')
        print(f"Age: {self.getAge()['result']} # ", end='')
        print(f"Talent: {self.getTalent()} # ", end='')
        print(f"Cultivation: { self.getRank() } ", end='')
        print(f"{self.qi}/{self.qiNext}")
