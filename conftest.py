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


@pytest.fixture(scope="session")
def filled_book_collection():
    filled_data = BooksCollector()
    books = [
        ['Мертвая зона', 'Ужасы'],
        ['Шерлок Холмс', 'Детективы'],
        ['Губка Боб Квадратные Штаны', 'Мультфильмы'],
        ['Похождения бравого солдата Швейка', 'Комедии']
    ]
    for book_name, genre in books:
        filled_data.add_new_book(book_name)
        filled_data.set_book_genre(book_name, genre)

    return filled_data
