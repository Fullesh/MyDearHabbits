from datetime import datetime, timedelta

import pytz as pytz
from django.db import models

from config import settings

zone = pytz.timezone(settings.TIME_ZONE)
current_datetime = datetime.now(zone)

NULLABLE = {'blank': True, 'null': True}

# Create your models here.


class Habbit(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name='Владелец', **NULLABLE)
    place = models.CharField(max_length=150, verbose_name='Место')
    time = models.DateTimeField(auto_now=True, verbose_name='Время когда выполняется привычка')
    action = models.CharField(max_length=150, verbose_name='Действие')
    is_plesant = models.BooleanField(default=False, verbose_name='признак приятной привычки')
    releated_habbit = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='Связанная привычка', **NULLABLE)
    period = models.PositiveSmallIntegerField(default=1, verbose_name='Периодичность в днях')
    revard = models.CharField(max_length=150, verbose_name='Вознаграждение')
    duration = models.DurationField(default=timedelta(minutes=2), verbose_name='Время на выполнение (минуты)')
    is_public = models.BooleanField(default=False, verbose_name='Публичная')
    users = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Пользователи",
                              related_name="users", **NULLABLE)

    def __str__(self):
        return f'Я буду {self.action} в {self.time} в {self.place}'

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
