from django.urls import path

from delete_if_null.views import StoreView


urlpatterns = [
    path("delete_if_null/", StoreView.as_view())
]
