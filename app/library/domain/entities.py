from dataclasses import dataclass, field
from uuid import UUID
from datetime import date

@dataclass
class BookEntity:
    id: UUID | None = field(default=None)
    title: str = field(default='')
    author: str = field(default='')
    description: str = field(default='')
    publication: date = field(default='')
    category: str = field(default='')
    stock: int = field(default=0)

    def change_title(self, title: str):
        if title:
            self.title = title

    def change_author(self, author: str):
        if author:
            self.author = author

    def change_description(self, description: str):
        if description:
            self.description = description

    def change_publication(self, publication: str):
        if publication:
            self.publication = publication

    def change_category(self, category: str):
        if category:
            self.category = category

    def change_stock(self, stock: int):
        if stock:
            self.stock = stock
