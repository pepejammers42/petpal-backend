from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView, ListAPIView, ListCreateAPIView
# Create your views here.
from .models import Application
from pet_listings.models import PetListing
from accounts.models import Seeker, Shelter
from .serializers import ApplicationSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError
from django.utils import timezone


class ApplicationCreate(ListCreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        pet = get_object_or_404(PetListing, id=self.kwargs['pk'])

        if pet.status != 'available':
            raise ValidationError({'detail': 'Pet is not available for application.'})

        try:
            _ = self.request.user.seeker
        except Seeker.DoesNotExist:
            raise ValidationError({'detail': 'User must be a Seeker to create an application.'})

        serializer.save()


class ApplicationRetrieveUpdate(RetrieveUpdateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_update(self, serializer):
        application = serializer.instance

        try: 
            if self.request.user.shelter:
                possible_changes = ['accepted', 'denied']
                cur_status = application.status
                new_status = serializer.validated_data.get('status', None)
                if cur_status != 'pending' or (new_status not in possible_changes):
                    raise ValidationError({'detail': 'Shelter can only update the status of an application from pending to accepted or denied.'})
        except Shelter.DoesNotExist:
            try:
                possible_changes = ['withdrawn']
                cur_status = application.status
                new_status = serializer.validated_data.get('status', None)
                if (cur_status not in ['pending', 'accepted']) or (new_status not in possible_changes):
                    raise ValidationError({'detail': 'Pet seeker can only update the status of an appilcation from pending to withdrawn.'})
            except Seeker.DoesNotExist:
                raise ValidationError({'detail': 'User must be a Seeker or Shelter to update an application.'})

        serializer.validated_data['last_update_time'] = timezone.now()
        serializer.save()  

class ShelterApplicationList(ListAPIView):
    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        try:
            _ = self.request.user.shelter
        except Shelter.DoesNotExist:
            raise ValidationError({'detail': 'User must be a Shelter to see applications.'})

        queryset = Application.objects.filter(pet_listing__shelter=self.request.user.shelter)

        status = self.request.query_params.get('status')
        if status is not None and status != '':
            queryset = queryset.filter(status=status)

        sort_by = self.request.query_params.get('sort')
        if sort_by is not None and sort_by != '':
            if sort_by == 'creation_time':
                queryset = queryset.order_by('creation_time')
            elif sort_by == 'last_update_time':
                queryset = queryset.order_by('last_update_time')

        return queryset
        


