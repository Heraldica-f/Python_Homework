import requests
import os
from YouGileAPI import YouGileAPI
from dotenv import load_dotenv
load_dotenv()

base_url = 'https://ru.yougile.com/api-v2/'
token = os.getenv('YouGile_token') 
user_id = os.getenv('YouGile_user_id') 

api = YouGileAPI(base_url, token, user_id)

def test_positive_get_by_id_project():
    create_proj = api.create_project('Тестовый проект 3')

    assert create_proj.status_code == 201

    project_id = create_proj.json()['id']
    get_by_id = api.get_project(project_id)

    assert get_by_id.status_code == 200
    
    resp_data = get_by_id.json()
    assert resp_data['title'] == 'Тестовый проект 3'
    assert resp_data['id'] == project_id

    delete_proj = api.delete_project(project_id)
    assert delete_proj.status_code == 200

def test_negative_get_by_id_project():
    fake_project_id = '00000000-0000-0000-0000-000000000000'

    get_by_id = api.get_project(fake_project_id)

    assert get_by_id.status_code == 404

    error_data = get_by_id.json()
    assert 'message' in error_data
