from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import News, Partners, Advert, Founders


# Create your views here.
class IndexView(TemplateView):
    template_name = 'base.html'


class NewsList(ListView):
    template_name = 'news/news_list.html'
    model = News
    context_object_name = 'news_list'
