# Generated by Django 3.2.11 on 2023-07-24 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0007_alter_image_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['number', 'place'], 'verbose_name': 'изображение', 'verbose_name_plural': 'изображение'},
        ),
        migrations.AlterModelOptions(
            name='places',
            options={'verbose_name': 'место', 'verbose_name_plural': 'места'},
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='', verbose_name='изображение'),
        ),
    ]
