# Generated by Django 3.1.2 on 2021-03-19 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='url',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
