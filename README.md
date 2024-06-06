<h1>Сервис MyDearHabbits.</h1>

<h3>Сервис вдохновлён книгой "Атомные привычки", которая посвящена приобретению новых полезных привычек и искоренению старых плохих привычек.. Реализация произведена модулями Django-REST-Framework. Переодические задачи реализованы через Celery. Права доступа реализованы через Django-Simple-JWT. Документация реализована при помощи DRF-YASG</h3>

<h5>В книге хороший пример привычки описывается, как конкретное действие, которое можно уложить в одно предложение: </h5> 
<h5>я буду ДЕЙСТВИЕ в ВРЕМЯ в МЕСТО</h5>

Для работы с программой необходимо:
1) Установить зависимости командой "pip -r requirements.txt"
2) Переименовать файл *.env_example* в *.env* и внести необходимые данные 
3) Создать аккаунт администратора коммандой python manage.py csu \
    *Дополнительно* \
    Данные для входа под аккаунтом администратора: \
    *Логин: admin@service.py* \
    *Пароль: 1* 
4) Запустить сервер коммандой: *python manage.py runserver* \
