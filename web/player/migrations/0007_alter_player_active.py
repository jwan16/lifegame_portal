# Generated by Django 4.1.2 on 2023-02-22 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("player", "0006_remove_player_live_status_player_active"),
    ]

    operations = [
        migrations.AlterField(
            model_name="player", name="active", field=models.BooleanField(default=True),
        ),
    ]
