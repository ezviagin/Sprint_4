import pytest
from main import BooksCollector


@pytest.fixture(scope="class")
def books_collector():
    return BooksCollector()


@pytest.fixture(scope="class")
def expected_genre():
    return ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']


@pytest.fixture(scope="class")
def expected_genre_18_plus():
    return ['Ужасы', 'Детективы']


@pytest.fixture(scope="class")
def filled_book_collection(books_collector):
    books_data = [
        ['Мертвая зона', 'Ужасы'],
        ['Шерлок Холмс', 'Детективы'],
        ['Губка Боб Квадратные Штаны', 'Мультфильмы'],
        ['Похождения бравого солдата Швейка', 'Комедии']
    ]
    for book_name, genre in books_data:
        books_collector.add_new_book(book_name)
        books_collector.set_book_genre(book_name, genre)
    return books_collector
