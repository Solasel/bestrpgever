class Silly:
    def __init__(self, health, attack, defense):
        self.h = health
        self.a = attack
        self.d = defense

    def __str__(self):
    	return "Silly: Attack = " + str(self.a) + " Defense = " + str(self.d) + " Health = " + str(self.h)

        
goblin = Silly(1, 1, 1)
print(goblin)

