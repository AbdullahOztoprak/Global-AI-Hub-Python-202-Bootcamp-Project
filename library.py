

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



	def add_book(self, isbn: str):
		"""
		Add a book by ISBN using Open Library API.
		Fetches title and author from API, creates Book, and adds to library.
		Returns True if successful, False otherwise.
		"""
		import httpx
		url = f"https://openlibrary.org/isbn/{isbn}.json"
		headers = {
			"User-Agent": "LibraryApp/1.0 (your-email@example.com)"
		}
		try:
			response = httpx.get(url, headers=headers, timeout=10, follow_redirects=True)
		except httpx.RequestError:
			print("Bağlantı hatası: API'ye ulaşılamıyor. Lütfen internet bağlantınızı kontrol edin.")
			return False
		if response.status_code == 404:
			print("Kitap bulunamadı. Lütfen geçerli bir ISBN girin.")
			return False
		try:
			response.raise_for_status()
			data = response.json()
		except Exception as e:
			print(f"API'den geçerli veri alınamadı. Hata: {e}")
			print(f"Status code: {response.status_code}")
			print(f"Response text: {response.text[:200]}...")
			return False
		title = data.get("title")
		if not title or not isinstance(title, str):
			print("Kitap başlığı API'den alınamadı.")
			return False
		authors = data.get("authors")
		author_names = []
		if authors:
			for author in authors:
				key = author.get("key")
				if key:
					author_url = f"https://openlibrary.org{key}.json"
					try:
						author_resp = httpx.get(author_url, headers=headers, timeout=5, follow_redirects=True)
						author_resp.raise_for_status()
						author_data = author_resp.json()
						name = author_data.get("name")
						if name:
							author_names.append(name)
					except Exception:
						continue
			author_str = ", ".join(author_names) if author_names else "Unknown"
		else:
			author_str = "Unknown"
		book = Book(title, author_str, isbn)
		self.books.append(book)
		self.save_books()
		return True

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
