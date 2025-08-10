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
def test_add_book_success(mock_get, tmp_path):
    # Mock book data
    mock_get.side_effect = [
        MockResponse(200, {"title": "Test Book", "authors": [{"key": "/authors/OL12345A"}]}),
        MockResponse(200, {"name": "Test Author"})
    ]
    test_file = tmp_path / "test_library.json"
    library = Library(str(test_file))
    result = library.add_book("9781234567897")
    assert result is True
    assert len(library.books) == 1
    assert library.books[0].title == "Test Book"
    assert library.books[0].author == "Test Author"

@patch("httpx.get")
def test_add_book_invalid_isbn(mock_get, tmp_path):
    mock_get.return_value = MockResponse(404)
    test_file = tmp_path / "test_library.json"
    library = Library(str(test_file))
    result = library.add_book("0000000000000")
    assert result is False
    assert len(library.books) == 0

@patch("httpx.get")
def test_add_book_connection_error(mock_get, tmp_path):
    import pytest
    mock_get.side_effect = Exception("Connection error")
    test_file = tmp_path / "test_library.json"
    library = Library(str(test_file))
    with pytest.raises(Exception):
        library.add_book("9781234567897")
