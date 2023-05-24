# A program which shuffles a list for users to guest the index of a given character "O"

# importation of function to shuffel a given list
from random import shuffle

# list containing character
my_list = ['','O','']
print("This list {} will be shuffled hope you guess the index of O".format(my_list))

# a funtion to handle the shuffle and return the shuffled list
def shuffel_list():
    shuffle(my_list)
    return my_list

shuffled = shuffel_list()

# a funtion to collect user guess index
def guessing():
    guess = ''
    while guess not in ['0','1','2']:
        guess = input('choose between 0,1 or 2 \n')
    return int(guess)

user_guest = guessing()

# a funtion to determine if a user want's to play again or not
def choice():
    play = input("Do you want to play again? yes or no \n")
    if play == 'yes':
        shuffled = shuffel_list()
        user_guest = guessing()
        compare(shuffled,user_guest)
    else:
        print("Great see you soon")

# a funtion to determine if user guest is true or false

def compare(shuffled,user_guest):
    if shuffled[user_guest] == 'O':
        print("The list is {} and you said O is at index {}".format(shuffled,user_guest))
        print("Woppy you are right amazing")
        
        # ask if user wants to play 
        choice()
    else:
        print("The list is {} and you said O is at index {} ".format(shuffled,user_guest))
        print("Oooooo you have loosed")
        
        # ask if user wants to play 
        choice()
        
compare(shuffled,user_guest)


        
        

