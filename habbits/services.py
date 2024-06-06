import requests
from config import settings


def send_telegram_message(habbit, message):
    """Функция отправки уведомления в Telegram"""
    params = {
        'chat_id': f'{habbit.users.telegram_id}',
        'text': message,
    }
    requests.post(
        f'{settings.TELEGRAM_URL}{settings.TELEGRAM_TOKEN}/sendMessage',
        params=params
    )
