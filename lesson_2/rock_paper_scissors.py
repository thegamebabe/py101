from random import choice 

VALID_CHOICES = ['rock', 'paper', 'scissors']

def display_winner(player, computer):
    print(f'Player: {player_choice}  ---  Computer: {computer_choice}')

    if ((player == "rock" and computer == "scissors") or
        (player == "paper" and computer == "rock") or
        (player == "scissors" and computer == "paper")):
        print("You win!")
    elif ((player == "rock" and computer == "paper") or
          (player == "paper" and computer == "scissors") or
          (player == "scissors" and computer == "rock")):
        print("Computer wins!")
    else:
        print("It's a tie!")

while True:
    player_choice = input(f'{", ".join(VALID_CHOICES)}? ')
    while player_choice.lower() not in VALID_CHOICES:
        player_choice = input(f'Please choose from {", ".join(VALID_CHOICES)}: ')
    
    computer_choice = choice(VALID_CHOICES)
    
    display_winner(player_choice, computer_choice)
    
    while True:
        play_again = input("Would you like to play again? (y/n) ").lower()
        if play_again in ('y', 'n'):
        # if answer.startswith('n') or answer.startswith('y'):
            break
    if play_again == 'n':
        break


    #test comment