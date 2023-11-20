from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView, ListAPIView
# Create your views here.
from .models import Application
from pet_listings.models.models import PetListing
from accounts.models.models import Seeker
from .serializers import ApplicationSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone


class ApplicationCreate(CreateAPIView):
    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        pet = get_object_or_404(PetListing, id=self.kwargs['pk'])

        if pet.status == 'available':
            if not isinstance(self.request.user, Seeker):
                return Response({'detail': 'User must be a Seeker to create an application.'}, status=status.HTTP_400_BAD_REQUEST)

            if serializer.is_valid():
                serializer.save(applicant=self.request.user, pet_listing=pet)
            else:
                print(serializer.errors)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'detail': 'Pet is not available for application.'}, status=status.HTTP_404_NOT_FOUND)


class ApplicationRetrieveUpdate(RetrieveUpdateAPIView):
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

class ShelterApplicationList(ListAPIView):
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
        


