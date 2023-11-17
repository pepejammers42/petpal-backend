from .models import PetListing
from rest_framework.serializers import ModelSerializer

class PetListingSerializer(ModelSerializer):
    class Meta:
        model = PetListing
        # Serialize all fields but shelter and status, which are automatically set
        fields = ["name", "description", "breed", "age", "size", "color", "gender", "medical_history", "behavior", "special_needs"]