from random import choice

from colors import Colors

class Player:
    """
    My objective with this class is to have easy access with all of player's attributes, and to facilitate the implementation of new features and attributes
    """
    def __init__(self, name, age = 240, qi = 0, rank = 0):
       
        """
        name: type string, name of the player
        age: type int, age of the player in months(increase after cultivating or exploring)
        qi: type int, current qi of the player, used when breaking through to a new rank
        rank: type int, current power level of the player, after each 10 ranks, you go up by a major rank

        qiNext: type int, necessary qi to rank up one time, simple power of two system, multiplied by 100
        amount: type int, base amount of qi gathered with one cultivation session
        ranksMajor: type list of strings, track of all cultivation ranks, move to separate class in the future
        ranksMinor: type list of strings, track of all minor cultivation ranks, move to separate class in the future
        grades: type list of dictionary(grade - string - name of talent grade, multiplier - int - mutliplier applied when cultivating), this determine the possible talents a player can get, in the future move to a different class
        talent: type dictionary(grade - string, multiplier - int), a talent chosen from grades
        """

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
        """
        Function to verify if the player has level up/break through a new rank, it also update the qiNext variable, return a bool value(True or False)
        """
        if self.qi >= self.qiNext:

            self.qi -= self.qiNext
            self.rank += 1
            self.qiNext = 2**self.rank * 100

            return True

        return False

    def gather(self):
        """
        Function used when cultivating increase qi by the amount multiplied by the talent, increase age by one month, return total qi gathered(totQi)
        """
        totQi = self.amount * self.talent["multiplier"]
        self.qi += totQi
        self.age += 1
        return totQi

    def getAmount(self):
        """
        Funtion that return default amount of qi gathered without talent multiplier
        """
        return self.amount

    def getTalent(self):
        """
        Funtion that return current player talent
        """
        return self.talent["grade"]

    def getRank(self):
        """
        Function that return in a pretty way the current rank of the player 
        """
        return f"{self.ranksMinor[ self.rank % 10 ]} {self.ranksMajor[ self.rank // 10 ]}"

    def getAge(self):
        """
        Function that return a dictionary with the current age in months and another key result the age in a pretty format
        """
        return { "value": self.age, "result": f"{self.age//12}y {self.age%12}m" }

    def increaseAge(self, val = 1):
        """
        Function that increase age by one month per default, can increase by another value with val variable
        """
        self.age += val

    def stats(self):

        """
        Function that prints the current stats of the player, like name, age, talent, cultivation and qi progress
        """

        statsArr = [self.name, self.getAge()['result'], self.getTalent(), self.getRank()]
        color = Colors()

        print(f"Name: {color.White(statsArr[0])} # ", end='')
        print(f"Age: {color.White(statsArr[1])} # ", end='')
        print(f"Talent: {color.White(statsArr[2])} # ", end='')
        print(f"Cultivation: { color.White(statsArr[3]) } ", end='')
        print(f"{self.qi}/{self.qiNext}")
