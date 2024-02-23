import random

def generate_number():
    return random.randint(0, 9)

def check_guess(secret_number, guess):
    points = 0
    for digit in guess:
        if digit in secret_number:
            points += 10
        return points

def main():
    print("Привет, давай сыграем в игру!")
    name = input("Введите ваш никнейм: ")
    print(f"Привет, {name}!")
    print("Твоя задача угадать хотя бы одну цифру из числа, которое загадал компьтер.")
    print("Вы можете выйти из игры нажатием кнопки 'E'")
    
    score = 0
    lives = 3

    while True:
        secret_number = [generate_number() for _ in range(4)]
        print("Компьютер загадал число, введите ваш ответ: ")
        guess = input()

        if guess == 'E':
            print (f"Ваш счёт: {score}")
            break
        
        guess = [int(digit) for digit in guess if digit.isdigit()]

        points = check_guess(secret_number, guess)
        if points > 0:
            print(f"Вы угадали и заработали {points} очков.")
            score += points
        else:
            lives -= 1
            print(f"Вы не угадали, у вас осталось {lives} жизней.")

            if lives == 0:
                print(f"Игра закончена, ваш счёт: {score}")
                break
main()


