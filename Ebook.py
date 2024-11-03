#Ebook.py
class Ebook:
    """Class for an e-book"""
    def __init__(self, title, author, pub_date, genre, price):
        """Initialize an e-book with its details"""
        self.title = title
        self.author = author
        self.pub_date = pub_date
        self.genre = genre
        self.price = price

    def __str__(self):
        """Return a string that shows the e-book info"""
        return self.title + " by " + self.author + " - " + self.genre + " ($" + str(self.price) + ")"
