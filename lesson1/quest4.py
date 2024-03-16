num1 = input('Введите число №1: ')
num2 = input('Введите число №2: ')
s = int(num1) + int(num2)
try:
    int(s)
    return True
except ValueError:
    return False
print (s)
