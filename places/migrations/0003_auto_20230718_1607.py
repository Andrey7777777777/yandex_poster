# Generated by Django 3.2.11 on 2023-07-18 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_alter_image_unique_together'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['number', 'place'], 'verbose_name': 'IMAGE', 'verbose_name_plural': 'IMAGES'},
        ),
        migrations.RenameField(
            model_name='image',
            old_name='image_number',
            new_name='number',
        ),
        migrations.AlterField(
            model_name='places',
            name='title',
            field=models.CharField(default='no title', max_length=200, verbose_name='название'),
        ),
    ]
