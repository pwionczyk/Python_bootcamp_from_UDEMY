from random import randint

target = randint(1,128)

answer = 0
times = 0

while answer != target:
	answer = int(input('Find a correct number from 1 to 128. Take a guess: '))
	if answer > target:
		print('That\'s too much! Try again.')
	elif answer < target:
		print('That\'s too little! Try again.')
	times += 1

print(f'Congratulation. You guessed after try for {times} times.')