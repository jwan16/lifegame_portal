# Generated by Django 4.1.2 on 2023-03-03 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("player", "0008_player_born_academic_level_player_born_defect_and_more"),
    ]

    operations = [
        migrations.RemoveField(model_name="player", name="born_status",),
    ]