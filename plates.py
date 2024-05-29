def main():
    print("Vanity Plates Testing:")
    test_plates = ["ABC123", "abcdefg1", "A12345", "a12345", "ABCDEF1", "1234567", "7654321"]
    for plate in test_plates:
        print(f"{plate}: {is_valid(plate)}")

def is_valid(s):
    if not s.isalpha() and not s.isdigit():
        return False
    if s.isalpha():
        s = s.upper()
    return True

if __name__ == "__main__":
    main()