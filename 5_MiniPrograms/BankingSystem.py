# Created by Burhanuddin Udaipurwala on 02/01/2019


import hashlib


class Account:
    def __init__(self, name, account_number, pin, initial_balance):
        self.__name = name
        self.__account_number = account_number
        self.__hashed_pin = hashlib.md5(pin.encode()).hexdigest()
        self.__balance = initial_balance

    def __str__(self):
        return str(self.__account_number) + str(self.__hashed_pin)

    def get_balance(self):
        return self.__balance

    def get_name(self):
        return self.__name

    def get_account_number(self):
        return self.__account_number

    def get_pin_hash(self):
        return self.__hashed_pin

    def withdraw(self, withdraw_amount):
        try:
            self.__balance = int(self.__balance) - int(withdraw_amount)
        except ValueError:
            print("Enter a valid integer value")
        print("Account balance: ", self.get_balance())

    def credit(self, credit_amount):
        try:
            self.__balance = int(self.__balance) + int(credit_amount)
        except ValueError:
            print("Enter a valid integer value")
        print("Account balance: ", self.get_balance())


# mimic api using a list
account_list = []

# track if user is logged in
account_logged_in = False


def create_account():
    name = input("Enter your name")
    initial_balance = input("Enter initial balance")
    pin = input("Enter pin")
    account_number = input("Enter 4 digit account number")

    for account in account_list:
        if account.get_account_number() == account_number:
            print("Account number already exists")

    account_number = input("Enter 4 digit account number")

    account_list.append(Account(name, account_number, pin, initial_balance))
    print("Account created, you can now log in")


def login():
    account_number = input("Enter account")
    pin = input("Pin")
    pin = hashlib.md5(pin.encode()).hexdigest()
    for account in account_list:
        if account.get_account_number() == account_number and account.get_pin_hash() == pin:
            return account

    print("Error: Account not found")
    return False


def print_account_balance():
    if not account_logged_in:
        print("Login to get balance")
        return

    print("Account balance: ", account_logged_in.get_balance())


def credit_balance():
    if not account_logged_in:
        print("Login to continue")
        return
    credit_amount = input("Enter amount to credit")
    account_logged_in.credit(credit_amount)


def withdraw_money():
    if not account_logged_in:
        print("Login to continue")
        return
    withdraw_amount = input("Enter amount to withdraw")
    account_logged_in.withdraw(withdraw_amount)


while True:
    print("Enter your choice")
    print("0. Exit")
    print("1. Create Account")
    print("2. Login")
    print("3. Get balance")
    print("4. Deposit money")
    print("5. Withdraw money")
    print("6. Log out")

    choice = int(input("Enter your choice"))

    if choice == 0:
        break
    elif choice == 1:
        create_account()
    elif choice == 2:
        account_logged_in = login()
    elif choice == 3:
        print_account_balance()
    elif choice == 4:
        credit_balance()
    elif choice == 5:
        withdraw_money()
    elif choice == 6:
        account_logged_in = False
    else:
        print("Incorrect choice, Enter a valid input")
