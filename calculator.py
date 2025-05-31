def calculate(num1, num2, operation):
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        return "Invalid input. Please enter numbers."

    if operation == "Addition":
        return num1 + num2
    elif operation == "Subtraction":
        return num1 - num2
    elif operation == "Multiplication":
        return num1 * num2
    elif operation == "Division":
        if num2 == 0:
            return "Error: Division by zero."
        return num1 / num2
    else:
        return "Unsupported operation."