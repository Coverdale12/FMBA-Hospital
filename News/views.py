from turtle import title
from django.shortcuts import render, get_object_or_404

# Create your views here.

from .models import News

def news_list(request):
    news_items = News.objects.all()
    return render(request, 'news/news.html', {'news_items': news_items})

def news_info(request, news_id):
    news_item = get_object_or_404(News, id=news_id)
    return render(request, 'news/news_info.html', {'news_item': news_item})

