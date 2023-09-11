num = int(input("Enter a int Number"))
print("You have entered a number->", str(num))

match num:
    case 0:
        print("You have entered 0")
    case num > 0 :
        print("+ve Number")
    case num < 0:
        print("-ve Number")
    case _:
        print("No Idea!")