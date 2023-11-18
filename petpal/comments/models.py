from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.conf import settings
# Create your models here.
class Comment(models.Model):
    User = settings.AUTH_USER_MODEL
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE) #'Shelter' or 'Application'
    object_id = models.PositiveIntegerField() #shelter_id or application_id
    content_object = GenericForeignKey('content_type','object_id')
    
