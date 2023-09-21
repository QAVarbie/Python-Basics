my_list = [1, 2, 3]
print(my_list[0])

print(my_list[0 : 2])
print(my_list[0 : 1])
print(my_list[0 : 3])
print(my_list[2 : ])
print(my_list[ : ])
print(my_list[ : -1])
print(my_list[ : -2])

my_list.extend([4,5])
print(my_list)

i = my_list.pop(1)
print(i)
print(my_list)
my_list.append(5)
print(my_list)

print(my_list.count(5))
my_list.reverse()
print(my_list)

my_list.pop()
print(my_list)