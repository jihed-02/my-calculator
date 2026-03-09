def sum(a, b):
    return a + b


def sub(a, b):
    return a - b


def realDivi(a, b):
    if b == 0:
        return "Error: division by zero"
    return a / b


def pow2(b):
    return 2 ** b


def menu():
    print("Calculator")
    print("1 - Sum")
    print("2 - Subtraction")
    print("3 - Real Division")
    print("4 - Power of 2")

    choice = input("Choose an operation: ")

    if choice == "4":
        b = float(input("Enter b: "))
        print("Result:", pow2(b))
    else:
        a = float(input("Enter a: "))
        b = float(input("Enter b: "))

        if choice == "1":
            print("Result:", sum(a, b))
        elif choice == "2":
            print("Result:", sub(a, b))
        elif choice == "3":
            print("Result:", realDivi(a, b))
        else:
            print("Invalid choice")


menu()