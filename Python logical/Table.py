import json
import random
from datetime import datetime
from Data_layer import *



class Table:
    def __init__(self, table_number, status):
        self.table_number = table_number
        self.status = status

    def __str__(self):
        return f"Table {self.table_number}: {self.status}"

    @staticmethod
    def reserve_table(table_number):
        tables_data = Data_Table.get_tables()

        table_data = next((t for t in tables_data['tables'] if t['table_number'] == table_number), None)

        if table_data and table_data['status'] == 'free for reservation':
            table_data['status'] = 'reserved'  
            Data_Table.save_tables(tables_data)
            print(f"Table {table_number} reserved successfully.")
        else:
            print(f"Table {table_number} is not available for reservation.")