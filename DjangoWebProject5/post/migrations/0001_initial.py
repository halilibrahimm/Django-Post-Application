# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-18 18:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Başlık')),
                ('content', models.TextField(verbose_name='İçerik')),
                ('publishingDate', models.DateTimeField(auto_now_add=True, verbose_name='Yayınlanma Tarihi')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('slug', models.SlugField(unique=True)),
            ],
            options={
                'ordering': ['-publishingDate', 'id'],
            },
        ),
    ]
