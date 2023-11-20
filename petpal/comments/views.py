from django.shortcuts import get_object_or_404, render
from rest_framework import generics, permissions
from .models import Comment
from accounts.models import Shelter, AuthUser
from applications.models import Application
from django.contrib.contenttypes.models import ContentType
from .serializers import CommentSerializer
from .permissions import IsApplicationRelated
# Create your views here.
class ShelterCommentCreateView(generics.CreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        shelter_id = self.kwargs['shelter_id']
        get_object_or_404(Shelter, pk=shelter_id) #check shelter exists
        content_type = ContentType.objects.get_for_model(Shelter)
        serializer.save(user=self.request.user, object_id=shelter_id, content_type=content_type)
                                            

class ShelterCommentListView(generics.ListAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        shelter_id = self.kwargs['shelter_id']
        content_type = ContentType.objects.get_for_model(Shelter)
        return Comment.objects.filter(content_type=content_type, object_id=shelter_id).order_by('-created_at') #descending order


class ApplicationCommentCreateView(generics.CreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsApplicationRelated]
    def perform_create(self, serializer):
        application_id = self.kwargs['application_id']
        assert get_object_or_404(Application, pk=application_id)
        content_type = ContentType.objects.get_for_model(Application)
        serializer.save(user=self.request.user, object_id=shelter_id, content_type=content_type)
                                            

class ApplicationCommentListView(generics.ListAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsApplicationRelated]

    def get_queryset(self):
        application_id = self.kwargs['application_id']
        content_type = ContentType.objects.get_for_model(Application)
        return Comment.objects.filter(content_type=content_type, object_id=application_id).order_by('-created_at') #descending order
