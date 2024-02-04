odin, dva, znak = int(input()), int(input()), input()
if znak == "/":
    if dva == 0:
        print("На ноль делить нельзя!")
    elif odin == 0:
        print(0.0)
    else:
        print(odin / dva)
if znak == "-":
    print(odin - dva)
if znak == "+":
    print(odin + dva)
if znak == "*":
    print(odin * dva)
if znak != "/" and znak != "*" and znak != "+" and znak != "-":
    print("Неверная операция")