# Generated by Django 4.1.2 on 2024-02-25 07:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("player", "0016_alter_instructorscore_record_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="instructorscore",
            name="record_time",
            field=models.DateTimeField(
                blank=True,
                default=datetime.datetime(
                    2024, 2, 25, 7, 42, 0, 837358, tzinfo=datetime.timezone.utc
                ),
            ),
        ),
    ]