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

class PetListingListAPIView(ListAPIView):
    queryset = PetListing.objects.all()
    serializer_class = PetListingSerializer
    permission_classes = [permissions.AllowAny] # All pet listings can be viewed, regardless of status, unless they are deleted.

class PetListingUpdateAPIView(UpdateAPIView):
    queryset = PetListing.objects.all()
    serializer_class = PetListingSerializer
    permission_classes = [permissions.IsAuthenticated]

class PetListingDestroyAPIView(DestroyAPIView):
    queryset = PetListing.objects.all()
    serializer_class = PetListingSerializer
    permission_classes = [permissions.IsAuthenticated]
