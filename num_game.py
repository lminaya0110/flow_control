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
        

        
        


'''
biggest_num = 100
num_to_guess = 45
num_found = False
num_guesses = 0
max_num_guesses = 5

while input( "Wanna play the number guessing game? (y or n) ==> ").upper() == "Y":
        while( not num_found and num_guesses < max_num_guesses ):

            my_guess = int( input(f"Enter a number between 1 and {biggest_num} ==> ") )

            if not( 0 < my_guess < biggest_num ):
               print(f"{my_guess} is an invalid entry... try again\n")
               continue

            num_guesses += 1
            if num_found :=  my_guess == num_to_guess :
                print(f'You found the number {num_to_guess}! '
                      f'And it took you {num_guesses} guesses to find it')
            else:

                print(f"{my_guess} is too {('high' if my_guess > num_to_guess else 'low')}")
                num_left = "no" if max_num_guesses == num_guesses \
                    else (max_num_guesses - num_guesses)
                print(f'You have {num_left} guesses left.\n')
'''
