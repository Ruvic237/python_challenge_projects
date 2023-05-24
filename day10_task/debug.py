# A program to test my debugging skills

#Describe problem
def my_function():
    for i in range(1, 20): # change 20 to 21 in range for if to turn true
        if i == 20:
            print("You got it")
show = my_function()


# Reproduce the Bug
from random import randint
dice_imgs = ["0","0","0","0","0","0"]
dice_num = randint(1,6) # for no error put randit(1,5) which considers 1 and 5 inclusively
# For bug to repeat dice_num must be equal to 6. Because 6 is out of range of dice_imgs size 
# print(dice_imgs[dice_num])


# Play computer and predict what can happen
year = int(input("What's your year of birth?"))
if year > 1980 and year < 1994:
    print("You are a millenial.")
elif year > 1994:
    print("You are a Gen Z.") 
# if I input 1994 or 1980 nothing will show as output because none of them evaluate to True in the block of code



          


           