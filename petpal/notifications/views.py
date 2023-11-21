from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from .models import Notification
from .serializers import NotificationSerializer

LISTING_PAGINATION_SIZE = 10 # Number of results to display per page (by default)
LISTING_PAGINATION_SIZE_MAX = 20 # Maximum number of results to display per page
LISTING_PAGINATION_SIZE_PARAM = 'page_size' # Query parameter to read page size from

class NotificationListPagination(PageNumberPagination):
    page_size = LISTING_PAGINATION_SIZE  # Number of results to display per page (by default)
    max_page_size = LISTING_PAGINATION_SIZE_MAX # Maximum number of results to display per page
    page_size_query_param = LISTING_PAGINATION_SIZE_PARAM # Query parameter to read page size from

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