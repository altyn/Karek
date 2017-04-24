from django.db import models
from django.utils import timezone


# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=300)
    thumb = models.ImageField(upload_to="images/thumb", null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    date = models.DateField(default=timezone.now, editable=False)

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

    def __str__(self):
        return '%s' % self.id