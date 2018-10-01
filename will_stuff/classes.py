import random, time

class Fighter:
    def __init__(self, health, attack, defense, speed, luck, name):
        self.h = health
        self.a = attack
        self.d = defense
        self.s = speed
        self.l = luck
        self.n = name

    def __str__(self):
        return str(self.n) + ":\n\tHealth = " + str(self.h) + "\n\tAttack = " + str(self.a) + "\n\tDefense = " + str(self.d) +  "\n\tSpeed = " + str(self.s) + "\n\tLuck = " + str(self.l)

