
"""
Library Management System API

This FastAPI application provides REST endpoints for managing a book library.
Users can add, update, delete, and list books through HTTP requests.
"""

# Import necessary libraries
from fastapi import FastAPI, HTTPException, Body
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from library import Library

# Pydantic models for request/response validation
class BookModel(BaseModel):
	"""Model representing a book with all its details"""
	title: str   # Book title
	author: str  # Author name
	isbn: str    # ISBN code

class ISBNModel(BaseModel):
	"""Model for requests that only need an ISBN"""
	isbn: str    # ISBN code for book lookup

class UpdateBookModel(BaseModel):
	"""Model for updating book details (optional fields)"""
	title: str | None = None   # New title (optional)
	author: str | None = None  # New author (optional)

# Create FastAPI application instance
app = FastAPI()

# Add CORS middleware to allow web frontend to access API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify your domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create library instance for managing books
library = Library()

@app.get("/books", response_model=list[BookModel])
def get_books():
	"""
	Get all books in the library
	Returns: List of all books with their details
	"""
	# Get all books from library and convert to API model format
	return [BookModel(title=book.title, author=book.author, isbn=book.isbn) for book in library.list_books()]

@app.post("/books", response_model=BookModel)
def add_book(isbn_data: ISBNModel):
	"""
	Add a new book by ISBN
	The system will fetch book details from Open Library API
	Args: ISBN code in request body
	Returns: Added book details
	"""
	# Try to add book using ISBN
	result = library.add_book(isbn_data.isbn)
	if result:
		# If successful, get the book details and return them
		book = library.find_book(isbn_data.isbn)
		return BookModel(title=book.title, author=book.author, isbn=book.isbn)
	# If failed, return error
	raise HTTPException(status_code=400, detail="Book could not be added. Check ISBN or API.")

@app.put("/books/{isbn}", response_model=BookModel)
def update_book(isbn: str, update: UpdateBookModel = Body(...)):
	"""
	Update book details by ISBN
	Args: ISBN in URL path, new details in request body
	Returns: Updated book details
	"""
	# First check if book exists
	book = library.find_book(isbn)
	if not book:
		raise HTTPException(status_code=404, detail="Book not found.")
	
	# Update the book with new details
	updated = library.update_book(isbn, title=update.title, author=update.author)
	if updated:
		# Return updated book details
		book = library.find_book(isbn)
		return BookModel(title=book.title, author=book.author, isbn=book.isbn)
	# If update failed, return error
	raise HTTPException(status_code=400, detail="Book could not be updated.")

@app.delete("/books/{isbn}")
def delete_book(isbn: str):
	"""
	Delete a book by ISBN
	Args: ISBN in URL path
	Returns: Success message
	"""
	# Check if book exists before trying to delete
	book = library.find_book(isbn)
	if book:
		# Delete the book
		library.remove_book(isbn)
		return {"message": "Book deleted."}
	# If book not found, return error
	raise HTTPException(status_code=404, detail="Book not found.")
