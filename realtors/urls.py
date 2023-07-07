from django.urls import path

from .views import (
    RealtorListView, 
    RealtorDetailView, 
    TopSellerView,
    )

urlpatterns = [
    path('api/realtor/', RealtorListView.as_view(), name='realtor-list'),
    path('api/realtor/<int:pk>/', RealtorDetailView.as_view(), name='realtor-detail'),
    path('api/realtor/topseller/', TopSellerView.as_view(), name='top-seller'),
]
