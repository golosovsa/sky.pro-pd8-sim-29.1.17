from django.urls import path

from fk_search.views import StoreView


urlpatterns = [
    path("fk_search/", StoreView.as_view())
]