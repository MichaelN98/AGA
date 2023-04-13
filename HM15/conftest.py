import pytest

from HM15.human import Human


@pytest.fixture()
def create_human():
    return Human('Alex', 23, 'female')


@pytest.fixture()
def create_human_dead():
    return Human('Tomas', 150, 'male')
