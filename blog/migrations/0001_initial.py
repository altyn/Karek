# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-24 14:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('thumb', models.ImageField(blank=True, null=True, upload_to='images/thumb')),
                ('content', models.TextField(blank=True, null=True)),
                ('date', models.DateField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name_plural': 'Новости',
                'verbose_name': 'Новость',
            },
        ),
    ]
