#11. Write a program to take two inputs from the user and perform division. Handle both ValueError (if user enters non-numeric input) and ZeroDivisionError.
try:
    a= int(input("ENter numerator"))
    b= int(input("ENter denominator"))
    result= a/b
    print(result)
except ValueError:
    print("Error:please eneter numeric value only")
except ZeroDivisionError:
    print("Error: Casnnot divide by zero")