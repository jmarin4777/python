def accountArray():
    arr=[]
    for i in range(1,1001):
        arr.append(i)
    return arr

accountNumbers = accountArray()
def getAccountNumber(arr):
    return arr.pop(0)

class User:
    def __init__(self, username):
        self.username = username
        self.primaryAccountNumber = getAccountNumber(accountNumbers)
        self.account = {self.primaryAccountNumber: BankAccount(self.primaryAccountNumber, 0, 0.02)}

    #num is account number
    def addAccounts(self, num):
        for i in range(num):
            x = getAccountNumber(accountNumbers)
            self.account[x] = BankAccount(x, 0, 0.02)
    def deposit(self, amount, num):
        self.account[num].deposit(amount)
        print(f"${amount} was deposited into {self.username}'s account.")
        return self
    def withdraw(self, amount, num):
        self.account[num].withdraw(amount)
        print(f"${amount} was withdrawn from {self.username}'s account.")
        return self
    def display_account_info(self):
        print(f"{self.username} Account Info:")
        for key in self.account:
            self.account[key].display_bank_account_info()
        return self
    def calc_interest(self, num):
        self.account[num].yield_interest()
        return self
    def transfer_money(self, num, other_user, num2, amount):
        self.account[num].withdraw(amount)
        other_user.account[num2].deposit(amount)
        print(f"${amount} was transferred from {self.username}'s account to {other_user.username}'s account.")
        self.display_account_info()
        other_user.display_account_info()
        return self

class BankAccount:
    def __init__(self, account_number, balance=0, int_rate=0.01):
        self.account_number = account_number
        self.balance = balance
        self.int_rate = int_rate
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        self.balance -= amount
        return self
    def display_bank_account_info(self):
        print(f"Account Number: {self.account_number}\nBalance: ${self.balance}\nCurrent Interest Rate: {self.int_rate*100}%\n")
        return self
    def yield_interest(self):
        temp = self.balance
        self.balance += self.balance*self.int_rate
        print(f"Current Interest Rate: {self.int_rate*100}%\nBalance Before Interest: ${temp}\nBalance After Interest: ${self.balance}")
        return self

jeff = User('jeff_rocks')
bob = User('bob_the_builder')
jimmy = User('jimmy_johns')

jeff.deposit(1000,1).withdraw(100,1).transfer_money(1,jimmy,3,400)
bob.deposit(1000,2).withdraw(200,2).calc_interest(2).display_account_info()
jimmy.deposit(1000,3).withdraw(300,3).display_account_info()

