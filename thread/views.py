from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, TemplateView, FormView, CreateView
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
        

class TopicCreateView(CreateView):
    """トピック投稿用関数

    CreateViewの練習用クラスとして作成

    """
    template_name = 'thread/create_topic.html'
    form_class = TopicCreateForm
    model = Topic
    success_url = reverse_lazy('top')
    
    def form_valid(self, form):
        ctx = {'form': form}
        if self.request.POST.get('next', '') == 'confirm':
            return render(self.request, 'thread/confirm_topic.html', ctx)
        if self.request.POST.get('next', '') == 'back':
            return render(self.request, 'thread/create_topic.html', ctx)
        if self.request.POST.get('next', '') == 'create':
            return super().form_valid(form)
        else:
            # 正常動作ではここは通らない。エラーページへの遷移でも良い
            return redirect(reverse_lazy('top'))