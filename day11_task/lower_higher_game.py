# A Higher or Lower game program
import random
from game_data import data

# Welcome users to the game
print("Welcome to the Higher or Lower Game")

# A function to check if user won or not
def guess_game():
    guess_one = random.choice(data)
    guess_two = random.choice(data)
     
    # check if guess_one not same as guess_two
    while guess_one == guess_two:
        guess_two = random.choice(data)
            
    # value of A and B
    A = guess_one["follower_count"]
    B = guess_two["follower_count"]
     
    # Display the information of those user will compare
    print("Compare A: {}, is one {} from {} ".format(guess_one["name"],guess_one["description"],guess_one["country"]))
    print("VS")
    print("Against B: {}, is one {} from {} ".format(guess_two["name"],guess_two["description"],guess_two["country"]))

    # Obtain the input of user for person with > followers
    user_choice = input("Who has more followers? Type A or B: ").upper()

    # Check if user input is either A or B
    is_correct = True
    while is_correct:
        if user_choice not in ['A','B']:
            print("Wrong input choose again")
            user_choice = input("Who has more followers? Type A or B: ").upper()          
        else:
            is_correct = False 
             
    # Game options
    if ((A > B) and (user_choice == 'A')) or ((A < B) and (user_choice == 'B')): 
        print("You are correct")
        return True
    elif A == B:
        print("They are equal to each other")
        return "Equal"
    else: 
        print("Sorry it is wrong")
        return False
                              
# Continue to ask user till they are wrong
correct = 0
start = True
while start:
    gaming = guess_game()
    if gaming == False:
        print("Game over your total score is {}".format(correct))
        start = False
        
    elif gaming == True:
        correct = correct + 1
        print("Your current score is {}".format(correct))
        start = True 
    
    else:      
        print("Your current score is {}".format(correct))
        start = True 