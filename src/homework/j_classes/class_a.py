#
import random

class die:
    def roll():
        return random.randint(1,6)
    def get_roll():
        return die.roll()
    
print(die.get_roll())