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
    
    def get_category_breakdown(self):
        breakdown = {}
        for exp in self._expenses:
            cat = exp.category
            if cat in breakdown:
                breakdown[cat] += exp.amount
            else:
                breakdown[cat] = exp.amount
        return breakdown

    def get_payment_breakdown(self):
        breakdown = {}
        for exp in self._expenses:
            method = exp.payment_method
            if method in breakdown:
                breakdown[method] += exp.amount
            else:
                breakdown[method] = exp.amount
        return breakdown

    def get_total(self):
        total = sum(exp.amount for exp in self._expenses)
        return total
    
    def display_stats(self):
        if not self._expenses:
            print("-- No expenses found --")

        total_spent = self.get_total()
        remaining = self._budget - total_spent

        print("=" * 120)
        print(f"\nTotal Spent: ₹{total_spent:>8.2f}")
        print(f"Remaining Budget: ₹{remaining:>8.2f}\n")
        print("=" * 120)

        if total_spent > self._budget:
            print("-- WARNING !! | ⚠️ OVER BUDGET ⚠️")

        print(" Category Breakdown: \n")
        cat_break = self.get_category_breakdown()
        for cat, amt in sorted(cat_break.items()):
            print(f"{cat:<20} | ₹ {amt:>.2f}")
        print("-" * 120)
        print(" Payment Breakdown: \n")
        pay_break = self.get_payment_breakdown()
        for method, amount in sorted(pay_break.items()):
            print(f"{method:<20} | ₹ {amount:>.2f}")
        print("\n"+"=" * 120)
        #print("-" * 120)

    def get_monthly_summary(self):
        monthly = {}
        for exp in self._expenses:
            month  = exp.get_month_year()
            monthly[month] = monthly.get(month, 0) + exp.amount
        return monthly

    def display_monthly_summary(self):
        summary = self.get_monthly_summary()
        if not summary:
            print("-- No monthly data --\n")
            return
        print("\nMonthly Summary: ")
        for month in sorted(summary.keys()):
            print(f" {month}: | ₹ {summary[month]:>.2f}")

    def save_to_file(self):
        data = [exp.to_dict() for exp in self._expenses]
        with open(self.file_name, 'w')as file:
            json.dump(data, file, indent=4)
    
    def get_next_id(self):
        if not self._expenses:
            return 1
        else:
            return max(exp.id for exp in self._expenses) +1
    
    def add_expense(self, exp_obj):
        self._expenses.append(exp_obj)
        self.save_to_file()

    def load_from_file(self):
        if not os.path.exists(self.file_name):
            print("-- File not found --\n")
            return
        
        try:
            with open(self.file_name, "r") as file:
                raw_data = json.load(file)
                if isinstance(raw_data, list):
                    expenses_data = raw_data

                elif isinstance(raw_data, dict):
                    self._budget = raw_data.get("budget", 5000)
                    expenses_data = raw_data.get("expenses", [])

                else:
                    raise ValueError("-- Invalid JSON Format --")
                
                self._expenses = []

                for d in expenses_data:
                    new_obj=Expense(
                        id=d["id"],
                        date=d["date"],
                        item=d["item"],
                        amount=float(d["amount"]),
                        category=d["category"],
                        payment_method=d["payment_method"],
                        notes=d["notes"]
                    )
                    self._expenses.append(new_obj)
                
                print(f"\n- Expenses loaded: {self.get_expense_count()}")
        except Exception as e:
            print(f"Error Loading: {e}")

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
        