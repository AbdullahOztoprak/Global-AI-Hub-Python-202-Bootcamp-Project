
from fastapi import FastAPI, HTTPException, Body
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from library import Library

# Pydantic models
class BookModel(BaseModel):
	title: str
	author: str
	isbn: str

class ISBNModel(BaseModel):
	isbn: str

class UpdateBookModel(BaseModel):
	title: str | None = None
	author: str | None = None

app = FastAPI()

# Add CORS middleware to allow web frontend to access API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify your domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
	raise HTTPException(status_code=400, detail="Book could not be added. Check ISBN or API.")

@app.put("/books/{isbn}", response_model=BookModel)
def update_book(isbn: str, update: UpdateBookModel = Body(...)):
	book = library.find_book(isbn)
	if not book:
		raise HTTPException(status_code=404, detail="Book not found.")
	updated = library.update_book(isbn, title=update.title, author=update.author)
	if updated:
		book = library.find_book(isbn)
		return BookModel(title=book.title, author=book.author, isbn=book.isbn)
	raise HTTPException(status_code=400, detail="Book could not be updated.")

@app.delete("/books/{isbn}")
def delete_book(isbn: str):
	book = library.find_book(isbn)
	if book:
		library.remove_book(isbn)
		return {"message": "Book deleted."}
	raise HTTPException(status_code=404, detail="Book not found.")
