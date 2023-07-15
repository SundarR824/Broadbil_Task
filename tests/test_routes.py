import sys
import os
import pytest
from flask_jwt_extended import create_access_token

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_login_route(client):
    response = client.post('/login', json={"username": "john", "password": "password123"})
    assert response.status_code == 200
    assert isinstance(response.json['access_token'], str)


def test_protected_route(client):
    with client.application.app_context():
        access_token = create_access_token(identity='john')
    response = client.get('/protected', headers={'Authorization': f'Bearer {access_token}'})
    assert response.status_code == 200
    assert isinstance(response.json['message'], str)


def test_home_page_route(client):
    with client.application.app_context():
        access_token = create_access_token(identity='john')
    response = client.get('/', headers={'Authorization': f'Bearer {access_token}'})
    assert response.status_code == 200
    assert response.json == {"message": "Table has been created successfully!!.."}


def test_find_mark_route(client):
    with client.application.app_context():
        access_token = create_access_token(identity='john')
    response = client.get('/find_by_id/mark/1', headers={'Authorization': f'Bearer {access_token}'})
    assert response.status_code == 200
    assert isinstance(response.json['message'], list)


def test_find_mark_list_route(client):
    with client.application.app_context():
        access_token = create_access_token(identity='john')
    response = client.get('/find_by_id/mark_list/1', headers={'Authorization': f'Bearer {access_token}'})
    assert response.status_code == 200
    assert isinstance(response.json['message'], list)


def test_find_student_route(client):
    with client.application.app_context():
        access_token = create_access_token(identity='john')
    response = client.get('/find_by_id/students/1', headers={'Authorization': f'Bearer {access_token}'})
    assert response.status_code == 200
    assert isinstance(response.json['message']['number_of_students'], int)


def test_find_all_route(client):
    with client.application.app_context():
        access_token = create_access_token(identity='john')
    response = client.get('/find_all', headers={'Authorization': f'Bearer {access_token}'})
    assert response.status_code == 200
    assert isinstance(response.json['message'], list)


def test_add_details_route(client):
    with client.application.app_context():
        access_token = create_access_token(identity='john')
    response = client.post('/add_details', headers={'Authorization': f'Bearer {access_token}'},
                           json={"first_name": "Sundar", "group_id": 2, "key": "Students", "last_name": "Raja"})
    assert response.status_code == 200
    assert isinstance(response.json['message'], str)


def test_update_details_route(client):
    with client.application.app_context():
        access_token = create_access_token(identity='john')
    response = client.put('/update_details/5', headers={'Authorization': f'Bearer {access_token}'},
                          json={"first_name": "sundar", "group_id": 2, "last_name": "Raja"})
    assert response.status_code == 200
    assert isinstance(response.json['message'], str)


def test_delete_details_route(client):
    with client.application.app_context():
        access_token = create_access_token(identity='john')
    response = client.delete('/delete_details/7', headers={'Authorization': f'Bearer {access_token}'},
                             json={"key": "delete_group"})
    assert response.status_code == 200
    assert isinstance(response.json['message'], str)


if __name__ == '__main__':
    pytest.main()
