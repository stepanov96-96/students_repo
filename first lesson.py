#1st 

name = str(input('Enter your name '))
age = int(input('Enter your age: '))

print(f'Hello, {name} you are {age} years old')

#2nd

a = int(input('Enter first number '))
b = int(input('Enter the second number: '))

print(f' sum - {a + b}\n diff - {a - b}\n multiplier - {{a * b}\n split - {a / b}\n remainder of division -{a % b})

#3rd

import math
r = int(input('Enter the Radius '))

print(f'S = {round(math.pi * r * 2,2)}')

#4th

import math
a = str(input('Enter first number '))
b = str(input('Enter the second number: '))

a = int(a); b = int(b)

print(f'sum - {a + b}')

#5th

n = int(input("Enter a number: "))

if n % 2 == 0 and n > 0:
    print("The number is even and positive")
else:
    print("The number is not even and positive")