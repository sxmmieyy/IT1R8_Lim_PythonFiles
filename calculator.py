def addition():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    return a + b

def subtraction():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    return a - b

def multiplication():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    return a * b

def division():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    if b == 0:
        print("Invalid. (Cannot divide by zero!)")
        return
    return a / b

print("Select operation.")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

try:

    choice = int(input("Enter choice: "))

    if choice == 1:
        print("=", addition())
    elif choice == 2:
        print("=", subtraction())
    elif choice == 3:
        print("=", multiplication())
    elif choice == 4:
        print("=", division())
    elif choice > 4:
        print("Pick only 1 to 4!")
        
except ValueError:
        print("Please enter a numeric value.")