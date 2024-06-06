from datetime import timedelta, datetime

from celery import shared_task

from habbits.models import Habbit
from habbits.services import send_telegram_message


@shared_task
def send_alert():
    """Функция оповещения о полезной привычке"""
    habbits = Habbit.objects.all().exclude(users__telegram_id=None)
    time_min = datetime.now() - timedelta(seconds=30)
    time_max = datetime.now() + timedelta(seconds=30)
    for habbit in habbits:
        if habbit.update_time is None:
            message = f"Полезная привычка: {habbit} \n" \
                      f"За выполнение вы можете: {habbit.related_habbit} \n" \
                      f"За выполнение вы можете: {habbit.reward}"
            if time_min.time() <= habbit.time <= time_max.time():
                send_telegram_message(habbit, message)
                habbit.update_time = datetime.now().date() + timedelta(days=habbit.period)
                habbit.save()
        else:
            message = f"Полезная привычка: {habbit} \n" \
                      f"За выполнение вы можете: {habbit.related_habbit} \n" \
                      f"За выполнение вы можете: {habbit.reward}"
            if datetime.now().date() == habbit.update_time:
                if time_min.time() <= habbit.time <= time_max.time():
                    send_telegram_message(habbit, message)
                    habbit.update_time += timedelta(days=habbit.period)
                    habbit.save()
