# Generated by Django 4.1.2 on 2024-01-20 01:37

import account.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0021_alter_user_encrypted_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="encrypted_id",
            field=models.CharField(
                default=account.models.generate_encrypted_string, max_length=32
            ),
        ),
    ]