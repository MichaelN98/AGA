import pytest

from HM17.data_object.post_data import PostData


@pytest.fixture()
def post_mock():
    return PostData()

