number = int(input("Enter a number:"))
num = abs(number)
def factorial(num):
    if num == 1:
        return 1
    else:
        num_factorial = num * factorial(num-1)
        return num_factorial
    
print(f" Factorial of {num} is {factorial(num)}")
