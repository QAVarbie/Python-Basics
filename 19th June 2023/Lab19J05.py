def sum_of_three_number(a,b,c) :
    d = a + b + c
    return d

r = lambda x,y,z: x + y + z
r2 = lambda x,y,z,a: x + y + z + a
r3 = lambda a : pow(2,a)

print(r(3,4,5))
print(r(3,4,10))
print(r(3,4,-5))
print(r(3,8,5))