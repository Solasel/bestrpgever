import random

def fight(p, e):

	while True:

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
		second.h -= 2 * first.a - second.d if fcrit else first.a - second.d
		if second.h <= 0:
			break

		# Second fighter attacks
		scrit = random.randint(0, 100) < second.l
		first.h -= 2 * second.a - first.d if scrit else second.a - first.d
		if first.h <= 0:
			break

	return p.h > 0

