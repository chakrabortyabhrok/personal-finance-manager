import os
import json
from expense import Expense

class FinanceManager:

    def __init__(self, initial_budget = 5000, file_name = None):
        self._expenses = []
        self._budget = initial_budget

        if file_name is None:
            BASE_DIR = os.path.dirname(os.path.abspath(__file__))
            self.file_name = os.path.join(BASE_DIR, "expenses.json")
        else:
            self.file_name = file_name