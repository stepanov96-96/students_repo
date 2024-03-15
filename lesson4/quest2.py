inventory = []

def add_item():
    print("Добро пожаловать в программу управления инвентарем!")
    item = input("Введите предмет, который нужно добавить в инвентарь: ")
    inventory.append(item)
    print("Предмет успешно добавлен в инвентарь!")

def remove_item():
    print("Удаление предмета из инвентаря.")
    item = input("Введите предмет, который нужно удалить из инвентаря: ")
    
    if item in inventory:
        inventory.remove(item)
        print("Предмет успешно удален из инвентаря!")
    else:
        print("Предмет не найден в инвентаре.")

def view_inventory():
    print("Просмотр инвентаря.")
    if len(inventory) > 0:
        print("Ваш текущий инвентарь:")
        for item in inventory:
            print(item)
    else:
        print("Инвентарь пуст. Добавьте предметы перед тем, как просмотреть инвентарь.")

while True:
    print("Меню:")
    print("1. Добавить предмет в инвентарь")
    print("2. Удалить предмет из инвентаря")
    print("3. Просмотреть инвентарь")
    print("4. Выйти")

    choice = input("Выберите пункт меню: ")

    if choice == "1":
        add_item()
    elif choice == "2":
        remove_item()
    elif choice == "3":
        view_inventory()
    elif choice == "4":
        break
    else:
        print("Некорректный ввод. Попробуйте еще раз.")

print("Спасибо за использование программы управления инвентарем!")