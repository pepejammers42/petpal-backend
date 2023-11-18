from django.urls import path
from .views import PetListingListCreate, PetListingRetrieveUpdateDestroy

urlpatterns = [
    path('petlistings/', PetListingListCreate.as_view(), name='pet-listing-list-create'),
    path('petlistings/<int:pk>/', PetListingRetrieveUpdateDestroy.as_view(), name='pet-listing-retrieve-update-destroy'),
]