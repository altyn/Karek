from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class IndexView(TemplateView):
    template_name = 'base.html'


class TabOneView(TemplateView):
    template_name = 'partials/tabs/tab-first.html'


class TabTwoView(TemplateView):
    template_name = 'partials/tabs/tab-second.html'


class TabThreeView(TemplateView):
    template_name = 'partials/tabs/tab-third.html'
