# a = int(input("Enter a number"))
# def num_if_50(num) :
#     if num > 50:
#         print("Greater than 50")
#         return num
#     else:
#         print("Less than 50")
#         return num
#
# print(num_if_50(a))

r = lambda num : "Greater than 50" if num>50 else "Less than 50"
print(r(4))

r2 = lambda x : x**2 if x>0 else (x*2 if x<0 else 0)
print(r2(3))
print(r2(-2))
print(r2(0))

user_input = int(input("Enter your number"))
r2 = lambda x : x**2 if x>0 else (x*2 if x<0 else 0)
print(r2(user_input))

user_input = int(input("Enter your number"))
print(r2(user_input))

user_input = int(input("Enter your number"))
print(r2(user_input))


