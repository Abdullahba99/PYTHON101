x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

operation = input("Enter operation (+, -, *, /): ")
if operation == '+':
    result = x + y
elif operation == '-':
    result = x - y
elif operation == '*':
    result = x * y
elif operation == '/':
    if y != 0:
        result = x / y
    else:
        result = "Error! Division by zero."
else:
    result = "Invalid operation."


print("The result is:", result)