import requests
from pathlib import Path


class APIRequester:
    """Базовый класс, который выполняет get-запрос."""

    def __init__(self, url):
        self.base_url = url

    def get(self, url_data):
        """Функция выполняет get-запрос к адресу url_data."""
        try:
            response = requests.get(self.base_url + url_data)
            response.raise_for_status()
            return response
        except requests.HTTPError:
            print('Возникла ошибка при выполнении запроса')
            return requests.Response()
        except requests.exceptions.RequestException:
            print('Возникла ошибка при выполнении запроса')
            return requests.Response()


class SWRequester(APIRequester):
    """
    Класс, который получает информацию о категориях
    по адресу https://swapi.dev/api.
    """

    def get_sw_categories(self):
        """Функция возвращает список категорий."""
        try:
            response = requests.get(f'{self.base_url}/')
            response.raise_for_status()
        except requests.HTTPError:
            print('Возникла ошибка при выполнении запроса')
        except requests.exceptions.RequestException:
            print('Возникла ошибка при выполнении запроса')
        else:
            json_response = response.json()
            categories = json_response.keys()
            return categories

    def get_sw_info(self, sw_type):
        """
        Функция получает информацию
        о категории, заданной в переменной sw_type.
        """
        try:
            response = requests.get(f'{self.base_url}/{sw_type}/')
            response.raise_for_status()
        except requests.HTTPError:
            print('Возникла ошибка при выполнении запроса')
        except requests.exceptions.RequestException:
            print('Возникла ошибка при выполнении запроса')
        else:
            return response.text


def save_sw_data():
    """Функция сохраняет информацию о всех категориях в каталог data."""
    requester = SWRequester('https://swapi.dev/api')
    categories = requester.get_sw_categories()
    if isinstance(categories, str):
        print(categories)
    else:
        Path('data').mkdir(exist_ok=True)
        for category in categories:
            with open(f'data/{category}.txt', 'w') as file:
                file.write(requester.get_sw_info(category))
