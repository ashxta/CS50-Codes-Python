fruits = {
        "apple": 130,
        "avocado": 50,
        "banana": 110,
        "cantaloupe": 50,
        "grapefruit": 60,
        "grapes": 90,
        "honeydew melon": 50,
        "kiwifruit": 90,
        "lemon": 15,
        "lime": 20,
        "nectarine": 60,
        "orange": 80,
        "peach": 60,
        "pear": 100,
        "pineapple": 50,
        "plumns": 70,
        "strawberries": 50,
        "sweet cherries": 100,
        "tangerine": 50,
        "watermelon": 80
}

a = input("Fruit: ").lower()

if a in fruits:
        print(f"Calories {fruits[a]}")
        def shorten(word):
    vowels = "AEIOUaeiou"
    # Use a list comprehension to filter out vowels from the word
    filtered_word = "".join(char for char in word if char not in vowels)
    return filtered_word

def main():
    word = input("Enter a word: ")
    shortened_word = shorten(word)
    print(f"Shortened word: {shortened_word}")

if __name__ == "__main__":
    main()
