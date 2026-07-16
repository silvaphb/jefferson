from typing import List, Optional
from ninja import Router

from library.application.dtos import BookUpdateDTO
from library.api.dependencies import LibraryContainer
from library.infrastruture.models import Book
from library.api.schemas import BookIn, BookOut, BookUpdate

from library.application.use_cases import (
    RegisterBookUseCase,
    ReturnBookUseCase,
    DeleteBookUseCase,
    UpdateBookUseCase,
)
from library.infrastruture.repository import BookRepository

api = Router()
container = LibraryContainer()


@api.post('/book', response={201: BookOut, 404: dict})
def new_book(request, book: BookIn):
    use_case = container.register_book_use_case()
    book_dto = book.to_dto()
    response = use_case.execute(book_dto)
    if not response:
        return 404, {'Error': 'already exists'}

    return 201, BookOut.from_domain(response)


@api.get('/book', response={200: List[BookOut] | BookOut})
def view_books(request, id: Optional[int] = None):
    use_case = container.return_book_use_case()
    response = use_case.execute(id)
    if type(response) == list:
        books = [BookOut.from_domain(book) for book in response]
        return 200, books

    return 200, response


@api.delete('/remove_book', response={200: bool, 404: dict, 500: dict})
def delete_book(request, id: int):
    use_case = container.delete_book_use_case()
    response = use_case.execute(id)
    return 200, response


@api.patch('/update_book', response={200: BookOut, 404: dict, 500: dict})
def update_book(request, id: int, book: BookUpdate):
    use_case = container.update_book_use_case()
    response = use_case.execute(id, book)
    return 200, response
