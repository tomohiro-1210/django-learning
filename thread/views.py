from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, TemplateView
from django.urls import reverse_lazy

from . models import Topic
from . forms import TopicCreateForm ,TopicForm

class TopicDetailView(DetailView):
    """トピック表示用クラス

    DetailView使用例として作成

    """
    template_name = 'thread/detail_topic.html'
    model = Topic
    context_object_name = 'topic'
    
def simple_topic_create(request):
    """シンプルなトピック投稿用関数

    関数ベースの投稿機能作成例として実装

    """
    template_name = 'thread/create_topic.html'
    ctx = {}
    if request.method == 'GET':
        ctx['form'] = TopicCreateForm()
        return render(request, template_name, ctx)
    
    if request.method == 'POST':
        topic_form = TopicCreateForm(request.POST)
        if topic_form.is_valid():
            topic_form.save()
            return redirect(reverse_lazy('base:top'))
        else:
            ctx['form'] = topic_form
            return render(request, template_name, ctx)
        
def topic_create(request):
    """トピック投稿用関数

    関数ベースのFormを用いた投稿機能の実装例

    """
    template_name = 'thread/create_topic.html'
    ctx = {}
    if request.method == 'GET':
        form = TopicForm()
        ctx['form'] = form
        return render(request, template_name, ctx)
    
    if request.method == 'POST':
        topic_form = TopicForm(request.POST)
        if topic_form.is_valid():
            # topic_form.save()
            topic = Topic()
            cleaned_data = topic_form.cleaned_data
            topic.title = cleaned_data['title']
            topic.message = cleaned_data['message']
            topic.user_name = cleaned_data['user_name']
            topic.category = cleaned_data['category']
            topic.save()            
            return redirect(reverse_lazy('base:top'))
        else:
            ctx['form'] = topic_form
            return render(request, template_name, ctx)