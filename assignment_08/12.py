#12. Write a program that reads a number from the user and prints its square. Use try-except-else so that else runs only if no exception occurs.

try:
    num= int(input("Enter a number: "))
except ValueError:
    print("Error: Enter Valid number.")
else:
    print(num ** 2)