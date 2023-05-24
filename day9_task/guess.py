import random
# Guess number program

# choosen number by computer for user to guess
computer_guess = random.choice(range(1,101))

# print statements to user when game starts
print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100.")


# User difficulty choice and game difficulty level
start = True
user_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
while start:
    
    if user_difficulty not in ["easy","hard"]:
        print("Wrong input choose between easy and hard")
        user_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    
    else:
        #Game life base on difficulty
        
        if user_difficulty == "easy":
            attemp = 10
        elif user_difficulty == "hard":
            attemp = 5
        else:
            pass    
        start = False    
 

print("You have {} attempts remaining to guess the number.".format(attemp))               


# determine if user guess is in range
def guessing():
    play = True
    user_guess = int(input("Make a guess user \n"))
    while play:
        
        if user_guess not in range(1,101) and play == True:
            print("wrong number choose between 1 and 100 inclusive")
            user_guess = int(input("Make a guess user \n"))
        else:
            play = False 
    
    return user_guess  
      
user_guess_value = guessing()


# Game section 
game =  True
while game:
        
    # determine if user guess found , low or high
    if user_guess_value == computer_guess:
        print("You have choosed {} and computer choosed {}".format(user_guess_value,computer_guess))
        print("So woupii correct Guess")
        game = False
    elif user_guess_value < computer_guess:
        attemp = attemp - 1
        if attemp == 0:
            print("Attemps expired you lose")
            print("Correct number is {}".format(computer_guess))
            break
        print("Guess again.")
        print("Guess to low.")
        print("You have {} attempts remaining to guess the number.".format(attemp))
        user_guess_value = guessing()
    else:
        attemp = attemp - 1
        if attemp == 0:
            print("Attemps expired")
            break
        print("Guess again.")
        print("Guess too high.")
        print("You have {} attempts remaining to guess the number.".format(attemp))
        user_guess_value = guessing()

               