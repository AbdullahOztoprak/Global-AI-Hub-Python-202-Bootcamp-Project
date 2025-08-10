
from fastapi import FastAPI
from pydantic import BaseModel

# Pydantic models
class BookModel(BaseModel):
	title: str
	author: str
	isbn: str

class ISBNModel(BaseModel):
	isbn: str


from library import Library

app = FastAPI()
library = Library()

@app.get("/books", response_model=list[BookModel])
def get_books():
	return [BookModel(title=book.title, author=book.author, isbn=book.isbn) for book in library.list_books()]

@app.post("/books", response_model=BookModel)
def add_book(isbn_data: ISBNModel):
	result = library.add_book(isbn_data.isbn)
	if result:
		book = library.find_book(isbn_data.isbn)
		return BookModel(title=book.title, author=book.author, isbn=book.isbn)
	return {"error": "Book could not be added. Check ISBN or API."}

@app.delete("/books/{isbn}")
def delete_book(isbn: str):
	book = library.find_book(isbn)
	if book:
		library.remove_book(isbn)
		return {"message": "Book deleted."}
	return {"error": "Book not found."}
