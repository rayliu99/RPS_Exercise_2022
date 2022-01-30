


#
# todo: write some Python code here to satisfy the exercise objectives
# ... https://github.com/prof-rossetti/intro-to-python/blob/main/exercises/rock-paper-scissors/README.md
#



import random               # load the module to avoid `NameError: name 'random' is not defined`
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


