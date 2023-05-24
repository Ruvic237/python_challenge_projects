import random
 
# hangman game program

# ascii of lives in an array
lives_stage = ['''
               
               --:---:--
                 |   |
                 o   |
                /|\  |
                / \  | 
                     |
                =======
     
               ''','''
               
               --:---:--
                 |   |
                 o   |
                /|\  |
                /    | 
                     |
                =======
     
               ''','''
               
               --:---:--
                 |   |
                 o   |
                /|\  |
                     | 
                     |
                =======
     
               ''','''
               
               --:---:--
                 |   |
                 o   |
                /|   |
                     | 
                     |
                =======
     
               ''','''
               
               --:---:--
                 |   |
                 o   |
                 |   |
                     | 
                     |
                =======
     
               ''','''
               
               --:---:--
                 |   |
                 o   |
                     |
                     | 
                     |
                =======
     
               ''','''
               
               --:---:--
                 |   |
                     |
                     |
                     | 
                     |
                =======
     
               '''
               ]

logo = '''
Welcome to Ruvic...
 _
| |
| |___   __ _ _ __   _ _ _ _ ____   __ _ _ _
| |--  \/ _` |  _ \ / _'| '_`  _ \ / _` | '_ \  
| |  | | (_| | | | | (_|| | | | | | (_| | | | | game
|_|  |_|\_,__|_| |_|\_, |_| |_| |_|\__,_|_| |_|
                    __/ |
                   |___/ 
'''
# list of words user can be ask to guess
game_list = ["ardvark","baboon","camel"]


#choosen variable
choosen_word = random.choice(game_list)


#empty list to generate free space "_"
empty = []
i = 0

#add "_" to list base on size of choosen word
while i < len(choosen_word):
    empty.append("_")
    i = i + 1
    
    
#continuosly asking user to guess until all blanks are filled up    
start_of_game = True
live = 6
print(logo)
print("Let's get started")
while start_of_game:
        
    #ask user to guess a character
    user_guess = input("Guess a letter which may occur in a predicted word dear user \n").lower()

    if user_guess in empty:
        print("You have already guess this letter")
        
    #check if letter is in choosen word
    for position in range(0,len(choosen_word)):
        if choosen_word[position] == user_guess:
            empty[position] = user_guess 
    
    
    # reduce life if wrong guest
    if user_guess not in choosen_word:
        print("The letter {} is not present in the choosen word you loose a life".format(user_guess))
        live = live -  1    
        if live == 0:
            start_of_game = False
            print("Game Over you have been hanged the choosen word is: {}".format(choosen_word)) 
               
    print(" ".join(empty) )
    print("You have {} chances left to guess".format(live))
    
    # stop game and declare user winner
    if "_" not in empty:
        start_of_game = False
        print("you win")
    
    print(lives_stage[live])              
 
