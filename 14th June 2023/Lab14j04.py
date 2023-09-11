if "x" in "xyz" :
    print("True")

string = input("Enter a String")
substring ="mod"

match string:
    case x if substring in x:
        print("Present")
    case _:
        print("Not present")