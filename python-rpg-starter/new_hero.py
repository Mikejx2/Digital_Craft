class Characters:
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    def alive(self):
        if self.health > 0: 
            return True
        else:
            return False

    
# class Zombie(Characters):
    
#     def zombie_Health():
#     if enemy.health <= 0:
#             print("You killed the goblin")



class Hero(Characters):

    def attack(self, enemy):
        enemy.health -= self.power
        print("You did {} damage to the goblin.".format(self.power))
        
        if enemy.health <= 0:
            print("You killed the goblin")
    
    def print_status(self):
        print("You have {} health and {} power.".format(self.health, self.power))
        


class Goblin(Characters):
        
    def goblinAttack(self, enemy):
        enemy.health -= self.power
        print("The goblin does {} damage to you.".format(self.power))
        if enemy.health <= 0:
            print("You are dead.")
            

    def print_status(self):
        print("The goblin has {} health and {} power.".format(self.health, self.power))    
        


def main():
    hero = Hero("hero",10, 5)
    goblin = Goblin("goblin",6, 2)

    while goblin.alive() and hero.alive():
        hero.print_status()
        goblin.print_status()
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do not")
        print("3. flee")
        print("> ", end=' ')
        raw_input = input()
        if raw_input == "1":
            # Hero attacks goblin
            hero.attack(goblin)
        
        elif raw_input == "2":
            goblin.goblinAttack(hero)
        elif raw_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input {}".format(raw_input))

            
main()