# Generated by Django 4.1.2 on 2023-02-22 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("player", "0005_alter_player_user"),
    ]

    operations = [
        migrations.RemoveField(model_name="player", name="live_status",),
        migrations.AddField(
            model_name="player",
            name="active",
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
