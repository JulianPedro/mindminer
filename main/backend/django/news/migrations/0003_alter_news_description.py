# Generated by Django 3.2.3 on 2021-08-26 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20210826_0022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='description',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Description'),
        ),
    ]
