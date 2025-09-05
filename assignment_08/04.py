#4. Write a program that asks the user for a word and searches for it in a text file, printing the line numbers where it appears.
word = input("Enter a word to search: ")

file = open("multilines.txt", "r")
line_num = 1
found = False

for line in file:
    if word in line:
        print("Found in line", line_num, ":", line.strip())
        found = True
    line_num += 1

file.close()

if not found:
    print("Word not found in file.")