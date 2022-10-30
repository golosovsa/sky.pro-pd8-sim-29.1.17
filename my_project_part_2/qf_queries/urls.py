from django.urls import path

from qf_queries.views import StoreView


urlpatterns = [
    path("qf_queries/", StoreView.as_view())
]