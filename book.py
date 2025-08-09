
class Book:
	"""
	Represents a book with title, author, and ISBN.
	"""
	def __init__(self, title: str, author: str, isbn: str):
		self.title = title
		self.author = author
		self.isbn = isbn

	def __str__(self):
		return f"{self.title} by {self.author} (ISBN: {self.isbn})"
