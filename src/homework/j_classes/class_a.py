#
import random

class die:
    roll_value= 0
    def roll():
        die.roll_value= random.randint(1,6)
        return die.roll_value
    def get_rolled_value():
        if die.roll_value==0:
            die.roll_value= die.roll()
        return "The rolled value is "+ str(die.roll_value)

