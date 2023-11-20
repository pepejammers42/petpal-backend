from django.db import models
from applications.models import Application
from accounts.models import Seeker, Shelter, AuthUser

class Notification(models.Model):
    NOTIFICATION_TYPES = [
        ('application', 'Application'),
        ('message', 'Message'),
        ('pet_listing', 'Pet Listing'),
        ('pet', 'Pet'),
        ('shelter', 'Shelter'),
        ('seeker', 'Seeker'),
        ('user', 'User'),
    ]

    notification_type = models.CharField(choices=NOTIFICATION_TYPES, max_length=20)
    message = models.TextField()
    creation_time = models.DateTimeField(auto_now_add=True)
    last_update_time = models.DateTimeField(auto_now=True)
    is_read = models.BooleanField(default=False)
    recipient = models.ForeignKey('accounts.AuthUser', on_delete=models.CASCADE)
    sender = models.ForeignKey('accounts.AuthUser', on_delete=models.CASCADE, related_name='sender', null=True, blank=True)
    pet_listing = models.ForeignKey('pet_listings.PetListing', on_delete=models.CASCADE, null=True, blank=True)
    application = models.ForeignKey('applications.Application', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.message
