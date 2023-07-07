from django.urls import path
from .views import ListingsView, ListingView, SearchView, ContactCreateView

urlpatterns = [
    path('api/listings/', ListingsView.as_view(), name='listings'),
    path('api/listings/search/', SearchView.as_view(), name='search-listings'),
    path('api/listings/<int:pk>/', ListingView.as_view(), name='listing-detail'),
    path('api/contact/', ContactCreateView.as_view(), name='contact'),
]