import random

def game():
    name = input("Введите свой ник: ")
    print("Добро пожаловать, " + name + "!")
    print("Правила игры:")
    print("Программа загадывает 4-х значное число.")
    print("Тебе же нужно угадать одну из цифр от 1 до 9.")
    print("У тебя всего 3 жизни. После каждой ошибки вычитается одна из них.")
    print("Если же ты угадаешь число, то тебе будут начислены 10 очков!")
    print("Также ты можешь выйти их игры с помощью клавиши E.")

    record = 0

    while True:
        number = str(random.randint(1000, 9999))
        lives = 3
        points = 0
        print("Постарайся угадать одну из цифр!")

        while lives > 0:
            print("* * * *")
            guess = input("Введите цифру от 0 до 9: ")

            if guess.lower() == "E":
                print("Выход из игры...")
                break

            if guess in number:
                print("Верно! На твой счет начислены 10 очков!.")
                points += 10
            else:
                print("Не верно:( -1 жизнь.")
                lives -= 1
                print("У тебя осталось", lives, "жизней.")

            if points > record:
                record = points

        if lives == 0:
            print("Game over! Ты набрал", points, "очков!")

        play_again = input("Хотите сыгрвть ещё раз? (y/n): ")
        if play_again.lower() != "y":
            print("Твой рекорд", record, "очков!")
            break

game()
