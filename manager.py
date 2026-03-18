import os
import json
from expense import Expense

class FinanceManager:

    def __init__(self):
        self._expenses = []
        self._budget = None
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        self.file_name = os.path.join(BASE_DIR, "expenses.json")
        
    def get_budget(self):
        return self._budget
    
    def get_expense_count(self):
        return (len(self._expenses))
    
    def save_to_file(self):
        data = [exp.to_dict() for exp in self._expenses]
        with open(self.file_name, 'w')as file:
            json.dump(data, file, indent=4)
    
    def get_next_id(self):
        if not self._expenses:
            return 1
        else:
            return max(exp.id for exp in self._expenses) +1
    
    def add_expense(self, date, item, amount, category, payment_method, notes):
        new_id = self.get_next_id()
        new_exp = Expense(new_id, date, item, amount, category, payment_method, notes)
        self._expenses.append(new_exp)
        self.save_to_file()

    def load_from_file(self):
        if not os.path.exists(self.file_name):
            print("-- File not found --\n")
            return
        
        try:
            with open(self.file_name, "r") as file:
                raw_data = json.load(file)
                self._budget = 5000
                self._expenses = []
                for d in raw_data:
                    new_obj=Expense(
                        id=d["id"],
                        date=d["date"],
                        item=d["item"],
                        amount=d[float("amount")],
                        category=d["category"],
                        payment_method=d["payment_method"],
                        notes=d["notes"]
                    )
                    self._expenses.append(new_obj)

                print(f"Loaded {len(self._expenses)} expenses | Budget: ₹{self.get_budget()}")
        except Exception as e:
            print(f"Error Loading: {e}")