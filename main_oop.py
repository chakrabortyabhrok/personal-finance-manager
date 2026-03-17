import os
from expense import Expense
from manager import FinanceManager

def main():
    manager = FinanceManager()
    
    MENU =  """
                        --- MENU ---
        a - Add Expense              v - View All
        d - Delete Expense           s - Show Stats      
        b - Show Current Budget      i - Import from CSV
        u - Update Budget            x - Export to CSV
        f - Show by Category         e - Exit
        """
    while True:
        print(MENU)
        choice = input("- Enter your choice: ").strip().lower()
        if choice == "e":
            print("-- GOODBYE --")
            break

if __name__ == "__main__":
    main()