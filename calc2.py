odin, dva, znak = int(input()), int(input()), input()
if znak == "/":
    if dva == 0:
        print("На ноль делить нельзя!")
    elif odin == 0:
        print(0.0)
    else:
        print(odin / dva)
elif znak == "-":
    print(odin - dva)
elif znak == "+":
    print(odin + dva)
elif znak == "*":
    print(odin * dva)
elif znak != "/" and znak != "*" and znak != "+" and znak != "-":
    print("Неверная операция")
