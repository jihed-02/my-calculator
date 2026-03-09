def sum(a, b):
    return a + b


def sub(a, b):
    return a - b


def menu():
    print("Calculator")
    print("1 - Sum")
    print("2 - Subtraction")

    choice = input("Choose an operation: ")

    a = float(input("Enter a: "))
    b = float(input("Enter b: "))

    if choice == "1":
        print("Result:", sum(a, b))
    elif choice == "2":
        print("Result:", sub(a, b))
    else:
        print("Invalid choice")


menu()