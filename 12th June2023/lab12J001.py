# age = int(input("Enter your Age "))
# if age > 18:
#     print("You can watch the A rated Movie")
# else:
#     print("Cant watch")

num = int(input("Enter a positive integer: "))
factorial = 1

if num < 0:
    print("Factorial is not defined for negative numbers.")
elif num == 0:
    print("The factorial of 0 is 1.")
else:
    for i in range(1, num + 1):
        factorial *= i
    print("The factorial of", num, "is", factorial)

