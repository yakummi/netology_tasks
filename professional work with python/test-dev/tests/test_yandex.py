import pytest
import requests
from yandex_api import CreateFolder


@pytest.fixture()
def teardown():
    print("Let's go!")
    yield
    url = CreateFolder().url
    headers = CreateFolder().headers
    params = {
        'path': 'new_folder',
        'permanently': 'true'
    }
    requests.delete(url, params=params, headers=headers)


def test_correct_folder_creation(teardown):
    resp = CreateFolder().create_folder('h1')
    assert resp.status_code in [200, 201]
    return resp


def test_folder_presence(teardown):
    resp = CreateFolder().create_folder('h2')
    assert 'href' in resp.json().keys()


@pytest.mark.xfail()
def test_fail_folder_creation(teardown):
    resp = CreateFolder().create_folder('h3')
    assert resp.status_code in [400, 401, 403, 404, 406, 409, 413, 423, 429, 503, 507]
