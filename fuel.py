def convert(fraction):
    x, y = fraction.split('/')
    x = int(x)
    y = int(y)
    if x < 0 or y < 0 or x > y:
        raise ValueError("Invalid fraction")
    if y == 0:
        raise ZeroDivisionError("Division by zero")
    return round((x / y) * 100)

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

def main():
    while True:
        try:
            fuel = input("Enter fuel level as a fraction (e.g., 1/2): ")
            percentage = convert(fuel)
            result = gauge(percentage)
            print(f"The gauge reads: {result}")
        except (ValueError, ZeroDivisionError) as e:
            print(f"Error: {e}")