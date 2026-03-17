import os
from expense import Expense
from manager import FinanceManager

def main():
    manager = FinanceManager()
    
    WELCOME_MSG = (f"\n- Budget: ₹{manager.get_budget():.2f} | {manager.get_expense_count()} expenses loaded")
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
         #if choice == "a":
            
         #elif choice == "d":
            
         #elif choice == "b":

         #elif choice == "u":

         #elif choice == "f":

         #elif choice == "v":

         #elif choice == "s":

         #elif choice == "i":

         #elif choice == "x":

        if choice == "e":
            print("-- GOODBYE --")
            break

if __name__ == "__main__":
    main()