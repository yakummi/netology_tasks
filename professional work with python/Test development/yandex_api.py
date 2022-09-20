import requests
import json
from config.token_yandex import TOKEN
class CreateFolder:

    def __init__(self):
        self.token = TOKEN
        self.url = 'https://cloud-api.yandex.net/v1/disk/resources/'
        self.headers = {
            'Authorization': f'OAuth {self.token}',
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
        self.dir_href = None

    def create_folder(self, name_dir: str):
        parametrs = {
            'path': f'/{name_dir}/'
        }
        response = requests.put(self.url, headers=self.headers, params=parametrs)
        return response


if __name__ == '__main__':
    user = UsersYD()
    print(user.create_folder('new_folder_python').json())