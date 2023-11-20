from rest_framework.serializers import ModelSerializer
from .models import Application
from pet_listings.models import PetListing
from django.utils import timezone


class ApplicationSerializer(ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'
