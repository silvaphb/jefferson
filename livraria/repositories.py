from abc import ABC, abstractmethod
from .entities import BookEntity

class IBookRepository(ABC):
    @abstractmethod
    def save(self, book: BookEntity) -> BookEntity:
        ...

    @abstractmethod
    def get_unique(self, id: int) -> BookEntity:
        ...

    @abstractmethod
    def verify_exists(self) -> bool:
        ...

    @abstractmethod
    def find_by_id(self, id: int) -> BookEntity:
        ...

    @abstractmethod
    def search_all(self) -> BookEntity:
        ...

    @abstractmethod
    def delete(self, id: int) -> None:
        ...
    