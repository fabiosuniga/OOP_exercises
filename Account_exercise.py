class Account:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return "Owner name: " + self.owner + ", Balance: $" + str(self.balance)

    def withdraw(self, value):
        if self.balance > value:
            self.balance -= value
            print("Withdrawal Accepted")
        else: print("Insuficient balance for this operation!")

    def deposit(self, value):
        self.balance += value
        print("Deposit Accepted")

acct1 = Account('Jose',100)
print(acct1)
acct1.deposit(50)
acct1.withdraw(75)
acct1.withdraw(500)

