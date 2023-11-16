
from rest_framework.serializers import ModelSerializer, DateTimeField, ListField, \
    PrimaryKeyRelatedField, HyperlinkedRelatedField, EmailField, CharField
from .models import Shelter, Seeker

class ShelterSerializer(ModelSerializer):
    email = EmailField(write_only=True)
    password = CharField(write_only=True)

    class Meta:
        model = Shelter
        fields = ['email', 'password', 'shelter_name', 'address', 'description']
        # Include other fields as necessary

    def create(self, validated_data):
        # The actual creation logic is handled in the view's perform_create method
        # hash the password
        password = validated_data.pop('password', None)
        shelter = Shelter(**validated_data)
        if password:
            shelter.set_password(password)
        shelter.save()
        return shelter

class SeekerSerializer(ModelSerializer):
    class Meta:
        model = Seeker
        fields = ['email', 'password', 'first_name', 'last_name', 'avatar', 'phone_number', 'location', 'preference']
    def create(self, validated_data):

        # hash the password
        password = validated_data.pop('password', None)
        seeker = Seeker(**validated_data)
        if password:
            seeker.set_password(password)
        seeker.save()
        return seeker

