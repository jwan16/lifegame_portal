# Generated by Django 3.1.2 on 2020-12-19 08:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booth', '0006_remove_boothscoring_booth'),
    ]

    operations = [
        migrations.RenameField(
            model_name='boothscoring',
            old_name='score_name',
            new_name='name',
        ),
    ]
