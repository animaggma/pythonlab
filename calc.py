def calculator():
    operations = {
        '1': ('+', lambda x, y: x + y),
        '2': ('-', lambda x, y: x - y),
        '3': ('*', lambda x, y: x * y),
        '4': ('/', lambda x, y: x / y if y != 0 else 'Error: Division by zero')
    }

    print("1: Addition (+)")
    print("2: Subtraction (-)")
    print("3: Multiplication (*)")
    print("4: Division (/)")

    choice = input("Choose an operation (1/2/3/4): ")

    if choice not in operations:
        print("Invalid selection.")
        return

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    operator, operation = operations[choice]
    result = operation(num1, num2)
    
    if result == 'Error: Division by zero':
        print(result)
    else:
        print(f"{num1} {operator} {num2} = {result}")

if __name__ == "__main__":
    calculator()
