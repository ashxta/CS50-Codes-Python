def value(greeting):
    greeting = greeting.lower()  # Convert the input to lowercase for case-insensitive comparison

    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100

def main():
    greeting = input("Enter a greeting: ")
    result = value(greeting)
    print(f"Value: {result}")

if __name__ == "__main__":
    main()
