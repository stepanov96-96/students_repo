import random

questions = {}

def add_question():
    print("Добро пожаловать в программу! Здесь вы можете добавить вопрос и его ответ в словарь.")
    question = input("Введите вопрос: ")
    answer = input("Введите ответ: ")
    
    questions[question] = answer
    print("Вопрос успешно добавлен в словарь!")

def edit_question():
    print("Вы можете изменить ответ на существующий вопрос в словаре.")
    question = input("Введите вопрос, который нужно отредактировать: ")
    if question in questions:
        new_answer = input("Введите новый ответ: ")
        questions[question] = new_answer
        print("Вопрос успешно отредактирован!")
    else:
        print("Вопрос не найден.")

def delete_question():
    print("Удаление вопроса из словаря.")
    question = input("Введите вопрос, который нужно удалить: ")
    if question in questions:
        del questions[question]
        print("Вопрос успешно удален из словаря!")
    else:
        print("Вопрос не найден.")

def random_question():
    print("Давайте выберем случайный вопрос из словаря.")
    if len(questions) > 0:
        question = random.choice(list(questions.keys()))
        print("Случайный вопрос:")
        print(question)
    else:
        print("Словарь пуст. Добавьте вопросы перед тем, как выбрать случайный вопрос.")

while True:
    print("Меню:")
    print("1. Добавить вопрос")
    print("2. Редактировать вопрос")
    print("3. Удалить вопрос")
    print("4. Случайный вопрос")
    print("5. Выйти")

    choice = input("Выберите пункт меню: ")

    if choice == "1":
        add_question()
    elif choice == "2":
        edit_question()
    elif choice == "3":
        delete_question()
    elif choice == "4":
        random_question()
    elif choice == "5":
        break
    else:
        print("Некорректный выбор. Попробуйте еще раз.")

print("Спасибо за использование программы!")