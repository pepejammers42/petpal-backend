
from rest_framework.serializers import ModelSerializer, DateTimeField, ListField, \
    PrimaryKeyRelatedField, HyperlinkedRelatedField, EmailField, CharField
from .models import Shelter, Seeker

class ShelterSerializer(ModelSerializer):

    class Meta:
        model = Shelter
        fields = ['email', 'password', 'shelter_name', 'avatar', 'phone_number', 'address', 'description']

    def create(self, validated_data):
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
        fields = ['id','email', 'password', 'first_name', 'last_name', 'avatar', 'phone_number', 'location', 'preference']

    def create(self, validated_data):

        # hash the password
        password = validated_data.pop('password', None)
        seeker = Seeker(**validated_data)
        if password:
            seeker.set_password(password)
        seeker.save()
        return seeker

