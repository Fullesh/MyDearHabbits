from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='E-mail')

    is_verified = models.BooleanField(default=False, verbose_name='Подтверждение')
    token = models.CharField(max_length=10, verbose_name='Токен', **NULLABLE)
    telegram_id = models.CharField(max_length=50, unique=True, verbose_name='ID в телеграмм', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email}: {self.is_verified}; {self.token}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
