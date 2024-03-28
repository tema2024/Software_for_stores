class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}  # Словарь для хранения товаров и их цен

    def add_item(self, item_name, price):
        """Добавляет товар в ассортимент магазина."""
        self.items[item_name] = price

    def remove_item(self, item_name):
        """Удаляет товар из ассортимента магазина."""
        if item_name in self.items:
            del self.items[item_name]

    def get_price(self, item_name):
        """Возвращает цену товара по его названию."""
        return self.items.get(item_name, None)

    def update_price(self, item_name, new_price):
        """Обновляет цену товара."""
        if item_name in self.items:
            self.items[item_name] = new_price

# Создание объектов класса Store
store1 = Store("Фруктовая лавка", "г. Москва, ул. Садовая, д. 50")
store2 = Store("Книжная лавка", "г. Москва, ул. Мельникова, д. 5")
store3 = Store("Техно лавка", "г. Москва, ул. Мельника, д. 20")

# Добавление товаров в магазины
store1.add_item("apples", 0.5)
store1.add_item("bananas", 0.75)
store2.add_item("The Great Gatsby", 10)
store2.add_item("War and Peace", 12)
store3.add_item("Smartphone", 299)
store3.add_item("Laptop", 599)

# Протестировать методы одного из магазинов
# Для магазина store1
print(f"Цены до обновления: {store1.items}")
store1.update_price("apples", 0.65)  # Обновляем цену
print(f"Цены после обновления: {store1.items}")

store1.remove_item("bananas")  # Удаляем товар
print(f"Ассортимент после удаления: {store1.items}")

price_apples = store1.get_price("apples")  # Запрашиваем цену
print(f"Цена яблок: {price_apples}")

price_oranges = store1.get_price("oranges")  # Пытаемся получить цену несуществующего товара
print(f"Цена апельсинов: {price_oranges}")
