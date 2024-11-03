#Customer.py
class Customer:
    """Class for a customer"""
    def __init__(self, name, contact, is_loyalty_member=False):
        """Initialize a customer with their info"""
        self.name = name
        self.contact = contact
        self.is_loyalty_member = is_loyalty_member

    def __str__(self):
        """Return a string that shows the customer info"""
        return "Customer: " + self.name + ", Contact: " + self.contact + ", Loyalty Member: " + str(self.is_loyalty_member)
