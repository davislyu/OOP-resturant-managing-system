import json

class Data_Employee:
    @staticmethod
    def get_employees():
        with open('employees.json', 'r') as file:
            employees_data = json.load(file)
        return employees_data

    @staticmethod
    def save_employees(employees):
        with open('employees.json', 'w') as file:
            json.dump(employees, file, indent=2)

class Data_Stock:
    @staticmethod
    def get_ingredients():
        with open('Stock.json', 'r') as file:
            ingredients_data = json.load(file)
        return ingredients_data

    @staticmethod
    def save_ingredients(ingredients):
        with open('Stock.json', 'w') as file:
            json.dump(ingredients, file, indent=2)

class Data_Menu:
    @staticmethod
    def display_menu():
        with open('menu.json', 'r') as file:
            menu_data = json.load(file)
        return menu_data
    @staticmethod
    def save_to_menu(menu_data):
        with open('menu.json', 'w') as file:
            json.dump(menu_data, file, indent=2)

class Data_Table:
    @staticmethod
    def get_tables():
        with open('tables.json', 'r') as file:
            tables_data = json.load(file)
        return tables_data

    @staticmethod
    def save_tables(tables):
        with open('tables.json', 'w') as file:
            json.dump(tables, file, indent=2)

class Data_OrderHistory:
    @staticmethod
    def get_order_history():
        with open('order_history.json', 'r') as file:
            order_history_data = json.load(file)
        return order_history_data
    @staticmethod
    def save_order_history(order_history):
        with open('Order_history.json', 'w') as file:
            json.dump(order_history, file, indent=4)
