# Simple Calculator

# Taking user input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Choose operation to perform:")
print("1. Add")
print("2. Sub")
print("3. Multiply")
print("4. Div")


# Asking for an operator
operator = input("Enter an operator number: ")

# Performing the operation
if operator == '1':
    result = num1 + num2
elif operator == '2':
    result = num1 - num2
elif operator == '3':
    result = num1 * num2
elif operator == '4':
    if num2 == 0:
        result = "Error! Division by zero is not allowed."
    else:
        result = num1 / num2
else:
    result = "Invalid operator! Please enter valid operator"

# Displaying the result
print("Result:", result)
