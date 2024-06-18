import requests


class TestYandexDisk:
    def setup_method(self):
        self.headers = {'Authorization': 'тут ваш яндекс токен'}

    def test_create_folder(self):
        params = {'path': 'folder_1'}
        response = requests.put('https://cloud-api.yandex.net/v1/disk/resources',
                                headers=self.headers,
                                params=params)

        assert response.status_code == 201

    def test_create_folder_again(self):
        params = {'path': 'folder_1'}
        response = requests.put('https://cloud-api.yandex.net/v1/disk/resources',
                                headers=self.headers,
                                params=params)

        assert response.status_code == 409
