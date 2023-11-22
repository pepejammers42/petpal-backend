from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.exceptions import ValidationError
from accounts.models import Seeker, Shelter

from ..models import PetListing
from ..serializers import PetListingSerializer

"""
TODO:
"""
LISTING_PAGINATION_SIZE = 10 # Number of results to display per page (by default)
LISTING_PAGINATION_SIZE_MAX = 20 # Maximum number of results to display per page
LISTING_PAGINATION_SIZE_PARAM = 'page_size' # Query parameter to read page size from

class PetListingListPagination(PageNumberPagination):
    page_size = LISTING_PAGINATION_SIZE  # Number of results to display per page (by default)
    max_page_size = LISTING_PAGINATION_SIZE_MAX # Maximum number of results to display per page
    page_size_query_param = LISTING_PAGINATION_SIZE_PARAM # Query parameter to read page size from

class PetListingListCreate(ListCreateAPIView):
    serializer_class = PetListingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self): # Called when querying for pet listings
        queryset = PetListing.objects.all()

        # Retrieve filter parameters
        shelter = self.request.query_params.get('shelter', None)
        status = self.request.query_params.get('status', "available")
        sort_by = self.request.query_params.get('sort_by', None)

        # Apply sorting based on parameters
        if shelter:
            queryset = queryset.filter(shelter__shelter_name__icontains=shelter)

        if status:
            queryset = queryset.filter(status=status)

        if sort_by:
            queryset = queryset.order_by(sort_by)

        return queryset
    
    def perform_create(self, serializer): # Called after a pet listing is created
        # Ensure this user is a shelter (sekeers can't make pet listings)
        try:
            _ = self.request.user.shelter
        except Shelter.DoesNotExist:
            raise ValidationError({'detail': 'User must be a Shelter to create an application.'})
        
        # self is the shelter
        # status should be available at the time of creation
        serializer.save(shelter=self.request.user, status="available")

class PetListingRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    serializer_class = PetListingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        # Search for the pet listing with this id and owned by the current shelter
        return get_object_or_404(PetListing, id=self.kwargs['pk'], shelter=self.request.user)