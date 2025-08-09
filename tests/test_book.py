import pytest
from book import Book

def test_book_creation():
    book = Book("Ulysses", "James Joyce", "978-0199535675")
    assert book.title == "Ulysses"
    assert book.author == "James Joyce"
    assert book.isbn == "978-0199535675"

def test_book_str():
    book = Book("Ulysses", "James Joyce", "978-0199535675")
    assert str(book) == "Ulysses by James Joyce (ISBN: 978-0199535675)"
