from random import randint
class Dice:
    def __init__(self,sides):
        self.sides = sides
    def roll_die(self):
        x = randint(1,self.sides)
        return  x
test=Dice(6)
print(test.roll_die())

