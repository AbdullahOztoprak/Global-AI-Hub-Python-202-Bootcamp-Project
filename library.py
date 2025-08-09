
import json
from book import Book

class Library:
	"""
	Manages a collection of Book objects and handles persistence in a JSON file.
	"""
	def __init__(self, filename="library.json"):
		self.filename = filename
		self.books = []
		self.load_books()

	def add_book(self, book: Book):
		self.books.append(book)
		self.save_books()

	def remove_book(self, isbn: str):
		self.books = [book for book in self.books if book.isbn != isbn]
		self.save_books()

	def list_books(self):
		return self.books

	def find_book(self, isbn: str):
		for book in self.books:
			if book.isbn == isbn:
				return book
		return None

	def load_books(self):
		try:
			with open(self.filename, "r", encoding="utf-8") as f:
				data = json.load(f)
				self.books = [Book(**item) for item in data]
		except (FileNotFoundError, json.JSONDecodeError):
			self.books = []

	def save_books(self):
		with open(self.filename, "w", encoding="utf-8") as f:
			json.dump([book.__dict__ for book in self.books], f, ensure_ascii=False, indent=4)
