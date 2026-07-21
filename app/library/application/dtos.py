from pydantic import BaseModel
from typing import Optional


class BookInDTO(BaseModel):
    title: str
    author: str
    description: str
    publication: str
    category: str
    stock: int


class BookOutDTO(BaseModel):
    id: int
    title: str
    author: str
    description: str
    publication: str
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
    publication: Optional[str] = None
    category: Optional[str] = None
    stock: Optional[int] = None
