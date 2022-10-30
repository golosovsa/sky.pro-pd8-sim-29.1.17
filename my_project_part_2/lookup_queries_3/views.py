# TODO опишите view-функцию ниже
from django.db.models import Q
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from lookup_queries_3.models import Store
from lookup_queries_3.serializers import StoreSerializer


class StoreView(ListAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer

    def list(self, request, *args, **kwargs):
        query = self.get_queryset()
        query = query.filter(Q(open_hour__gte=8) and Q(open_hour__lte=10))
        serializer = StoreSerializer(query, many=True)
        return Response(serializer.data)
