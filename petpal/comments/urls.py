from django.urls import path
from .views import ShelterCommentCreateView,  ShelterCommentListView

urlpatterns = [
    # path('<int:application_id>/comments/', ),
    # path('<int:application_id>/comment/<int:comment_id>/', ),
    path('shelters/<int:shelter_id>/comments/', ShelterCommentListView.as_view()),
    path('shelters/<int:shelter_id>/comment/<int:comment_id>/', ShelterCommentCreateView.as_view()),
]
