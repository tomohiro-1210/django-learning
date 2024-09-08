from django.urls import path
from django.views.generic import TemplateView
from .views import *
app_name = 'base'

urlpatterns = [
    # path('', top, name='top'),
    path('', TopicListView.as_view(), name='top'),
    path('terms/', TemplateView.as_view(template_name='base/terms.html'), name='terms'),
]