# TODO здесь необходимо настроить urls приложения
from django.urls import path

from lookup_queries.views import StoreView


urlpatterns = [
    path("lookup_queries/", StoreView.as_view())
]
