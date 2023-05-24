# Bank account program

class Bank_Account():
    
    # constructor of the class
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
        
    # Balance method
    def balance_check(self):
        return "Account balance: £{}".format(self.balance)
    
    # Owner method
    def owner_check(self):
        return "Account owner: {}".format(self.owner)
    
    # Deposit method
    def deposit_check(self,deposit):
        self.balance = deposit + self.balance
        return "Deposit done successfully"
    
    # Withdraw method
    def withdraw_check(self,withdraw):
        if withdraw <= self.balance:
            self.balance = self.balance - withdraw
            print("Withdrawal Accepted")
            return "Money left: {}£".format(self.balance)
        else:
            return "Funds Unavailable"
        
    # dunder method for string
    def __str__(self):
        return "Account owner: {} \nBalance is {}".format(self.owner,self.balance)
               
    
account1 = Bank_Account("John",100)
#depositing = account1.deposit_check(800)
#withdrawing = account1.withdraw_check(300)
#balancing = account1.balance_check()
print(account1)
