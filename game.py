


#
# todo: write some Python code here to satisfy the exercise objectives
# ... https://github.com/prof-rossetti/intro-to-python/blob/main/exercises/rock-paper-scissors/README.md
#


import pytest
import random               # load the module to avoid `NameError: name 'random' is not defined
import os                   # import os module to include environment variable

# bonus challenge 1 
player_name = os.getenv("PLAYER_NAME", default="Player One")
print("The name of Player one is ", player_name)

# bonus challenge 2, to test all the scnazrios 

def determine_winner(choice_1, choice_2):
    if choice_1 == choice_2 :
        return None
    elif choice_1 == "rock":
        if choice_2 == "scissors":
            return choice_1
        elif choice_2 == "paper":
            return choice_2
    elif choice_1 == "scissors":
        if choice_2 == "paper":
            return choice_1
        elif choice_2 == "rock":
            return choice_2
    elif choice_1 == "paper":
        if choice_2 == "rock":
            return choice_1
        elif choice_2 == "scissors":
            return choice_2
    exit()                   
if __name__ == "__main__":
    print("WELCOME TO MY ROCK PAPER SCISSORS GAME!")

# regular requirements
# Ask for user input
print("Welcome to the game of rock paper and scissors")
u = input("Please choose one of: 'rock', 'paper', 'scissors': ")

print("USER CHOSE:", u)


 # Validations
 # create a list of input that is acceptable
valid_input = ["rock", "paper", "scissors"]

# convert user input into lower cases
u_lower = u.lower()

# for loop to test the validity of user input
# the loop would return false if user input is invalid
Valid_test = False
for x in valid_input:
    if x != u_lower:
        continue                                # continue iterations until it is valid
    else: 
        Valid_test = True
        break
if Valid_test == False:                          # if the input is invalid, stop the program
    print("Please enter a valid input. Thank you!")
    exit()


 # computer choice
 # computer makes its random choice
computer_choice = random.choice(valid_input)
print("Computer chose ", computer_choice)

# comparing user input and computer choice 

if computer_choice == u_lower:
    print("It's a tie game. You and computer made the same choice, please try again")
    exit()

elif computer_choice == "rock":
    if u_lower == "scissors":
        print("Unfortunately, you lose the game, computer is the winner this time!")
        exit()
    else:
        print("Congratualations, you are the winner!")
        exit()

elif computer_choice == "scissors":
    if u_lower == "paper":
        print("Unfortunately, you lose the game, computer is the winner this time!")
        exit()
    else:
        print("Congratualations, you are the winner!")
        exit()

elif computer_choice == "paper":
    if u_lower == "rock":
        print("Unfortunately, you lose the game, computer is the winner this time!")
        exit()
    else:
        print("Congratualations, you are the winner!")
        exit()
 # determine the winner


Print("Thank you for playing the game. See you next time!")

 # final results 




