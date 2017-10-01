class BankAccount(object):
  balance = 0
  def __init__(self, name):
    self.name = name

  def __repr__(self):
    return "Account owner: %s \nAccount Balance: $%.2f"%(self.name, 		float(self.balance))

  def show_balance(self):
    return "The current balance is: $%.2f"%(float(self.balance))

  def deposit(self, amount):
    self.amount = amount
    if self.amount <= 0:
      print("Amount should be higher than zero")
      return
    else:
      print("The amount of the deposit: $%.2f")% (self.amount)
      self.balance += self.amount
      self.show_balance()

  def withdraw(self, amount):
    self.amount = amount
    if self.amount > self.balance:
      print("Amount not available")
      return
    else:
      print("Amount withdraw: $%.2f")%(self.amount)
      self.balance -= self.amount
      self.show_balance()

my_account = BankAccount("KBC")
print(my_account)
my_account.show_balance()
my_account.deposit(2000)
my_account.withdraw(1000)
print(my_account)






