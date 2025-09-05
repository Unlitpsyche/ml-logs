#13. Write a program to open a file, read its contents, and handle FileNotFoundError. Ensure that a message like ”File operation complete” is printed using finally.
try:
    with open("don't_exist.txt", "r") as file:
        data = file.read()
except FileNotFoundError:
    print("File not found!")
finally:
    print("File operation complete.")