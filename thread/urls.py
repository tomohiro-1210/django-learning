from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.TopicDetailView.as_view(), name='topic'),
]