# Personal Finance Manager (OOP Edition)

A simple, command-line personal finance tracker built in Python with OOP principles. Track your daily expenses, view summaries by category and payment method, filter records, delete entries, and persist everything in JSON.

Perfect for beginners learning object-oriented programming while building a real, useful application.

## Features

- **Add expenses** with date (auto-today option), item name, amount, category, payment method, and notes
- **View all expenses** in a clean, aligned table
- **Statistics & summaries** — total spent, remaining budget, over-budget warning, category breakdown, payment method breakdown
- **Filter expenses** by category (case-insensitive)
- **Delete expenses** by ID
- **Persistent storage** using JSON (data saved automatically after changes)
- **Fully OOP structure**:
  - `Expense` class for individual records
  - `FinanceManager` class for managing the collection, calculations, file I/O

## Technologies / Concepts Used

- Python 3
- Object-Oriented Programming (classes, self, methods, encapsulation)
- JSON file persistence
- List comprehensions & dictionary handling
- Date handling with `datetime`
- Command-line menu interface
- Error handling (try/except for inputs)

## Installation & Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/abhrok/finance-tracker-oop.git
   cd finance-tracker-oop
