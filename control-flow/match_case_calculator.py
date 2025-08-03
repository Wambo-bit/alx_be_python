#prompt for user input
num1 = float (input("Enter the first number:"))
num2 = float (input("Enter the second number:"))
operation = input("choose the operation (+, -, *, /): ")
#match case calculator
match operation:
    case "+":
        result = num1 + num2
        print(f"The result is: {result}")
    case "-":
        result = num1 - num2
        print(f"The result is: {result}")
    case "*":
        result = num1 * num2
        print(f"The result is: {result}")
    case "/":
        if num2 != 0:
            result = num1 / num2
            print(f"The result is: {result}")
        else:
            result = "Cannot divide by zero."
    case _:
        result = "Invalid operation selected."


