from rest_framework import pagination


class ListPagination(pagination.PageNumberPagination):
    page_size = 1
    page_size_query_param = 'per_page'
    max_page_size = 3
    page_query_param = 'page'
