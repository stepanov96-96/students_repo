class TaskManager:
    def __init__(self):
        self.tasks = {"backlog": [], "в работе": [], "выполнено": []}
        self.loaded_from_file = False
        self.load_tasks_from_file()

    def add_task(self, title, description):
        task = {"title": title, "description": description}
        self.tasks["backlog"].append(task)
        print("Задача добавлена в backlog.")

    def display_tasks(self, category=None):
        if category:
            tasks = self.tasks[category]
            if not tasks:
                print(f'Задачи "{category}" пусты.')
                return
            print(f'\nЗадачи "{category}":')
            for i, task in enumerate(tasks, start=1):
                print(f'{i}. {task["title"]} - {task["description"]}')
        else:
            for category, tasks in self.tasks.items():
                if not tasks:
                    print(f'Задачи "{category}" пусты.')
                    continue
                print(f'\nЗадачи "{category}":')
                for i, task in enumerate(tasks, start=1):
                    print(f'{i}. {task["title"]} - {task["description"]}')

    def display_categories(self):
        for i, category in enumerate(self.tasks.keys(), start=1):
            print(f'{i}. {category}')
        if not any(task_list for task_list in self.tasks.values()):
            print("Категории задач пусты.")

    def edit_tasks_menu(self):
        while True:
            self.display_categories()
            print("\nРедактировать задачи - Выберите категорию")
            print("0. Вернуться в предыдущее меню")

            category_number = int(input("Выберите номер категории (0 для выхода): ")) - 1

            if category_number == -1:
                break

            if 0 <= category_number < len(self.tasks):
                category = list(self.tasks.keys())[category_number]
                self.edit_tasks(category)
            else:
                print("Некорректный номер категории.")

    def edit_tasks(self, category):
        while True:
            self.display_tasks(category)
            print("\nРедактировать задачи")
            print("1. Изменить название")
            print("2. Изменить описание")
            print("3. Изменить категорию")
            print("4. Удалить задачу")
            print("5. Вернуться в предыдущее меню")

            choice = input("Выберите действие (1-5): ").strip()

            if choice == '1':
                self.edit_task_menu(category, "title")
            elif choice == '2':
                self.edit_task_menu(category, "description")
            elif choice == '3':
                self.edit_task_category_menu(category)
            elif choice == '4':
                self.remove_task_menu(category)
            elif choice == '5':
                break
            else:
                print("Некорректный ввод. Пожалуйста, выберите от 1 до 5.")

    def edit_task_menu(self, category, field):
        while True:
            self.display_tasks(category)
            print(f"\nРедактировать задачи - Изменить {field}")

            task_number = int(input("Введите номер задачи для редактирования (0 для выхода): ")) - 1

            if task_number == -1:
                break

            tasks = self.tasks[category]
            if 0 <= task_number < len(tasks):
                task = tasks[task_number]
                new_value = input(f"Введите новое {field} задачи: ")
                task[field] = new_value
                print(f"{field.capitalize()} задачи успешно изменено.")
            else:
                print("Некорректный номер задачи.")

    def edit_task_category_menu(self, old_category):
        while True:
            self.display_tasks(old_category)
            print("\nРедактировать задачи - Изменить категорию")

            task_number = int(input("Введите номер задачи для изменения категории (0 для выхода): ")) - 1

            if task_number == -1:
                break

            task, _ = self.get_task_by_number(task_number, old_category)
            if task:
                print(f'Выбранная задача: {task["title"]} - {task["description"]}')
                print("Выберите новую категорию для задачи:")
                self.display_categories()
                new_category_number = int(input("Введите номер категории (1-3): ")) - 1

                if 0 <= new_category_number < len(self.tasks):
                    new_category = list(self.tasks.keys())[new_category_number]
                    self.move_task(task_number, old_category, new_category)
                    print(f'Задача "{task["title"]}" успешно перемещена в категорию "{new_category}".')
                else:
                    print("Некорректный номер категории.")
            else:
                print("Некорректный номер задачи.")

    def remove_task_menu(self, category):
        while True:
            self.display_tasks(category)
            print("\nРедактировать задачи - Удалить задачу")

            task_number = int(input("Введите номер задачи для удаления (0 для выхода): ")) - 1

            if task_number == -1:
                break

            task, _ = self.get_task_by_number(task_number, category)
            if task:
                self.remove_task(task_number, category)
                print(f'Задача "{task["title"]}" успешно удалена.')
            else:
                print("Некорректный номер задачи.")

    def move_task_menu(self, category):
        while True:
            self.display_tasks(category)
            print("\nРедактировать задачи - Переместить задачу в другую категорию")

            task_number = int(input("Введите номер задачи для перемещения (0 для выхода): ")) - 1

            if task_number == -1:
                break

            task, _ = self.get_task_by_number(task_number, category)
            if task:
                print(f'Выбранная задача: {task["title"]} - {task["description"]}')
                print("Выберите новую категорию для задачи:")
                self.display_categories()
                new_category_number = int(input("Введите номер категории (1-3): ")) - 1

                if 0 <= new_category_number < len(self.tasks):
                    new_category = list(self.tasks.keys())[new_category_number]
                    self.move_task(task_number, category, new_category)
                    print(f'Задача "{task["title"]}" успешно перемещена в категорию "{new_category}".')
                else:
                    print("Некорректный номер категории.")
            else:
                print("Некорректный номер задачи.")

    def get_task_by_number(self, task_number, category):
        tasks = self.tasks[category]
        if 0 <= task_number < len(tasks):
            return tasks[task_number], category
        return None, None

    def move_task(self, task_number, old_category, new_category):
        task, _ = self.get_task_by_number(task_number, old_category)
        if task:
            self.tasks[old_category].pop(task_number)
            self.tasks[new_category].append(task)

    def remove_task(self, task_number, category):
        task, _ = self.get_task_by_number(task_number, category)
        if task:
            self.tasks[category].pop(task_number)

    def load_tasks_from_file(self):
        try:
            with open("tasks.txt", "r", encoding="utf-8") as file:
                lines = file.readlines()

            if not lines:
                raise ValueError("Файл с задачами пуст.")

            cleaned_lines = []
            for line in lines:
                clean_line = line.strip()
                if not clean_line:
                    continue

                parts = clean_line.split(";")
                if len(parts) != 3:
                    print(f"Некорректная строка в файле: {clean_line}. Пропущена.")
                    continue

                category, title, description = parts[0].strip(), parts[1].strip(), parts[2].strip()
                if not category or not title or not description:
                    print(f"Некорректная строка в файле: {clean_line}. Пропущена.")
                    continue

                cleaned_lines.append(clean_line)
                self.tasks[category].append({"title": title, "description": description})

            if cleaned_lines:
                with open("tasks.txt", "w", encoding="utf-8") as file:
                    file.write('\n'.join(cleaned_lines))

            self.loaded_from_file = True
            print("Задачи успешно загружены.")
        except FileNotFoundError:
            print("Файл с задачами не найден. Создан новый файл 'tasks.txt'.")
        except ValueError as e:
            print(f"Ошибка при загрузке задач: {e}")

    def save_tasks_to_file(self):
        with open("tasks.txt", "w", encoding="utf-8") as file:
            for category, tasks in self.tasks.items():
                for task in tasks:
                    file.write(f"{category};{task['title']};{task['description']}\n")

    def print_menu(self):
        print("\nМеню:")
        print("1. Добавить задачу")

        if any(task_list for task_list in self.tasks.values()):
            print("2. Просмотреть и редактировать задачи")

        print("3. Выйти")

    def run(self):
        while True:
            self.print_menu()
            choice = input("Выберите действие (1-3): ").strip()

            if choice == '1':
                title = input("Введите название задачи: ")
                description = input("Введите описание задачи: ")
                self.add_task(title, description)
            elif choice == '2' and any(task_list for task_list in self.tasks.values()):
                self.edit_tasks_menu()
            elif choice == '3':
                self.save_tasks_to_file()
                print("Выход из программы. До свидания!")
                break
            else:
                print("Некорректный ввод. Пожалуйста, выберите от 1 до 3.")


if __name__ == "__main__":
    task_manager = TaskManager()
    task_manager.run()
