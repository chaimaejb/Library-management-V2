import pytest
from main.model.Book import Book


def test_new_book_is_available():
    book = Book("Clean Code", "Robert C. Martin")

    assert book.status == "Available"

def test_checkout_book():
    book = Book("Clean Code", "Robert C. Martin")
    member = "John"

    book.check_out(member)

    assert book.status == "Not available"
    assert book.holder == "John"
    assert book.check_out_date is not None

def test_invalid_status_raises_error():
    book = Book("Clean Code", "Robert C. Martin")

    with pytest.raises(ValueError):
        book.status = "Something wrong"

def test_check_in_book():
    book = Book("Clean Code", "Robert C. Martin")
    member = "John"

    book.check_out(member)
    book.check_in()

    assert book.status == "Available"
    assert book.holder is None
    assert book.check_out_date is None

def test_cannot_checkout_unavailable_book():
    book = Book("Clean Code", "Robert C. Martin")
    member_1 = "John"
    member_2 = "Sara"

    book.check_out(member_1)
    book.check_out(member_2)

    assert book.status == "Not available"
    assert book.holder == "John"

def test_check_in_available_book():
    book = Book("Clean Code", "Robert C. Martin")

    book.check_in()

    assert book.status == "Available"
    assert book.holder is None
    assert book.check_out_date is None