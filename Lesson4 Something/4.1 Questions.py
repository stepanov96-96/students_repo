import random
import re

class QuizApp:
    def __init__(self):
        self.questions = {}
        self.loaded_from_file = False
        self.load_questions_from_file()

    def add_question(self, question, answers, manual=True):
        if question.lower() in [q["question"].lower() for q in self.questions.values()]:
            print("Такой вопрос уже существует. Вопросы должны быть уникальными.")
            return

        if not all(re.match(r'^[\w\s]+$', answer) for answer in answers):
            print("Некорректный формат ответов. В ответах могут быть только буквы, цифры и один пробел между ответами.")
            return

        question_number = len(self.questions) + 1
        self.questions[question_number] = {"question": question, "answers": answers}
        if manual:
            print("Вопрос добавлен.")

    def edit_question(self, question_number):
        if question_number in self.questions:
            print(f"\nМеню для вопроса №{question_number}:")
            print("1. Редактировать сам вопрос")
            print("2. Редактировать ответы")
            print("3. Вернуться к списку вопросов")

            choice = input("Выберите действие (1-3): ").strip()

            if choice == '1':
                new_question = input("Введите новый вопрос: ")
                self.questions[question_number]["question"] = new_question
                print(f'Вопрос №{question_number} успешно отредактирован.')
            elif choice == '2':
                new_answers = input("Введите новые ответы через запятую: ").split(',')
                self.questions[question_number]["answers"] = [answer.strip() for answer in new_answers]
                print(f'Ответы к вопросу №{question_number} успешно отредактированы.')
            elif choice == '3':
                return
            else:
                print("Некорректный ввод. Пожалуйста, выберите от 1 до 3.")
        else:
            print(f'Вопрос №{question_number} не найден.')

    def delete_question(self, question_number):
        if question_number in self.questions:
            del self.questions[question_number]
            print(f'Вопрос №{question_number} успешно удален.')
        else:
            print(f'Вопрос №{question_number} не найден.')

    def view_questions(self):
        if not self.questions:
            print("Нет добавленных вопросов.")
            return

        while True:
            print("\nСписок вопросов:")
            for question_number, data in self.questions.items():
                num_answers = len(data["answers"])
                if num_answers == 1:
                    answer_label = "Ответ"
                else:
                    answer_label = "Ответы"
                print(f"{question_number}. {data['question']} - {answer_label}: {', '.join(data['answers'])}")

            question_number = int(input("\nВведите номер вопроса для редактирования или удаления (0 для выхода): "))
            if question_number == 0:
                return
            elif question_number in self.questions:
                self.print_edit_delete_menu(question_number)
            else:
                print(f'Вопрос №{question_number} не найден.')

    def print_edit_delete_menu(self, question_number):
        print(f"\nМеню для вопроса №{question_number}:")
        print("1. Редактировать вопрос")
        print("2. Удалить вопрос")
        print("3. Вернуться к списку вопросов")

        choice = input("Выберите действие (1-3): ").strip()

        if choice == '1':
            self.edit_question(question_number)
        elif choice == '2':
            self.delete_question(question_number)
        elif choice == '3':
            pass
        else:
            print("Некорректный ввод. Пожалуйста, выберите от 1 до 3.")

    def ask_random_question(self):
        if not self.questions:
            print("Нет доступных вопросов.")
            return

        question_number = random.choice(list(self.questions.keys()))
        question_data = self.questions[question_number]

        user_answer = input(f'Вопрос №{question_number}: {question_data["question"]}\nВаши ответы: ').strip().lower()

        correct_answers = [answer.lower() for answer in question_data["answers"]]
        if user_answer in correct_answers:
            print('Правильный ответ!')
        else:
            print(f'Неправильный ответ. Правильные ответы: {", ".join(correct_answers)}')

    def load_questions_from_file(self):
        try:
            with open("questions.txt", "r", encoding="utf-8") as file:
                lines = file.readlines()

            if not lines:
                raise ValueError("Файл с вопросами пуст.")

            cleaned_lines = []
            for line in lines:
                clean_line = line.strip()
                if not clean_line:
                    continue

                parts = clean_line.split(";")
                if len(parts) < 2:
                    print(f"Некорректная строка в файле: {clean_line}. Пропущена.")
                    continue

                question = parts[0].strip()
                answers = [answer.strip() for answer in parts[1:]]
                if not question or not any(answers) or not all(re.match(r'^[\w\s]+$', answer) for answer in answers):
                    print(f"Некорректная строка в файле: {clean_line}. Пропущена.")
                    continue

                cleaned_lines.append(clean_line)
                self.add_question(question, answers, manual=False)

            if cleaned_lines:
                with open("questions.txt", "w", encoding="utf-8") as file:
                    file.write('\n'.join(cleaned_lines))

            self.loaded_from_file = True
            print("База вопросов загружена.")
        except FileNotFoundError:
            print("Файл с вопросами не найден. Создан новый файл 'questions.txt'.")
        except ValueError as e:
            print(f"Ошибка при загрузке вопросов: {e}")

    def save_questions_to_file(self):
        with open("questions.txt", "w", encoding="utf-8") as file:
            for question_number, data in self.questions.items():
                file.write(f"{data['question']};{' '.join(data['answers'])}\n")

    def print_menu(self):
        print("\nМеню:")
        print("1. Добавить вопрос")
        if self.questions:
            print("2. Список вопросов")
            print("3. Задать случайный вопрос")
        print("4. Выйти")

    def run(self):
        while True:
            self.print_menu()
            choice = input("Выберите действие (1-4): ").strip()

            if choice == '1':
                question = input("Введите новый вопрос: ")
                answers = input("Введите ответы через запятую: ").split(',')
                self.add_question(question, [answer.strip() for answer in answers])
            elif choice == '2' and self.questions:
                self.view_questions()
            elif choice == '3' and self.questions:
                self.ask_random_question()
            elif choice == '4':
                self.save_questions_to_file()
                print("Выход из программы. До свидания!")
                break
            else:
                print("Некорректный ввод. Пожалуйста, выберите от 1 до 4.")

if __name__ == "__main__":
    quiz_app = QuizApp()
    quiz_app.run()
