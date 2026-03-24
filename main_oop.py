from manager import FinanceManager
from datetime import date
from expense import Expense

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
        print(MENU)
        choice  = input("Enter your choice: \n").strip().lower()
        if choice == "a":
            print("-- ADD NEW EXPENSE --\n")

            today_date = date.today().strftime("%Y/%m/%d")

            item = input("Enter item name: ").capitalize()
            while True:
                
                try:
                    amount = int(input("Enter amount: "))
                    if amount == "":
                        print("-- No value entered --")
                    elif amount == 0:
                        print("-- Enter a positive number --")
                    else:
                        break
                except ValueError:
                    if ValueError:
                        print("-- INVALID INPUT --")
            
            category = input("Enter category name: ").capitalize()
            payment_method = input("Enter payment method: ").capitalize()
            notes = input("Enter notes: ").capitalize()
            
            manager.add_expense(today_date, item, amount, category, payment_method, notes)

        elif choice == "v":
            manager.display_all()
        
        elif choice == "d":
            print("-- DELETE EXPENSE --\n")
            id_to_del = int(input("Enter ID to delete: "))
            if manager.delete_expense(id_to_del):
                print("-- Expense Deleted --")
            else:
                print("-- Couldn't find ID --")

if __name__ == "__main__":
    main()