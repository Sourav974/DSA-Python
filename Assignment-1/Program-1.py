""" 1. Write a program to reverse a number.
 Example: 123 -> 321 
"""


num = int(input("Enter the number "))
rev = 0
i = 1

while num != 0:
    n = num % 10
    rev = (10 * rev) + n
    num = num // 10

    
    
    
print("reverse is", rev)
