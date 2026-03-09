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
    print("1 - Sum")
    print("2 - Subtraction")
    print("3 - Real Division")
    print("4 - Power")

    choice = input("Choose an operation: ")

    a = float(input("Enter a: "))
    b = float(input("Enter b: "))

    if choice == "1":
        print("Result:", sum(a, b))
    elif choice == "2":
        print("Result:", sub(a, b))
    elif choice == "3":
        print("Result:", realDivi(a, b))
    elif choice == "4":
        print("Result:", pow(a, b))
    else:
        print("Invalid choice")


menu()