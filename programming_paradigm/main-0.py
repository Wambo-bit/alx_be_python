import sys
from bank_account import BankAccount

account = BankAccount(250.0)  # default initial balance

if len(sys.argv) < 2:
    print("Usage: python main-0.py [deposit:amount | withdraw:amount | display]")
    sys.exit(1)

action = sys.argv[1]

if action.startswith("deposit:"):
    amount = float(action.split(":")[1])
    print(account.deposit(amount))

elif action.startswith("withdraw:"):
    amount = float(action.split(":")[1])
    print(account.withdraw(amount))

elif action == "display":
    print(account.display_balance())

else:
    print("Invalid command.")
