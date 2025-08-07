class BankAccount:
    def __init__(self, initial_balance=0):
        self.__account_balance = initial_balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount  # Add to balance

    def withdraw(self, amount):
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount  # Deduct from balance
            return True
        return False  # If not enough balance

    def display_balance(self):
        print(f"Current Balance: ${self.__account_balance}")
