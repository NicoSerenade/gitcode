import random

def roll():
    min_num = 1
    max_num = 6
    roll = random.randint(min_num, max_num)

    return roll
print('Welcome to Dado Loco!')
while True:
    players_number = input('\nSelect the number of players (2-4): ')
    if players_number.isdigit():
        players_number = int(players_number)
        if 2 <= players_number <= 4:
            break
        else: print('\nIt must be between (2-4)')
    else: print('\nIt must be a number')

max_score = 20
player_scores = [0 for x in range(players_number)]

while max(player_scores) < max_score:
    for x in range(players_number):
        current_score = 0
        print(f'Player number {x + 1}, turn has just started')
        print(f'This is the score: {player_scores}')
        

        while True:
            should_roll = input('Do you wanna roll? Enter (y/n): ')
            if should_roll.lower() == 'y':
                value = roll()
                if value == 1:
                    current_score = 0
                    print('You rolled a 1, turn done!')
                    break

                current_score += value 
                print(f'You rolled a {value}\nYour current score is {current_score}')

            elif should_roll.lower() == 'n':
                print('You are a coward🐔')
                break

            else:
                print('Please enter (y/n)')
        player_scores[x] += current_score

print(f'This is the final score: {player_scores}')
winners = [winner + 1 for winner, y in enumerate(player_scores) if y >= max_score]
if len(winners) == 1:
    print(f'Player number {winners[0]} is the winner!')
else:
    print(f"We have a draw between players number: {', '.join(map(str, winners))}.") #map allows to apply a function individually for x in interate

# This is other way to do the map roll
    # winners_str = []
    # for x in (winners):
    #     winners_str.append(str(x))
    #     print(f'We have a draw between players number {', '.join(winners_str)}.')
