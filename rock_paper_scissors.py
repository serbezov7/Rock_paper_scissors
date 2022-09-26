import random

rock = 'Rock'
scissors = 'Scissors'
paper = 'Paper'

player_choice = input("Please choose 'r' for rock, 's' for scissors and 'p' for paper: ").lower()

if player_choice == 'r':
    player_choice = rock
elif player_choice == 's':
    player_choice = scissors
elif player_choice == 'p':
    player_choice = paper
else:
    print('Invalid choice ! \nPlease try again !')
    exit()

computer_choice = random.randint(1, 3)

if computer_choice == 1:
    computer_choice = rock
elif computer_choice == 2:
    computer_choice = scissors
elif computer_choice == 3:
    computer_choice = paper
print(f'Computer\'s choose : {computer_choice}')

if player_choice == rock and computer_choice == scissors or \
        player_choice == scissors and computer_choice == paper or \
        player_choice == paper and computer_choice == rock:
    print('You win !')
elif player_choice == computer_choice:
    print('Draw ! \nChoose again !')
else:
    print('You lose ! \nTry again')
