import random
# A program for The blackjack game 

# game cards 10 as k,j,q and 11 as ace 
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
user_cards = []
computer_cards = []


# Function to get random numbers for both users
def get_card():
    
    user = random.choice(cards)
    computer = random.choice(cards)
    user_cards.append(user)
    computer_cards.append(computer)
    

get_card()


# Function to sum their scores
def sum_cards(player):
    result_sum = sum(player)
    if 11 in player:
        if result_sum > 21:
            print("sum greater")
            player.remove(11)
            player.append(1)
            result_sum = sum(player)
        else:
            pass
            
    return result_sum


# Function to check if there is a blackjack
def black_jack():
    user_sum = sum_cards(user_cards)
    computer_sum = sum_cards(computer_cards)

    if user_sum > 21 and computer_sum > 21:
        print("Game over but draw")
        print(f"User got {user_cards} cards and computer got {computer_cards} ... ")
        print("Therefore user has {}pts and computer has {}pts".format(sum(user_cards),sum(computer_cards)))
        return False
    if computer_sum > 21 and user_sum < 21:
        print("Gameover user wins")
        print(f"User got {user_cards} cards and computer got {computer_cards} ... ")
        print("Therefore user has {}pts and computer has {}pts".format(sum(user_cards),sum(computer_cards)))
        return False     
    if user_sum > 21 and computer_sum < 21:
        print("Gameover computer wins") 
        print(f"User got {user_cards} cards and computer got {computer_cards} ... ")
        print("Therefore user has {}pts and computer has {}pts".format(sum(user_cards),sum(computer_cards)))
        return False 
    if user_sum < 21 and computer_sum < 21:
        return True
    

# funtion checks
def game_check():
    play = black_jack()

    while play == True:
        print(f"user choice is {user_cards} and computer choice is {[computer_cards[0]]}")
        
        t = input("Do you want to draw a card (y or n) ? \n").lower()
        
        if t == "y":
            get_card()
            play = black_jack()
            
        elif t == "n":
            
            print("game over")
            
            if sum(user_cards) > sum(computer_cards):
                print(f"User got {user_cards} cards and computer got {computer_cards} ... ")
                print("Therefore user has {}pts and computer has {}pts".format(sum(user_cards),sum(computer_cards)))
                print("Hence winner is user")
                break 
            
            elif sum(user_cards) < sum(computer_cards):
                print(f"User got {user_cards} cards and computer got {computer_cards} ... ")
                print("Therefore user has {}pts and computer has {}pts".format(sum(user_cards),sum(computer_cards)))           
                print("Hence winner is computer")
                break
            
            else:
                print(f"User got {user_cards} cards and computer got {computer_cards} ... ")
                print("Therefore user has {}pts and computer has {}pts".format(sum(user_cards),sum(computer_cards)))
                print("Hence There is a draw")
                break
            
        else:
            print("wrong input try again")  
              

choice = input("Do you want to play ? \n").lower()

if choice == "y":
       game_check()      
elif choice == 'n':
       print("Ok see you")
else:
    print("wrong input")        

  