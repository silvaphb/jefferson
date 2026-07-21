from app.library.domain.repositories import IBookRepository
from app.library.domain.entities import BookEntity
from app.library.application.dtos import BookInDTO, BookOutDTO, BookUpdateDTO
from uuid import UUID


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
            stock=book.stock,
        )

        book_saved = self.book_repo.save(book=data)
        return BookOutDTO.from_domain(book_saved)


class ReturnBookUseCase:
    def __init__(self, book_repo: IBookRepository) -> None:
        self.book_repo = book_repo

    def execute(self, id: UUID) -> BookOutDTO:
            book = self.book_repo.find_by_id(id)
            if not book:
                raise Exception('book don´t exists')
            return BookOutDTO.from_domain(book)


class DeleteBookUseCase:
    def __init__(self, book_repo: IBookRepository):
        self.book_repo = book_repo

    def execute(self, id: UUID) -> bool:
        return self.book_repo.delete(id)


class UpdateBookUseCase:
    def __init__(self, book_repo: IBookRepository) -> None:
        self.book_repo = book_repo

    def execute(self, id: UUID, dto: BookUpdateDTO) -> BookOutDTO:
        book = self.book_repo.find_by_id(id)
        if not book:
            raise Exception('book don´t exists')

        if dto.title:
            book.change_title(dto.title)

        if dto.author:
            book.change_author(dto.author)

        if dto.description:
            book.change_description(dto.description)

        if dto.publication:
            book.change_publication(dto.publication)

        if dto.category:
            book.change_category(dto.category)

        if dto.stock:
            book.change_stock(dto.stock)

        book_entity = self.book_repo.save(book)
        return BookOutDTO.from_domain(book_entity)
