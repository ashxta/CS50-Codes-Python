user_answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything")
user_answer = user_answer.strip()
if user_answer == "42" or user_answer == "forty-two" or user_answer == "forty two" or user_answer == " 42 " or user_answer == "FoRty TwO":
    print("Yes")
else:
    print("No")

