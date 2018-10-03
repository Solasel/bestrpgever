import random

class Fighter:
	def __init__(self, h, a, d, s, l, n):
		self.health = h
		self.attack = a
		self.defense = d
		self.speed = s
		self.luck = l
		self.name = n

		self.money = 0

	def __str__(self):
		return str(self.name) + ":\n\tHealth = " + str(self.health) + "\n\tAttack = " + str(self.attack) + "\n\tDefense = " + str(self.defense) +  "\n\tSpeed = " + str(self.speed) + "\n\tLuck = " + str(self.luck)

	def deposit(self, amount):
		self.money += amount
	
	def withdraw(self, amount):
		self.money -= amount

	def gamble(self, amount, guess):
		print("You are betting " + str(amount) + " doodles on the roll of a 6-die.")
		print("Your guess is " + str(guess) + ". If you win, you receive double the money. If you lose, you lose it all!\n")

		if random.randint(1, 6) == guess:
			print("You win!")
			self.deposit(amount)
			return
		print("You lose!")
		self.withdraw(amount)
		return

class Place:
	def __init__(self, n, d, t):
		self.name = n
		self.desc = d
		self.type = t

	def __str__(self):
		return self.name + ": " + self.type + "\n- " + self.desc

class Map:
	def __init__(self, n, w, h, s):
		self.name = n
		self.width = w
		self.height = h
		self.grid = [[None] * w] * h

		self.start_tile = s

