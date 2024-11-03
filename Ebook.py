#Ebook.py
class Ebook:
    """Class for an e-book"""
    def __init__(self, title: str, author: str, pub_date: str, genre: str, price: float):
        """Initialize an e-book with its details"""
        self.title = title
        self.author = author
        self.pub_date = pub_date
        self.genre = genre
        self.price = price

    def __str__(self) -> str:
        """Return a string that shows the e-book info"""
        return f"{self.title} by {self.author} - {self.genre} (${self.price:.2f})"
