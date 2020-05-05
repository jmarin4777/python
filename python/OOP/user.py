class User:
    def __init__(self, username, account_balance):
        self.username = username
        self.account_balance = account_balance
    
    def deposit(self, amount):
        self.account_balance += amount
        print(f"{self.username} deposited ${amount}.")
        return self
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        print(f"{self.username} withdrew ${amount}.")
        return self
    def display_user_balance(self):
        print(f"Username: {self.username}\nBalance: ${self.account_balance}")
        return self
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        print(f"{self.username} transferred ${amount} to {other_user.username}.")
        return self

jeff = User('jeff_rocks', 500)
bob = User('bob_the_builder', 250)
jimmy = User('jimmy_johns', 1000)

jeff.deposit(500).deposit(150).deposit(250).make_withdrawal(500).display_user_balance()
bob.deposit(100).deposit(100).make_withdrawal(50).make_withdrawal(100).display_user_balance()
jimmy.deposit(1000).make_withdrawal(750).make_withdrawal(750).make_withdrawal(250).display_user_balance()
jeff.transfer_money(jimmy,400).display_user_balance()
jimmy.display_user_balance()




