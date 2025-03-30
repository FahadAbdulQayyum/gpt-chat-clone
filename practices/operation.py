operation: str = str(input("Enter the operation: "))
num1: float = float(input("Enter the first number: "))
num2: float = float(input("Enter the second number: "))

result = num1 + num2 if operation == "+" else num1 - num2 if operation == "-" else num1 * num2 if operation == "*" else num1 / num2 if operation == "/" else "Invalid operation"
print(f"The result of {num1} {operation} {num2} is: {result}")