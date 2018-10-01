import random
import classes

def fight(p, e):

	turn = 1
	print(p)
	print("\n===== VERSUS =====\n")
	print(e)
	print("\nStarting health:")

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
		dmg = 2 * first.a - second.d if fcrit else first.a - second.d
		print(first.n + (" crits for " + str(dmg) + " damage!" if fcrit else " attacks for " + str(dmg) + " damage."))
		second.h -= dmg
		if second.h <= 0:
			second.h = 0
			break

		# Second fighter attacks
		scrit = random.randint(0, 100) < second.l
		dmg = 2 * second.a - first.d if scrit else second.a - first.d
		print(second.n + (" crits for " + str(dmg) + " damage!" if scrit else " attacks for " + str(dmg) + " damage."))
		first.h -= dmg
		if first.h <= 0:
			first.h = 0
			break

		turn += 1

	# Print final health values.
	print(str(p.n) + ": " + str(p.h) + "\n" + str(e.n) + ": " + str(e.h) + "\n")
	print(p.n + " wins!" if p.h > 0 else e.n + " wins!")
	return p.h > 0

player = classes.Fighter(10, 2, 1, 5, 10, "Buton")
enemy = classes.Fighter(10, 1, 1, 5, 10, "Sam")

print()

fight(player, enemy)

print()
