import os
import json
from expense import Expense

class FinanceManager:

    def __init__(self, initial_budget = 5000, file_name = None):
        self._expense = []
        self._budget = initial_budget

        if file_name is None:
            base_path = os.path.dirname(os.path.abspath(__file__))
            self.file_name = os.path.join(base_path, "export_test.csv")
        else:
            self.file_name = file_name
    
    def get_budget(self):
        return self._budget
    
    def get_expense_count(self):
        return (len(self._expense))
