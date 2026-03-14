import os
import json
from expense import Expense
import csv

class FinanceManager:  

    def __init__(self):
        self._expenses = []
        self._budget = None
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        self.file_name = os.path.join(BASE_DIR, "data.json")
    
    def get_budget(self):
        return self._budget
    
    def update_budget(self, new_value):
        if new_value > 0:
            self._budget = new_value
            self.save_to_file()
            return True
        else:
            print("-- Budget must be positive --")
            return False
        
    def import_as_csv(self, file_name = "expense_export.csv"):
        
        base_dir = os.path.dirname(os.path.abspath(__file__))
        full_path = os.path.join(base_dir, file_name)
        if not os.path.exists(full_path):
            print(f"-- File {full_path} not found --")
            return 0
        imported_count = 0
        self.expenses = []
        try:
            with open(full_path, "r", encoding="utf-8") as csvfile:
                reader= csv.DictReader(csvfile)
                expected = {"id", "date", "item", "amount", "category", "payment_method", "notes"}
                if not expected.issubset(reader.fieldnames):
                    print("-- Warning: CSV missing some columns --")
                for row in reader:
                    try:
                        exp_id = int(row["id"])
                        amount = float(row["amount"])

                        new_exp =Expense(
                            id = exp_id,
                            date= row["date"],
                            item= row["item"],
                            amount= amount,
                            category= row['category'],
                            payment_method= row["payment_method"],
                            notes= row.get("notes", "")
                        )
                    
                        self.expenses.append(new_exp)
                        imported_count += 1

                    except (ValueError, KeyError) as e:
                        print(f"-- Skipping invalid row: {row}")
                        continue
            self.save_to_file()
            print(f"\nImported {imported_count} expenses from '{full_path}'")
            return imported_count

        except Exception as e:
            print(f"Error importing CSV: {e}")
            return 0
        
    def export_to_csv(self, file_name):
        if not self.expenses:
            print("-- No expenses to export --")
            return
        
        fieldnames = ["id", "date", "item", "amount", "category", "payment_method", "notes"]

        base_path = os.path.dirname(os.path.abspath(__file__))
        full_path = os.path.join(base_path, file_name)

        try:
            with open(full_path, 'w', newline='', encoding='utf-8')as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                writer.writeheader()

                for exp in self.expenses:
                    to_dictionary = exp.to_dict()
                    writer.writerow(to_dictionary)
            print(f"- Exported {len(self.expenses)} expenses in {full_path}")

        except Exception as e:
            print(f"- Error exporting CSV: {e}")

        
    def add_expense(self, expense_object):
        self.expenses.append(expense_object)
        self.save_to_file()

    def delete_by_id(self, expense_id):
        for exp in self.expenses:
            if exp.id == expense_id:
                self.expenses.remove(exp)
                self.save_to_file()
                return True
        return False
    
    def filter_by_category(self, category_name):
        return[
            exp for exp in self.expenses
            if exp.category.lower() == category_name.lower()
            ]
    
    def get_total(self):
        return sum(exp.amount for exp in self.expenses)
    
    def get_next_id(self):
        if not self.expenses:
            return 1
        return max(exp.id for exp in self.expenses) + 1
    
    def get_category_breakdown(self):
        breakdown = {}
        for exp in self.expenses:
            cat = exp.category
            if cat in breakdown:
                breakdown[cat] += exp.amount
            else:
                breakdown[cat] = exp.amount
        return breakdown

    def get_payment_breakdown(self):
        breakdown = {}
        for exp in self.expenses:
            method = exp.payment_method
            if method in breakdown:
                breakdown[method] += exp.amount
            else:
                breakdown[method] = exp.amount
        return breakdown
    
    def display_stats(self):
        if not self.expenses:
            print("-- No expenses to show stats --")
            return
        
        total = self.get_total()
        remaining = self._budget - total
        print(f"\n- Total Spent: ₹{total:.2f}")
        print(f"- Remaining Budget: ₹{remaining:.2f}")
        if total > self._budget:
            print("⚠️  WARNING: OVER BUDGET!!  ⚠️")
        
        print("\nCategory Breakdown: ")
        cat_break = self.get_category_breakdown()
        for cat, amount in sorted(cat_break.items()):
            print(f"\n- {cat:<20} - {amount:>8.2f}")
        
        print(f"\nPayment Breakdown: ")
        method_break = self.get_payment_breakdown()
        for method, amount in sorted(method_break.items()):
            print(f"\n- {method:<15} - {amount:>8.2f}")

    def display_all(self):
        if  not self.expenses:
            print("-- No expense recorded yet. --")
            return
        
        print("\n" + "="*120)
        print("ID  |    DATE    |           ITEM            |   AMOUNT   |       CATEGORY       |     PAYMENT     |     NOTES    ")
        print("="*120)
        for exp in self.expenses:
            print(exp.display_row())
        print("="*120 + "\n")
    
    def load_from_file(self):
        if not os.path.exists(self.file_name):
            print("-- No file found. Starting fresh. --")
            return
        
        try:
            with open(self.file_name, "r") as f:
                raw_data = json.load(f)

                self._budget = raw_data.get("budget", 5000)
                
                expenses_data = raw_data.get("expenses", [])
                self.expenses = []
                
                for d in expenses_data:
                    new_obj = Expense(
                        id=d["id"], 
                        date=d["date"], 
                        item=d["item"], 
                        amount=float(d["amount"]),
                        category=d["category"],
                        payment_method=d["payment_method"], # <--- Watch this key!
                        notes=d["notes"]
                    )
                    self.expenses.append(new_obj)
                print(f"Loaded: {len(self.expenses)} expenses | Budget: ₹{self._budget}")

        except Exception as e:
            print(f"Error loading data: {e}")

    def save_to_file(self):
        data_to_save = {
            "budget": self._budget,
            "expenses": [exp.to_dict() for exp in self.expenses]
        }
        with open(self.file_name, "w") as f:
            json.dump(data_to_save, f, indent=4)