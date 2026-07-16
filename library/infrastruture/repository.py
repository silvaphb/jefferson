from library.domain.repositories import IBookRepository
from library.domain.entities import BookEntity

from typing import List

from .models import Book


class BookRepository(IBookRepository):
    def save(self, book: BookEntity) -> BookEntity:
        obj, _ = Book.objects.update_or_create(
            id=book.id,
            defaults={
                'title': book.title,
                'author': book.author,
                'description': book.description,
                'publication': book.publication,
                'category': book.category,
                'stock': book.stock,
            },
        )
        return self._to_model(obj)

    def verify_exists(self, title: str) -> bool:
        return Book.objects.filter(title=title).exists()

    def find_by_id(self, id: int) -> BookEntity | bool:
        if Book.objects.filter(id=id).exists():
            book = Book.objects.get(id=id)
            return self._to_model(book)

        return False

    def get_unique(self, id: int) -> BookEntity | None:
        try:
            book = Book.objects.get(id=id)
            if not book:
                return None
            return self._to_model(book)
        except Book.DoesNotExist:
            return None

    def search_all(self) -> List[BookEntity]:
        books = Book.objects.all()
        return [self._to_model(book) for book in books]

    def delete(self, id: int) -> None:
        try:
            Book.objects.get(id=id).delete()
            return True
        except Book.DoesNotExist:
            return False

    def _to_model(self, book) -> BookEntity:
        return BookEntity(
            id=book.id,
            title=book.title,
            author=book.author,
            description=book.description,
            publication=book.publication,
            category=book.category,
            stock=book.stock,
        )
