    
import math

try:
# Take integer input from the user
    number = int(input("Enter a number :"))
# Square root is calculated using absolute value to avoid errors
    abs_number = abs(number)
    print(f"Square root of {abs_number} is {math.sqrt(abs_number)}")

# Logarithm is defined only for positive numbers
    if number > 0:
        print(f"Log of {number} is {math.log(number)}")
    else:
        print("Logarithm is not defined for zero or negative numbers.")
# Sine calculation (works for all real numbers)
    radians = math.radians(number)
    print(f"Sin of {number} is {math.sin(radians)}")
except ValueError:
# Handling non-integer input
    print("Invalid input. Please enter an integer.")
