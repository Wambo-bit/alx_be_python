from bank_account import BankAccount
import sys

def main():
    account = BankAccount(100)

    if len(sys.argv) > 1:
        command = sys.argv[1]

        if command.startswith("deposit:"):
            amount = float(command.split(":")[1])
            print(account.deposit(amount))  # print the returned message

        elif command.startswith("withdraw:"):
            amount = float(command.split(":")[1])
            print(account.withdraw(amount))  # print the returned message

        elif command == "display":
            print(account.display_balance())  # print the returned balance

if __name__ == "__main__":
    main()
