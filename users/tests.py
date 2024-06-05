from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from users.models import User


# Create your tests here.
class UsersTestCase(APITestCase):
    """Тестирование привычек"""

    def setUp(self) -> None:
        self.user = User.objects.create(email="admin@service.py")
        self.user.set_password("123qwe456")
        self.user.save()
        self.client.force_authenticate(user=self.user)

    def test_user_create(self):
        """Тест создания пользователя"""
        url = reverse("users:create_user")
        data = {
            "email": "test_user@service.py",
            "password": "4112341"
        }
        response = self.client.post(url, data=data)
        print("\ntest_user_create")
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.all().count(), 2)