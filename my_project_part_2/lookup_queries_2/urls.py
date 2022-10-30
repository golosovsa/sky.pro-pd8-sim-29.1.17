from django.urls import path

from lookup_queries_2.views import StoreView


urlpatterns = [
    path("lookup_queries_2/", StoreView.as_view())
]
