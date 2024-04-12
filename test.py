import pytest

from main import BooksCollector


@pytest.fixture(scope="class")
def books_collector():
    return BooksCollector()


@pytest.fixture(scope="class")
def book_sample():
    return 'Властелин Колец'


@pytest.fixture(scope="class")
def filled_book_collection(book_sample):
    filled_data = BooksCollector()
    books = [
        [book_sample, 'Фантастика'],
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

    def test_genre_init_correctly(self, books_collector):
        expected = ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
        assert books_collector.genre == expected

    def test_genre_age_rating_init_correctly(self, books_collector):
        expected = ['Ужасы', 'Детективы']
        assert books_collector.genre_age_rating == expected

    @pytest.mark.parametrize("book_name, expected_result", [
        ("Властелин Колец", True),
        ("Очень длинное название, которое не должно добавиться в качестве названия книги", False)
    ])
    def test_add_new_book_orig_and_less_than_41_symbol(self, book_name, expected_result, books_collector):
        books_collector.add_new_book(book_name)
        assert (book_name in books_collector.books_genre) == expected_result

    def test_add_new_book_twice(self, book_sample, books_collector):
        books_collector.add_new_book(book_sample)
        books_collector.set_book_genre(book_sample, 'Фантастика')
        books_collector.add_new_book(book_sample)
        assert len(books_collector.books_genre) == 1 and books_collector.get_book_genre(book_sample) == 'Фантастика'

    def test_set_book_genre(self, books_collector, book_sample):
        books_collector.add_new_book(book_sample)
        books_collector.set_book_genre(book_sample, 'Фантастика')
        assert books_collector.books_genre[book_sample] == 'Фантастика'

    def test_get_book_genre(self, book_sample, filled_book_collection):
        assert filled_book_collection.get_book_genre(book_sample) == 'Фантастика'

    def test_get_books_for_children(self, book_sample, filled_book_collection):
        expected = ['Властелин Колец', 'Губка Боб Квадратные Штаны', 'Похождения бравого солдата Швейка']
        assert filled_book_collection.get_books_for_children() == expected

    def test_add_book_in_favorites_existing_book(self, filled_book_collection):
        filled_book_collection.add_new_book("Волшебник изумрудного города")
        filled_book_collection.add_book_in_favorites("Волшебник изумрудного города")
        assert "Волшебник изумрудного города" in filled_book_collection.favorites

    def test_add_book_in_favorites_non_existing_book(self, filled_book_collection):
        filled_book_collection.add_book_in_favorites("Нет такой книги")
        assert "Нет такой книги" not in filled_book_collection.favorites

    def test_delete_book_from_favorites_existing_book(self, filled_book_collection):
        filled_book_collection.add_new_book("Волшебник изумрудного города")
        filled_book_collection.add_book_in_favorites("Волшебник изумрудного города")
        filled_book_collection.delete_book_from_favorites("Волшебник изумрудного города")
        assert "Волшебник изумрудного города" not in filled_book_collection.favorites

    def test_delete_book_from_favorites_non_existing_book(self, filled_book_collection):
        filled_book_collection.delete_book_from_favorites("Нет такой книги")
        assert "Нет такой книги" not in filled_book_collection.favorites

    def test_get_list_of_favorites_books(self, filled_book_collection):
        filled_book_collection.add_new_book("Волшебник изумрудного города")
        filled_book_collection.add_book_in_favorites("Волшебник изумрудного города")
        assert filled_book_collection.get_list_of_favorites_books() == ["Волшебник изумрудного города"]
