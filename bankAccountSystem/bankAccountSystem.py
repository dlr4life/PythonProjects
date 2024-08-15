class BankAccount:
    def __init__(self, owner, balance=0): 
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance: 
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}") 
        else:
            print("Insufficient funds!")

# Using the class
my_account = BankAccount("John Doe", 1000)
my_account.deposit(500)
my_account.withdraw(200)
