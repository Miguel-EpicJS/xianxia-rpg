from random import choice

from colors import Colors

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
        statsArr = [self.name, self.getAge()['result'], self.getTalent(), self.getRank()]
        color = Colors()
        print(f"Name: {color.White(statsArr[0])} # ", end='')
        print(f"Age: {color.White(statsArr[1])} # ", end='')
        print(f"Talent: {color.White(statsArr[2])} # ", end='')
        print(f"Cultivation: { color.White(statsArr[3]) } ", end='')
        print(f"{self.qi}/{self.qiNext}")
