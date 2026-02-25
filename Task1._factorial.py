def factorial(num):
       """
Calculate factorial of a non-negative integer using recursion
 """
       if num == 1 or num == 0 :
           return 1
       else:
    # Calling the function using recursion
           num_factorial = num * factorial(num-1)
       return num_factorial
try :
    num = int(input("Enter a number :"))
    if num < 0:
              print("Factorial is not defined for negative numbers.")
    else:
              print(f"Factorial of {num} is {factorial(num)}")
except ValueError:
    print("Invalid input. Please enter an integer.")
   
