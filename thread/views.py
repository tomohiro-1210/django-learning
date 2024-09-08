from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, TemplateView, FormView, CreateView, ListView
from django.urls import reverse_lazy
from django import forms

from . models import Topic, Category, Comment
from . forms import TopicCreateForm ,TopicForm, CommentModelForm

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
        
class CategoryView(ListView):
    template_name = 'thread/category.html'
    context_object_name = 'topic_list'

    def get_queryset(self):
        return Topic.objects.filter(category__url_code = self.kwargs['url_code'])
     
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['category'] = get_object_or_404(Category, url_code=self.kwargs['url_code'])
        return ctx
    
# コメント
class TopAndCommentView(FormView):
    template_name = 'thread/detail_topic.html'
    form_class = CommentModelForm
    
    def form_valid(self, form):
        # comment = form.save(commit=False)
        # comment.topic = Topic.ojbects.get(id=self.kwargs['pk'])
        # comment.no = Comment.objects.filter(topic=self.kwargs['pk']).count() + 1
        # comment.save()
        
        CommentModelForm.save_with_topic(self.kwargs.get('pk'))
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('thread:topic', kwargs={'pk': self.kwargs['pk']})
    
    def get_context_data(self):
        ctx = super().get_context_data()
        ctx['topic'] = Topic.objects.get(id=self.kwargs['pk'])
        ctx['comment_list'] = Comment.objects.filter(topic_id=self.kwargs['pk'].order_by('no'))
        return ctx