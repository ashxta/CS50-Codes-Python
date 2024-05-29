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
