import random

def play_game():
    nickname = input("Введите ваш никнейм: ")
    print("Правила игры: ПК загадывает 4-значное число, вы должны угадать хотя бы одну цифру из него.")
    print("За каждую угаданную цифру начисляется 10 очков. У вас 3 жизни.")
    
    score = 0
    lives = 3
    record = 0
    
    while lives > 0:
        pc_number = str(random.randint(1000, 9999))
        user_guess = input("Введите число от 0 до 9: ")
        
        if user_guess in pc_number:
            score += 10
            print("Поздравляем! +10 очков")
        else:
            lives -= 1
            print(f"Неверно! Осталось жизней: {lives}")
        
        if score > record:
            record = score
        
    print(f"Игра окончена. Набранные очки: {score}, Рекорд: {record}")
    
    repeat = input("Хотите сыграть еще раз? (да/нет): ")
    if repeat.lower() == "да":
        play_game()
    else:
        print("Спасибо за игру!")

play_game()