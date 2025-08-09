import pytest
import os
import json
from library import Library
from book import Book

def test_add_and_list_books(tmp_path):
    test_file = tmp_path / "test_library.json"
    library = Library(str(test_file))
    book = Book("Ulysses", "James Joyce", "978-0199535675")
    library.add_book(book)
    books = library.list_books()
    assert len(books) == 1
    assert books[0].isbn == "978-0199535675"

def test_remove_book(tmp_path):
    test_file = tmp_path / "test_library.json"
    library = Library(str(test_file))
    book = Book("Ulysses", "James Joyce", "978-0199535675")
    library.add_book(book)
    library.remove_book("978-0199535675")
    assert len(library.list_books()) == 0

def test_find_book(tmp_path):
    test_file = tmp_path / "test_library.json"
    library = Library(str(test_file))
    book = Book("Ulysses", "James Joyce", "978-0199535675")
    library.add_book(book)
    found = library.find_book("978-0199535675")
    assert found is not None
    assert found.title == "Ulysses"

def test_persistence(tmp_path):
    test_file = tmp_path / "test_library.json"
    library = Library(str(test_file))
    book = Book("Ulysses", "James Joyce", "978-0199535675")
    library.add_book(book)
    # Reload library
    library2 = Library(str(test_file))
    books = library2.list_books()
    assert len(books) == 1
    assert books[0].isbn == "978-0199535675"

def test_corrupted_json(tmp_path):
    test_file = tmp_path / "test_library.json"
    with open(test_file, "w", encoding="utf-8") as f:
        f.write("not a json")
    library = Library(str(test_file))
    assert library.list_books() == []
