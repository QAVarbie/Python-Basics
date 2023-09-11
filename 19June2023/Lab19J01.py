user_input = input("Enter a Number and I will do num^2")
user_input = int(user_input)


def pow_by_2(num):
    return pow(2,num)

result = pow_by_2(user_input)
print(result)