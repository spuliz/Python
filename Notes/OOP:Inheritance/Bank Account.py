class bankAccount:
    def __init__(self, balance):
        self.balance = balance
    def __str__(self):
        return "Your current balance is: {}$".format(self.balance)
    def withdrawn(self, amount):
         self.balance = self.balance - amount
    def deposit(self, amount):
        self.balance = self.balance + amount


class savingAccount(bankAccount):
    def __init__(self, interest):
        self.interest = interest




class currentAccount(bankAccount):
    def __init__(self, overdraft):
        self.overdraf = overdraft
