import random

def generate_number():
    return str(random.randint(0, 9))
nickname = input("Введите ваш никнейм: ")
def show_menu():
    print("Меню:")
    print("1. Начать игру")
    print("2. Правила игры")
    print("3. Выйти отсюда..")

def handle_menu_choice(current_high_score, nickname):
    choice = input("Выберите действие (1-3): ")
    if choice == '1':
        play_game(current_high_score, nickname)
    elif choice == '2':
        print("Правила игры: Угадайте хотя бы одну цифру из четырех, которые загадал ПК.")
    elif choice == '3':
        return False
    else:
        print("Некорректный выбор. Попробуйте еще раз.")

    return True

def play_game(current_high_score, nickname):
    lives = 3
    score = 0

    print(f"Добро пожаловать, {nickname}, в игру 'Угадай число'!")

    while lives > 0:
        pc_number = ''.join([generate_number() for _ in range(4)])
        print("ПК загадал число. У вас", lives, "healthpoint.")

        user_input = input("Введите четырехзначное число: ")

        correct_digits = sum([1 for i in range(4) if user_input[i] in pc_number])
        print("Вы угадали", correct_digits, "цифр.")

        score += correct_digits * 10
        if correct_digits > 0:
            print("Хорошая попытка")
            if score > current_high_score:
                current_high_score = score
        else:
            lives -=1

    print("Игра окончена. Вы набрали", score, "очков. Ваш текущий рекорд:", current_high_score)

    play_again = input("Хотите сыграть еще раз? (да/нет): ")
    if play_again.lower() == 'да':
        play_game(current_high_score, nickname)
    else:
        print("Спасибо за игру!")

high_score = 0
while True:
    show_menu()
    continue_playing = handle_menu_choice(high_score, nickname)
    if not continue_playing:
        break