# Generated by Django 4.1.2 on 2024-01-28 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("booth", "0010_transaction_bank_deposit_alter_boothscoring_flat_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="transaction",
            name="bank_deposit",
        ),
        migrations.AddField(
            model_name="transaction",
            name="interest_rate",
            field=models.FloatField(default=0, verbose_name="利率"),
        ),
        migrations.AlterField(
            model_name="transaction",
            name="money",
            field=models.IntegerField(default=0, verbose_name="金錢"),
        ),
    ]
