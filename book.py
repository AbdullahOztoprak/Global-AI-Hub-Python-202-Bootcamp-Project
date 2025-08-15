class Book:
    """
    Represents a book with its title, author, and ISBN.

    Attributes:
        title (str): The title of the book.
        author (str): The author of the book.
        isbn (str): The International Standard Book Number of the book.
    """

    def __init__(self, title: str, author: str, isbn: str):
        """
        Initializes a Book instance with the given title, author, and ISBN.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            isbn (str): The ISBN of the book.
        """
        self.title = title  # Set the title of the book
        self.author = author  # Set the author of the book
        self.isbn = isbn  # Set the ISBN of the book

    def __str__(self):
        """
        Returns a string representation of the book.

        Returns:
            str: A string in the format 'Title by Author (ISBN: ISBN)'.
        """
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"
