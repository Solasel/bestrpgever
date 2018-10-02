import random, time

class Fighter:
	def __init__(self, h, a, d, s, l, n):
		self.health = h
		self.attack = a
		self.defense = d
		self.speed = s
		self.luck = l
		self.name = n

	def __str__(self):
		return str(self.name) + ":\n\tHealth = " + str(self.health) + "\n\tAttack = " + str(self.attack) + "\n\tDefense = " + str(self.defense) +  "\n\tSpeed = " + str(self.speed) + "\n\tLuck = " + str(self.luck)

