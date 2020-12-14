'''
ROSHAMBO PROGRAM
----------------

Create a program that randomly prints 1, 2, or 3.
Expand the program so it randomly prints rock, paper, or scissors using if statements. Don't select from a list.
Add to the program so it first asks the user their choice as well as if they want to quit.
(It will be easier if you have them enter 1 for rock, 2 for paper, and 3 for scissors.)
Add conditional statements to figure out who wins and keep the records
When the user quits print a win/loss record

'''

import random

wins = 0
losses = 0

print("Use 1 for rock, 2 for paper and 3 for scissors.")

player = "false"

while player == "false":
    choice = int(input("What is your move?"))
    comp_choice = random.randint(1, 3)
    if choice == 2 and comp_choice == 1:
        print("You win!")
        wins = wins + 1
    if choice == 1 and comp_choice == 3:
        print("You win!")
        wins = wins + 1
    if choice == 3 and comp_choice == 2:
        print("You win!")
        wins = wins + 1
    if choice == 1 and comp_choice == 2:
        print("You lose.")
        losses = losses + 1
    if choice == 2 and comp_choice == 3:
        print("You lose.")
        losses = losses + 1
    if choice == 3 and comp_choice == 1:
        print("You lose.")
        losses = losses + 1
    quit = input("Do you want to quit? ").lower()
    if quit == "yes":
        print("You won", wins ,"times! You lost", losses ,"times.")
    if quit == "yes":
        exit()
    if quit == "no":
        player = "false"