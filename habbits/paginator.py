from rest_framework.pagination import PageNumberPagination


class HabbitPaginator(PageNumberPagination):
    page_size = 5