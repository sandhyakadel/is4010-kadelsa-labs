class Book:
    """A blueprint for a standard book."""

    def __init__(self, title, author, year):
        # Assigning values to 'self' makes them instance attributes
        self.title = title
        self.author = author
        self.year = year

    def get_age(self):
        """Calculates age based on the current year 2025."""
        return 2025 - self.year

    def __str__(self):
        """Returns a string representation of the book."""
        return f"\"{self.title}\" by {self.author} ({self.year})"
    
class EBook(Book): 
    """A class representing a digital book, inheriting from Book..."""

    def __init__(self, title, author, year, file_size):
        # super() sends the first 3 arguments to the Book constructor
        super().__init__(title, author, year)
        self.file_size = file_size

    def __str__(self):
        # super().__str__() gets the string from the Book class
        base_string = super().__str__()
        return f"{base_string} ({self.file_size} MB)"
    
if __name__ == '__main__':
    # Create a Book object
    my_book = Book("The Hobbit", "J.R.R. Tolkien", 1937)
    print(my_book)
    print(f"Age: {my_book.get_age()} years")

    # Create an EBook object
    my_ebook = EBook("Dune", "Frank Herbert", 1965, 5)
    print(my_ebook)