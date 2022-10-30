# TODO опишите view-функцию ниже
from django.db.models import Q
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from delete_if_null.models import Store
from delete_if_null.serializers import StoreSerializer


class StoreView(ListAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer

    def list(self, request, *args, **kwargs):
        query = self.get_queryset()
        count, deleted = query.filter(visits=0).delete()
        query = self.get_queryset()
        serialized = StoreSerializer(query, many=True)
        return Response(serialized.data)
