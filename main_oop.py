from manager import FinanceManager
from datetime import date
from expense import Expense

def main():
    manager = FinanceManager()
    manager.load_from_file()
    while True:
        choice  = input("Enter your choice: \n").strip().lower()


if __name__ == "__main__":
    main()