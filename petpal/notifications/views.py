from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from .models import Notification
from .serializers import NotificationSerializer

# Create your views here.
class NotificationListCreate(ListCreateAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Notification.objects.all()

        queryset = queryset.order_by('creation_time') # Sort notifications by creation time (2 mark)
        queryset = queryset.filter(recipient=self.request.user) # Users (shelter and seeker) can only view their own notifications (1 mark)

        is_read = self.request.query_params.get('is_read', False) # Default filter to show unread notifications
        if is_read:
            queryset = queryset.filter(is_read=is_read) # Filter notifications by read/unread (2 mark)            

        return queryset
    
    def perform_create(self, serializer):
        serializer.save(recipient=self.request.user, is_read = False)

class NotificationRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        # Users (shelter and seeker) can only view their own notifications (1 mark)
        return get_object_or_404(Notification, id=self.kwargs['pk'], recipient=self.request.user)