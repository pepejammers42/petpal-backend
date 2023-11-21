from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# Create your views here.
class NotificationCreate(ListCreateAPIView):
    def get_queryset(self):
        pass
    
    def perform_create(self, serializer):
        pass

class NotificationRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    def get_object(self):
        pass