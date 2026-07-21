from abc import ABC, abstractmethod
from app.library.domain.entities import BookEntity
from uuid import UUID


class IBookRepository(ABC):
    @abstractmethod
    def save(self, book: BookEntity) -> BookEntity:
        ...

    @abstractmethod
    def verify_exists(self) -> bool:
        ...

    @abstractmethod
    def find_by_id(self, id: UUID) -> BookEntity:
        ...

    @abstractmethod
    def search_all(self) -> BookEntity:
        ...

    @abstractmethod
    def delete(self, id: UUID) -> None:
        ...
