# Generated by Django 4.1.2 on 2024-02-03 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0002_alter_newscategory_name"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="news",
            name="time",
        ),
        migrations.RemoveField(
            model_name="news",
            name="url",
        ),
        migrations.AlterField(
            model_name="news",
            name="date",
            field=models.DateTimeField(verbose_name="發怖時間"),
        ),
    ]
