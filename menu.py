'''
Part 2: Code a simple menu
Write a program that displays a menu for C (create), R (read), U(update),
D(delete) or Q(quit). The output should resemble:
Enter:
C to create,
R to read,
U to update,
D to delete or
Q to quit ==> c
Calling CREATE routine..…
Enter:
C to create,
R to read,
U to update,
D to delete or
Q to quit ==> t
Your entry T is invalid - try again
Enter:
C to create,
R to read,
U to update,
D to delete or
Q to quit ==> r
Calling READ routine..…
Enter:
C to create,
R to read,
U to update,
D to delete or
Q to quit ==> q
Exiting program
'''

user_choice = input( 'Enter: \n\tC to create, \n\tR to read, \n\tU to update, \n\tD to delete or \n\tQ to quit ==> ').upper()

if user_choice == "C":
    print("Calling CREATE routine.....")
elif user_choice == "R":
    print("Calling READ routine.....")
elif user_choice == "U":
    print("Calling UPDATE routine.....")
elif user_choice == "D":
    print("Calling DELETE routine.....")
elif user_choice == "Q":
    print("Exiting program")
else: 
    print(f'Your entry {user_choice} is invalid - try again')
    