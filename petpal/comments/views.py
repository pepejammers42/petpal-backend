from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Comment
from accounts.models import Shelter
# from ..applications.models import Application
from django.contrib.contenttypes.models import ContentType
from .serializers import CommentSerializer
# Create your views here.

class ShelterCommentCreateView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_create(self, serializer):
        shelter_id = self.kwargs['shelter_id']
        content_type = ContentType.objects.get_for_model(Shelter)
        serializer.save(content_type=content_type,object_id=shelter_id)

class ShelterCommentListView(generics.ListAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        shelter_id = self.kwargs['shelter_id']
        content_type = ContentType.objects.get_for_model(Shelter)
        return Comment.objects.filter(content_type=content_type, object_id=shelter_id).order_by('-created_at')
