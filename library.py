

import json
from book import Book

class Library:
	"""
	Manages a collection of Book objects and handles persistence in a JSON file.
	Ensures all changes are saved and loaded reliably.
	"""
	def __init__(self, filename="library.json"):
		self.filename = filename
		self.books = []
		self.load_books()

	def add_book(self, book: Book):
		"""Add a book and save to JSON."""
		self.books.append(book)
		self.save_books()

	def remove_book(self, isbn: str):
		"""Remove a book by ISBN and save to JSON."""
		self.books = [book for book in self.books if book.isbn != isbn]
		self.save_books()

	def list_books(self):
		"""Return the list of books."""
		return self.books

	def find_book(self, isbn: str):
		"""Find a book by ISBN."""
		for book in self.books:
			if book.isbn == isbn:
				return book
		return None

	def load_books(self):
		"""
		Load books from the JSON file.
		If the file is missing or corrupted, start with an empty list.
		"""
		try:
			with open(self.filename, "r", encoding="utf-8") as f:
				data = json.load(f)
				self.books = [Book(**item) for item in data]
		except FileNotFoundError:
			self.books = []
		except json.JSONDecodeError:
			print(f"Uyarı: {self.filename} bozuk veya geçersiz. Kütüphane boş başlatıldı.")
			self.books = []

	def save_books(self):
		"""
		Save the current list of books to the JSON file.
		"""
		try:
			with open(self.filename, "w", encoding="utf-8") as f:
				json.dump([book.__dict__ for book in self.books], f, ensure_ascii=False, indent=4)
		except Exception as e:
			print(f"Hata: Kitaplar kaydedilemedi: {e}")
