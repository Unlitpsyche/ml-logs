#2. Create a text file with multiple lines. Write a program to read the file and print its content line by line.
with open("multilines.txt", "w") as f:
    f.write("Line 1: Python is fun\n")
    f.write("Line 2: File handling is easy\n")
    f.write("Line 3: Let's practice coding\n")

with open("multilines.txt", "r") as f:
    for line in f:
        print(line.strip())

