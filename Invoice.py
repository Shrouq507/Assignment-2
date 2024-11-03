#Invoice.py
class Invoice:
    """Class for creating an invoice for an order"""
    def __init__(self, order, total_amount):
        """Create an invoice from an order"""
        self.order = order
        self.total_amount = total_amount

    def __str__(self):
        """Show invoice details"""
        return "Invoice for Order: " + str(self.order) + ", Total Amount: $" + "{:.2f}".format(self.total_amount)
