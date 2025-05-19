import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from users.models import User

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def create_user():
    def make_user(**kwargs):
        data = {
            "email": "user@example.com",
            "first_name": "John",
            "last_name": "Doe",
            "password": "strongpassword123",
        }
        data.update(kwargs)
        return User.objects.create_user(**data)
    return make_user

@pytest.mark.django_db
def test_user_registration(api_client):
    url = reverse("user-list")  # djoser route: /auth/users/
    payload = {
        "email": "newuser@example.com",
        "first_name": "New",
        "last_name": "User",
        "password": "newpassword123",
        "re_password": "newpassword123"
    }
    response = api_client.post(url, payload)
    print(response.data) 
    assert response.status_code == 201
    assert response.data["email"] == "newuser@example.com"

@pytest.mark.django_db
def test_jwt_token_create(api_client, create_user):
    user = create_user(email="authuser@example.com", password="password123")
    url = reverse("jwt-create")  # /auth/jwt/create/
    payload = {
        "email": "authuser@example.com",
        "password": "password123"
    }
    response = api_client.post(url, payload)
    assert response.status_code == 200
    assert "access" in response.data
    assert "refresh" in response.data

@pytest.mark.django_db
def test_get_user_me_authenticated(api_client, create_user):
    user = create_user(email="me@example.com", password="password123")
    login_url = reverse("jwt-create")
    response = api_client.post(login_url, {
        "email": "me@example.com",
        "password": "password123"
    })
    access_token = response.data["access"]
    
    api_client.credentials(HTTP_AUTHORIZATION=f"Bearer {access_token}")
    response = api_client.get(reverse("user-me"))  # /auth/users/me/
    
    assert response.status_code == 200
    assert response.data["email"] == "me@example.com"

@pytest.mark.django_db
def test_get_user_me_unauthenticated(api_client):
    response = api_client.get(reverse("user-me"))
    assert response.status_code == 401
