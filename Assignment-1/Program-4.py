# 4. Write a program to find the factorial of a given number.

n = int(input("Enter the no. "))
factorial = 1

if n < 0:
    print("Factorial of 0 is not exist")
    
elif n == 0:
    print('Factorial of 0 is 1')

else:
    for i in range(1, n+1):
        factorial = factorial * i
    print("The factorial of",n,"is",factorial)
    