class Cashier:
    def __init__(self):
        self.products = {
            "кетчунез": 80,
            "лаваш": 45,
            "сухарики": 22,
            "сыр": 120,
            "картофель фри (100 грамм)": 25,
            "куриное филе (100 грамм)": 40,
            "лук (100 грамм)": 12,
            "огурцы (100 грамм)": 14,
            "салат (100 грамм)": 10,
            "томаты (100 грамм)": 15
        }
        self.denominations = [1, 5, 7, 10, 15]

    def calculate_total(self, cart):
        total_price = sum(self.products[item] * quantity for item, quantity in cart.items())
        return total_price

    def give_change(self, total_price, payment):
        change = payment - total_price
        print("\nПожалуйста, ваша сдача:", change, "р.")
        change_denominations = []
        remaining_change = change

        while remaining_change > 0:
            for denom in sorted(self.denominations, reverse=True):
                while remaining_change >= denom:
                    change_denominations.append(denom)
                    remaining_change -= denom

        print("Минимальное количество монет для сдачи:", len(change_denominations))
        denominations_count = {}
        for denom in self.denominations:
            count = change_denominations.count(denom)
            if count > 0:
                denominations_count[denom] = count

        denominations_string = ", ".join([f"{k} ({v})" for k, v in denominations_count.items()])
        print("Номиналы монет для сдачи:", denominations_string)


def main():
    cashier = Cashier()

    cart = {}
    print("\nДоступные продукты и их цены:")
    for item, price in cashier.products.items():
        print(f"{item}: {price}р.")

    while True:
        item = input("\nВыберите продукт (или перейдите 'к оплате'): ").lower()
        if item == 'к оплате':
            break

        found_products = [key for key in cashier.products.keys() if item in key]
        if len(found_products) == 0:
            print("Продукт не найден.")
            continue
        elif len(found_products) > 1:
            print("Уточните ваш запрос, найдено несколько продуктов:")
            for prod in found_products:
                print(prod)
            continue
        else:
            item = found_products[0]

        if "(100 грамм)" in item:
            weight = int(input(f"Введите вес в граммах: "))
            cart[item] = weight / 100
        else:
            quantity = int(input(f"Введите количество: "))
            cart[item] = quantity

    if not cart:
        print("\nНам очень жаль, что вы не нашли того, что искали.")
        return

    print("\nВаша корзина:")
    for item, quantity in cart.items():
        if "(100 грамм)" in item:
            print(f"{item}: {quantity * 100} гр, {cashier.products[item] * quantity}р.")
        else:
            print(f"{item}: {quantity} шт, {cashier.products[item] * quantity}р.")

    total_price = cashier.calculate_total(cart)
    print("\nК оплате:", total_price, "р.")

    while True:
        payment = input("Введите сумму, которой вы собираетесь рассчитаться (или 'нету у меня стока'): ")
        if payment.lower() == 'нету у меня стока':
            print("Молодой человек, не задерживайте очередь!!!")
            return

        try:
            payment = float(payment)
        except ValueError:
            print("Введите корректную сумму.")
            continue

        if payment < total_price:
            print("Недостаточно денег для оплаты.")
        else:
            break

    cashier.give_change(total_price, payment)


if __name__ == "__main__":
    main()
