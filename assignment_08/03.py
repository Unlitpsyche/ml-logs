#3. Write a program that reads a file and counts the number of words, characters, and lines in it.
filename = "multilines.txt"
with open(filename, "r") as f:
    lines = f.readlines()
total_lines = len(lines)
total_words = sum(len(line.split()) for line in lines)
total_chars = sum(len(line) for line in lines)
print(total_lines)
print(total_words)
print(total_chars)
