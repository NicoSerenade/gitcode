import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

print('')
player = int(input('Enter...\n1 for rock,\n2 for paper, or\n3 for scissors:\n\n'))
if player < 1 or player > 3: sys.exit('you must enter 1, 2 or 3.')
print('')
python = random.choice('123')
python = int(python)
print(f'You chose {str(RPS(player)).replace('RPS.', '')}.\n')
print(f'Python chose {str(RPS(python)).replace('RPS.', '')}.\n')
if player == 1 and python == 3: print('🥳 You win!')
elif player == 2 and python == 1: print('🥳 You win!')
elif player == 3 and python == 2: print('🥳 You win!')
elif player == python: print('🐢 Tie game!')
else: print('🐍 Python wins!')
print('')