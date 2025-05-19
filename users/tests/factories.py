import factory
from users.models import User

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    first_name = "John"
    last_name = "Doe"
    email = factory.Sequence(lambda n: f"user{n}@example.com")
    password = factory.PostGenerationMethodCall("set_password", "password123")
