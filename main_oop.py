from expense import Expense
from manager import FinanceManager
from datetime import date

def main():
    manager = FinanceManager()
    manager.load_from_file()


    MENU = """
                        --- MENU ---

        a - Add Expense              v - View All
        d - Delete Expense           s - Show Stats      
        b - Show Current Budget      i - Import from CSV
        u - Update Budget            x - Export to CSV
        f - Show by Category         e - Exit
    
        """
    while True:
        print(MENU)
        print("-- Welocome to the task manager --\n")
        choice = input("- Enter a choice: \n").lower().strip()

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
            print("\n-- Expense Added --")

        elif choice == "d":
            try:
                id_no = input("Input the ID: \n").strip()
                id_to_delete = int(id_no)
                if manager.delete_by_id(id_to_delete):
                    print(f"\nExpense ID - {id_to_delete} deleted successfuly")
                else:
                    print(f"\n-- No expense found with {id_to_delete} ID --")

            except ValueError:
                print("-- Enter a valid number --")

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

        elif choice == "f":
            category_name = input("\n- Input the category name: ").lower()
            if not category_name:
                print("-- No category entered --")
                continue

            filtered = manager.filter_by_category(category_name)

            if not filtered:
                print(f"-- No category named {category_name}")
            else:
                print(f"\nExpenses in {category_name.title()}: ")
                print("\n" + "="*120)
                print("ID  |    DATE    |           ITEM            |   AMOUNT   |       CATEGORY       |     PAYMENT     |     NOTES    ".title())
                print("="*120)
                for exp in filtered:
                    print(exp.display_row())
                print("="*120)

        elif choice == "v":
            manager.display_all()

        elif choice == "s":
            manager.display_stats()

        elif choice == "i":
            filename = input("Enter CSV filename to import (default: expense_export.csv): ").strip()
            if not filename:
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

        elif choice == "e":
            print("-- Goodbye --")
            break
        else:
            print("-- Invalid Input. Enter a valid choice --")

if __name__ == "__main__":
    main()