import requests
from YouGileAPI import YouGileAPI

base_url = 'https://ru.yougile.com/api-v2/'
token = 'CDQBQEouQE1MNO2r7mV+VBY2EhiQPeGW5BteNVKzT8HTdjlnu2agaKgacvRlkEwF' # Указать личный токен компании
user_id = '2660968b-501d-405e-9780-c1dfe73eecaf' # Указать личный user id

api = YouGileAPI(base_url, token, user_id)
invalid_api = YouGileAPI(base_url, "123", user_id)


def test_positive_create_project():
    resp = api.create_project('Тестовый проект 1')

    assert resp.status_code == 201

    resp_data = resp.json()
    assert 'id' in resp_data

def test_negative_create_project():
    resp = invalid_api.create_project('Тестовый проект 2')

    assert resp.status_code == 401