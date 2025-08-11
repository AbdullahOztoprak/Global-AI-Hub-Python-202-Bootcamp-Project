	def update_book(self, isbn: str, title: str = None, author: str = None):
		"""Update book details by ISBN. Only non-None fields are updated."""
		conn = self._get_connection()
		try:
			fields = []
			values = []
			if title is not None:
				fields.append("title = ?")
				values.append(title)
			if author is not None:
				fields.append("author = ?")
				values.append(author)
			if not fields:
				return False
			values.append(isbn)
			with conn:
				result = conn.execute(f"UPDATE books SET {', '.join(fields)} WHERE isbn = ?", values)
			return result.rowcount > 0
		finally:
			conn.close()


import sqlite3
from book import Book

class Library:
	"""
	Manages a collection of Book objects and handles persistence in SQLite database.
	Ensures all changes are saved and loaded reliably.
	"""
	def __init__(self, db_name="library.db"):
		self.db_name = db_name
		self._create_table()

	def _get_connection(self):
		"""Get a new SQLite connection for each operation to handle threading."""
		conn = sqlite3.connect(self.db_name, check_same_thread=False)
		conn.row_factory = sqlite3.Row
		return conn

	def _create_table(self):
		conn = self._get_connection()
		try:
			with conn:
				conn.execute(
					"""
					CREATE TABLE IF NOT EXISTS books (
						id INTEGER PRIMARY KEY AUTOINCREMENT,
						title TEXT NOT NULL,
						author TEXT NOT NULL,
						isbn TEXT UNIQUE NOT NULL
					)
					"""
				)
		finally:
			conn.close()



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
		conn = self._get_connection()
		try:
			with conn:
				conn.execute(
					"INSERT INTO books (title, author, isbn) VALUES (?, ?, ?)",
					(book.title, book.author, book.isbn)
				)
			return True
		except sqlite3.IntegrityError:
			print("Bu ISBN zaten mevcut.")
			return False
		finally:
			conn.close()

	def remove_book(self, isbn: str):
		"""Remove a book by ISBN from the database."""
		conn = self._get_connection()
		try:
			with conn:
				conn.execute("DELETE FROM books WHERE isbn = ?", (isbn,))
		finally:
			conn.close()

	def list_books(self):
		"""Return the list of books from the database."""
		conn = self._get_connection()
		try:
			cursor = conn.execute("SELECT title, author, isbn FROM books")
			return [Book(row["title"], row["author"], row["isbn"]) for row in cursor.fetchall()]
		finally:
			conn.close()

	def find_book(self, isbn: str):
		"""Find a book by ISBN in the database."""
		conn = self._get_connection()
		try:
			cursor = conn.execute("SELECT title, author, isbn FROM books WHERE isbn = ?", (isbn,))
			row = cursor.fetchone()
			if row:
				return Book(row["title"], row["author"], row["isbn"])
			return None
		finally:
			conn.close()

	# JSON persistence methods removed; all data is now in SQLite
