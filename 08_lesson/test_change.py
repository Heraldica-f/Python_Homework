import requests
from YouGileAPI import YouGileAPI

base_url = 'https://ru.yougile.com/api-v2/'
token = 'CDQBQEouQE1MNO2r7mV+VBY2EhiQPeGW5BteNVKzT8HTdjlnu2agaKgacvRlkEwF' # Указать личный токен компании
user_id = '2660968b-501d-405e-9780-c1dfe73eecaf' # Указать личный user id

api = YouGileAPI(base_url, token, user_id)

def test_positive_change_progect():
    title_before = 'Тестовый проект 4'
    create_proj = api.create_project(title_before)
    assert create_proj.status_code == 201

    project_id = create_proj.json()['id']
    get_by_id_before = api.get_project(project_id)
    project_before = get_by_id_before.json()
    
    title_after = 'Обновленный тестовый проект'
    update_project = api.change_project(project_id, title=title_after)

    assert update_project.status_code == 200

    update_data = update_project.json()
    assert update_data['id'] == project_id

    get_by_id_after = api.get_project(project_id)
    project_after = get_by_id_after.json()

    assert project_after['title'] != project_before['title']
    assert project_after['title'] == title_after

def test_negative_change_priject():
    fake_project_id = '00000000-0000-0000-0000-000000000000'
    update_proj = api.change_project(fake_project_id, title="Новое название")

    assert update_proj.status_code == 404