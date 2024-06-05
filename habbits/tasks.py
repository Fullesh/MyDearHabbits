from datetime import timedelta

from celery import shared_task
from django.utils import timezone

from habbits.services import send_telegram_message

from habbits.models import Habbit


@shared_task
def send_alert():
    """Функция оповещения о полезной привычке"""
    current_datetime = timezone.now().today().replace(second=0, microsecond=0)
    habbits = Habbit.objects.filter(is_plesant=False).filter(time=current_datetime)
    for habbit in habbits:
        message_1 = f"Полезная привычка: {habbit}"
        if habbit.related_habit:
            message_2 = f"За выполнение Вы можете: {habbit.related_habit}"
        elif habbit.reward:
            message_3 = f"За выполнение Вам можно: {habbit.reward}"

        for user in habbit.users.all():
            if user.telegram_id:
                send_telegram_message(
                    telegram_id=user.telegram_id,
                    message=message_1,
                )
                if habbit.related_habit:
                    send_telegram_message(
                        telegram_id=user.telegram_id,
                        message=message_2,
                    )
                elif habbit.reward:
                    send_telegram_message(
                        telegram_id=user.telegram_id,
                        message=message_3,
                    )
        habbit.time = habbit.time + timedelta(days=habbit.period)
        habbit.save()
