from typing import List
from ninja import NinjaAPI
from .models import Book
from django.forms.models import model_to_dict
from .schemas import BookIn, BookOut, BookUpdate


api = NinjaAPI()


@api.get('/livros', response={200: List[BookOut]})
def view_books(request):
    books = list(Book.objects.all().values())
    return 200, books

@api.post('/livro', response={201: BookOut, 404: dict})
def new_book(request, book: BookIn):
    try:
        if Book.objects.filter(title=book.title).exists():
            return 404, {'Error': 'Livro já existente!'}
        new_book = Book(title=book.title, author=book.author, description=book.description, publication=book.publication, category=book.category, stock=book.stock)
        new_book.save()
        return 201, BookOut.from_domain(new_book)
    except Exception as error:
        return 404, {'Error': error}

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
