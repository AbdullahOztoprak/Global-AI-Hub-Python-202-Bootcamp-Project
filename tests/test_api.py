import pytest
from fastapi.testclient import TestClient
from api import app

client = TestClient(app)

def test_get_books():
    response = client.get("/books")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_add_book():
    isbn = "978-0140449136"  # The Odyssey
    response = client.post("/books", json={"isbn": isbn})
    assert response.status_code == 200
    data = response.json()
    assert "title" in data
    assert "author" in data
    assert "isbn" in data
    assert data["isbn"] == isbn

def test_delete_book():
    isbn = "978-0140449136"
    # Add book first
    client.post("/books", json={"isbn": isbn})
    # Delete book
    response = client.delete(f"/books/{isbn}")
    assert response.status_code == 200
    assert response.json()["message"] == "Book deleted."
    # Try deleting again
    response = client.delete(f"/books/{isbn}")
    assert response.status_code == 200
    assert "error" in response.json()
