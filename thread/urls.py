from django.urls import path
from . import views

urlpatterns = [
    # トピック詳細画面
    path('<int:pk>/', views.TopicDetailView.as_view(), name='topic'),

    # 今回追加。シンプルなトピック投稿画面
    path('create_topic/', views.simple_topic_create, name='create_topic'),
    
    # カテゴリーごと
    path('category/<str:url_code>/', views.CategoryView.as_view(), name='category'),
]