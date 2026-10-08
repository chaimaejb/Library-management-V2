from main.repositories.BookRepository import BookRepository


def test_get_all_books():
    repository = BookRepository()

    books = repository.get_all()

    assert isinstance(books, list)


def test_get_book_by_id():
    repository = BookRepository()

    books = repository.get_all()
    book = books[0]

    result = repository.get_by_id(book.id)

    assert result is not None
    assert result.id == book.id

def test_get_book_by_id_returns_none_when_not_found():
    repository = BookRepository()

    result = repository.get_by_id("does-not-exist")

    assert result is None

def test_get_book_by_title_and_author_ignores_case():
    repository = BookRepository()

    books = repository.get_all()
    book = books[0]

    result = repository.get_by_title_and_author(
        book.title.upper(),
        book.author.upper()
    )

    assert result is not None
    assert result.id == book.id

def test_get_book_by_title_and_author_returns_none_when_not_found():
    repository = BookRepository()

    result = repository.get_by_title_and_author(
        "This Book Does Not Exist",
        "Unknown Author"
    )

    assert result is None