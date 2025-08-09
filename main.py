
from library import Library
from book import Book

def main():
	"""
	Main application loop for the library CLI.
	"""
	library = Library()
	while True:
		print("\nKütüphane Yönetimi")
		print("1. Kitap Ekle")
		print("2. Kitap Sil")
		print("3. Kitapları Listele")
		print("4. Kitap Ara")
		print("5. Çıkış")
		choice = input("Seçiminizi girin (1-5): ").strip()

		if choice == "1":
			title = input("Kitap adı: ").strip()
			author = input("Yazar: ").strip()
			isbn = input("ISBN: ").strip()
			if not title or not author or not isbn:
				print("Hata: Tüm alanlar doldurulmalıdır.")
				continue
			if library.find_book(isbn):
				print("Hata: Bu ISBN ile zaten bir kitap var.")
				continue
			book = Book(title, author, isbn)
			library.add_book(book)
			print("Kitap eklendi.")

		elif choice == "2":
			isbn = input("Silinecek kitabın ISBN'i: ").strip()
			if library.find_book(isbn):
				library.remove_book(isbn)
				print("Kitap silindi.")
			else:
				print("Hata: Bu ISBN ile kitap bulunamadı.")

		elif choice == "3":
			books = library.list_books()
			if not books:
				print("Kütüphanede hiç kitap yok.")
			else:
				for book in books:
					print(book)

		elif choice == "4":
			isbn = input("Aranacak kitabın ISBN'i: ").strip()
			book = library.find_book(isbn)
			if book:
				print(book)
			else:
				print("Kitap bulunamadı.")

		elif choice == "5":
			print("Çıkılıyor...")
			break
		else:
			print("Geçersiz seçim. Lütfen 1-5 arasında bir değer girin.")

if __name__ == "__main__":
	main()
