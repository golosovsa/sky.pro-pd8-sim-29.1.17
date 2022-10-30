# TODO опишите view-функцию ниже
from django.db.models import Q
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from fk_search.models import Store
from fk_search.serializers import StoreSerializer


class StoreView(ListAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer

    def list(self, request, *args, **kwargs):
        query = self.get_queryset()
        query = query.filter(city__name="Самара")
        serializer = StoreSerializer(query, many=True)
        return Response(serializer.data)
