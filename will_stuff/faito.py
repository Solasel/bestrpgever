import random
import classes

def fight(p, e):

	turn = 1
	print(p)
	print("\n===== VERSUS =====\n")
	print(e)
	print("\nStarting health:")

	if (p.health == 0):
		print(p.name + " is already dead!")
		return False
	if (e.health == 0):
		print(e.name + " is already dead!")
		return True

	while True:

		print(str(p.name) + ": " + str(p.health) + "\n" + str(e.name) + ": " + str(e.health) + "\n")

		print("Turn " + str(turn) + ":")

		# Roll to determine who goes first
		proll = p.speed + random.randint(1, 6)
		eroll = e.speed + random.randint(1, 6)

		# Assign first and second based on rolls
		first = p if proll > eroll else e
		second = e if proll > eroll else p

		# If we had a tie, break the tie
		if proll == eroll:
			tiebreak = random.randint(0, 1)
			first = p if tiebreak == 1 else e
			second = e if tiebreak == 1 else p

		# First fighter attacks
		fcrit = random.randint(0, 100) < first.luck
		dmg = 2 * first.attack - second.defense if fcrit else first.attack - second.defense
		print(first.name + (" crits for " + str(dmg) + " damage!" if fcrit else " attacks for " + str(dmg) + " damage."))
		second.health -= dmg
		if second.health <= 0:
			second.health = 0
			break

		# Second fighter attacks
		scrit = random.randint(0, 100) < second.luck
		dmg = 2 * second.attack - first.defense if scrit else second.attack - first.defense
		print(second.name + (" crits for " + str(dmg) + " damage!" if scrit else " attacks for " + str(dmg) + " damage."))
		first.health -= dmg
		if first.health <= 0:
			first.health = 0
			break

		turn += 1

	# Print final health values.
	print(str(p.name) + ": " + str(p.health) + "\n" + str(e.name) + ": " + str(e.health) + "\n")
	print(p.name + " wins!" if p.health > 0 else e.name + " wins!")
	return p.health > 0

player = classes.Fighter(10, 2, 1, 5, 10, "Buton")
enemy = classes.Fighter(10, 1, 1, 5, 50, "Sam")

print()

fight(player, enemy)

print()

def potion(p):
	p.health += 20

pot = classes.Item(potion)

print(player.name + " uses a potion!")
print(player)
pot.use(player)
print(player)
print()

