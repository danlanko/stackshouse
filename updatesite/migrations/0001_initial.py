# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-22 10:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PhotoGallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo_title', models.CharField(max_length=50)),
                ('upload_image', models.ImageField(upload_to='photo_gallery')),
            ],
        ),
        migrations.CreateModel(
            name='SetPhotoCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo_gallery_category', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SetVideoCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_category', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ShowReel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_title', models.CharField(max_length=250, unique=True)),
                ('video_id', models.CharField(help_text='Please copy and paste VIDEO ID only(eg: DhbtCIQuGv4)', max_length=250)),
                ('select_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='updatesite.SetVideoCategory')),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slider_title', models.CharField(max_length=50)),
                ('slider_image', models.ImageField(upload_to='slider_image')),
                ('slider_desc', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='photogallery',
            name='select_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='updatesite.SetPhotoCategory'),
        ),
    ]