class BankAccount:
    def __init__(self, initial_balance=0.0):
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited: ${amount:.1f}"
        else:
            return "Invalid deposit amount."

    def withdraw(self, amount):
     if 0 < amount <= self.balance:
        self.balance -= amount
        return f"Withdrew: ${amount:.1f}"
     else:
        return "Insufficient funds."



    def display_balance(self):
        return f"Current Balance: ${self.balance:.2f}"
