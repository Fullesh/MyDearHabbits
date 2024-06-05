from rest_framework import serializers

from habbits.models import Habbit
from habbits.validators import MultiplyChoiseHabbitValidator, ReleatedHabbitValidator, PleasantHabbitValidator, \
    PeriodValidator, DurationValidator


class HabbitSerializer(serializers.ModelSerializer):
    period = serializers.IntegerField(validators=[PeriodValidator()])
    duration = serializers.DurationField(validators=[DurationValidator()])

    class Meta:
        model = Habbit
        fields = '__all__'
        validators = [
            MultiplyChoiseHabbitValidator(
                revard="revard", related_habbit="releated_habbit"
            ),
            ReleatedHabbitValidator(
                related_habbit="related_habbit"
            ),
            PleasantHabbitValidator(
                is_pleasant='is_pleasant', revard='revard', related_habbit='related_habbit'
            )
        ]
