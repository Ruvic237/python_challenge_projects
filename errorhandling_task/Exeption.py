# Problem one
try:
    
    for i in ['a','b','c']:
        print(i**2)
        
except Exception as e:
    
    print(e)
    print("Sorry can't perfom power on characters")


# Problem two
try:
    
    x,y = 5,0
    z = x/y
    print(z)
    
except ZeroDivisionError:
    print("Sorry can't divide a number by Zero")
    
finally:
    print("All done")

    
# Problem Three
# Function which ask's user an integer and returns it's square
def ask():
    
    while True:
        
        try:
            number = int(input("Enter a number to square \n"))
            a = number ** 2
            
        except ValueError:
            print("Sorry can't perform such operations on strings")    
        
        else:
            break
        
    return a  
  
print(ask())                       
    
    
# function to be test using unittest 
def cap(word):
    '''
    Take Input and Return First letter capitalzed
    '''
    return word.title()            