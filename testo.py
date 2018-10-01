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

player = Player(10, 10, 2, 10, 1, 'Will')
monster = Enemy(10, 10, 2, 10, 1, 'Burton')
print(player)

def textBox(text):
    for i in text:
        print(i, end='')
        time.sleep(.01)
    print()

def fight(p, e):
    battle = 1 #Determines whether or not
    firstTurn = 1 #Is it the first turn of the battle?
    attack = None
    while battle == 1:
        print()
        dice = random.randint(1,6) #Dice roll that determines speed
        speedEnemy = dice + e.s
        dice = random.randint(1,6)
        speedPlayer = dice + p.s
        if speedEnemy > speedPlayer: #Enemy outspeeds
            turn = 0
        elif speedEnemy < speedPlayer: #Player outspeeds
            turn = 1
        elif speedEnemy == speedPlayer: #If both characters tie...
            speedtie = random.randint(0,1)
            if speedtie == 0: #Enemy goes first
                turn = 0
            else:
                turn = 1 #Player goes first
        if firstTurn == 1:
            if turn == 0:
                textBox('You were ambushed by the %s!' % (e.n))
                firstTurn = 0
            if turn == 1:
                textBox('You encounter a %s!' % (e.n))
                firstTurn = 0
        #textBox('What do you do?')
        #action = input()
        if turn == 0: #Enemy goes first
                attack = e.a
                crit = random.randint(1,10)
                if crit <= e.l:
                    attack = p.a * 2
                    textBox('CRITICAL HIT!')
                damage = attack - p.d
                p.h -= damage
                textBox('The enemy %s did %s damage!' % (e.n, damage))
                if p.h <= 0: #Calculates if player dead
                    battle = 0
                    textBox('You lose.')
                    textBox('The home you worked so hard to defend has fallen.')
                    textBox(':(')
                    break
                crit = random.randint(1,10)
                attack = p.a
                if crit <= p.l:
                        attack = p.a * 2
                        textBox('CRITICAL HIT!')
                damage = attack - e.d
                p.h -= damage
                textBox('You punch for %s damage.' % (damage))
                if e.h <= 0: #Calculates if enemy dead
                    battle = 0
                    textBox('You win!!!!!!')
                    break
        if turn == 1: #Player attacks first
                attack = p.a
                crit = random.randint(1,10)
                if crit <= p.l:
                    attack *= 2
                    textBox('CRITICAL HIT!')
                damage = attack - e.d
                e.h -= damage
                textBox('You punch for %s damage.' % (damage))
                if e.h <= 0: #Calculates if enemy dead
                    battle = 0
                    textBox('You win!!!!!!')
                    break
                crit = random.randint(1,10)
                attack = e.a
                if crit <= e.l:
                        attack = e.a * 2
                        textBox('CRITICAL HIT!')
                damage = attack - p.d
                p.h -= damage
                textBox('The enemy %s did %s damage!' % (e.n, damage))
                if p.h <= 0: #Calculates if player dead
                    battle = 0
                    textBox('You lose.')
                    textBox('The home you worked so hard to defend has fallen.')
                    textBox(':(')
                    break
                    
        
        
        
        
        
        
    
    
fight(player, monster)
