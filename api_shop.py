import requests
from data import Url, ApiUrls


class ApiShop:

    @staticmethod
    def create_user(body):
        return requests.post(f'{Url.MAIN_URL}{ApiUrls.CREATE_USER}', json=body)

    @staticmethod
    def delete_user(token):
        return requests.delete(f'{Url.MAIN_URL}{ApiUrls.DELETE_USER}', headers={'Authorization': token})