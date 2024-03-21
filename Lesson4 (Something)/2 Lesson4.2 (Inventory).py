import re

class InventoryManager:
    def __init__(self):
        self.inventory = {}
        self.loaded_from_file = False
        self.load_inventory_from_file()

    def add_item(self, item_name, quantity, description):
        if item_name.lower() in [item["name"].lower() for item in self.inventory.values()]:
            print("Такой предмет уже существует. Предметы должны быть уникальными.")
            return

        if not re.match(r'^[\w\s]+$', item_name):
            print("Некорректный формат имени предмета. Имя может содержать только буквы, цифры и пробелы.")
            return

        quantity = int(quantity)
        if quantity < 0:
            print("Количество предметов не может быть отрицательным.")
            return

        self.inventory[item_name] = {"name": item_name, "quantity": quantity, "description": description}
        print(f"Предмет '{item_name}' добавлен в инвентарь с количеством {quantity} и описанием: {description}.")

    def edit_item(self, item_name):
        if item_name in self.inventory:
            print(f"\nМеню для предмета '{item_name}':")
            print("1. Редактировать имя предмета")
            print("2. Редактировать количество")
            print("3. Редактировать описание")
            print("4. Вернуться к списку предметов")

            choice = input("Выберите действие (1-4): ").strip()

            if choice == '1':
                new_name = input("Введите новое имя предмета: ")
                self.inventory[item_name]["name"] = new_name
                print(f"Имя предмета '{item_name}' успешно отредактировано на '{new_name}'.")
            elif choice == '2':
                new_quantity = int(input("Введите новое количество: "))
                self.inventory[item_name]["quantity"] = new_quantity
                print(f"Количество предмета '{item_name}' успешно отредактировано на {new_quantity}.")
            elif choice == '3':
                new_description = input("Введите новое описание: ")
                self.inventory[item_name]["description"] = new_description
                print(f"Описание предмета '{item_name}' успешно отредактировано на '{new_description}'.")
            elif choice == '4':
                return
            else:
                print("Некорректный ввод. Пожалуйста, выберите от 1 до 4.")
        else:
            print(f"Предмет '{item_name}' не найден.")

    def delete_item(self, item_name):
        if item_name in self.inventory:
            del self.inventory[item_name]
            print(f"Предмет '{item_name}' успешно удален.")
        else:
            print(f"Предмет '{item_name}' не найден.")

    def view_inventory(self):
        if not self.inventory:
            print("Инвентарь пуст.")
            return

        while True:
            print("\nСписок предметов в инвентаре:")
            for item_name, data in self.inventory.items():
                print(f"{item_name} - Количество: {data['quantity']}, Описание: {data['description']}")

            item_name = input("\nВведите имя предмета для редактирования или удаления (0 для выхода): ").strip()
            if item_name == '0':
                return
            elif item_name in self.inventory:
                self.print_edit_delete_menu(item_name)
            else:
                print(f"Предмет '{item_name}' не найден.")

    def print_edit_delete_menu(self, item_name):
        print(f"\nМеню для предмета '{item_name}':")
        print("1. Редактировать предмет")
        print("2. Удалить предмет")
        print("3. Вернуться к списку предметов")

        choice = input("Выберите действие (1-3): ").strip()

        if choice == '1':
            self.edit_item(item_name)
        elif choice == '2':
            self.delete_item(item_name)
        elif choice == '3':
            pass
        else:
            print("Некорректный ввод. Пожалуйста, выберите от 1 до 3.")

    def load_inventory_from_file(self):
        try:
            with open("inventory.txt", "r", encoding="utf-8") as file:
                lines = file.readlines()

            if not lines:
                raise ValueError("Файл с инвентарём пуст.")

            for line in lines:
                parts = line.strip().split(";")
                if len(parts) != 3:
                    print(f"Некорректная строка в файле: {line}. Пропущена.")
                    continue

                item_name = parts[0].strip()
                quantity = int(parts[1].strip())
                description = parts[2].strip()

                self.inventory[item_name] = {"name": item_name, "quantity": quantity, "description": description}

            self.loaded_from_file = True
            print("Инвентарь загружен.")
        except FileNotFoundError:
            print("Файл с инвентарём не найден. Создан новый файл 'inventory.txt'.")
        except ValueError as e:
            print(f"Ошибка при загрузке инвентаря: {e}")

    def save_inventory_to_file(self):
        with open("inventory.txt", "w", encoding="utf-8") as file:
            for item_name, data in self.inventory.items():
                file.write(f"{data['name']};{data['quantity']};{data['description']}\n")

    def print_menu(self):
        print("\nМеню:")
        print("1. Добавить предмет")
        if self.inventory:
            print("2. Список предметов в инвентаре")
        print("3. Выйти")

    def run(self):
        while True:
            self.print_menu()
            choice = input("Выберите действие (1-3): ").strip()

            if choice == '1':
                item_name = input("Введите имя нового предмета: ")
                quantity = input("Введите количество: ")
                description = input("Введите описание: ")
                self.add_item(item_name, quantity, description)
            elif choice == '2' and self.inventory:
                self.view_inventory()
            elif choice == '3':
                self.save_inventory_to_file()
                print("Выход из программы. До свидания!")
                break
            else:
                print("Некорректный ввод. Пожалуйста, выберите от 1 до 3.")

if __name__ == "__main__":
    inventory_manager = InventoryManager()
    inventory_manager.run()
