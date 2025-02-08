# Generated by Django 4.2.19 on 2025-02-08 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("player", "0004_alter_player_born_academic_level"),
    ]

    operations = [
        migrations.AlterField(
            model_name="player",
            name="born_academic_level",
            field=models.IntegerField(
                choices=[
                    (0, "無學歷"),
                    (1, "小學畢業"),
                    (2, "中學畢業"),
                    (3, "大專畢業"),
                    (4, "大學畢業"),
                ]
            ),
        ),
    ]
