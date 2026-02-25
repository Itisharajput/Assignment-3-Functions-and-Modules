number = int(input("Enter a number:"))
num = abs(number)
def factorial(num):
"""
Calculate factorial of a non-negative integer using recursion
"""
    if num == 1 or n == 0 :
        return 1
    else:
        num_factorial = num * factorial(num-1)
        return num_factorial
    
print(f" Factorial of {num} is {factorial(num)}")
