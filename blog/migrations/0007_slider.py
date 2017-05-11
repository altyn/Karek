# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-11 12:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import filer.fields.file


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0007_auto_20161016_1055'),
        ('blog', '0006_auto_20170510_2145'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc_1', models.TextField()),
                ('desc_2', models.TextField()),
                ('desc_3', models.TextField()),
                ('image_1', filer.fields.file.FilerFileField(on_delete=django.db.models.deletion.CASCADE, related_name='slider_image_1', to='filer.File')),
                ('image_2', filer.fields.file.FilerFileField(on_delete=django.db.models.deletion.CASCADE, related_name='slider_image_2', to='filer.File')),
                ('image_3', filer.fields.file.FilerFileField(on_delete=django.db.models.deletion.CASCADE, related_name='slider_image_3', to='filer.File')),
                ('news_link_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='news_link_1', to='blog.News')),
                ('news_link_2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='news_link_2', to='blog.News')),
                ('news_link_3', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='news_link_3', to='blog.News')),
            ],
            options={
                'verbose_name': 'Слайдер',
                'verbose_name_plural': 'Слайдеры',
            },
        ),
    ]
