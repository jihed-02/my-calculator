def sum(a, b):
    return a + b


def menu():
    print("Calculator")
    print("1 - Sum")

    choice = input("Choose an operation: ")

    if choice == "1":
        a = float(input("Enter a: "))
        b = float(input("Enter b: "))
        print("Result:", sum(a, b))
    else:
        print("Invalid choice")


menu()