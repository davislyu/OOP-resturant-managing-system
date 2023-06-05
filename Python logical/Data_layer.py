import json
import os


class DataFactory:
    @staticmethod
    def get_data(file_path):
        # Retrieve data from the specified file path
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data

    @staticmethod
    def save_data(file_path, data):
        # Save the updated data to the specified file path
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=2)


class Data_Employee:
    @staticmethod
    def get_employees():
        # Retrieve employee data from 'Databases/employees.json'
        data_path = os.path.join("Databases", "employees.json")
        return DataFactory.get_data(data_path)

    @staticmethod
    def save_employees(employees):
        # Save updated employee data to 'Databases/employees.json'
        data_path = os.path.join("Databases", "employees.json")
        DataFactory.save_data(data_path, employees)


class Data_Stock:
    @staticmethod
    def get_ingredients():
        # Retrieve ingredient data from 'Databases/Stock.json'
        data_path = os.path.join("Databases", "Stock.json")
        return DataFactory.get_data(data_path)

    @staticmethod
    def save_ingredients(ingredients):
        # Save updated ingredient data to 'Databases/Stock.json'
        data_path = os.path.join("Databases", "Stock.json")
        DataFactory.save_data(data_path, ingredients)


class Data_Menu:
    @staticmethod
    def display_menu():
        # Retrieve menu data from 'Databases/menu.json'
        data_path = os.path.join("Databases", "menu.json")
        return DataFactory.get_data(data_path)

    @staticmethod
    def save_to_menu(menu_data):
        # Retrieve menu data from 'Databases/menu.json'
        data_path = os.path.join("Databases", "menu.json")
        existing_data = DataFactory.get_data(data_path)
        existing_data['menu_items'] = menu_data['menu_items']
        DataFactory.save_data(data_path, existing_data)


class Data_Table:
    @staticmethod
    def get_tables():
        # Retrieve table data from 'Databases/tables.json'
        data_path = os.path.join("Databases", "tables.json")
        return DataFactory.get_data(data_path)

    @staticmethod
    def save_tables(tables):
        # Save updated table data to 'Databases/tables.json'
        data_path = os.path.join("Databases", "tables.json")
        DataFactory.save_data(data_path, tables)


class Data_OrderHistory:
    @staticmethod
    def get_order_history():
        # Retrieve order history data from 'Databases/order_history.json'
        data_path = os.path.join("Databases", "order_history.json")
        return DataFactory.get_data(data_path)

    @staticmethod
    def save_order_history(order_history):
        # Save updated order history data to 'Databases/order_history.json'
        data_path = os.path.join("Databases", "order_history.json")
        DataFactory.save_data(data_path, order_history)
