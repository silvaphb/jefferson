from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from datetime import date

class BookInDTO(BaseModel):
    title: str
    author: str
    description: str
    publication: str
    category: str
    stock: int


class BookOutDTO(BaseModel):
    id: UUID
    title: str
    author: str
    description: str
    publication: date
    category: str
    stock: int

    @classmethod
    def from_domain(cls, model):
        return cls(
            id=model.id,
            title=model.title,
            author=model.author,
            description=model.description,
            publication=model.publication,
            category=model.category,
            stock=model.stock,
        )


class BookUpdateDTO(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    description: Optional[str] = None
    publication: Optional[date] = None
    category: Optional[str] = None
    stock: Optional[int] = None
