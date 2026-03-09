def sum(a, b):
    return a + b


def sub(a, b):
    return a - b


def realDivi(a, b):
    if b == 0:
        return "Error: division by zero"
    return a / b


def pow(a, b):
    return a ** b


def menu():

    print("Calculator")
    print("1 Sum")
    print("2 Sub")
    print("3 Division")
    print("4 Power")

    choice = input("Choose operation: ")

    a = float(input("a: "))
    b = float(input("b: "))

    if choice == "1":
        print(sum(a, b))
    elif choice == "2":
        print(sub(a, b))
    elif choice == "3":
        print(realDivi(a, b))
    elif choice == "4":
        print(pow(a, b))
    else:
        print("Invalid choice")


menu()