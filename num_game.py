import random

comp_choice = random.randint(0,100)
print(comp_choice)
user_choice = None
rounds = 3
guess = 0

while input("Want to play the number guessing game? Enter Y for yes or N for no: ").upper() == "Y":
    guess = 0
    rounds = 3
    while user_choice != comp_choice and guess < rounds:
        user_choice = int(input(f"I am thinking of a number between 1 and 100\n Guess the number: "))
        
        if (user_choice < 0 or user_choice > 100):
            print(f"Invalid entry. Please input a number between 0 and 100")
            continue
        
        guess += 1
        rounds -=1
        
        if user_choice < comp_choice and guess < 3:
            print(f'{user_choice} is too low. You have {rounds} guesses left.')
        elif user_choice > comp_choice and guess < 3:
            print(f'{user_choice} is too high. You have {rounds} guesses left.')
        elif user_choice == comp_choice and guess < 3:
            print(f'Correct! You chose the right number with {rounds} guesses left! YOU WIN!')
        else:
            print(f'You did not guesss the number in the alotted amount of tries, YOU LOSE.')
        

