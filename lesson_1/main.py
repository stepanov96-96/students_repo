import math

#################################################

name = input("введите ваше имя: ")
age = input("введите ваш возраст: ")
print(f"привет, {name}! тебе {age} лет.")
print(f"Name: {type(name)}")
print(f"Age: {type(age)}")

#################################################

num1 = float(input("введите первое число: "))
num2 = float(input("введите второе число: "))
sum_result = num1 + num2
difference_result = num1 - num2
product_result = num1 * num2
if num2 != 0:
    division_result = num1 / num2
    remainder_result = num1 % num2
else:
    division_result = "деление на ноль невозможно"
    remainder_result = "деление на ноль невозможно"
print(f"сложение: {sum_result}")
print(f"вычитание: {difference_result}")
print(f"умножение: {product_result}")
print(f"деление: {division_result}")
print(f"остаток от деления: {remainder_result}")

##################################################

radius = float(input("введите радиус круга: "))
area = math.pi * math.pow(radius, 2)
print(f"площадь круга с радиусом {radius} равна {area}")

##################################################

num1_str = input("введите первое число: ")
num2_str = input("введите второе число: ")
num1 = int(num1_str)
num2 = int(num2_str)
sum_result = num1 + num2
print(f"cумма: {sum_result}")

################################################################

number = float(input("Введите число: "))
even = number % 2 == 0
positive = number > 0
if even and positive:
    print("введенное число является четным и положительным")
else:
    print("не соответствует четным и положительным")
