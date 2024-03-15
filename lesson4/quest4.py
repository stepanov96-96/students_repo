tasks = {
    "бэклог": [],
    "в работе": [],
    "выполнено": []
}

def show_tasks():
    for status, task_list in tasks.items():
        print(f"{status}:")
        for index, task in enumerate(task_list, start=1):
            print(f"{index}. {task}")
        print()

def add_task():
    task = input("Введите новую задачу: ")
    tasks["бэклог"].append(task)
    print(f"Задача '{task}' добавлена в бэклог")

def move_task():
    show_tasks()
    from_status = input("Из какого столбца переместить задачу (бэклог, в работе, выполнено): ").lower()
    to_status = input("В какой столбец переместить задачу (бэклог, в работе, выполнено): ").lower()

    if from_status in tasks and to_status in tasks:
        task_index = int(input("Введите номер задачи для перемещения: ")) - 1
        
        if task_index < len(tasks[from_status]):
            task = tasks[from_status].pop(task_index)
            tasks[to_status].append(task)
            print(f"Задача '{task}' перемещена из '{from_status}' в '{to_status}'")
        else:
            print("Неверный номер задачи")
    else:
        print("Неверный столбец")

def delete_task():
    show_tasks()
    status = input("Выберите столбец, из которого удалить задачу (бэклог, в работе, выполнено): ").lower()
    
    if status in tasks:
        task_index = int(input("Введите номер задачи для удаления: ")) - 1
        
        if task_index < len(tasks[status]):
            task = tasks[status].pop(task_index)
            print(f"Задача '{task}' удалена из '{status}'")
        else:
            print("Неверный номер задачи")
    else:
        print("Неверный столбец")

if __name__ == '__main__':
    while True:
        print("\nМеню:")
        print("1. Показать задачи")
        print("2. Добавить задачу")
        print("3. Переместить задачу")
        print("4. Удалить задачу")
        print("5. Выйти")
        
        choice = input("Выберите действие: ")

        if choice == '1':
            show_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            move_task()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            break
        else:
            print("Неверный выбор. Попробуйте снова.")