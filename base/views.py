from django.shortcuts import render

def top(request):
    template = 'base/top.html'
    ctx = {'title': 'Django学習ちゃんねる(仮)'}
    return render(request, template, ctx)