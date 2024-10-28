# Generated by Django 5.0.6 on 2024-10-27 17:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_article_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='created_at',
            field=models.DateField(blank=True, default=datetime.datetime(2024, 10, 27, 17, 53, 15, 799520, tzinfo=datetime.timezone.utc), help_text='Укажите дату создания', null=True, verbose_name='Дата создания'),
        ),
    ]
