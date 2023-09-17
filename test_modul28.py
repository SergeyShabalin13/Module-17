from pydantic import BaseModel
import pytest
import requests

class AccessTokenRequest(BaseModel):
    access_token: str

class User(BaseModel):
    id: int
    first_name: str
    last_name: str

def test_access_token_required():
    request = {
        "access_token": "token123"
    }
    AccessTokenRequest(**request)

def test_users_get_response():
    response = [
        {"id": 123, "first_name": "Jack", "last_name": "London"},
        {"id": 456, "first_name": "Jack", "last_name": "London"}
    ]
    users = [User(**user) for user in response]

def test_access_token_required():
    request = {}
    with pytest.raises(ValueError):
        AccessTokenRequest(**request)

def test_access_token_format():
    request = {
        "access_token": "invalid_token_format"
    }
    with pytest.raises(ValueError):
        AccessTokenRequest(**request)

def test_users_get_success():
    response = [
        {"id": 123, "first_name": "Jack", "last_name": "London"},
        {"id": 456, "first_name": "Jack", "last_name": "London"}
    ]
    users = [User(**user) for user in response]
    assert len(users) == 2
    assert users[0].id == 123
    assert users[0].first_name == "Jack"
    assert users[0].last_name == "London"

def test_users_get_no_users():
    response = []
    users = [User(**user) for user in response]
    assert len(users) == 0

def test_user_format():
    user = {
        "id": "invalid_id_format",
        "first_name": "Jack",
        "last_name": "London"
    }
    with pytest.raises(ValueError):
        User(**user)

def test_user_name_format():
    user = {
        "id": 123,
        "first_name": "Jack777",
        "last_name": "London"
    }
    with pytest.raises(ValueError):
        User(**user)

def test_user_lastname_format():
    user = {
        "id": 123,
        "first_name": "Jack",
        "last_name": "London777"
    }
    with pytest.raises(ValueError):
        User(**user)
