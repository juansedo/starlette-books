import json
import os
import sys

import pytest
from starlette.testclient import TestClient

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from main import app

client = TestClient(app)

@pytest.fixture(scope='session', autouse=True)
def before_after_db():
    import up
    yield
    import down

def test_app():
    response = client.get('/')
    assert response.status_code == 200

def test_get_all_books():
    response = client.get('/books')
    data = json.loads(response.text)
    assert 'data' in data
    assert len(data['data']) == 0

def test_create_one_book():
    response = client.post('/books', json={ "title": "Hola", "year": "2002" })
    data = json.loads(response.text)
    assert data['message'] == 'Book created!'
    assert response.status_code == 201

def test_create_one_book_fails():
    response = client.post('/books', json={ "title": "Hola" })
    data = json.loads(response.text)
    assert data['message'] != 'Book created!'
    assert response.status_code == 400

def test_get_one_book():
    response = client.get('/books/1')
    data = json.loads(response.text)
    assert data['title'] == 'Hola'

def test_get_one_book_fails():
    response = client.get('/books/2')
    assert response.status_code == 400
