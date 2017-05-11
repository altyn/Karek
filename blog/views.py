from django.views.generic import TemplateView, ListView
from .models import News, Partners, Advert, Founders


# Create your views here.
class IndexView(TemplateView):
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        try:
            context["news_list"] = News.objects.all()
        except News.DoesNotExist:
            context["news_list"] = []
        try:
            context["partners_list"] = Partners.objects.all()
        except Partners.DoesNotExist:
            context["partners_list"] = []
        print(context)
        return context


class NewsList(ListView):
    template_name = 'news/news_list.html'
    model = News
    context_object_name = 'news_list'
