# Encapsulation

# create a bank class
class bank:

    def __init__(self,accntNo,accntBalance):
        self.__accntNo = accntNo
        self.__accntBalance = accntBalance
    
    @property
    def balance(self):
        return self.__accntBalance
    
    @balance.setter
    def balance(self,new_balance):
        if new_balance >= 0:
            self.__accntBalance = new_balance
        else:
            print("Balance should not be negative!")
    
    def deposit(self,amt):
        if amt > 0:
            self.__accntBalance += amt
        else:
            print("Cannot deposit a negative value")

    def withdraw(self,amt):
        if 0 < amt <= self.__accntBalance:
            self.__accntBalance -= amt
        else:
            print("Invalid withdrawal amount")        

myBank = bank("20765490",100000.00)

# check balance
print("Balance: {}".format(myBank.balance))

# Update balance
myBank.balance = 50000.00

# check balance
print("Balance: {}".format(myBank.balance))

# make a deposit
myBank.deposit(100)

# check balance
print("Balance: {}".format(myBank.balance))

# make a withdrawal
myBank.withdraw(30000)

# check balance
print("Balance: {}".format(myBank.balance))