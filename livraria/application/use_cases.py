from typing import Optional, List

from ..repositories import IBookRepository
from ..entities import BookEntity
from .dtos import BookInDTO, BookOutDTO, BookUpdateDTO
from ..repository import BookRepository

class RegisterBookUseCase:
    def __init__(self, book_repo: IBookRepository) -> None:
        self.book_repo = book_repo
    
    def execute(self, book: BookInDTO) -> BookOutDTO | None:
        if self.book_repo.verify_exists(book.title):
            return None
        
        data = BookEntity(
            title=book.title,
            author=book.author,
            description=book.description,
            publication=book.publication,
            category=book.category,
            stock=book.stock
        )

        book_saved = self.book_repo.save(book=data)
        return BookOutDTO.from_domain(book_saved)
    
class ReturnBookUseCase:
    def __init__(self, book_repo: IBookRepository) -> None:
        self.book_repo = book_repo

    def execute(self, id: Optional[int]) -> BookOutDTO | List[BookOutDTO]:

        if id:
            book = self.book_repo.get_unique(id)
            return BookOutDTO.from_domain(book)
        
        
        
        return [BookOutDTO.from_domain(book) for book in self.book_repo.search_all()]
        
        