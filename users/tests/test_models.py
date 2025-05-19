import pytest
from users.models import User

@pytest.mark.django_db
def test_create_user():
    user = User.objects.create_user(
        email="test@example.com",
        first_name="Test",
        last_name="User",
        password="password123"
    )
    assert user.email == "test@example.com"
    assert user.first_name == "Test"
    assert user.last_name == "User"
    assert user.check_password("password123")
    assert not user.is_staff
    assert user.is_active

@pytest.mark.django_db
def test_create_superuser():
    superuser = User.objects.create_superuser(
        email="admin@example.com",
        password="admin123",
        first_name="Admin",
        last_name="User"
    )
    assert superuser.is_superuser
    assert superuser.is_staff
