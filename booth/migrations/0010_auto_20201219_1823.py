# Generated by Django 3.1.2 on 2020-12-19 10:23

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('booth', '0009_auto_20201219_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booth',
            name='booth_admins',
            field=models.ManyToManyField(blank=True, null=True, related_name='booth_admins', to=settings.AUTH_USER_MODEL),
        ),
    ]