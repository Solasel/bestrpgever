import random
import testo

def fight(p, e):

	turn = 0
	print("Starting health:")

	while True:

		print(str(p.n) + ": " + str(p.h) + "\n" + str(e.n) + ": " + str(e.h) + "\n")

		print("Turn " + str(turn) + ":")

		# Roll to determine who goes first
		proll = p.s + random.randint(1, 6)
		eroll = e.s + random.randint(1, 6)

		# Assign first and second based on rolls
		first = p if proll > eroll else e
		second = e if proll > eroll else p

		# If we had a tie, break the tie
		if proll == eroll:
			tiebreak = random.randint(0, 1)
			first = p if tiebreak == 1 else e
			second = e if tiebreak == 1 else p

		# First fighter attacks
		fcrit = random.randint(0, 100) < first.l
		print(first.n + (" crits!" if fcrit else " attacks."))
		second.h -= 2 * first.a - second.d if fcrit else first.a - second.d
		if second.h <= 0:
			second.h = 0
			break

		# Second fighter attacks
		scrit = random.randint(0, 100) < second.l
		print(second.n + (" crits!" if fcrit else " attacks."))
		first.h -= 2 * second.a - first.d if scrit else second.a - first.d
		if first.h <= 0:
			first.h = 0
			break

		turn += 1

	# Print final health values.
	print(str(p.n) + ": " + str(p.h) + "\n" + str(e.n) + ": " + str(e.h) + "\n")
	print(p.n + " wins!" if p.h > 0 else e.n + " wins!")
	return p.h > 0

player = testo.Player(10, 2, 1, 5, 50, "Buton")
enemy = testo.Enemy(10, 1, 1, 5, 50, "Sam")

print()

fight(player, enemy)

print()
