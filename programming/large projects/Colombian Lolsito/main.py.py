'''To do list:
custom dragon names and phrases
balance stats of champs, maps, dragons'''
import random 
import sqlite3
import sys

CHAMP1 = ("Sicco",100,0,500,0,5) #name, ad, ap, health, armor, skill (x5 damage)
CHAMP2 = ("Nico",80,0,1000,50,2) #skill x2 damage
CHAMP3 = ("Santi",50,200,200,0,2) #skill health points.

DRAGON1 = ("George of the jungle", 2) # duplicates de target health
DRAGON2 = ("Séneca",500)

MAP1 = ("Catatumbo", 500)
MAP2 = ("Uniandes", 100)

class Champ():
    def __init__(self, name, ad, ap, health, armor, skill):
        self.name = name
        self.ad = ad
        self.ap = ap
        self.health = health
        self.armor = armor
        self.skill = skill

    def attack(self, target):
        raw_damage = self.ad
        target_armor_reduction = (raw_damage / 100) * target.armor
        net_damage = raw_damage - target_armor_reduction
        target.health -= net_damage
        if target.is_alive():
            print(f"\n{self.name} has attaacked {target.name} by {net_damage} of damage")
            print(f"{target.name} has {target.health} of health left")
        else:
            print(f"\n{self.name} has defeated {target.name}")
            print(f"{target.name} has {target.health} of health left")
        return target.is_alive()

    def is_alive(self):
        return self.health > 0
    
class champ1(Champ):
    def __init__(self, name, ad, ap, health, armor, skill):
        super().__init__(name, ad, ap, health, armor, skill)
    
    def ability(self, target):
        raw_damage = self.ad * self.skill
        target_armor_reduction = (raw_damage / 100) * target.armor
        net_damage = raw_damage - target_armor_reduction
        target.health -= net_damage
        if target.is_alive():
            print(f"\n{self.name} has awaken {target.name} at 3:00AM hurting him by {net_damage}")
            print(f"{target.name} has {target.health} of health left")
            return target.is_alive()
        else:
            print(f"{self.name} has defeated {target.name}")
            print(f"{target.name} has {target.health} of health left")
            return target.is_alive()
    
class champ2(Champ):
    def __init__(self, name, ad, ap, health, armor, skill):
        super().__init__(name, ad, ap, health, armor, skill)
    
    def ability(self, target):
        raw_damage = self.ad * self.skill
        target_armor_reduction = (raw_damage / 100) * target.armor
        net_damage = raw_damage - target_armor_reduction
        target.health -= net_damage
        if target.is_alive():
            print(f"\n{self.name} has thrown a guitar on {target.name}'s head, hurting him by {net_damage}")
            print(f"{target.name} has {target.health} of health left")
            return target.is_alive()
        else:
            print(f"\n{self.name} has defeated {target.name}")
            print(f"{target.name} has {target.health} of health left")
            return target.is_alive()

class champ3(Champ):
    def __init__(self, name, ad, ap, health, armor, skill):
        super().__init__(name, ad, ap, health, armor, skill)
    
    def ability(self, target):
        raw_health = self.ap * self.skill
        net_health = raw_health
        self.health += net_health
        print(f"\n{self.name} has cured himself by {net_health} using the power of friendship")
        print(f"{self.name} has {self.health} of health left")
        return target.is_alive()

class Dragon():
    def __init__(self, name, ap):
        self.name = name
        self.ap = ap

    def wake_up():
        dragon_awaken = random.randint(1,4)
        return dragon_awaken == 1
              
class dragon1(Dragon):
    def __init__(self, name, ap):
        super().__init__(name, ap)

    def attack(self, champ_player1, champ_player2, dragon_state):
        if dragon_state:
            print(f"\n{self.name} has been awaken!")
            target = random.choice([champ_player1,champ_player2])
            healing = self.ap * target.health
            target.health += healing
            print(f"{self.name} has healed {target.name} by {healing} with an ancestral sopita de pescado!")
            print(f"{target.name} has {target.health} of health left")
            return target.is_alive()
        else:
            return True # means target is alive

class dragon2(Dragon):
    def __init__(self, name, ap):
        super().__init__(name, ap)

    def attack(self, champ_player1, champ_player2, dragon_state):
        if dragon_state:
            print(f"\n{self.name} has been awaken!")
            target = random.choice([champ_player1,champ_player2])
            target.health -= self.ap
            if target.is_alive():
                print(f"{self.name} has canceled out {target.name}'s semester, hurting him by {self.ap} of damage!")
                print(f"{target.name} has {target.health} of health left")
                return target.is_alive()
            else:
                print(f"{self.name} has banned {target.name} at Uniandes, defeating him!")
                return target.is_alive()
        else: 
            return True

class Map():
    def __init__(self, name, ap):
        self.name = name
        self.ap = ap

    def wake_up():
        map_awaken = random.randint(1,2)
        if map_awaken == 1:
            return map_awaken == 1

class map1(Map):
    def __init__(self, name, ap):
        super().__init__(name, ap)

    def attack(self, champ_player1, champ_player2, map_state):
        if map_state:
            target = random.choice([champ_player1,champ_player2])
            target.health -= self.ap
            if target.is_alive():
                print(f"\nLas Farc has attacked {target.name}, by {self.ap} of damage for getting too deep into the {MAP1[0]}!")
                print(f"{target.name} has {target.health} of health left")
                return target.is_alive()
            else:
                print(f"\nLas Farc has defeated {target.name} for getting to deep into the {MAP1[0]}!")
                return target.is_alive()
        else:
            return True # means target is alive

class map2(Map):
    def __init__(self, name, ap):
        super().__init__(name, ap)

    def attack(self, champ_player1, champ_player2, map_state):
        if map_state:
            target = random.choice([champ_player1,champ_player2])
            target.health -= self.ap
            if target.is_alive():
                print(f"\n{target.name} got a cramp in the ML and fell down the stairs, getting {self.ap} of damage!")
                print(f"{target.name} has {target.health} of health left")
                return target.is_alive()
            else:
                print(f"\n{target.name} got a cramp in the ML, fell down the stairs and died!")
                return target.is_alive()
            
        else: 
            return True # means target is alive

class Player():
    def __init__(self, name, champ):
        self.name = name
        self.champ = champ

    def registration():
        print("Welcome summoner 1!")
        name_player1 = input("Enter your name: ").title()
        print()
        print("Welcome summoner 2!")
        name_player2 = input("Enter your name: ").title()
        return name_player1, name_player2
    
    def get_map(name_player1, name_player2):
        maps = {"1": map1(*MAP1), "2": map2(*MAP2)}
        while True:
            print("\nChoose your desired map\n")
            desired_map1 = input(f"{name_player1} enter (1) {MAP1[0]} or (2) for {MAP2[0]}: ")
            if desired_map1 in ["1", "2"]:
                break
            else:
                print("invalid choice")
        while True:
            desired_map2 = input(f"{name_player2} enter (1) for {MAP1[0]} or (2) for {MAP2[0]}: \n")
            if desired_map2 in ["1", "2"]:
                chosen_map = random.choice([maps[desired_map1],maps[desired_map2]])
                print(f"Welcome to {chosen_map.name}!")

                if chosen_map is maps["1"]:
                    dragon = dragon1(*DRAGON1)
                    print(f"{dragon.name} is currently sleeping")
                    return chosen_map, dragon
                
                elif chosen_map is maps["2"]:
                    dragon = dragon2(*DRAGON2)
                    print(f"{dragon.name} is currently sleeping")
                    return chosen_map, dragon
            else:
                print("invalid choice")
            
    def get_champ(name_player1, name_player2): #stats of champs
        champions = {"1": champ1(*CHAMP1), "2": champ2(*CHAMP2), "3": champ3(*CHAMP3)}
        while True:
            print(f"\nchoose your champ \n")
            print(f"Champions list: \n{CHAMP1[0]} (1) \n{CHAMP2[0]} (2) \n{CHAMP3[0]} (3)")
            number_champ_player1 = input(f"\n{name_player1}, enter your champion's number: ")
            if number_champ_player1 in ["1","2","3"]:
                break
            else:
                 print("invalid choice")

        while True:
            number_champ_player2 = input(f"{name_player2}, enter your champion's number: ")
            if number_champ_player2 in ["1","2","3"]:
                break
            else:
                print("invalid choice")

        return champions[number_champ_player1], champions[number_champ_player2]

def start_game (player1, player2, chosen_map, dragon):
    while player1.champ.is_alive() and player2.champ.is_alive():
        map_state = Map.wake_up()
        dragon_state = Dragon.wake_up()
        target_alive = player1.champ.attack(player2.champ)
        if target_alive:
            target_alive = player2.champ.attack(player1.champ)
            if target_alive:
                target_alive = player1.champ.ability(player2.champ)
                if target_alive:
                    target_alive = player2.champ.ability(player1.champ)
                    if target_alive:
                        target_alive = chosen_map.attack(player1.champ,player2.champ, map_state)
                        if target_alive:
                            target_alive = dragon.attack(player1.champ,player2.champ,dragon_state)
                        else:
                            break
                    else:
                        break
                else:
                    break
            else:
                break
        else:
            break

    if player1.champ.is_alive():
        winner = player1.name
        loser = player2.name
        print(f"\n{player2.name} and his invocation {player2.champ.name} has been defeated by the great sumoner {player1.name} and his invocation {player1.champ.name} with {player1.champ.health} of health left at {chosen_map.name}!")
    
    else:
        winner = player2.name
        loser = player1.name
        print(f"{player1.name} and his invocation {player1.champ.name} has been defeated by the great summoner {player2.name} and his invocation {player2.champ.name} with {player2.champ.health} of health left at {chosen_map.name}!")
    return winner, loser

def final_menu(winner, loser):
    print(f"\n{winner} is the winner and {loser} is the loser")
    print(f"{winner} and {loser}, would you like to play again?")
    while True:
        play_again = input(f"\nEnter (y) for yes or (n) for no: ")
        if play_again in ["y", "n"]:
            return play_again == "y"
        else:
            print("Invalid choice")

def main():
    while True:
        name_player1, name_player2 = Player.registration()
        chosen_map, dragon = Player.get_map(name_player1, name_player2)
        champ_player1, champ_player2 = Player.get_champ(name_player1, name_player2)
        player1 = Player(name_player1, champ_player1)
        player2 = Player(name_player2, champ_player2)
        winner, loser = start_game(player1, player2, chosen_map, dragon)
        play_again = final_menu(winner, loser)
        if play_again:
            None
        else:
            sys.exit("GoodBye!")
main()


