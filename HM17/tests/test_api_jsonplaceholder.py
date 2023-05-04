from HM17.api_collection.post_api import PostAPI
from HM17.data_object.post_data import PostData

from http import HTTPStatus


def test_get_all_posts(env, post_mock):
    expected_post = post_mock
    response = PostAPI(env).get_post(1)
    response_data = response.json()
    actual_post = PostData.from_json(**response_data)
    assert response.status_code == HTTPStatus.OK, 'Status code is not as expected'
    assert actual_post == expected_post, 'Post is not expected'


def test_create_post(env, post_mock):
    expected_post = post_mock
    response = PostAPI(env).create_post(PostData.post_data)
    response_data = response.json()
    actual_post = PostData.from_json(**response_data)
    assert response.status_code == 201
    assert actual_post == expected_post


def test_update_post(env, post_mock):
    expected_post = post_mock
    response = PostAPI(env).get_post(1)
    response_data = response.json()
    actual_post = PostAPI.update_post(1, PostData.updated_post_data)
    assert response.status_code == 200
    assert actual_post == expected_post == 'updated title'


def test_delete_post(env, post_mock):
    expected_post = post_mock
    response = PostAPI(env).get_post(1)
    response_data = response.json()
    actual_post = PostAPI.delete_post(1)
    assert response.status_code == 200
    assert actual_post == expected_post  # Empty JSON response
