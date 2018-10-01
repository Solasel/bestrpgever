import random, time

class Enemy:
    def __init__(self, health, attack, defense, speed, luck, name):
        self.h = health
        self.a = attack
        self.d = defense
        self.s = speed
        self.l = luck
        self.n = name

    def __str__(self):
        return str(self.n) + ": Health = " + str(self.h) + " Attack = " + str(self.a) + " Defense = " + str(self.d) +  " Speed = " + str(self.s) + " Luck = " + str(self.l)

class Player:
    def __init__(self, health, attack, defense, speed, luck, name):
        self.h = health
        self.a = attack
        self.d = defense
        self.s = speed
        self.l = luck
        self.n = name

    def __str__(self):
        return str(self.n) + ":\n\tHealth = " + str(self.h) + "\n\tAttack = " + str(self.a) + "\n\tDefense = " + str(self.d) +  "\n\tSpeed = " + str(self.s) + "\n\tLuck = " + str(self.l)

player = Player(10, 10, 10, 10, 10, "Will")
print(player)

def textBox(text):
    for i in text:
        print(i, end='')
        time.sleep(.01)
    print()

