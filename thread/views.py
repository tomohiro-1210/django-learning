from django.shortcuts import render
from django.views.generic import DetailView

from . models import Topic

class TopicDetailView(DetailView):
    """トピック表示用クラス

    DetailView使用例として作成

    """
    template_name = 'thread/detail_topic.html'
    model = Topic
    context_object_name = 'topic'