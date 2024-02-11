import random
import sys


def intro():
    print("добро пожаловать в игру угадай число!!!\n")
    nickname = input("Пожалуйста, введите ваш никнейм: ")
    print(f"\nпривет, {nickname}!")
    print("\nправила игры:")
    print("1. компьютер загадывает 4-значное число.\n2. ваша задача ввести число от 0 до 9 и угадать хотя бы одну цифру.\n3. если угадали - получаете 10 очков, если нет - теряете одну жизнь.\n4. у вас всего 3 жизни.\n5. для выхода из игры нажмите 'E'.\n")
    return nickname


def generate_number():
    return random.sample(range(10), 4)


def get_user_input():
    while True:
        user_input = input("введите число  от 0 до 9 или 'E' для выхода: ").strip().lower()
        if user_input == 'e':
            print("выход из игры")
            sys.exit()
        if user_input.isdigit() and 0 <= int(user_input) <= 9:
            return int(user_input)
        else:
            print("некорректный ввод! от 0 до 9")


def check_number(user_number, secret_number):
    return user_number in secret_number


def play_game():
    nickname = intro()
    best_score = 0
    play_again = 'да'

    while play_again.lower() == 'да':
        score = 0
        lives = 3
        while lives > 0:
            secret_number = generate_number()
            print("\nпк загадал новое число.")
            user_number = get_user_input()
            if check_number(user_number, secret_number):
                score += 10
                print(f"вы угадали! счет: {score}")
            else:
                lives -= 1
                print(f"не угадали. Осталось жизней: {lives}")
            if lives == 0:
                print(f"игра окончена, {nickname}. Ваш счет: {score}")
                if score > best_score:
                    best_score = score
                print(f"ваш рекорд: {best_score}")

        play_again = input("\nхотите сыграть еще раз? (да / нет): ")
        if play_again.lower() != 'да':
            print("Спасибо за игру!")
            break


if __name__ == "__main__":
    play_game()
