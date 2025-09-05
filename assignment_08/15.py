#15. Write a program that writes user input to a file. Handle cases where the file cannot be opened (e.g., invalid file path).
try:
    filename= "user.txt"
    with open("user.txt", "w") as file:
        text= input("Enter text to write into file: ")
        file.write(text)
    print(f"Data written to {filename} successfully")
except OSError:
    print("Error: Could not be opened or written to file")