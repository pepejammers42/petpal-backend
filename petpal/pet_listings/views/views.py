from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions
from rest_framework.response import Response

from ..models import PetListing
from ..serializers import PetListingSerializer

"""
TODO: 
- Filtering options (modify listapiview get_queryset)
"""
DEFAULT_STATUS_FILTER = 'available'

class PetListingListCreate(ListCreateAPIView):
    serializer_class = PetListingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = PetListing.objects.all()

        # Retrieve filter parameters
        shelter = self.request.query_params.get('shelter', None)
        status = self.request.query_params.get('status', DEFAULT_STATUS_FILTER)
        sort_by = self.request.query_params.get('sort_by', None)

        # Apply sorting based on parameters
        if shelter:
            queryset = queryset.filter(shelter__shelter_name__icontains=shelter)

        if status:
            queryset = queryset.filter(status=status)

        if sort_by:
            queryset = queryset.order_by(sort_by)

        return queryset
    
    def perform_create(self, serializer): # Called after a listing is created
        # self is the shelter
        # status should be available at the time of creation
        serializer.save(shelter=self, status="available")

class PetListingRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    serializer_class = PetListingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return get_object_or_404(PetListing, id=self.kwargs['pk'], shelter=self)
