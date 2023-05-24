# a program which displays the biggest or lowest number if they are odd or even

# function to compare and display result
def compare_numbers(a,b):
    if a % 2 == 0 and b % 2 == 0:
        return min(a,b)
    else:
        return max(a,b) 

result = compare_numbers(2,5)    
# print(result)


# Program to determine if 1st letters of strings are the same
def words(string_one,string_two):
    if string_one[0] == string_two[0]:
        return True
    else:
        return False
    
check = words("Ruvic","Rohn")
# print(check)


# Program to determine if a list contains 007 in that order

# empty list (listing) to collect 0 and 7 in their oder
listing = []

o = input('enter list of numbers! make sure to space each of them ')
list_user = o.split()

# function to collect 0 and 7
def collect(list):
    for i in list:
        if i == '0' or i == '7':
            listing.append(i)
        else:
            pass
        
    return listing

store_collect = collect(list_user)    

# funtion to check if listing is same as 007
def check():
    if store_collect == ['0','0','7']:
        return True
    else:
        return False

check_collect = check() 
# print(check_collect)


# determine if sum of two numbers is equal 20 or any of them
def is_twenty(a,b):
    sum = a+b
    
    if sum == 20 or a == 20 or b == 20:
        return True
    else:
        return False
    
sum_result = is_twenty(20,10) 
# print(sum_result)      


# A funcion to capitalise 1 and 3 letter of a word
def Capitalise(word):
    
  letter_one = word[0]
  in_between = word[1:3]
  letter_four = word[3]
  rest = word[4:]
  
  return letter_one.upper() + in_between + letter_four.upper() + rest 

result = Capitalise("michel")     
# print(result) 
    
# function to reverse a word

def Reverse(words):
    words_list = words.split(" ") # each item seperated by space is member of list
    store_list = words_list[::-1] # list items are reversed from end to start
    words_string = ' '.join(store_list) # list converted to string seperator (space)
    return words_string

result_reverse = Reverse("I am called ruvic")
# print(result_reverse)


# function to detrmine if a list contains adjacent 3 
def Consecutive(number_list):
    
    for i in range(len(number_list)-1):
        
        if number_list[i] == 3 and number_list[i+1] == 3:
            return True
        else:
            pass  
              
    return False
       
is_33 = Consecutive([1,1,3,3])        
# print(is_33)


# Program to multiply every character in a string by 3
listo = []

# function to perform operation
def multiply_letters(word):
    for i in word:
        a = i*3
        listo.append(a)
    return ''.join(listo)

result_letters = multiply_letters("Brroo")  
# print(result_letters)  


# bLACK JACK funtion
def Black(a,b,c):
    sum = a+b+c

    if sum <= 21:
        return "the sum is {}".format(sum)
    
    elif 11 in [a,b,c] and (sum-10) <= 21:
        return "the sum is {} the removed 10 ".format(sum)
    
    else:
         return "BUST"         
        
final = Black(10,10,10)
# print(final)


# Program to sum up all elements in a list not in the range 6 to 9
# a is the variable function for the list
def erase(a):
    summ = 0 
    if 6 in a and 9 in a:
        for i in a[a.index(6):a.index(9)+1]:
                z = a.index(i)
                a.remove(a[z])
           
    for j in a:
            summ = summ + j
        
    return summ

out_put = erase([4,5,5,7])
# print(out_put)

# available for any worry
        

            
            

    
        


                


