from rest_framework import generics, mixins

from .serializers import RealtorSerializer
from .models import Realtor

class RealtorListView(generics.ListAPIView):
    queryset = Realtor.objects.all()
    serializer_class = RealtorSerializer
    pagination_class = None


class RealtorDetailView(generics.RetrieveAPIView):
    queryset = Realtor.objects.all()
    serializer_class = RealtorSerializer
    pagination_class = None


class TopSellerView(generics.ListAPIView):
    queryset = Realtor.objects.filter(top_seller=True)
    serializer_class = RealtorSerializer
    pagination_class = None
