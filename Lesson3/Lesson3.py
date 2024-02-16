import random

def get_player_name():
    return input('Введите ваше имя: ')

def check_player_name(name):
    print()
    response = input(f'{name}, хотите изменить имя? (да/нет): ')
    return response.lower() == 'нет'

def play_again():
    response = input('Хотите сыграть ещё раз? (да/нет): ')
    return response.lower() == 'да'

def show_rules():
    print()
    print(f'{player_name}, добро пожаловать в азартную игру "Числовая Фортуна"! Правила просты:')
    print('→ Я загадываю 4-х значное число, и ваша задача – угадать одну его цифру.')
    print('→ За каждую правильно угаданную цифру вы получаете 10 Social Credit.')
    print('→ Всего у вас есть 3 жизни. Если вы не угадываете число, то теряете одну, ошибаетесь три раза – проигрываете.')
    print('Чтобы выйти из игры, напишите "E".')

player_name = get_player_name()
show_rules()

while True:
    score = 0
    lives = 3

    while lives > 0:
        random_number = str(random.randint(1000, 9999))

        print()
        guess = input('Введите число от 0 до 9: ')

        if guess.upper() == 'E':
            print()
            print(f'Игра окончена. Ваш рекорд: {score} Social Credit.')
            break

        if not guess.isdigit() or len(guess) != 1:
            print('Боже, что вы за ****?!!! НАПИСАНО ЖЕ ПРОСТЫМИ СЛОВАМИ!!! Вы должны ввести одно число от 0 до 9!!!')
            continue

        if guess in random_number:
            print(f'Вы угадали число. Загаданное число было: {random_number}')
            score += 10
            print(f'Ваш текущий счёт: {score} Social Credit.')
        else:
            print(f'К сожалению, вы не угадали. Загаданное число было: {random_number}')
            lives -= 1
            print(f'Осталось жизней: {lives}')

    if lives == 0:
        print()
        print(f'Игра окончена. Ваш счёт: {score} Social Credit.')

        try:
            with open('Lesson3_RecordFile.txt', 'r') as file:
                record = int(file.read())
        except FileNotFoundError:
            record = 0

        if score > record:
            record = score
            with open('Lesson3_RecordFile.txt', 'w') as file:
                file.write(str(record))
            print('Поздравляем! Вы установили новый рекорд!')
        else:
            print(f'Ваш рекорд остаётся {record} Social Credit.')

    if not play_again():
        print()
        print('Спасибо за игру. До свидания!')
        break

    if not check_player_name(player_name):
        player_name = get_player_name()

    response = input('Повторить правила игры? (да/нет): ')
    if response.lower() == 'да':
        show_rules()
