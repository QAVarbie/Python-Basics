choice = ''
while choice != '3':
    print("\n 1. Say Hello \n 2. Do nothing \n 3. Quit")
    choice = input("Choice 1-3")
    if choice == '1' :
        print("Say Hello")
    elif choice == '2' :
        pass
    elif choice == '3':
        print("Quit")
        break
    else:
        print("Invalid Option")

print("End")