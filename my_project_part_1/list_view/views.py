from rest_framework import generics

from list_view.models import Store
from list_view.serializers import StoreSerializer


# TODO опишите ListView ниже
class StoreListView(generics.ListAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
