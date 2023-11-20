from django.urls import path
from .views import ApplicationCreate, ApplicationRetrieveUpdate, ShelterApplicationList

urlpatterns = [
    path('pets/<int:pk>/applications', ApplicationCreate.as_view()),
    path('applications/<int:pk>', ApplicationRetrieveUpdate.as_view()),
    path('applications/', ShelterApplicationList.as_view()),
]

