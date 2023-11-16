from django.urls import path
from . import views

urlpatterns=[
    path('shelter/', views.ShelterListCreateAPIView.as_view(), name='shelter_list_create'),
    path('seeker/', views.SeekerListCreateAPIView.as_view(), name='seeker_list_create'),
]