# Generated by Django 4.1.2 on 2024-02-25 15:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("booth", "0021_alter_boothscoring_record_time_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="participation",
            name="remarks",
        ),
        migrations.RemoveField(
            model_name="transaction",
            name="remarks",
        ),
        migrations.AlterField(
            model_name="boothscoring",
            name="record_time",
            field=models.DateTimeField(
                blank=True,
                default=datetime.datetime(
                    2024, 2, 25, 15, 23, 30, 645449, tzinfo=datetime.timezone.utc
                ),
                verbose_name="時間",
            ),
        ),
        migrations.AlterField(
            model_name="boothtraffic",
            name="record_time",
            field=models.DateTimeField(
                blank=True,
                default=datetime.datetime(
                    2024, 2, 25, 15, 23, 30, 645449, tzinfo=datetime.timezone.utc
                ),
            ),
        ),
        migrations.AlterField(
            model_name="participation",
            name="record_time",
            field=models.DateTimeField(
                blank=True,
                default=datetime.datetime(
                    2024, 2, 25, 15, 23, 30, 645449, tzinfo=datetime.timezone.utc
                ),
                verbose_name="時間",
            ),
        ),
        migrations.AlterField(
            model_name="transaction",
            name="record_time",
            field=models.DateTimeField(
                blank=True,
                default=datetime.datetime(
                    2024, 2, 25, 15, 23, 30, 645449, tzinfo=datetime.timezone.utc
                ),
                verbose_name="時間",
            ),
        ),
    ]