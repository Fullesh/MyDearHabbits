from datetime import timedelta

from rest_framework import serializers


class MultiplyChoiseHabbitValidator:

    def __init__(self, revard, related_habbit):
        self.revard = revard
        self.related_habbit = related_habbit

    def __call__(self, value):
        if value.get(self.revard) == value.get(self.related_habbit):
            raise serializers.ValidationError(
                'У полезной привычки не может быть вознаграждения'
                ' и связанной привычки одновременно'
            )


class DurationValidator:

    def __call__(self, value):
        if value:
            if value > timedelta(minutes=2):
                raise serializers.ValidationError(
                    'Время на выполнение привычки не должно превышать 120 секунд'
                )


class ReleatedHabbitValidator:

    def __init__(self, related_habbit):
        self.related_habbit = related_habbit

    def __call__(self, value):
        if value.get(self.related_habbit):
            if not value.get(self.related_habbit).is_pleasant:
                raise serializers.ValidationError(
                    'В связанные привычки могут попадать только привычки'
                    'с признаком "приятной" привычки'
                )


class PleasantHabbitValidator:

    def __init__(self, is_pleasant, revard, related_habbit):
        self.is_pleasant = is_pleasant
        self.revard = revard
        self.related_habbit = related_habbit

    def __call__(self, value):
        if value.get(self.is_pleasant) and (value.get(self.revard) or value.get(self.related_habbit)):
            raise serializers.ValidationError(
                'У приятной привычки не может быть вознаграждения'
                'или связанной привычки'
            )


class PeriodValidator:

    def __call__(self, value):
        if value:
            if not 1 <= value <= 7:
                raise serializers.ValidationError(
                    'Нельзя выполнять привычку реже, чем 1 раз в 7 дней'
                )
