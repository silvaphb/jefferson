from typing import List, Optional
from ninja import NinjaAPI
from .models import Book
from .schemas import BookIn, BookOut, BookUpdate

from .application.use_cases import RegisterBookUseCase, ReturnBookUseCase
from .repository import BookRepository

api = NinjaAPI()


@api.get('/livros', response={200: List[BookOut] | BookOut})
def view_books(request, id: Optional[int] = None):
    use_case = ReturnBookUseCase(BookRepository())
    response = use_case.execute(id)
    if type(response) == list:
        books = [BookOut.from_domain(book) for book in response]
        return 200, books
    
    return 200, response


@api.post('/livro', response={201: BookOut, 404: dict})
def new_book(request, book: BookIn):
    use_case = RegisterBookUseCase(BookRepository())
    book_dto = book.to_dto()
    response = use_case.execute(book_dto)
    if not response:
        return 404, {'Error': 'already exists'}
    
    return 201, BookOut.from_domain(response)

@api.delete('/remover_livro', response={200: dict, 404: dict, 500: dict})
def delete_book(request, id: int):
    try:
        if not Book.objects.filter(id=id).exists():
            return 404, {'Error': 'Não existe este livro'}
        
        book = Book.objects.get(id=id)
        book.delete()
        return 200, {'Success': True}
    except Exception as error:
        return 500, {'Error': error}

@api.patch('/atualizar_livro', response={200: BookOut, 404: dict, 500: dict})
def update_book(request, id: int, book: BookUpdate):
    try:
        if not Book.objects.filter(id=id).exists():
            return 404, {'Error': 'Não existe este livro'}
        
        updated_book = Book.objects.get(id=id)
        for attr, value in book.dict().items():
            setattr(updated_book, attr, value)

        updated_book.save()
        return BookOut.from_domain(updated_book)
    
    except Exception as error:
        return 500, {'Error': error}
