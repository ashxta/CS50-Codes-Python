def calculate_expression(x, operator, z):
    if operator == '+':
        return x + z
    elif operator == '-':
        return x - z
    elif operator == '*':
        return x * z
    elif operator == '/':
        if z != 0:
            return x / z
        else:
            print("Error: Division by zero is not allowed.")
            return None
    else:
        print(f"Error: Invalid operator '{operator}'")
        return None

def main():
    input_str = input("Enter an arithmetic expression : ")
    x, op, z = input_str.split()
    x = int(x)
    z = int(z)

    if op in "+-*/":
        result = calculate_expression(x, op, z)
        if result is not None:
            print(f"Result: {result:.1f}")
    else:
        print("Error: Invalid operator.")

if __name__ == "__main__":
    main()
