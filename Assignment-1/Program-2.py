
# 2. Write a program to convert Celsius to Fahrenheit and vice versa.


option = int(input("Enter 1 or 2 "))
print()

if option == 1:
    temperature = int(input('Enter temp. in Farenheit '))
    faren_to_celcius = (temperature - 32) * 5/9
    print("Temp. in Celcius is: ", faren_to_celcius)
elif option == 2:
    temperature = int(input('Enter temp. in Celcius '))
    celcius_to_faren = (temperature * 1.8) + 32
    print("Temp. in Farenheit is: ", celcius_to_faren)
else:
    print('Invalid input')
    
    
