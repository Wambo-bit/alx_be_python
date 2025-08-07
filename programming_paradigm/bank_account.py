class BankAccount:
    def __init__(self, initial_balance=0.0):
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited: ${amount:.1f}"
        return "Invalid deposit amount."

    def withdraw(self, amount):
        if amount <= 0:
            return "Invalid withdrawal amount."
        if amount > self.balance:
            return "Insufficient funds."
        self.balance -= amount
        return f"Withdrew: ${amount:.1f}"

    def display_balance(self):
        return f"Current Balance: ${self.balance:.2f}"
