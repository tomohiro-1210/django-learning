from django.urls import path
from . import views

urlpatterns = [
    # トピック詳細画面
    path('<int:pk>/', views.TopicDetailView.as_view(), name='topic'),
    #path('<int:pk>/', views.TopicTemplateView.as_view(), name='topic'),
    #path('<int:pk>/', views.detail_topic, name='topic'),

    # 今回追加。シンプルなトピック投稿画面
    #path('create_topic/', views.simple_topic_create, name='create_topic'),
    # path('create_topic/', views.topic_create, name='create_topic'),
    # path('create_topic/', views.TopicFormView.as_view(), name='create_topic'),
    path('create_topic/', views.TopicCreateView.as_view(), name='create_topic')
]