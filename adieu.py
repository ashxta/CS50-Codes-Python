def bid_adieu(names):
    if len(names) == 1:
        return f"Adieu, adieu, to {names[0]}"
    elif len(names) == 2:
        return f"Adieu, adieu, to {names[0]} and {names[1]}"
    else:
        farewell = ", ".join(names[:-1]) + f", and {names[-1]}"
        return f"Adieu, adieu, to {farewell}"

def main():
    names = []

    try:
        while True:
            name = input("Enter a name (or press Ctrl-D to finish): ").strip()
            if name:
                names.append(name)
            else:
                print("Invalid name. Please try again.")
    except EOFError: 
        if not names:
            print("No names entered.")
        else:
            for i in range(1, len(names) + 1):
                farewell = bid_adieu(names[:i])
                print(farewell)

if __name__ == "__main__":
    main()
