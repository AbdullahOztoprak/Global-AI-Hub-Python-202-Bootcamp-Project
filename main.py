from library import Library
from book import Book

def main():
	"""
	Kütüphane uygulamasının ana döngüsünü başlatır.
	Kullanıcıya basit bir menü sunar ve kitap ekleme, silme, listeleme, arama işlemlerini yapar.
	"""
	library = Library()  # Kütüphane nesnesi oluşturulur
	while True:
		# Menü seçeneklerini ekrana yazdır
		print("\nKütüphane Yönetimi")
		print("1. Kitap Ekle")
		print("2. Kitap Sil")
		print("3. Kitapları Listele")
		print("4. Kitap Ara")
		print("5. Çıkış")
		choice = input("Seçiminizi girin (1-5): ").strip()


		# 1. Kitap ekleme işlemi
		if choice == "1":
			isbn = input("ISBN: ").strip()
			if not isbn:
				print("Hata: ISBN alanı boş olamaz.")
				continue
			# Aynı ISBN varsa ekleme
			if library.find_book(isbn):
				print("Hata: Bu ISBN ile zaten bir kitap var.")
				continue
			# Sadece ISBN giriliyor, başlık ve yazar API'den alınacak
			result = library.add_book(isbn)
			if result:
				print("Kitap eklendi.")
			else:
				print("Kitap eklenemedi.")

		# 2. Kitap silme işlemi
		elif choice == "2":
			isbn = input("Silinecek kitabın ISBN'i: ").strip()
			if library.find_book(isbn):
				library.remove_book(isbn)
				print("Kitap silindi.")
			else:
				print("Hata: Bu ISBN ile kitap bulunamadı.")

		# 3. Kitapları listeleme işlemi
		elif choice == "3":
			books = library.list_books()
			if not books:
				print("Kütüphanede hiç kitap yok.")
			else:
				for book in books:
					print(book)

		# 4. Kitap arama işlemi
		elif choice == "4":
			isbn = input("Aranacak kitabın ISBN'i: ").strip()
			book = library.find_book(isbn)
			if book:
				print(book)
			else:
				print("Kitap bulunamadı.")

		# 5. Çıkış işlemi
		elif choice == "5":
			print("Çıkılıyor...")
			break
		# Geçersiz seçim durumu
		else:
			print("Geçersiz seçim. Lütfen 1-5 arasında bir değer girin.")

# Programın ana kısmı buradan başlar
if __name__ == "__main__":
	main()
