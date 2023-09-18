def minimum (first, second):
    if (first < second):
        print(first)
        return first
    else:
        print(second)
        return second

min_no = minimum(4,5)
print("Result ->"+ str(min_no))