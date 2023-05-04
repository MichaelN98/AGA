import requests


class BaseAPI:
    def __init__(self, env):
        self.__requests = requests
        self.__base_url = env.base_api_url
        self.__headers = {"Accept": "*/*"}

    def _get(self, url, headers=None, params=None):
        if headers is None:
            headers = self.__headers
        return self.__requests.get(f'{self.__base_url}{url}', headers=headers, params=params)

    def _post(self, url, body, headers=None, params=None):
        if headers is None:
            headers = self.__headers
        return self.__requests.post(f'{self.__base_url}{url}', data=body, headers=headers, params=params)

    def call_api(self, endpoint, method='GET', headers=None, data=None, params=None):
        url = f"{self.__base_url}/{endpoint}"
        response = requests.request(method=method, url=url, headers=headers, data=data, params=params)
        return response
