from rest_framework.serializers import ModelSerializer
from .models import Application
from pet_listings.models.models import PetListing
from django.utils import timezone


class ApplicationSerializer(ModelSerializer):

    class Meta:
        model = Application
        fields = '__all__'
        #read_only_fields = ['pet_listing','applicant', 'creation_time', 'last_update_time']

 