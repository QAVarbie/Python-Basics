# for i in range(1,5):
#     print(i)
#     print("Varsha")


# for i in reversed(range(10)):
#     print(str(i) + "Varsha")

num1 = float(input("Enter the first number: "))
operator = input("Enter an operator (+, -, *, /): ")
num2 = float(input("Enter the second number: "))

if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Division by zero is not allowed."
else:
    result = "Invalid operator"

print("Result:", result)
