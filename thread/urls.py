from django.urls import path
from . import views

urlpatterns = [
    # トピック詳細画面
    path('<int:pk>/', views.TopicDetailView.as_view(), name='topic'),

    # 今回追加。シンプルなトピック投稿画面
    path('create_topic/', views.TopicCreateView.as_view(), name='create_topic')
]