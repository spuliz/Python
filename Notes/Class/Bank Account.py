class bankAccount:
    def __init__(self, balance):
        self.balance = balance
    def __str__(self):
        return "Your current balance is: {}$".format(self.balance)
    def withdrawn(self, amount):
         self.balance = self.balance - amount
    def deposit(self, amount):
        self.balance = self.balance + amount

ba1 = bankAccount(500)
print(ba1)

ba1.withdrawn(250)

print(ba1)

ba1.deposit(250)

print(ba1)
