# Задание 1.
print('Задание 1.')
name = input('Введите ваше имя: ')
age = input('Введите ваш возраст: ')
print(f'Привет, {name}! Тебе {age} лет.')
print(type(name))
print(type(age))
print()

# Задание 2.
print('Задание 2.')
num1 = float(input('Введите первое число: '))
num2 = float(input('Введите второе число: '))
sum = num1 + num2
diff = num1 - num2
mult = num1 * num2
div = num1 / num2
mod = num1 % num2
print(f'Сложение: {sum}, вычитание: {diff}, умножение: {mult}, деление: {div}, остаток от деления: {mod}')
print()

# Задание 3.
print('Задание 3.')
import math
radius = float(input('Введите радиус круга: '))
area = math.pi * (radius ** 2)
print(f'Площадь круга с радиусом {radius} = {area}')
print()

# Задание 4.
print('Задание 4.')
num1 = input('Введите первое число: ')
num2 = input('Введите второе число: ')
num1 = float(num1)
num2 = float(num2)
sum = num1 + num2
print(f'Сумма чисел = {sum}')
print()

# Задание 5.
print('Задание 5.')
num1 = int(input('Введите число: '))
if num1 % 2 == 0 and num1 > 0:
    print('Ваше число чётное и положительное')
else:
    print('ну нет, так не пойдёт')
