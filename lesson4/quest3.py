import random
import string

def generate_password(length, use_digits, use_special_chars, use_uppercase):
    all_chars = string.ascii_lowercase
    if use_digits:
        all_chars += string.digits
    if use_special_chars:
        all_chars += string.punctuation
    if use_uppercase:
        all_chars += string.ascii_uppercase

    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

print("Программа генерации случайных паролей")

while True:
    try:
        length = int(input("Укажите длину пароля: "))
        use_digits = input("Использовать цифры (да/нет): ").lower() == 'да'
        use_special_chars = input("Использовать специальные символы (да/нет): ").lower() == 'да'
        use_uppercase = input("Использовать заглавные буквы (да/нет): ").lower() == 'да'

        password = generate_password(length, use_digits, use_special_chars, use_uppercase)
        print("Сгенерированный пароль:", password)

        another = input("Хотите сгенерировать еще один пароль? (да/нет): ")
        if another.lower() != 'да':
            print("Спасибо за использование программы!")
            break
    except ValueError:
        print("Ошибка: введите корректное целое число для длины пароля.")