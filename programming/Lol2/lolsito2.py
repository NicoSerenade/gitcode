import random
import sqlite3
import sys

MAP1 = 'China'
MAP2 = 'Tibet'

DRAGON1 = ['Mountain Dragon', 200]
DRAGON2 = ['Ancient Dragon', 400]

CHAMP1 = 'Nasus'
CHAMP2 = 'Zed'
CHAMP3 = 'Azir'

WARRIOR_ABILITY = 2 # / el armor for create the result of the shield and spines
WARRIOR_A_ENERGY = 1

ASSASSIN_ABILITY = 20 # * el ad
ASSASSIN_A_ENERGY = 10

WIZARD_ABILITY = 2 # * el ap
WIZARD_A_MANA = 2

#sqlite3
class Database():

    def __init__(self, db_name):
        self.name = db_name
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def create_table(self):
        self.cursor.execute('''
    CREATE TABLE IF NOT EXISTS lol_table (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE,
        wins INTEGER,
        losses INTEGER,
        winrate REAL GENERATED ALWAYS AS (
            CASE
                WHEN (wins + losses) > 0 THEN (CAST(wins AS REAL) / (wins + losses)) * 100
                ELSE 0
            END
            ) VIRTUAL
        )
    ''')
        self.conn.commit()

    def check_name_table(self, name):
        self.cursor.execute('SELECT name FROM lol_table WHERE name = ?', (name,))
        user = self.cursor.fetchone()
        return user is None

    def add_user(self, name):
        try:
            self.cursor.execute('INSERT INTO lol_table (name, wins, losses) VALUES (?, 0, 0)', (name,))
            self.conn.commit()
            if self.name == 'lol_users.db':
                print(f'Summoner {name} has been registered successfully')

        except sqlite3.IntegrityError:
            if self.name == 'lol_users.db':
                print(f'Welcome again summoner {name}')

    def add_win(self, name):
        self.cursor.execute('UPDATE lol_table SET wins = wins + 1 WHERE name = ?', (name,))
        self.conn.commit()

    def add_lose(self, name):
        self.cursor.execute('UPDATE lol_table SET losses = losses + 1 WHERE name = ?', (name,))
        self.conn.commit()

    def print_fame_hall(self):
        self.cursor.execute('SELECT name, winrate FROM lol_table ORDER BY winrate DESC LIMIT 3')
        self.fame_hall = self.cursor.fetchall() # [(name, winrate), (name, winrate)]
        if self.fame_hall:
            for i, (name, winrate) in enumerate(self.fame_hall):
                print(f'Rank: {i + 1}. {name}, winrate: %{winrate}')
        else:
            if self.name == 'lol_users.db':
                print('There are no summoners registered yet')

            elif self.name == 'lol_champs.db':
                print('There are no champions in the system')

    def __del__(self):
        self.conn.close()

users_db = Database('lol_users.db')
champs_db = Database('lol_champs.db')
# python


class Player():
    def __init__(self, name, champ):
        self.name = name
        self.champ = champ

    @staticmethod
    def registration():
        print('Welcome summoner 1!')
        choice1 = input('Press... \n(r) for registration or sing in or, \n(ENTER) for play as a guest: ')
        if choice1 == 'r':
            name1 = input("Please enter your summoners name: ").title()
            users_db.add_user(name1)
        else:
            name1 = 'guest1'
            
        
        print('Welcome summoner 2!')
        choice2 = input('Press... \n(r) for registration or sing in or, \n(ENTER) for play as a guest: ')
        if choice2 == 'r':
            name2 = input("Please enter your summoners name: ").title()
            users_db.add_user(name2)
        else:
            name2 = 'guest2'
            
        
        return name1, name2

    @staticmethod
    def choose_fame_hall():
        while True:
            choice = input('Press... \n(f) to see the hall of fame, \n(w) to see the champs winrate or, \n(ENTER) to skip: ').lower()
            if choice == 'f': 
                users_db.print_fame_hall()
            elif choice == 'w': 
                champs_db.print_fame_hall()
            else:
                break

    @staticmethod
    def get_map(name1, name2):
        while True:
            choice1 = input(f'{name1}, Enter your desired map \nPress... \n(1) for select map: {MAP1}, or \n(2) for select map: {MAP2}: ')
            if not choice1 in ['1', '2']:
                print('Invalid choice')
            else:
                while True:
                    choice2 = input(f'{name2}, Enter your desired map \nPress... \n(1) for select map: {MAP1}, or \n(2) for select map: {MAP2}: ')
                    if not choice2 in ['1', '2']:
                        print('Invalid choice')
                    else:          
                        choice = random.choice([choice1, choice2])
                        Game.welcome_map(choice)
                        if choice == '1':
                            game = Game(MAP1)
                        elif choice == '2':
                            game = Game(MAP2)

                        return game, game.set_dragon() 

    def get_champs(name1, name2):

        champs_template = { # lambda makes a blueprint of the object, but do not create it, each time I reference lambda, is going to create an unique object.
        '1': lambda: Warrior('warrior', CHAMP1, 1500, 20, 40, 10), # armor ad energy 
        '2': lambda: Assassin('assassin', CHAMP2, 500, 5, 30, 10),
        '3': lambda: Wizard('wizard', CHAMP3, 600, 2, 5, 100, 20) # armor ad ap mana
        }


        print(f'Available champions: \n1. {CHAMP1} \n2. {CHAMP2} \n3. {CHAMP3}')
        while True:
            choice1 = input(f'{name1}, select the number of your champ: ')
            if not choice1 in ['1', '2', '3']:
                print('Invalid choice')
            else:
                print(f'Available champions: \n1. {CHAMP1} \n2. {CHAMP2} \n3. {CHAMP3}')
                while True:
                    choice2 = input(f'{name2}, select the number of your champ: ')
                    if not choice2 in ['1', '2', '3']:
                        print('Invalid choice')
                    else:
                        champ1 = champs_template[choice1]() #the () tells lambda to crate a new object
                        champ2 = champs_template[choice2]()
                        return champ1, champ2

class Sleepy_dragon():
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def wake_up(self):
        self.awaken = random.randint(1, 50)
        if self.awaken == 1:
            print(f'{self.name} has been awaken!')
        return self.awaken == 1
    
    def attack(self, player1, player2):
        target = random.choice([player1, player2])
        not_target = player1 if target == player2.champ else player2
        target.champ.health -= self.damage
        if target.champ.is_alive():
            print(f'{self.name} has attacked {target.champ.name} by {self.damage} of damage for being noisy')
            print(f'{target.champ.name} has {target.champ.health} of health left')
        else:
            print(f'{self.name} has killed {target.champ.name} for being noisy')
        return target.is_alive(), not_target, target

class Champion():
    def __init__(self, type, name, health, armor, ad):
        self.type = type
        self.name = name
        self.health = health
        self.armor = armor
        self.ad = ad
    
    def attack(self, target):
        reduction = round(self.ad * (target.armor / 100))
        damage = self.ad - reduction
        target.health -= damage
        print(f'{self.name} has attacked {target.name} by {damage} of damage')
    
    def is_alive(self):
        return self.health > 0
    
class Human(Champion):
    def __init__(self, type, name, health, armor, ad, energy):
        super().__init__(type, name, health, armor, ad,)
        self.energy = energy
        
    def add_energy(self):
        self.energy += 1
    
class God(Champion):
    def __init__(self, type, name, health, armor, ad, ap, mana):
        super().__init__(type, name, health,armor, ad)
        self.ap = ap
        self.mana = mana

    def add_mana(self):
        self.mana += 1
    
class Warrior(Human):
    def __init__(self, type, name, health, armor, ad, energy):
        super().__init__(type, name, health, armor, ad, energy)
        self.warrior_defense = False
        
    def ability(self, target):
        if self.energy >= WARRIOR_A_ENERGY:
            self.warrior_defense = True
            self.spines_shield = round(self.armor / WARRIOR_ABILITY)
            self.energy -= WARRIOR_A_ENERGY
            print(f'{self.name} has put the shield on')
        else:
            print(f'{self.name} have not enough energy to cast the ability')

class Assassin(Human):
    def ability(self, target):
        if self.energy >= ASSASSIN_A_ENERGY:
            reduction = round((self.ad * ASSASSIN_ABILITY) * (target.armor / 100))
            damage = (self.ad * ASSASSIN_ABILITY) - reduction
            target.health -= damage
            self.energy -= ASSASSIN_A_ENERGY
            print(f'{self.name} has attacked {target.name} by {damage} of damage')
            if isinstance(target, Warrior) and target.warrior_defense:
                spines_damage = round((self.ad * ASSASSIN_ABILITY) * (target.spines_shield / 100))
                self.health -= spines_damage
                print(f'{self.name} got {spines_damage} of damage by {target.name} spines shield') 
        else:
            print(f'{self.name} have not enough energy to cast the ability')

class Wizard(God):
    def ability(self, target):
        if self.mana >= WIZARD_A_MANA:
            damage = self.ap * WIZARD_ABILITY
            target.health -= damage
            self.mana -= WIZARD_A_MANA
            print(f'{self.name} has attacked {target.name} by {damage} of magical damage')

        else:
            print(f'{self.name} have not enough mana to cast the ability')

class Game():

    def __init__(self, map):
        self.map = map
    
    def welcome_map(map_num):
        if map_num == '1':
            print(f'Welcome to {MAP1}')
            print(f'The {DRAGON1[0]} is currently sleeping')
        elif map_num == '2':
            print(f'Welcome to {MAP2}')
            print(f'The {DRAGON2[0]} is currently sleeping')

    def set_dragon(self):
        if self.map == MAP1:
            dragon = Sleepy_dragon(*DRAGON1)
        elif self.map == MAP2:
            dragon = Sleepy_dragon(*DRAGON2)
        return dragon

    def start_game(self, player1, player2, dragon):
        while player1.champ.is_alive() and player2.champ.is_alive():
            player1.champ.attack(player2.champ)
            if player2.champ.is_alive():
                player2.champ.attack(player1.champ)
                if not player1.champ.is_alive():
                    print(f'{player1.champ.name} got kill by {player2.champ.name}')
                    return player2, player1
            else:
                print(f'{player2.champ.name} got kill by {player1.champ.name}')
                return player1, player2

            player1.champ.ability(player2.champ)
            if player2.champ.is_alive() and player1.champ.is_alive():
                player2.champ.ability(player1.champ)
                if not player1.champ.is_alive():
                    print(f'{player1.champ.name} got kill by {player2.champ.name}')
                    return player2, player1
                
                elif not player2.champ.is_alive():
                    print(f'{player2.champ.name} got kill by {player1.champ.name} spines shield')
                    return player1, player2

            elif not player1.champ.is_alive():
                    print(f'{player1.champ.name} got kill by {player2.champ.name} spines shield')
                    return player2, player1
            else:
                print(f'{player2.champ.name} got kill by {player1.champ.name}')
                return player1, player2

            print(f'{player1.champ.name} has {player1.champ.health} of health left')
            print(f'{player2.champ.name} has {player2.champ.health} of health left')

            player1.champ.add_energy() if isinstance(player1.champ, Human) else player1.champ.add_mana()
            player2.champ.add_energy() if isinstance(player2.champ, Human) else player2.champ.add_mana()

            if dragon.wake_up():
                target_alive, not_target, target = dragon.attack(player1, player2)
                if not target_alive:
                    return not_target, target
    
    def final_message(self, winner, loser):
        print(f'Summoner {loser.name} and his invocation {loser.champ.name} has been defeated by the great summoner {winner.name} and his invocation {winner.champ.name} with {winner.champ.health} of health left in {self.map}')

    def final_menu():
        choice = input('Press... \n(q) to quit or, \n(ENTER) to play again: ')
        if choice == 'q': 
            sys.exit()

def main():
    while True:
        users_db.create_table()
        champs_db.create_table()

        Player.choose_fame_hall()
        name_player1, name_player2 = Player.registration()
        game, dragon = Player.get_map(name_player1, name_player2)
        champ_player1, champ_player2 = Player.get_champs(name_player1, name_player2)

        player1 = Player(name_player1, champ_player1)
        player2 = Player(name_player2, champ_player2)

        winner_player, loser_player = game.start_game(player1, player2, dragon)

        game.final_message(winner_player, loser_player)

        if not winner_player.name in ['guest1', 'guest2'] and not loser_player.name in ['guest1', 'guest2']:
            users_db.add_win(winner_player.name)
            users_db.add_lose(loser_player.name)

            champs_db.add_user(winner_player.champ.name)
            champs_db.add_user(loser_player.champ.name)

            champs_db.add_win(winner_player.champ.name)
            champs_db.add_lose(loser_player.champ.name)

        Game.final_menu()

if __name__ == '__main__':
    main()

