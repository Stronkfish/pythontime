main = input("Stronkfish Brand Calculator\n\nAddition = a\nSubtraction = b\nMultiplication = c\nDivision = d\n\n") # Selecting Operation (1)
if main == "a": # Calculation (2-21)
    print("\nOperation: Addition\n")
    a = int(input("First Number: "))
    b = int(input("Second Number: "))
    print(f"\nAnswer: {a + b}")
if main == "b":
    print("\nOperation: Subtraction\n")
    a = int(input("First Number: "))
    b = int(input("Second Number: "))
    print(f"\nAnswer: {a - b}")
if main == "c":
    print("\nOperation: Multiplication\n")
    a = int(input("First Number: "))
    b = int(input("Second Number: "))
    print(f"\nAnswer: {a * b}")
if main == "d":
    print("\nOperation: Division\n")
    a = int(input("First Number: "))
    b = int(input("Second Number: "))
    print(f"\nAnswer: {a / b}")
