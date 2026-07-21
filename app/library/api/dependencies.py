from dependency_injector import containers, providers

from app.library.application.use_cases import (
    DeleteBookUseCase,
    RegisterBookUseCase,
    ReturnBookUseCase,
    UpdateBookUseCase,
)
from app.library.infrastruture.repository import BookRepository


class LibraryContainer(containers.DeclarativeContainer):
    book_repo = providers.Factory(BookRepository)
    register_book_use_case = providers.Factory(
        RegisterBookUseCase, book_repo=book_repo
    )
    return_book_use_case = providers.Factory(
        ReturnBookUseCase, book_repo=book_repo
    )
    delete_book_use_case = providers.Factory(
        DeleteBookUseCase, book_repo=book_repo
    )
    update_book_use_case = providers.Factory(
        UpdateBookUseCase, book_repo=book_repo
    )
