class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient balance"
        self.balance -= amount
        return f"Remaining balance is {self.balance}"

account1 = Account(str(input("Enter name of the owner: ")), int(input("Enter initial balance: ")))
account1.deposit(int(input("Enter amount to deposit: ")))
print(account1.withdraw(int(input("Enter amount to withdraw: "))))
