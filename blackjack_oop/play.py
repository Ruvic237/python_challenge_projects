from player_account import Player
from cards_choice import Cards

player_name = input("Enter your name dear user \n")
while True:
    try:
        account_balance = int(input("How much do you want to add to your account?"))
    except:
        print("An error occured Make sure to enter only numbers")  
    else:
        break      

player1 = Player(player_name,account_balance)

print(f"Welcome to the black jack game {player1.name}")

computer_card = Cards()
player_card = Cards()

# function to check who won if no one exceeds 21
def check_winner():
    if player_card.score > computer_card.score and player_card.score <= 21:
        return "player"
    elif player_card.score < computer_card.score and computer_card.score <=21:
        return "computer"
    elif player_card.score == computer_card.score:
        return "draw"
    
# check if some one won incase there is a score > 21
def check_burst():
    if player_card.score > 21 and computer_card.score <= 21:
        print(f"user:{player_card.card} and computer final:{computer_card.card}")
        return "computer"
    elif player_card.score <= 21 and computer_card.score > 21:
        print(f"user:{player_card.card} and computer final:{computer_card.card}")
        return "player"
    elif player_card.score > 21 and computer_card.score > 21:
        print(f"user:{player_card.card} and computer final:{computer_card.card}")
        return "draw"

# check for ace in computer or player list of cards
def ace_check():
    play_ace = 11 in player_card.card and player_card.score > 21
    computer_ace = 11 in computer_card.card and computer_card.score > 21
    
    if play_ace and computer_ace:
        player_card.card.remove(11)
        player_card.card.append(1)  
        computer_card.card.remove(11)
        computer_card.card.append(1)
    elif play_ace:
        player_card.card.remove(11)
        player_card.card.append(1)
    elif computer_ace:     
        computer_card.card.remove(11)
        computer_card.card.append(1)
   
# Game starts here        
play = True
while play:
    
    # when ever game starts player and computer list of cards is empty
    player_card.card = []
    computer_card.card = []
    
    print(f"Your total account is {player1.balance} fcfa")
    choice = input("Should we start the game ? (yes or no)")
    
    # determine if player wan't to start playing the game
    if choice == "yes": 
        money = int(input("Input how much you want to bet \n"))
        computer_money = money
        # check if money to bet is sufficient in user player account     
        if money <= player1.balance:
            
            # both player and computer pick two cards
            computer_card.pick()
            player_card.pick()
            
            print(f"user:{player_card.card} and computer:{[computer_card.card[0]]}")    
            
            # Determine if user want's to pick or not and check winner or looser or draw 
            while True:
                option = input("Do you want to pick again?")
                
                # permiting computer to choose two cards 
                if player_card.score < 17:
                    computer_card.pick()
                    
                    # determine if computer cards contains an ace
                    ace_check()
                    
                    # determine who won if user score is < 17 and user decided to stop picking
                    # add or remove bet money base on winner
                    if option == "no":
                        print(f"user:{player_card.card} and computer final:{computer_card.card}")
                        status = check_winner()
                    
                        if status == "computer":
                            print("computer won")
                            player1.remove(money)
                            break    
                        elif status == "player":
                            print("player won")
                            player1.make_deposit(money)
                            break
                        elif status == "draw":
                            print("Draw")
                            break 
                        else:
                            print("player won")
                            player1.make_deposit(money)
                            break

                
                # if user picks, we check if he has an ace and if someone score > 21
                # base on winner or looser we remove or add bet money to account    
                if option == "yes":
                    player_card.pick()
                    ace_check()
                    print(f"user:{player_card.card} and computer:{[computer_card.card[0]]}") 
                    state = check_burst()
                    
                    if state == "computer":
                        print("computer won")
                        player1.remove(money)
                        break    
                    elif state == "player":
                        print("player won")
                        player1.make_deposit(money)
                        break
                    elif state == "draw":
                        print("Both of you exceeded 21")
                        break
                
                # if user don't pick , we check winner and add or remove his bet money    
                elif option == "no":
                    ace_check()
                    print(f"user:{player_card.card} and computer final:{computer_card.card}") 
                    status = check_winner()
                    
                    if status == "computer":
                        print("computer won")
                        player1.remove(money)
                        break    
                    elif status == "player":
                        print("player won")
                        player1.make_deposit(money)
                        break
                    elif status == "draw":
                        print("Draw")
                        break         
                    
        # no enough money to bet in the game                
        else:
            print("No money in your account deposit more") 
            break
    
    # user decides to stop the game        
    else:
        
        # Give the player the somarry of what he won or loosed  
        
        if player1.balance > account_balance:
            won = player1.balance - account_balance
            print(f"Game over the total money you won is {won} fcfa")
        elif player1.balance < account_balance:
            loose = account_balance - player1.balance
            print(f"Game over the total money you have loosed is {loose} fcfa")
        else:
            print("Game over you have won 0 fcfa and loosed 0 fcfa")        
        
        play = False 
               

    


       
    
            
           
             
                                     
   