from .repositories import IBookRepository
from .entities import BookEntity

from typing import List

from .models import Book

class BookRepository(IBookRepository):
    def save(self, book: BookEntity) -> BookEntity:
        Book.objects.update_or_create(
            id=book.id,
            defaults={
                'title': book.title,
                'author': book.author,
                'description': book.description,
                'publication': book.publication,
                'category': book.category,
                'stock': book.stock
            }
        )
        return book
    
    def verify_exists(self, title: str) -> bool:
        return Book.objects.filter(title=title).exists()
    
    def find_by_id(self, id: int) -> BookEntity | bool:
       if Book.objects.filter(id=id).exists():
           book = Book.objects.get(id=id)
           return self._to_model(book)
       
       return False

    def get_unique(self, id: int) -> BookEntity | None:
        book = Book.objects.get(id=id)
        if not book:
            return None
        return self._to_model(book)

    def search_all(self) -> List[BookEntity]:
        books = Book.objects.all()
        return [self._to_model(book) for book in books]
    
    def delete(self, id: int) -> None:
        try:
            Book.objects.get(id=id).delete()
            return None
        except Book.DoesNotExist:
            return None
    
    def _to_model(self, book) -> BookEntity:
        return BookEntity(
            id=book.id,
            title=book.title,
            author=book.author,
            description=book.description,
            publication=book.publication,
            category=book.category,
            stock=book.stock
        )