# player.py - documentation

## Class
- My objective with this class is to have easy access with all of player's attributes, and to facilitate the implementation of new features and attributes

### __init__
  - name: type string, name of the player
  - age: type int, age of the player in months(increase after cultivating or exploring)
  - qi: type int, current qi of the player, used when breaking through to a new rank
  - rank: type int, current power level of the player, after each 10 ranks, you go up by a major rank

  - qiNext: type int, necessary qi to rank up one time, simple power of two system, multiplied by 100
  - amount: type int, base amount of qi gathered with one cultivation session
  - ranksMajor: type list of strings, track of all cultivation ranks, move to separate class in the future
  - ranksMinor: type list of strings, track of all minor cultivation ranks, move to separate class in the future
  - grades: type list of dictionary(grade - string - name of talent grade, multiplier - int - mutliplier applied when cultivating), this determine the possible talents a player can get, in the future move to a different class
  - talent: type dictionary(grade - string, multiplier - int), a talent chosen from grades

### levelUp
  - Function to verify if the player has level up/break through a new rank, it also update the qiNext variable, return a bool value(True or False)

### gather
  - Function used when cultivating increase qi by the amount multiplied by the talent, increase age by one month, return total qi gathered(totQi).

### getAmount
  - Funtion that return default amount of qi gathered without talent multiplier

### getTalent
  - Funtion that return current player talent

### getRank
  - Function that return in a pretty way the current rank of the player

### getAge
  - Function that return a dictionary with the current age in months and another key result the age in a pretty format

### increaseAge
  - Function that increase age by one month per default, can increase by another value with val variable

### stats
  - Function that prints the current stats of the player, like name, age, talent, cultivation and qi progress


## TODO

Add attributes for attack and defense, luck and destine, breaking through percentage, foundation of cultivation, currency and other xianxia/wuxia like attributes










