#1. Write a program to create a text file named notes.txt and write the line ”Python file handling is easy!” into it.
file = open("notes.txt", "w")
file.write("Python file handling is easy!")
file.close()

print("notes.txt created and text written successfully")