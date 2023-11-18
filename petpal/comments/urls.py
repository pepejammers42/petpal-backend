from django.urls import path
from .views import ShelterCommentCreateView,  ShelterCommentListView

urlpatterns = [
    # path('<int:application_id>/comments/', ),
    # path('<int:application_id>/comments/create/', ),
    path('shelters/<int:shelter_id>/comments/', ShelterCommentListView.as_view()),
    path('shelters/<int:shelter_id>/comments/create/', ShelterCommentCreateView.as_view()),
]
