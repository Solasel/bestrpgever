import random, time

class Enemy:
    def __init__(self, health, attack, defense, speed, luck, name):
        self.hp = health
        self.atk = attack
        self.defense = defense
        self.spd = speed
        self.lck = luck
        self.name = name

    def __str__(self):
        return self.name + ": Health = " + str(self.hp) + " Attack = " + str(self.atk) + " Defense = " + str(self.defense) +  " Speed = " + str(self.spd) + " Luck = " + str(self.lck)

class Player:
    def __init__(self, health, attack, defense, speed, luck, name):
        self.hp = health
        self.atk = attack
        self.defense = defense
        self.spd = speed
        self.lck = luck
        self.name = name

    def __str__(self):
        return self.name + ":\n\tHealth = " + str(self.hp) + "\n\tAttack = " + str(self.atk) + "\n\tDefense = " + str(self.defense) +  "\n\tSpeed = " + str(self.spd) + "\n\tLuck = " + str(self.lck)

class Place:
    def __init___(self, n, d, t):
        self.name = n
        self.desc = d
        self.type = t

    def __str__(self):
        return "You have arrived to the amazing" + self.name + ". This is the description:" + self.desc
    
placeareaplace = Place(1, 2)
print(placeareaplace)
    
player = Player(10, 10, 2, 10, 1, 'Will')
monster = Enemy(10, 10, 2, 10, 1, 'Burton')
print(player)


def textBox(text):
    for i in text:
        print(i, end='')
        time.sleep(.01)
    print()

def fight(p, e):
    #Determines if battle is going
    #Is it the first turn of the battle?
    firstTurn = 1 
    attack = None
    while True:
        print()
        #Dice roll that determines speed
        speedEnemy = random.randint(1,6) + e.spd
        speedPlayer = random.randint(1,6) + p.spd
        #Enemy outspeeds
        if speedEnemy > speedPlayer: 
            turn = 0
        #Player outspeeds
        elif speedEnemy < speedPlayer: 
            turn = 1
        #If both characters tie...
        elif speedEnemy == speedPlayer: 
            speedtie = random.randint(0,1)
            #Enemy goes first
            if speedtie == 0: 
                turn = 0
            else:
                #Player goes first
                turn = 1 
        if firstTurn == 1:
            if turn == 0:
                textBox('You were ambushed by the %s!' % (e.name))
                firstTurn = 0
            if turn == 1:
                textBox('You encounter a %s!' % (e.name))
                firstTurn = 0
        #textBox('What do you do?')
        #action = input()
        if turn == 0: #Enemy goes first
                attack = e.atk
                crit = random.randint(1,10)
                if crit <= e.lck:
                    attack = p.atk * 2
                    textBox('CRITICAL HIT!')
                damage = attack - p.defense
                p.hp -= damage
                textBox('The enemy %s did %s damage!' % (e.name, damage))
                if p.hp <= 0: #Calculates if player dead
                    
                    textBox('You lose.')
                    textBox('The home you worked so hard to defend has fallen.')
                    textBox(':(')
                    break
                crit = random.randint(1,10)
                attack = p.atk
                if crit <= p.lck:
                        attack = p.atk * 2
                        textBox('CRITICAL HIT!')
                damage = attack - e.defense
                p.hp -= damage
                textBox('You punch for %s damage.' % (damage))
                if e.hp <= 0: #Calculates if enemy dead
                    
                    textBox('You win!!!!!!')
                    break
        if turn == 1: #Player attacks first
                attack = p.atk
                crit = random.randint(1,10)
                if crit <= p.lck:
                    attack *= 2
                    textBox('CRITICAL HIT!')
                damage = attack - e.defense
                e.hp -= damage
                textBox('You punch for %s damage.' % (damage))
                if e.hp <= 0: #Calculates if enemy dead
                    
                    textBox('You win!!!!!!')
                    break
                crit = random.randint(1,10)
                attack = e.atk
                if crit <= e.lck:
                        attack = e.atk * 2
                        textBox('CRITICAL HIT!')
                damage = attack - p.defense
                p.hp -= damage
                textBox('The enemy %s did %s damage!' % (e.name, damage))
                if p.hp <= 0: #Calculates if player dead
                    
                    textBox('You lose.')
                    textBox('The home you worked so hard to defend has fallen.')
                    textBox(':(')
                    break
                    
        
        
        
        
        
        
    
    
fight(player, monster)
