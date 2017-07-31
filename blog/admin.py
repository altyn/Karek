from django.contrib import admin
from .models import News, Founders, Social
from .models import Partners, Advert, Slider
from .models import Gallery


# Register your models here.
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)


@admin.register(Founders)
class FoundersAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


@admin.register(Partners)
class PartnersAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


@admin.register(Advert)
class AdvertsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'text',)


@admin.register(Slider)
class SlidersAdmin(admin.ModelAdmin):
    list_display = ('id', 'desc', 'link',)

    def has_add_permission(self, request):
        if Slider.objects.count() > 3:
            return False
        else:
            return True


@admin.register(Social)
class SocialsAdmin(admin.ModelAdmin):
    list_display = ('header', 'facebook', 'vk', 'ok', 'twitter', 'instagram',)
    list_display_links = ('header',)

    def has_add_permission(self, request):
        if Social.objects.count() > 0:
            return False
        else:
            return True
