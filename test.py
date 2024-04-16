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


class TestBooksCollector:

    def test_books_genre_init_empty(self, books_collector):
        assert books_collector.books_genre == {}

    def test_favorites_init_empty(self, books_collector):
        assert books_collector.favorites == []

    def test_genre_init_correctly(self, expected_genre, books_collector):
        assert books_collector.genre == expected_genre

    def test_genre_age_rating_init_correctly(self, expected_genre_18_plus, books_collector):
        assert books_collector.genre_age_rating == expected_genre_18_plus

    @pytest.mark.parametrize("book_name, expected_result", [
        ('Властелин Колец', True),
        ("Очень длинное название, которое не должно добавиться в качестве названия книги", False)
    ])
    def test_add_new_book_orig_and_less_than_41_symbol(self, book_name, expected_result, books_collector):
        books_collector.add_new_book(book_name)
        assert (book_name in books_collector.books_genre) == expected_result

    @pytest.mark.parametrize("book_name, expected_result", [('Властелин Колец', '')])
    def test_add_new_book_genre_is_empty(self, book_name, expected_result, books_collector):
        books_collector.add_new_book(book_name)
        assert (books_collector.books_genre[book_name]) == expected_result and books_collector.get_book_genre(
            book_name) == expected_result

    @pytest.mark.parametrize('book_name, book_name_genre', [('Властелин Колец', 'Фантастика')])
    def test_add_new_book_twice(self, books_collector, book_name, book_name_genre):
        books_collector.add_new_book(book_name)
        books_collector.set_book_genre(book_name, book_name_genre)
        books_collector.add_new_book(book_name)
        assert len(books_collector.books_genre) == 1 and books_collector.get_book_genre(book_name) == book_name_genre

    @pytest.mark.parametrize('book_name, book_name_genre', [('Властелин Колец', 'Фантастика')])
    def test_set_book_genre_correct(self, books_collector, book_name, book_name_genre):
        books_collector.add_new_book(book_name)
        books_collector.set_book_genre(book_name, book_name_genre)
        assert books_collector.books_genre[book_name] == book_name_genre or books_collector.get_book_genre(
            book_name) == book_name_genre

    @pytest.mark.parametrize('book_name, book_name_genre', [('Властелин Колец', 'Фантастика')])
    def test_get_book_genre_correct(self, filled_book_collection, book_name, book_name_genre):
        filled_book_collection.add_new_book(book_name)
        filled_book_collection.set_book_genre(book_name, book_name_genre)
        assert filled_book_collection.get_book_genre(book_name) == book_name_genre

    def test_get_books_for_children_no_adult_genres(self, filled_book_collection, expected_genre_18_plus):
        children_books = filled_book_collection.get_books_for_children()
        assert all(filled_book_collection.get_book_genre(book) not in expected_genre_18_plus for book in children_books)

    def test_add_book_in_favorites_existing_book_success(self, filled_book_collection, book_favorite='Гарри Поттер и Узник Азкабана'):
        filled_book_collection.add_new_book(book_favorite)
        filled_book_collection.add_book_in_favorites(book_favorite)
        assert book_favorite in filled_book_collection.favorites

    def test_add_book_in_favorites_non_existing_book_failed(self, filled_book_collection):
        book_name = 'Нет такой книги'
        filled_book_collection.add_book_in_favorites(book_name)
        assert book_name not in filled_book_collection.favorites

    @pytest.mark.parametrize('book_name', [('Волшебник изумрудного города', 'Нет такой книги')])
    def test_delete_book_from_favorites_existing_book_success(self, filled_book_collection, book_name):
        filled_book_collection.add_new_book(book_name)
        filled_book_collection.add_book_in_favorites(book_name)
        filled_book_collection.delete_book_from_favorites(book_name)
        assert book_name not in filled_book_collection.favorites

    @pytest.mark.parametrize('book_name', [('Волшебник изумрудного города', 'Нет такой книги')])
    def test_delete_book_from_favorites_non_existing_book_failed(self, filled_book_collection, book_name):
        filled_book_collection.add_new_book(book_name)
        filled_book_collection.add_book_in_favorites(book_name)
        filled_book_collection.delete_book_from_favorites(book_name)
        assert book_name not in filled_book_collection.favorites
