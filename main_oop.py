from expense import Expense
from manager import FinanceManager
from datetime import date

def main():
    manager = FinanceManager()
    manager.load_from_file()

    MENU =  """
                        --- MENU ---
            a - Add Expense              v - View All
            d - Delete Expense           s - Show Stats      
            b - Show Current Budget      i - Import from CSV
            u - Update Budget            x - Export to CSV
            f - Show by Category         e - Exit
            m - Monthly Summary
        """
    
    while True:
        print()
        print(MENU)
        choice = input("- Enter your choice: ").strip().lower()
        
        if choice == "a":
            print("\n-- Add expense --\n")
            item = input("Enter item name: \n").capitalize()
            while True:
                try:
                    amount = float(input("Enter amount: \n"))
                    if not amount > 0:
                        print("-- Please enter a positive amount --\n")
                    else:
                        break
                except ValueError:
                    print("-- Please enter a valid number --")
                
            category = input("Enter category: \n").capitalize()
            payment_method = input("Enter payment method: \n").capitalize()
            notes = input("Enter note: \n").capitalize()

            new_id = manager.get_next_id()
            today = date.today().strftime("%Y-%m-%d")

            new_exp = Expense(new_id, today, item, amount, category, payment_method, notes)
            manager.add_expense(new_exp)

        elif choice == "b":
            budget = manager.get_budget()
            print(f"Budget: ₹{budget:.2f}")

        elif choice == "u":
            try:
                new_budget = float(input("- Enter New Budget: "))
                if manager.update_budget(new_budget):
                    print(f"Budget updated to ₹{new_budget:.2f}")
                    
                else:
                    print("Enter a positive number")
            except ValueError:
                print("-- Enter a valid number --")

        elif choice == "i":
            filename = input("Enter CSV filename to import (default: expense_export.csv): ").strip()
            if filename == "":
                filename = "expense_export.csv"
            
            count = manager.import_as_csv(filename)
            
            if count > 0:
                print(f"Successfully imported {count} expenses.")
            else:
                print("-- No expenses imported (check file or errors above). --")

        elif choice == "x":
            user_name = input("Enter a file name: (press ENTER to set to default) \n").strip()
            if user_name == "":
                user_name = "expense_export.csv"
                
            manager.export_to_csv(user_name)

        elif choice == "v":
            manager.display_all()

        elif choice == "s":
            manager.display_stats()

        elif choice == "f":
            cat_name = input("- Enter the category name: \n").strip()
            if not cat_name:
                print("-- No category entered --")
                continue
            filtered = manager.filter_by_category(cat_name)
            print(f"\nExpenses in {cat_name.title()}:")
            if not filtered:
                print(" -- None Found --")
            else:
                print("\n" + "=" * 120)
                print("ID  |    DATE    |           ITEM            |   AMOUNT   |       CATEGORY       |     PAYMENT     |     NOTES    ")
                print("="*120)
                for exp in filtered:
                    print(exp.display_row())
                print("="*120 + "\n")
        
        elif choice  == "d":
            try:
                id_str = input("Enter the Expense-ID to delete: \n").strip()
                id_to_delete = int(id_str)
                if manager.delete_expenses(id_to_delete):
                    print(f"-- Deleted expense ID {id_to_delete} successfully --")
                else:
                    print(f"-- No expense with ID {id_to_delete}")
            except ValueError:
                print("-- Enter a valid number --")
        
        elif choice == "m":
            manager.display_monthly_summary()

        elif choice == "e":
            print("-- GOODBYE --")
            break

        else:
            print("\n-- Invalid Choice | Try Again -- \n")
            

if __name__ == "__main__":
    main()
    #test_exp = Expense(1, "2026-03-18", "Test Coffee", 45.5, "Food", "UPI", "Morning break")
    #print(test_exp)
    #print(test_exp.to_dict())
    #print(test_exp.get_month_year())