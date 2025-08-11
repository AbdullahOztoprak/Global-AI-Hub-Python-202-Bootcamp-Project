import pytest
import os
import sqlite3
from library import Library

import pytest
from unittest.mock import patch
from library import Library

class MockResponse:
    def __init__(self, status_code, json_data=None):
        self.status_code = status_code
        self._json = json_data or {}
    def json(self):
        return self._json
    def raise_for_status(self):
        if self.status_code >= 400:
            raise Exception("HTTP error")

@patch("httpx.get")
def test_add_and_list_books(mock_get, tmp_path):
    mock_get.side_effect = [
        MockResponse(200, {"title": "Ulysses", "authors": [{"key": "/authors/OL12345A"}]}),
        MockResponse(200, {"name": "James Joyce"})
    ]
    test_file = tmp_path / "test_library.json"
    library = Library(str(test_file))
    result = library.add_book("978-0199535675")
    books = library.list_books()
    assert result is True
    assert len(books) == 1
    assert books[0].isbn == "978-0199535675"
    assert books[0].title == "Ulysses"
    assert books[0].author == "James Joyce"

@patch("httpx.get")
def test_remove_book(mock_get, tmp_path):
    mock_get.side_effect = [
        MockResponse(200, {"title": "Ulysses", "authors": [{"key": "/authors/OL12345A"}]}),
        MockResponse(200, {"name": "James Joyce"})
    ]
    test_file = tmp_path / "test_library.json"
    library = Library(str(test_file))
    library.add_book("978-0199535675")
    library.remove_book("978-0199535675")
    assert len(library.list_books()) == 0

@patch("httpx.get")
def test_find_book(mock_get, tmp_path):
    mock_get.side_effect = [
        MockResponse(200, {"title": "Ulysses", "authors": [{"key": "/authors/OL12345A"}]}),
        MockResponse(200, {"name": "James Joyce"})
    ]
    test_file = tmp_path / "test_library.json"
    library = Library(str(test_file))
    library.add_book("978-0199535675")
    found = library.find_book("978-0199535675")
    assert found is not None
    assert found.title == "Ulysses"

@patch("httpx.get")
def test_persistence(mock_get, tmp_path):
    mock_get.side_effect = [
        MockResponse(200, {"title": "Ulysses", "authors": [{"key": "/authors/OL12345A"}]}),
        MockResponse(200, {"name": "James Joyce"})
    ]
    test_file = tmp_path / "test_library.json"
    library = Library(str(test_file))
    library.add_book("978-0199535675")
    # Reload library
    library = Library(str(test_file))
    books = library.list_books()
    assert len(books) == 1
    assert books[0].isbn == "978-0199535675"

def test_corrupted_database(tmp_path):
    # Create a corrupted database file
    test_file = tmp_path / "test_library.db"
    with open(test_file, "w", encoding="utf-8") as f:
        f.write("not a database")
    
    # Should handle corrupted database gracefully
    import pytest
    with pytest.raises(sqlite3.DatabaseError):
        library = Library(str(test_file))
