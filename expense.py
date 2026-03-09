class Expense:

    def __init__(self, id, date, item, amount, category, payment_method, notes):
        self.id = int(id)
        self.date = date
        self.item = item
        self.amount = float(amount)
        self.category = category
        self.payment_method = payment_method
        self.notes = notes

    def display_row(self):
        return (f"{self.id:<3} | {self.date:<10} | {self.item:<25} | ₹{self.amount:>10.2f} | {self.category:<20} | {self.payment_method:<15} | {self.notes}")
    
    def to_dict(self):
        return {
            "id": self.id,
            "date": self.date,
            "item": self.item,
            "amount": self.amount,
            "category": self.category,
            "payment_method": self.payment_method,
            "notes": self.notes
        }