# здесь я исправил: оформление, логику, добавил постоянные очки, которые сбрасываются когда пользователей заканчивает сеанс, также после окончания игры - открывается меню
import random

def privet():
    nick = input("Введите ник: ")
    print(f"Привет, {nick}! В этой игре тебе нужно угадать число, вводя цифры.")
    
noll = 0

def menu():
    global noll
    print("---------------------")
    print("1. Start")
    print("2. Pravila")
    print("3. Record")
    print("4. Exit")
    print("---------------------")
    
    a = input()
    if a == '1' or a.lower() == "старт" or a.lower() == "start":
        guess_number()
    elif a == '2':
        print("В этой игре тебе нужно угадать мое четырехзначное число, используя только цифры. Также у тебя всего 3 жизни.")
        print("Back (e)")
        b = input().lower()
        if b == "e":  
            menu()
        else:
            menu()
    elif a == "3":
        print(noll)
        menu()
    elif a == '4' or a.lower() == "e":
        print("Пока :(")

def guess_number():
    global noll
    number = str(random.randint(1000, 9999))
    attempts = 0
    life = 3
    
    print("Я загадал число, попробуй угадать в нем одну цифру!")
    while life > 0:
        guess = input("Моя цифра - ")
        if guess.isdigit() and len(guess) == 1:
            attempts += 1
            if guess in number:
                print("Ты угадал цифру!", end="\n\n")
                noll += 10
                if noll == len(number) * 10:
                    print(f"Поздравляю, ты угадал все цифры числа {number} за {attempts} попыток! Очки: {noll}")
                    break
            else:
                print("Промах, давай еще.", end="\n\n")
                life -= 1
                print(f"У тебя осталось {life} жизней.")
        else:
            print("Введи ОДНУ цифру и не букву")

    if life == 0:
        print(f"Ты проиграл :( Загаданное число было: {number}")
    menu()

privet()
menu()
