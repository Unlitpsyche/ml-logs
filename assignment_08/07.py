#7. Write a program to search for the line numbers that contain a given word.
search_word = "Line"
print("Q7 Output: Searching for word:", search_word)
with open("multilines.txt", "r") as file:
    for i, line in enumerate(file, start=1):
        if search_word in line:
            print(f"Word found in line {i}")
print()