#Order.py
from datetime import datetime
class Order:
    """Class for an order made by a customer"""

    def __init__(self, cart):
        """Initialize an order with a shopping cart"""
        self.cart = cart  # The shopping cart for this order
        self.order_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Current date and time

    def __str__(self):
        """Show order details"""
        return "Order Date: " + self.order_date + ", " + str(self.cart)
