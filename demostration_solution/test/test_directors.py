from unittest.mock import MagicMock

import pytest

from demostration_solution.dao.director import DirectorDAO
from demostration_solution.dao.model.director import Director
from demostration_solution.service.director import DirectorService


@pytest.fixture
def director_dao():
    director_dao = DirectorDAO(None)

    director1 = Director(
        id=1,
        name="d1",
    )

    director2 = Director(
        id=2,
        name="d2",
    )

    director3 = Director(
        id=3,
        name="d3",
    )

    directors = {
        1: director1,
        2: director2,
        3: director3
    }

    director_dao.get_one = MagicMock(return_value = directors.get(1))
    director_dao.get_all = MagicMock(return_value = [director1, director2, director3])
    director_dao.create = MagicMock(return_value = Director(id=4, name="d4"))
    director_dao.delete = MagicMock(return_value = directors.pop(1))
    director_dao.update = MagicMock()

    return director_dao

class TestDirectorService():
    @pytest.fixture(autouse=True)
    def director_service(self, director_dao):
        self.director_service = DirectorService(dao = director_dao)

    def test_get_one(self):
        director = self.director_service.get_one(1)
        assert director != None

    def test_get_all(self):
        directors = self.director_service.get_all()
        assert len(directors) > 0

    def test_create(self):
        director = self.director_service.create("some data")
        assert director.id != None

    def test_delete(self):
        self.director_service.delete(1)

    def test_update(self):
        director_data = {
            "id": 2,
            "name": "d2_new",
        }
        self.director_service.update(director_data)

