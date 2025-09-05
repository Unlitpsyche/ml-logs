#10. Write a program to divide two numbers given by the user. Handle the case when the denominator is 0 using try-except and display a friendly message
print("Q10 Output:")
try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denominator: "))
    result = a / b
    print("Result =", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.\n")