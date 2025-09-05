#8. Create a program to count the number of words in a file
with open("multilines.txt", "r") as file:
    words = file.read().split()
print("Q8 Output: Total words =", len(words), "\n")