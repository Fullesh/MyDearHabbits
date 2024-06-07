from datetime import timedelta
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from habbits.models import Habbit
from users.models import User


# Create your tests here.
class HabitsTestCase(APITestCase):
    """Тестирование привычек"""

    def setUp(self) -> None:
        self.user = User.objects.create(email="admin@service.py")
        self.user.set_password("123qwe456")
        self.user.save()
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

        self.habit = Habbit.objects.create(
            owner=self.user,
            place="дома",
            time="2024-05-27 08:05:00",
            action="выпить стакан воды",
            is_plesant=False,
            period=1,
            duration=timedelta(minutes=1),
            revard="погладить кошку",
            is_public=True,
            releated_habbit=None,
        )

    def test_habbit_create(self):
        """Тест создания привычки"""
        url = reverse("habbits:create_habbit")
        data = {
            "owner": self.user.id,
            "place": "дома",
            "time": "2024-05-27 08:40:00",
            "action": "съесть кашу на завтрак",
            "is_plesant": False,
            "period": 3,
            "duration": timedelta(minutes=2),
            "revard ": "выпить кофе",
            "is_public": True,
        }
        response = self.client.post(url, data=data)
        print("\ntest_habbit_create")
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habbit.objects.all().count(), 2)

    def test_habbits_retrieve(self):
        """Тест получения привычки"""
        url = reverse("habbits:detail_habbit", kwargs={"pk": self.habit.id})
        response = self.client.get(url)
        print("\ntest_habbits_retrieve")
        data = response.json()
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("action"), self.habit.action)

    def test_habbit_update(self):
        """Тестирование изменения привычки"""
        url = reverse("habbits:update_habbit", kwargs={"pk": self.habit.id})
        new_data = {
            "revard": "послушать любимую песню",
        }
        response = self.client.patch(url, data=new_data)
        print("\ntest_habbit_update")
        data = response.json()
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("revard"), "послушать любимую песню")

    def test_habbit_delete(self):
        """Тестирование удаления привычки"""
        url = reverse("habbits:delete_habbit", kwargs={"pk": self.habit.id})
        response = self.client.delete(url)
        print("\ntest_habbit_delete")
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habbit.objects.all().count(), 0)

    def test_habbit_list(self):
        """Тестирование вывода списка привычек"""
        url = reverse("habbits:public_habbits_list")
        response = self.client.get(url)
        print("\ntest_habbit_list")
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Habbit.objects.all().count(), 1)

    def test_DurationValidator(self):
        """Тестирование валидации времени выполнения привычки"""
        url = reverse('habbits:create_habbit')
        data = {'owner': self.user.id,
                'place': "дома",
                'action': "позвонить маме",
                'is_plesant': False,
                'period': 7,
                'duration': timedelta(minutes=3),
                'revard ': "скушать конфетку",
                'is_public': True,
                }
        response = self.client.post(url, data=data)
        print("\ntest_DurationValidator")
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        
