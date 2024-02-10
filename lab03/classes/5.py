class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Withdrawal amount exceeds available balance.")
        else :
            self.balance -= amount
            print(f"Withdrawn ${amount}. New balance: ${self.balance}")

name = input("Enter the name of owner: ")  
balance = int(input("Enter the initial balance: "))

account = Account(name, balance)

account.deposit(100)
account.deposit(50)

account.withdraw(30)
account.withdraw(200)
