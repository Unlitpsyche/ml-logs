#6. Write a program to count the number of lines in a file.
file = open("multilines.txt", "r")
lines = file.readlines()
file.close()

print("Number of lines in file:", len(lines))