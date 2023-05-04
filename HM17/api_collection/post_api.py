from HM17.utilities.api.base_api import BaseAPI


class PostAPI(BaseAPI):
    def __init__(self, env):
        super().__init__(env)
        self.__post_api = '/post/1'

    def get_post(self, post_id, headers=None):
        return self._get(url=f'{self.__post_api}/{post_id}', headers=headers)

    def get_all_posts(self):
        return BaseAPI(self.__base_url).call_api(self.__post_api)

    def get_post_by_id(self, post_id):
        endpoint = f"{self.__base_url}/{post_id}"
        return BaseAPI(self.__base_url).call_api(endpoint)

    def create_post(self, data):
        return BaseAPI(self.__base_url).call_api(self.__base_url, method='POST', data=data)

    def update_post(self, post_id, data):
        endpoint = f"{self.__base_url}/{post_id}"
        return BaseAPI(self.__base_url).call_api(endpoint, method='PUT', data=data)

    def delete_post(self, post_id):
        endpoint = f"{self.__base_url}/{post_id}"
        return BaseAPI(self.__base_url).call_api(endpoint, method='DELETE')
