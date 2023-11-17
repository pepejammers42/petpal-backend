from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    UpdateAPIView,
    DestroyAPIView,
)
from rest_framework import permissions
from rest_framework.response import Response

from ..models import PetListing
from ..serializers import PetListingSerializer

"""
TODO: 
- Filtering options (modify listapiview get_queryset)
"""

class PetListingCreateAPIView(CreateAPIView):
    queryset = PetListing.objects.all()
    serializer_class = PetListingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # self is the shelter
        # status should be available at the time of creation
        serializer.save(shelter=self, status="available")

class PetListingListAPIView(ListAPIView):
    queryset = PetListing.objects.all()
    serializer_class = PetListingSerializer
    permission_classes = [permissions.AllowAny] # All pet listings can be viewed, regardless of status, unless they are deleted.

    def get_queryset(self):
        queryset = PetListing.objects.all()

        # Retrieve filter parameters
        shelter = self.request.query_params.get('shelter', None)
        status = self.request.query_params.get('status', None)
        breed = self.request.query_params.get('breed', None)
        age = self.request.query_params.get('age', None)
        size = self.request.query_params.get('size', None)
        color = self.request.query_params.get('color', None)
        gender = self.request.query_params.get('gender', None)

        # Apply sorting based on parameters
        if shelter:
            queryset = queryset.filter(shelter__name__icontains=shelter)

        if status:
            queryset = queryset.filter(status=status)

        if breed:
            queryset = queryset.filter(breed__icontains=breed)

        if age:
            queryset = queryset.filter(age=age)

        if size:
            queryset = queryset.filter(size=size)

        if color:
            queryset = queryset.filter(color__icontains=color)

        if gender:
            queryset = queryset.filter(gender=gender)

        return queryset

class PetListingUpdateAPIView(UpdateAPIView):
    queryset = PetListing.objects.all()
    serializer_class = PetListingSerializer
    permission_classes = [permissions.IsAuthenticated]

class PetListingDestroyAPIView(DestroyAPIView):
    queryset = PetListing.objects.all()
    serializer_class = PetListingSerializer
    permission_classes = [permissions.IsAuthenticated]
