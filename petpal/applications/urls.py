from django.urls import path
from .views import AppCreate, AppRetrieveUpdate, ShelterAppList

urlpatterns = [
    path('/pets/<int:pk>/applications', AppCreate.as_view()),
    path('/applications/<int:pk>', AppRetrieveUpdate.as_view()),
    path('/applications/', ShelterAppList.as_view()),
]

