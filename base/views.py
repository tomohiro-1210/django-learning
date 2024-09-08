from django.shortcuts import render
from django.views.generic import TemplateView, ListView
# from django.http import HttpResponse
# from django.template import loader
from thread.models import Topic

def top(request):
    """TOP画面表示用関数

    関数ベースのビューの説明として作成

    """
#    template = loader.get_template('base/top.html')
    ctx = {'title': 'Django学習ちゃんねる(仮)'}
#    return HttpResponse(template.render(ctx, request))
    return render(request, 'base/top.html', ctx)

class TopView(TemplateView):
    """TOP画面表示用クラス

    クラスベースのビューの説明として作成

    """
    template_name = 'base/top.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['title'] = 'IT学習ちゃんねる(仮)'
        return ctx

#今回追加したクラス
class TopicListView(ListView):
    """TOP画面表示クラス

    リストビューの説明として作成

    """
    template_name = 'base/top.html'
    # model = Topic
    queryset = Topic.objects.order_by('-created')
    context_object_name = 'topic_list'