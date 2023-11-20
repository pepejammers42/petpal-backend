from .models import PetListing
from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField, CharField

class PetListingSerializer(ModelSerializer):
    shelter = PrimaryKeyRelatedField(read_only=True)
    status = CharField(read_only=True)

    class Meta:
        model = PetListing
        fields = '__all__'