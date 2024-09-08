from django.shortcuts import render
from django.views.generic import TemplateView

def top(request):
    template = 'base/top.html'
    ctx = {'title': 'Django学習ちゃんねる(仮)'}
    return render(request, template, ctx)

# TOPビュー

class TopView(TemplateView):
    template_name = 'base/top.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['title'] = 'IT学習ちゃんねる(仮)'
        return ctx