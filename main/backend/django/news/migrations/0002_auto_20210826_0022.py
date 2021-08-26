# Generated by Django 3.2.3 on 2021-08-26 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='image_url',
            field=models.URLField(max_length=5000, verbose_name='Image URL'),
        ),
        migrations.AlterField(
            model_name='news',
            name='source_url',
            field=models.URLField(max_length=5000, verbose_name='Source URL'),
        ),
    ]