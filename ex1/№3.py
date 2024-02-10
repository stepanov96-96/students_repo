import math
print("Введите радиус круга:")
a = float(input())
b = math.pi * a ** 2 #я не знаю будет ли придирка к этому, но  мне было легче сделать через **, а не math.sqrt()
b = round(b, 2)
print(f"Площадь круга равна: {b}")