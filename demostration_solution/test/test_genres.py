from unittest.mock import MagicMock

import pytest

from demostration_solution.dao.genre import GenreDAO
from demostration_solution.dao.model.genre import Genre
from demostration_solution.service.genre import GenreService


@pytest.fixture
def genre_dao():
    genre_dao = GenreDAO(None)

    genre1 = Genre(
        id=1,
        name="g1",
    )

    genre2 = Genre(
        id=2,
        name="g2",
    )

    genre3 = Genre(
        id=3,
        name="g3",
    )

    genres = {
        1: genre1,
        2: genre2,
        3: genre3
    }

    genre_dao.get_one = MagicMock(return_value = genres.get(1))
    genre_dao.get_all = MagicMock(return_value = [genre1, genre2, genre3])
    genre_dao.create = MagicMock(return_value = Genre(id=4, name="g4"))
    genre_dao.delete = MagicMock(return_value = genres.pop(1))
    genre_dao.update = MagicMock()

    return genre_dao

class TestGenreService():
    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao):
        self.genre_service = GenreService(dao = genre_dao)

    def test_get_one(self):
        genre = self.genre_service.get_one(1)
        assert genre != None

    def test_get_all(self):
        genres = self.genre_service.get_all()
        assert len(genres) > 0

    def test_create(self):
        genre = self.genre_service.create("some data")
        assert genre.id != None

    def test_delete(self):
        self.genre_service.delete(1)

    def test_update(self):
        genre_data = {
            "id": 2,
            "name": "g2_new",
        }
        self.genre_service.update(genre_data)

