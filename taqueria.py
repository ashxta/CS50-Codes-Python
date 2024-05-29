menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    order = []
    total_cost = 0.0

    try:
        while True:
            item = input("Enter an item from the menu (or press Ctrl-D to finish): ").strip().title()

            if item in menu:
                order.append(item)
                total_cost += menu[item]
                print(f"Total Cost: ${total_cost:.2f}")
            else:
                print("Item not found on the menu. Please try again.")

    except EOFError: 
        if order:
            print("Your order:")
            for item in order:
                print(item)
            print(f"Total Cost: ${total_cost:.2f}")
        else:
            print("No items ordered.")

if __name__ == "__main__":
    main()
