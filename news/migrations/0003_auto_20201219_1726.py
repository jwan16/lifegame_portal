# Generated by Django 3.1.2 on 2020-12-19 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_news_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='message',
            field=models.TextField(max_length=200),
        ),
    ]