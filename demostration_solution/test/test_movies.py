from unittest.mock import MagicMock

import pytest

from demostration_solution.dao.model.movie import Movie
from demostration_solution.dao.movie import MovieDAO
from demostration_solution.service.movie import MovieService


@pytest.fixture
def movie_dao():
    movie_dao = MovieDAO(None)

    movie1 = Movie(
        id=1,
        title="m1",
        description="M1 DESCR",
        trailer="tr1",
        year=2001,
        rating=1.5,
        genre_id=1,
        director_id=1,
    )

    movie2 = Movie(
        id=2,
        title="m2",
        description="M2 DESCR",
        trailer="tr2",
        year=2002,
        rating=2.5,
        genre_id=2,
        director_id=2,
    )

    movie3 = Movie(
        id=3,
        title="m3",
        description="M3 DESCR",
        trailer="tr3",
        year=2003,
        rating=3.5,
        genre_id=3,
        director_id=3,
    )

    movies = {
        1: movie1,
        2: movie2,
        3: movie3
    }

    movie_dao.get_one = MagicMock(return_value = movies.get(1))
    movie_dao.get_all = MagicMock(return_value = [movie1, movie2, movie3])
    movie_dao.create = MagicMock(return_value = Movie(id=4, title="m4"))
    movie_dao.delete = MagicMock(return_value = movies.pop(1))
    movie_dao.update = MagicMock()

    return movie_dao

class TestMovieService():
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(dao = movie_dao)

    def test_get_one(self):
        movie = self.movie_service.get_one(1)
        assert movie != None

    def test_get_all(self):
        movies = self.movie_service.get_all()
        assert len(movies) > 0

    def test_create(self):
        movie = self.movie_service.create("some data")
        assert movie.id != None

    def test_delete(self):
        self.movie_service.delete(1)

    def test_update(self):
        movie_data = {
            "id": 2,
            "title": "m2_new",
            "description": "M2 DESCR_new",
            "trailer": "tr2_new",
            "year": 2022,
            "rating": 2.6,
            "genre_id": 2,
            "director_id": 2,
        }
        self.movie_service.update(movie_data)

