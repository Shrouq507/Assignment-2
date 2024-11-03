#Discount.py
class Discount:
    """Class for a discount that can be applied to an order"""
    def __init__(self, description, percentage):
        """Create a discount"""
        self.description = description
        self.percentage = percentage

    def apply(self, total):
        """Apply the discount to a total"""
        return total * (1 - self.percentage / 100)

    def __str__(self):
        """Show discount info"""
        return self.description + ": " + str(self.percentage) + "%"
