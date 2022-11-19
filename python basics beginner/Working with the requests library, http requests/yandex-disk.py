import requests
import os

class YandexUploader:
    upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
    def __init__(self, token: str):
        self.token = token

    def _get_upload_link(self):
        headers = {
            'Authorization': f'OAuth {self.token}',
            'Content-Type': 'application/json'
        }
        params = {'path': '/papka.txt', 'overwrite': True}
        response = requests.get(self.upload_url, headers=headers, params=params)

        return response.json()

    def upload_file(self, path):
        response = requests.get(self._get_upload_link().get('href', ''), data=open(path, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            return 'Download completed'

if __name__ == '__main__':
    path_to_file = os.path.join(os.getcwd(), '2.py')
    TOKEN = ''
    print(YandexUploader(TOKEN).upload_file(path_to_file))
