# TODO опишите view-функцию ниже
from django.db.models import Q
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from qf_queries.models import Store
from qf_queries.serializers import StoreSerializer


class StoreView(ListAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer

    def list(self, request, *args, **kwargs):
        query = self.get_queryset()
        query = query.filter(Q(director__icontains="ivan") | Q(email__icontains="ivan"))
        serializer = StoreSerializer(query, many=True)
        return Response(serializer.data)
