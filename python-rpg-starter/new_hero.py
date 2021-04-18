import random

class Characters:
    def __init__(self, name, health, power, bounty, armor, evade):
        self.name = name
        self.health = health
        self.power = power
        self.bounty = bounty
        self.armor = armor
        self.evade = evade

    def alive(self):
        if self.health > 0: 
            return True
        else:
            return False


    def attack(self, enemy):
        
        if enemy.name == "zombie": 
            enemy.health += self.power
            

        if enemy.name == "shadow" and random.randint(0,10) < 1:
            enemy.health -= (self.power)
            
        elif enemy.name == "shadow":
            print("no damage")    
        
        elif enemy.name == "medic" and random.randint(0,100) < 20:
            enemy.health -= (self.power * 2)
            print("{} does double damage({}) to {}.".format(self.name, (self.power * 2), enemy.name))
        
        else:
            enemy.health -= self.power
            print("{} does {} damage to {}.".format(self.name, self.power, enemy.name))
        if enemy.health <= 0:
            print("{} killed the {}".format(self.name, enemy.name))
        
        if enemy.health <= 0:
            self.bounty += enemy.bounty
            print("You recieved {} coins".format(enemy.bounty))


    def print_status(self):
        print("The {} has {} health and {} power.".format(self.name, self.health, self.power))

class Shadow(Characters):
    pass

class Medic(Characters):
    
    def recuperateHealth(self):
        if enemy.name == "medic" and random.randint(0,100) < 20:
            enemy.health -= (self.power * 2)
            print("{} does double damage({}) to {}.".format(self.name, (self.power * 2), enemy.name))

class Zombie(Characters):
        
    def print_status(self):
        print("Zombie can not die!")   

class Hero(Characters):
    
    def coins(self):
        coin = self.bounty
        print(f"You have {coin} coins")

    def youAreDead(self):
        if self.health <= 0:
            print("You are dead.")

class Goblin(Characters):
    pass

class Store:
    def __init__(self, name, use):
        self.name = name
        self.use = use
    
    def items(self):
        print()
        print("1. Super Tonic")
        print("2. Armor")
        print("3. Evade")
        print("4. Sword")
        print("5. ssdad")
        print()
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            SuperTonic.addSuperTonic(self)
    
        elif raw_input == "2":
            Armor.addArmor(self)
            
        elif raw_input == "3":
            Evade.addEvade(self)
        
        elif raw_input == "4":
            Sword.addSword(self)
            
        
        elif raw_input == "5":
            pass
            
        
        else:
            print("Invalid input {}".format(raw_input))

class SuperTonic(Store):
    
    def addSuperTonic(self):
        if self.health >= 0:
            self.health += 10
            print("Your health has been restored by 10!")

class Evade(Store):

    def addEvade (self):
        evade = self.evade
        self.evade += 2
        print("You have {} Evade power, {} Armor!".format(self.evade, self.armor))

class Armor(Store):

    def addArmor (self):
        armor = self.armor
        self.armor += 2
        print("You have {} Evade power, {} Armor!".format(self.evade, self.armor))

class Sword(Store):

    def addSword (self):
        sword = self.power
        self.power ++ 2
        print("You are now equiped with a Sword!"))

# class Armor(Store):

#     def addArmor (self):
#         armor = self.armor
#         self.armor += 2
#         print("You have {} Armor!".format(self.armor))


def main():
    hero = Hero("hero",20, 5, 0, 0, 0)
    goblin = Goblin("goblin",12, 2, 4, 0, 0)
    zombie = Zombie("zombie", 1, 1, 3, 0, 0)
    shadow = Shadow("shadow", 6, 1, 4, 0, 0)
    medic = Medic("medic", 7, 2, 8, 0, 0)
    superTonic = SuperTonic("Super Tonic", 10 )
    armor = Armor("Armor", 2)
    # sword = store("Sword", 5)
    # asdsad = store("asdsad", 10)


    enemys = [ goblin, zombie, shadow, medic]
    random.shuffle(enemys)

    for enemy in enemys:


        while hero.alive() and enemy.alive():
            hero.print_status()
            enemy.print_status()
            hero.coins()
            print()
            print("What do you want to do?")
            print("1. fight enemy")
            print("2. do nothing")
            print("3. Store")
            print("4. flee")
            print()
            print("> ", end=' ')
            raw_input = input()
            if raw_input == "1":
                hero.attack(enemy)
                enemy.attack(hero)
            elif raw_input == "2":
                enemy.attack(hero)

            elif raw_input == "3":
                Store.items(hero)

            elif raw_input == "4":
                print("I'm outta here!.")
                break

            else:
                print("Invalid input {}".format(raw_input))


main()


