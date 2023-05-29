# Player account with it's chips
class Player:
    
    # Characteristics of player
    def __init__(self,name,balance):
        self.name = name
        self.balance = int(balance)
        
    # Method to add money to balance
    def make_deposit(self,money):
        while True:
            try:
                self.balance += money
                print("Deposit done succcefully")
            except:
                print("Invalid entry make sure to enter numbers")
            else:
                break
    
    # Method to withdraw money
    def withdraw_money(self,amount):
        while True:
            try:
                if amount <= self.balance:
                    self.balance -= amount
                    print("Succefful Withdraw of {} fcfa".format(amount))
                else:
                    print(f"Demanded Money exceeds Try again {self.name}")
                    print(f"Your current balance is {self.balance}")    
            except:
                print("Invalid entry make sure to enter numbers")
            else:
                break  
    
    def remove(self,game):
        self.balance -= game
                    