#9. Write a program that writes a list of numbers [10, 20, 30, 40, 50] to a file (one per line), then reads the file and prints the numbers as a list
numbers = [10, 20, 30, 40, 50]

file = open("numbers.txt", "w")
for num in numbers:
    file.write(str(num) + "\n")
file.close()

file = open("numbers.txt", "r")
read_numbers = []
for line in file:
    read_numbers.append(int(line.strip()))
file.close()

print("Numbers read from file:", read_numbers)