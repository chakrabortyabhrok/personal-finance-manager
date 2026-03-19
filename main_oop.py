from expense import Expense
from manager import FinanceManager
from datetime import date

def main():
    manager = FinanceManager()
    manager.load_from_file()
    
    WELCOME_MSG = (f"- Current Budget: ₹{manager.get_budget():.2f}")
    MENU =  """
                        --- MENU ---
            a - Add Expense              v - View All
            d - Delete Expense           s - Show Stats      
            b - Show Current Budget      i - Import from CSV
            u - Update Budget            x - Export to CSV
            f - Show by Category         e - Exit
        """
    
    while True:
        print(WELCOME_MSG)
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
            print("\n-- Expense Added --")

        elif choice == "v":
            manager.display_all()

        if choice == "e":
            print("-- GOODBYE --")
            break

if __name__ == "__main__":
    main()
    #test_exp = Expense(1, "2026-03-18", "Test Coffee", 45.5, "Food", "UPI", "Morning break")
    #print(test_exp)
    #print(test_exp.to_dict())
    #print(test_exp.get_month_year())