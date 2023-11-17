from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from ..models import Shelter, Seeker
from ..serializers import ShelterSerializer, SeekerSerializer

class ShelterListCreateAPIView(ListCreateAPIView):
    queryset = Shelter.objects.all()
    serializer_class = ShelterSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        serializer.save()

class SeekerListCreateAPIView(ListCreateAPIView):
    queryset = Seeker.objects.all()
    serializer_class = SeekerSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        serializer.save()

class SeekerRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = SeekerSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return get_object_or_404(Seeker, pk=self.kwargs['pk'])

class ShelterRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ShelterSerializer

    def get_object(self):
        return get_object_or_404(Shelter, pk=self.kwargs['pk'])
