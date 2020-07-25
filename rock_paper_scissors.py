# this is rock, paper, scissors game

from random import choice

player = input('Choose one of theese: rock (R) or paper (P) or scissors (S): ');
if player[0] == 'R' or player[0] == 'r':
  player = 'rock'
elif player[0] == 'P' or player[0] == 'p':
  player = 'paper'
elif player[0] == 'S' or player[0] == 's':
  player = 'scissors'
else:
  print('You ddin\'t choose any right option')

computer = choice(['rock', 'paper', 'scissors'])

print('\n Player choice: ' + player)
print(' Computer choice: ' + computer)
if computer == 'rock' and player == 'paper':
  print('You won this battle.')
elif computer == 'paper' and player == 'rock':
  print('Computer won this game.')
elif computer == 'paper' and player == 'scissors':
  print('You won this battle.')
elif computer == 'scissors' and player == 'paper':
  print('Computer won this game.')
elif computer == 'scissors' and player == 'rock':
  print('You won this battle.')
elif computer == 'rock' and player == 'scissors':
  print('Computer won this game.')
else:
  print('\nThis was a draw.\n')

