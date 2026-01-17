import requests
import os
from YouGileAPI import YouGileAPI
from dotenv import load_dotenv
load_dotenv()

base_url = 'https://ru.yougile.com/api-v2/'
token = os.getenv('YouGile_token') 
user_id = os.getenv('YouGile_user_id')

api = YouGileAPI(base_url, token, user_id)
invalid_api = YouGileAPI(base_url, "123", user_id)


def test_positive_create_project():
    resp = api.create_project('Тестовый проект 1')

    assert resp.status_code == 201

    resp_data = resp.json()
    assert 'id' in resp_data

    project_id = resp_data['id']
    delete_proj = api.delete_project(project_id)
    assert delete_proj.status_code == 200

def test_negative_create_project():
    resp = invalid_api.create_project('Тестовый проект 2')

    assert resp.status_code == 401

    error_data = resp.json()
    assert 'message' in error_data or 'error' in error_data