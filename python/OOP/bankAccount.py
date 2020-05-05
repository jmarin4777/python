class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, balance=0, int_rate=0.01):
        # your code here! (remember, this is where we specify the attributes for our class)
        self.balance = balance
        self.int_rate = int_rate
        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        self.balance += amount
        print(f"${amount} deposited.")
        return self
    def withdraw(self, amount):
        self.balance -= amount
        print(f"${amount} was withdrawn.")
        return self
    def display_account_info(self):
        print(f"User balance: ${self.balance}\nCurrent interest rate: {self.int_rate*100}%")
        return self
    def yield_interest(self):
        temp = self.balance
        self.balance += self.balance*self.int_rate
        print(f"Before interest: ${temp}\nAfter interest: ${self.balance}")
        return self

firstAccount = BankAccount(1000)
secondAccount = BankAccount(2000)
firstAccount.deposit(250).deposit(250).deposit(500).withdraw(1000).yield_interest().display_account_info()
secondAccount.deposit(1000).deposit(1000).withdraw(250).withdraw(250).withdraw(250).withdraw(250).yield_interest().display_account_info()
