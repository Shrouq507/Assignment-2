# shopping_cart.py
from typing import List
class ShoppingCart:
    """Class for a shopping cart"""
    def __init__(self, customer):
        """Initialize the cart for a customer"""
        self.customer = customer  # The customer for this cart
        self.ebooks = []  # List to keep e-books

    def add_ebook(self, ebook):
        """Add an e-book to the cart"""
        self.ebooks.append(ebook)

    def remove_ebook(self, ebook):
        """Remove an e-book from the cart if it's there"""
        if ebook in self.ebooks:
            self.ebooks.remove(ebook)

    def total_price(self):
        """Calculate total price of e-books in the cart"""
        return sum(ebook.price for ebook in self.ebooks)

    def clear_cart(self):
        """Clear all items in the cart"""
        self.ebooks.clear()

    def __str__(self):
        """Show what's in the cart"""
        ebook_list = ", ".join(str(ebook) for ebook in self.ebooks)
        return "Cart for " + self.customer.name + ": " + (ebook_list if ebook_list else "Empty Cart")
