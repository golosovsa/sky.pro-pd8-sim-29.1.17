# TODO опишите view-функцию ниже
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from lookup_queries_2.models import Store
from lookup_queries_2.serializers import StoreSerializer


class StoreView(ListAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer

    def list(self, request, *args, **kwargs):
        query = self.get_queryset()
        query = query.filter(address__endswith="д. 30")
        serializer = StoreSerializer(query, many=True)
        return Response(serializer.data)
