from typing import List
from ninja import Router

from app.library.api.dependencies import LibraryContainer
from app.library.api.schemas import BookIn, BookOut, BookUpdate

api = Router()
container = LibraryContainer()

@api.post('/book', response={201: BookOut})
def new_book(request, book: BookIn):
    use_case = container.register_book_use_case()
    book_dto = book.to_dto()
    response = use_case.execute(book_dto)
    return 201, BookOut.from_domain(response)


@api.get('/book', response={200: List[BookOut] | BookOut})
def view_books(request, id: int):
    use_case = container.return_book_use_case()
    response = use_case.execute(id)
    return 200, response


@api.delete('/remove_book', response={200: bool})
def delete_book(request, id: int):
    use_case = container.delete_book_use_case()
    response = use_case.execute(id)
    return 200, response


@api.patch('/update_book', response={200: BookOut})
def update_book(request, id: int, book: BookUpdate):
    use_case = container.update_book_use_case()
    response = use_case.execute(id, book)
    return 200, response