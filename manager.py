import os
import json
from expense import Expense
class FinanceManager:

    def __init__(self):
        self._budget = None
        self._expenses = []
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.file_name = os.path.join(base_dir, "expenses.json")

    def get_budget(self):
        return self._budget

    def load_from_file(self):
        if not os.path.exists(self.file_name):
            print("-- File not found --")
            return
        
        try:
            with open(self.file_name, "r") as file:
                raw_data = json.load(file)
                self._budget = raw_data.get("budget", 5000)
                expenses_data = raw_data.get("expenses", [])

                self._expenses = []
                    
                for d in expenses_data:
                    new_obj = Expense(
                        id=int(d["id"]),
                        date=d["date"],
                        item=d["item"],
                        amount=float(d["amount"]),
                        category=d["category"],
                        payment_method=d["payment_method"],
                        notes=d["notes"]
                        )
                    self._expenses.append(new_obj)
                print(f"Loaded {len(self._expenses)} | Budget: ₹{self._budget}")
                return
            
        except Exception as e:
            print(f"Load Error: {e}")
            return

    def save_to_file(self):   
        data = {"budget": self._budget, "expenses":[exp.to_dict() for exp in self._expenses]}
        with open(self.file_name, "w") as file:
            json.dump(data, file, indent=4)

    def get_next_id(self):
        if not self._expenses:
            return 1
        else:
            return max(exp.id for exp in self._expenses) + 1
        
    def add_expense(self, today_date, item, amount, category, payment_method, notes):
        new_exp = Expense(
                id=self.get_next_id(),
                date=today_date,
                item=item,
                amount=amount,
                category=category,
                payment_method=payment_method,
                notes=notes
            )
        self._expenses.append(new_exp)
        self.save_to_file()

    def display_all(self):
        if not self._expenses:
            print("-- No exepenses found --")
            return
        
        print("\n" + "=" * 120)
        print("ID  |    DATE    |           ITEM            |   AMOUNT   |       CATEGORY       |     PAYMENT     |     NOTES    ")
        print("="*120)
        for exp in self._expenses:
            print(exp.display_row())
        print("="*120 + "\n")
