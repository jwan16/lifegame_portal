# Generated by Django 4.1.2 on 2024-01-20 02:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("booth", "0006_transaction_saving_alter_participation_booth_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="transaction",
            name="saving",
        ),
        migrations.AddField(
            model_name="boothscoring",
            name="active",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="boothscoring",
            name="flat",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name="boothscoring",
            name="record_time",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now, verbose_name="時間"
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="boothscoring",
            name="academic_level",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="boothscoring",
            name="growth_score",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="boothscoring",
            name="health_score",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="boothscoring",
            name="money",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="boothscoring",
            name="relationship_score",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="boothscoring",
            name="skill_score",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name="boothscoring",
            name="steps",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]