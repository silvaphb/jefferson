from typing import Optional
from ninja import Schema
from app.library.application.dtos import BookInDTO


class BookIn(Schema):
    title: str
    author: str
    description: str
    publication: str
    category: str
    stock: int

    def to_dto(self) -> BookInDTO:
        return BookInDTO(
            title=self.title,
            author=self.author,
            description=self.description,
            publication=self.publication,
            category=self.category,
            stock=self.stock,
        )


class BookOut(Schema):
    id: int
    title: str
    author: str
    description: str
    publication: str
    category: str
    stock: int

    @staticmethod
    def from_domain(model):
        return BookOut(
            id=model.id,
            title=model.title,
            author=model.author,
            description=model.description,
            publication=model.publication,
            category=model.category,
            stock=model.stock,
        )


class BookUpdate(Schema):
    title: Optional[str] = None
    author: Optional[str] = None
    description: Optional[str] = None
    publication: Optional[str] = None
    category: Optional[str] = None
    stock: Optional[int] = None
