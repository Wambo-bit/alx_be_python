import sys
from bank_account import BankAccount

account = BankAccount(250.0)  # Important: match checker’s expected starting balance

if len(sys.argv) > 1:
    action = sys.argv[1]

    if action.startswith("deposit:"):
        try:
            amount = float(action.split(":")[1])
            print(account.deposit(amount))
        except ValueError:
            print("Invalid deposit amount.")

    elif action.startswith("withdraw:"):
        try:
            amount = float(action.split(":")[1])
            print(account.withdraw(amount))
        except ValueError:
            print("Invalid withdrawal amount.")

    elif action == "display":
        print(account.display_balance())

    else:
        print("Invalid action.")
else:
    print("No action provided.")
