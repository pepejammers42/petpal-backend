from django.urls import path
from .views import NotificationCreate, NotificationRetrieveUpdateDestroy

urlpatterns = [
    path('', NotificationCreate.as_view(), name='pet-listing-list-create'),
    path('<int:pk>/', NotificationRetrieveUpdateDestroy.as_view(), name='pet-listing-retrieve-update-destroy'),
]