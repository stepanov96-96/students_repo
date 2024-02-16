import random

def generate_number():
    number = []
    while len(number) < 4:
        digit = random.randint(0, 9)
        if digit not in number:
            number.append(digit)
    return number

def check_input(user_input):
    if len(user_input) != 4:
        return False
    if not user_input.isdigit():
        return False
    if len(set(user_input)) < 4:
        return False
    return True

def get_bulls_and_cows(secret_number, user_input):
    bulls = 0
    cows = 0
    for i in range(4):
        if user_input[i] == str(secret_number[i]):
            bulls += 1
        elif user_input[i] in str(secret_number):
            cows += 1
    return bulls, cows

def main():
    print("Добро пожаловать!")
    nickname = input("Введите свой никнейм: ")
    print(f"Привет, {nickname}!")
    print("Правила игры:")
    print("Компьютер загадывает 4-значное число.")
    print("Ваша задача - угадать хотя бы 1 число из этого числа.")
    print("За каждое угаданное число вам начисляется 10 очков.")
    print("Если вы не угадываете число, у вас отнимается одна жизнь.")
    print("У вас есть 3 жизни.")
    print("В любой момент вы можете выйти из игры, нажав клавишу 'E'.")
    print("Удачи!")
    
    play_again = True
    record = 0
    
    while play_again:
        secret_number = generate_number()
        score = 0
        lives = 3
        
        while lives > 0:
            user_input = input("Введите 4-значное число: ")
            
            if user_input == "E":
                print(f"Ваш рекорд: {record}")
                play_again = False
                break
            
            if not check_input(user_input):
                print("Ошибка! Введите 4-значное число без повторяющихся цифр.")
                continue
            
            bulls, cows = get_bulls_and_cows(secret_number, user_input)
            
            if bulls > 0:
                score += 10
                print(f"Поздравляю! Вы угадали {bulls} числ{'о' if bulls == 1 else 'а'}!")
                
                if score > record:
                    record = score
                
                if score == 40:
                    break
            else:
                lives -= 1
                print("Неудача! Попробуйте еще раз.")
                if lives > 0:
                    print(f"У вас осталось {lives} {'жизнь' if lives == 1 else 'жизни'}.")
        
        if lives == 0:
            print(f"Игра окончена. Ваш счет: {score}, рекорд: {record}")
        
        choice = input("Хотите сыграть еще раз? (да/нет): ")
        if choice.lower() != "да":
            play_again = False
    
    print("Спасибо за игру! До встречи!")

if __name__ == "__main__":
    main()