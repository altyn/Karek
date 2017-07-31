from django.views.generic import TemplateView, ListView
from .models import News, Partners, Advert
from .models import Founders, Slider, Social
from .models import Gallery


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
        try:
            context["founders_list"] = Founders.objects.all()
        except Founders.DoesNotExist:
            context["founders_list"] = []
        try:
            context["slider_list"] = Slider.objects.all()
        except Slider.DoesNotExist:
            context["slider_list"] = []
        try:
            context["social_list"] = Social.objects.all()
        except Social.DoesNotExist:
            context["social_list"] = []
        try:
            context["gallery_list"] = News.objects.all()
        except News.DoesNotExist:
            context["gallery_list"] = []
        return context


class NewsList(ListView):
    template_name = 'news/news_list.html'
    model = News
    context_object_name = 'news_list'


class GalleryList(ListView):
    template_name = 'gallery/gallery_list.html'
    model = Gallery
    context_object_name = 'gallery_list'
