# Develop a set of Python classes to model a bank.
# A bank has a name, a list of savings accounts, and a list of current accounts.
# Each account has an account number, a name of the account holder and a balance.
# Savings accounts have an interest rate and a method to calculate interest.
# Current accounts have an overdraft.
#
# A bank can hold a number of Bank account objects – some Savings accounts, some Current accounts.
# Write an update() function that iterates through the accounts, updating them in the following ways:
# SavingsAccounts get interest added (via the method you already wrote)
# CurrentAccounts get a letter sent if they are in overdraft.
# Write a small test program to test your classes. Include a method to print a list of account details for all accounts the bank.

class bank(object):
    def __init__(self, name):
        self.name = name
        self.savingsAccount = []
        self.currentAccount = []

    def update(self):
        for i in self.savingAccount:
            self.savingsAccount = self.savingsAccount + savingAccount.interest
        for i in self.currentAccount:
            if i < 0:
                print("Sent Letter")
            else:
                print("Account not in overdraft")

    def addSavingAccount(self, sa):
        self.savingsAccount.append(sa)

    def addcurrentAccount(self, ca):
        self.savingsAccount.append(ca)

class bankAccount(object):
    def __init__(self,  balance, accountHolder):
        self.accountNumber = int(input("Please insert a new account number: "))
        self.balance = balance
        self.accountHolder = accountHolder

    def __str__(self):
        return "Your current balance is: {}$".format(self.balance)

    def withdrawn(self, amount):
         self.balance = self.balance - amount

    def deposit(self, amount):
        self.balance = self.balance + amount

class savingAccount(object):
    def __init__(self):
        self.deposit = int(input("Add the deposit amount: "))
        self.interestRate = float(input("Add the interest rate: "))
        self.period = int(input("When is the interest paid (e.g. 12 for monthly payment): "))
        self.time = int(input("How long you will earn interest (e.g. 1 for one year): "))

    def interest(self):
        interest = self.deposit*((1+self.interestRate/self.period)^(self.period*self.time))
        print("interest: ", interest)

class currentAccount(object):
    def __init__(self):
        self.overdraft = int(input("Add the overdraft amount: "))

b1 = bank("KBC")
sa1 = savingAccount()
sa2 = savingAccount()
b1.addSavingAccount(sa1)
b1.addSavingAccount(sa2)
ca1 = currentAccount()
ca2 = currentAccount()
b1.addcurrentAccount(ca1)
b1.addcurrentAccount(ca2)

print(b1.savingsAccount, b1.currentAccount)



