from django.db import models
from django.utils import timezone
from filer.fields.file import FilerFileField


# Новости
class News(models.Model):
    title = models.CharField(max_length=300)
    thumb = FilerFileField()
    content = models.TextField(null=True, blank=True)
    date = models.DateField(default=timezone.now, editable=False)

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

    def __str__(self):
        return '%s' % self.id


# Основатели
class Founders(models.Model):
    name = models.CharField(max_length=300, default=0)
    desc = models.TextField(max_length=600, blank=True, null=True)
    image = FilerFileField()

    class Meta:
        verbose_name = "Основатель"
        verbose_name_plural = "Основатели"

    def __str__(self):
        return '%s' % self.id


# Партнеры
class Partners(models.Model):
    name = models.CharField(max_length=200, null=False)
    image = FilerFileField(related_name="image_1")

    class Meta:
        verbose_name = "Партнер"
        verbose_name_plural = "Партнеры"

    def __str__(self):
        return '%s' % self.id


# Объявление
class Advert(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    text = models.TextField(max_length=800, null=False, blank=False)
    image = FilerFileField()

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"

    def __str__(self):
        return '%s' % self.id
