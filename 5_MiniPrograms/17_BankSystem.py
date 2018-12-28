class Bank:

    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        return self.__balance

    def withdraw(self, amount):
        if self.__balance <= 0:
            print("No Money in Account")
        else:
            self.__balance -= amount
        return self.__balance

    def get_balance(self):
        return self.__balance


b1 = Bank(100)
b1.deposit(40)
print(b1.get_balance())

Customers = {'Arjun': [2000, '1111-2222-3333-4444', 234]}


class ATM(Bank):
    def __init__(self, balance, cardnumber, pin):
        super().__init__(balance)
        self.cardnumber = cardnumber
        self.pin = pin


EnterUserName = input("Enter User Name")

if EnterUserName in Customers:
    EnterCardnumber = input("Enter Card Number")
    EnterPin = int(input('Enter Pin'))
    if Customers[EnterUserName][1] == EnterCardnumber and Customers[EnterUserName][2] == EnterPin:
        money = int(input('How Much money would you like to withdraw'))
        am = ATM(Customers[EnterUserName][0], EnterCardnumber, EnterPin)
        am.withdraw(money)
        print('your Remaining Balance', am.get_balance())
    else:
        print("Invalid Credentials")
else:
    print('No DataBase found')

# Code Courtesy Vidit Shah
