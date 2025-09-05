#14. Write a program to take age as input. If age is less than 18, raise a ValueError with the message ”Age must be 18 or above.”
try:
    age= int(input("Enter your age: "))
    if age < 18:
        raise ValueError("Age must be 18 or above.")
    print("Valid age: ", age)
except ValueError as e:
    print("Error: ",e)