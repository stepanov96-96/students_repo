import random

def generate_number():
    return [random.randint(0, 9) for _ in range(4)]

def check_guess(secret_number, guess):
    points = 0
    for digit in guess:
        if digit in secret_number:
            points += 10
    return points

def main():
    print("Добро пожаловать в игру Угадай Число!")
    name = input("Введите ваш никнейм: ")
    print(f"Привет, {name}! Правила игры: угадайте хотя бы одну цифру из числа, загаданного компьютером.")
    print("Вы можете выйти из игры, нажав клавишу 'E'.")
    
    high_score = 0
    lives = 3
    
    while True:
        secret_number = generate_number()
        print("Компьютер загадал число. Введите вашу догадку:")
        guess = input()
        
        if guess == 'E':
            print(f"Ваш рекорд: {high_score}")
            break
        
        guess = [int(digit) for digit in guess if digit.isdigit()]
        
        points = check_guess(secret_number, guess)
        if points > 0:
            print(f"Вы угадали и заработали {points} очков.")
            high_score += points
        else:
            lives -= 1
            print(f"У вас осталось {lives} жизней.")
        
        if lives == 0:
            print(f"Игра окончена. Ваш счет: {high_score}. Ваш рекорд: {high_score}")
            choice = input("Хотите сыграть еще раз? (да/нет): ")
            if choice.lower() != 'да':
                break
            else:
                lives = 3

if __name__ == "__main__":
    main()