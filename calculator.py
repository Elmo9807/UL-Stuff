def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide (a, b):
    return a / b

inp = input("Welcome, please choose an operation to perform:")
print("A. Add")
print("B. Subtract")
print("C. Multiply")
print("D. Divide")
print('You have chosen:',inp)

continue_calculating = True
while continue_calculating is True:
    choice = input("Enter operation(A/B/C/D):")
    
    if choice in ('A', 'B', 'C', 'D'):
        try:
            num1 = float(input("Enter first value:"))
            num2 = float(input("Enter second value:"))
        except ValueError:
            print("Bad input, please enter a number value.")
            continue
        if choice == 'A':
            print(num1, "+", num2, "=", add(num1, num2))
        elif choice == 'B':
            print(num1, "-", num2, "=", subtract(num1, num2))
        elif choice == 'C':
            print(num1, "*", num2, "=", multiply(num1, num2))
        elif choice == 'D':
            print(num1, "/", num2, "=", divide(num1, num2))
            
        yes_or_no = input('Continue? (y/n): ')
        if yes_or_no == 'n':
            continue_calculating = False