import pytest
from users.serializers import UserCreateSerializer, UserSerializer
from users.models import User

@pytest.mark.django_db
def test_user_create_serializer_valid():
    data = {
        "email": "test@example.com",
        "first_name": "Test",
        "last_name": "User",
        "password": "securepass123"
    }
    serializer = UserCreateSerializer(data=data)
    assert serializer.is_valid()
    user = serializer.save()
    assert isinstance(user, User)
    assert user.email == "test@example.com"
    assert user.check_password("securepass123")

@pytest.mark.django_db
def test_user_serializer_output():
    user = User.objects.create_user(
        email="sample@example.com",
        first_name="Sample",
        last_name="User",
        password="somepassword"
    )
    serializer = UserSerializer(user)
    expected_fields = {"id", "first_name", "last_name", "email"}
    assert set(serializer.data.keys()) == expected_fields
    assert serializer.data["email"] == "sample@example.com"
