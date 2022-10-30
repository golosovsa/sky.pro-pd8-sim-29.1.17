from django.urls import path

from lookup_queries_3.views import StoreView


urlpatterns = [
    path("lookup_queries_3/", StoreView.as_view())
]