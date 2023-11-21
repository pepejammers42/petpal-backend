from django.urls import path
from .views import ShelterCommentCreateView,  ShelterCommentListView, ApplicationCommentCreateView, ApplicationCommentListView

urlpatterns = [
    path('applications/<int:application_id>/', ApplicationCommentListView.as_view()),
    path('applications/<int:application_id>/comment/', ApplicationCommentCreateView.as_view()),
    path('shelters/<int:shelter_id>/', ShelterCommentListView.as_view()),
    path('shelters/<int:shelter_id>/comments/', ShelterCommentCreateView.as_view()),
]
