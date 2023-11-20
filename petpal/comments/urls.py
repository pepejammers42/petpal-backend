from django.urls import path
from .views import ShelterCommentCreateView,  ShelterCommentListView

urlpatterns = [
    path('applications/<int:application_id>/comments/all/', ),
    path('applications/int:application_id>/comment/', ),
    path('shelters/<int:shelter_id>/comments/all/', ShelterCommentListView.as_view()),
    path('shelters/<int:shelter_id>/comments/', ShelterCommentCreateView.as_view()),
]
