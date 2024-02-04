print("вВЕДИТЕ ЧИСЛО")
a = int(input())
if a // 2 == 0 and a > 0:
    print("Число положительное и четное")
elif a // 2 != 0 or a <= 0:
    print("Число не то")