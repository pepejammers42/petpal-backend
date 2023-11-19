from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView, ListAPIView
# Create your views here.
from .models import Application
from ..pet_listings.models.models import PetListing
from .serializers import ApplicationSerializer
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse
from django.utils import timezone


class AppCreate(CreateAPIView):
    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        pet_id = self.kwargs.get('pk')
        pet = PetListing.objects.get(id=pet_id)

        if pet.status == 'available':
            serializer.save(applicant=self.request.user, pet_listing=pet)
        else:
            HttpResponse(pet.status, status=404)


class AppRetrieveUpdate(RetrieveUpdateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_update(self, serializer):
        application = serializer.instance
        
        if self.request.user.is_shelter:
            possible_changes = ['accepted', 'denied']
            cur_status = application.status
            new_status = serializer.validated_data.get('status', None)
            if cur_status != 'pending' or (new_status not in possible_changes):
                raise serializer.ValidationError("Shelter can only update the status of an application from pending to accepted or denied")
        else:
            possible_changes = ['withdrawn']
            cur_status = application.status
            new_status = serializer.validated_data.get('status', None)
            if (cur_status not in ['pending', 'accepted']) or (new_status not in possible_changes):
                raise serializer.ValidationError("Pet seeker can only update the status of an appilcation from pending to accepted or denied")

        serializer.validated_data['last_update_time'] = timezone.now()
        serializer.save()  

class ShelterAppList(ListAPIView):
    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        shelter = self.request.user
        queryset = Application.objects.filter(pet_listing__shelter=shelter)
        status = self.request.query_params.get('status','None')
        if status:
            queryset = queryset.filter(status=status)

        sort_by = self.request.query_params.get('sort', None)
        if sort_by == 'creation_time':
            queryset = queryset.order_by('creation_time')
        elif sort_by == 'last_update_time':
            queryset = queryset.order_by('last_update_time')

        return queryset
        


