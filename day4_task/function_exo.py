# Function to find volume of a sphere given a radius

# user_radius = int(input("Enter the radius of the sphere\n"))
def volume_of_sphere(radius):
    return (4/3)*(3.14)*(radius**3)

# result = volume_of_sphere(user_radius)
# print(result)


# Funtion to determine if a number is between a given range
def check_range(number,low,high):
    list_range = [num for num in range(low,high+1)]
    if number in list_range:
        print("{} is in the range between {} and {}".format(number,low,high))
        return True
    else:
        print("{} is not in the range between {} and {}".format(number,low,high))
        return False

result_check = check_range(8,2,7)
#print(result_check)


# A funtion which accepts a string a returns number of lower and uppercase characters
#user_text = input("Enter the sentence you want to check \n")
def number_char(information):
    count_small = 0
    count_big = 0
    
    for i in information:
        if i.islower():
            count_small = count_small + 1
        elif i.isupper():
            count_big = count_big + 1
        else:
            pass
    print("The sentence is {} ".format(information))    
    return "We have {} lowercase characters and {} uppercase characters".format(count_small,count_big)

#result_char = number_char(user_text)   
# print(result_char) 


# A funtion which takes a list and returns a new list of unique values of original one
def unique_list(change):
    new_list = list(set(change))
    return "The new list is {} ".format(new_list)

user_store = unique_list([5,1,5,1,8,7,6,8,9])
#print(user_store)
            

# A function to multiply all numbers in a list
def muliply(list_nums):
    mult = 0
    for i in list_nums:
        if mult == 0:   
            mult = mult + i
        else:
            mult = mult * i  
    return f"The result is {mult}"       

show = muliply([1,2,3,-4])
#print(show)


# Function to check if a word or sentence is a palindrome or not
def is_palindrome(word):
   no_space = word.replace(' ','')       

   if no_space == no_space[::-1]:
        return "The word {} is a palindrome".format(word)
    
   return "The word {} is not a palindrome".format(word)

result_palin = is_palindrome("nurses run")
#print(result_palin)

