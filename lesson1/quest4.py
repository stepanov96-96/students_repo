num1 = input('Введите число №1: ')
num2 = input('Введите число №2: ')
try:
    s = int(num1) + int(num2)
    int(s)
    print (s)
except ValueError:
    s = float(num1) + float(num2)
    print (s)
