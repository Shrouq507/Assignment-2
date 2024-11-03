#Main program to test everything
if __name__ == "__main__":
    # Create a customer
    customer = Customer("Ahmed Ali", "Ahmed.Ali@gmail.com", True)

    # Create some e-books
    ebook1 = Ebook("E-Book One", "Author A", "2024-08-20", "Fiction", 10.00)
    ebook2 = Ebook("E-Book Two", "Author B", "2024-09-20", "Non-Fiction", 15.00)

    # Create a shopping cart for the customer
    cart = ShoppingCart(customer)
    cart.add_ebook(ebook1)
    cart.add_ebook(ebook2)

    # Create an order based on the shopping cart
    order = Order(cart)

    # Calculate total before discounts
    total_amount = cart.total_price()

    # Create a discount and apply it
    discount = Discount("Loyalty Discount", 10)
    total_after_discount = discount.apply(total_amount)

    # Generate an invoice
    invoice = Invoice(order, total_after_discount)

    # Print the invoice
    print(invoice)
