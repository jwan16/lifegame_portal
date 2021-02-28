# Generated by Django 3.1.2 on 2021-02-27 15:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('player', '0005_instructorscore_record_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='instructorscore',
            name='instructor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='account.user'),
            preserve_default=False,
        ),
    ]
