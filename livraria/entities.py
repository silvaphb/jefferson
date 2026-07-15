from dataclasses import dataclass, field

@dataclass
class BookEntity:
    id: int = field(default=0)
    title: str = field(default='')
    author: str = field(default='')
    description: str = field(default='')
    publication: str = field(default='')
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