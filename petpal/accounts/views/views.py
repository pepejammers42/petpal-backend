from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny

from ..models import Shelter, Seeker
from ..serializers import ShelterSerializer, SeekerSerializer

class ShelterListCreateAPIView(ListCreateAPIView):
    queryset = Shelter.objects.all()
    serializer_class = ShelterSerializer

    def perform_create(self, serializer):
        # Extract user-related data from the request
        user_data = {
            'email': serializer.validated_data.pop('email', None),
            'password': serializer.validated_data.pop('password', None),
            # Include other user fields if necessary
        }

        # Create a User instance
        user = Shelter.objects.create_user(**user_data)

        # Save the Shelter instance with the created user
        serializer.save(user=user)

class SeekerListCreateAPIView(ListCreateAPIView):
    queryset = Seeker.objects.all()
    serializer_class = SeekerSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        serializer.save()
