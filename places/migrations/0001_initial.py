# Generated by Django 3.2.11 on 2023-07-16 12:44

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Places',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='default title', max_length=200, verbose_name='название')),
                ('short_description', models.TextField(blank=True, verbose_name='краткое описание')),
                ('long_description', tinymce.models.HTMLField(blank=True, verbose_name='полное описание')),
                ('latitude', models.FloatField(verbose_name='широта')),
                ('longitude', models.FloatField(verbose_name='долгота')),
            ],
            options={
                'verbose_name': 'PLACE',
                'verbose_name_plural': 'PLACES',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_number', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('image', models.ImageField(upload_to='')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='places.places', verbose_name='Место')),
            ],
            options={
                'verbose_name': 'IMAGE',
                'verbose_name_plural': 'IMAGES',
                'ordering': ['image_number', 'place'],
            },
        ),
    ]