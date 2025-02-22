# Generated by Django 4.2.19 on 2025-02-08 01:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("player", "0003_delete_instructorscore"),
        ("booth", "0002_delete_boothtraffic"),
    ]

    operations = [
        migrations.AlterField(
            model_name="transaction",
            name="booth",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="transaction_booth",
                to="booth.booth",
                verbose_name="攤位",
            ),
        ),
        migrations.AlterField(
            model_name="transaction",
            name="player",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="transaciton_player",
                to="player.player",
                verbose_name="玩家",
            ),
        ),
    ]
