# Generated by Django 3.1.2 on 2020-12-15 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20201215_2152'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='icon',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]