# Generated by Django 5.0.6 on 2024-10-28 09:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_article_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='created_at',
            field=models.DateField(blank=True, default=datetime.datetime(2024, 10, 28, 9, 44, 10, 903665, tzinfo=datetime.timezone.utc), help_text='Укажите дату создания', null=True, verbose_name='Дата создания'),
        ),
    ]
