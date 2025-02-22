# Generated by Django 4.2.19 on 2025-02-08 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("booth", "0007_alter_transaction_money"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="participation",
            name="score",
        ),
        migrations.AddField(
            model_name="participation",
            name="academic_level",
            field=models.IntegerField(
                blank=True,
                choices=[
                    (0, "無學歷"),
                    (1, "小學畢業"),
                    (2, "中學畢業"),
                    (3, "大專畢業"),
                    (4, "大學畢業"),
                ],
                default=0,
                null=True,
                verbose_name="學歷",
            ),
        ),
        migrations.AddField(
            model_name="participation",
            name="flat",
            field=models.IntegerField(
                blank=True, default=0, null=True, verbose_name="樓宇"
            ),
        ),
        migrations.AddField(
            model_name="participation",
            name="growth_score",
            field=models.IntegerField(
                blank=True, default=0, null=True, verbose_name="成長分數"
            ),
        ),
        migrations.AddField(
            model_name="participation",
            name="health_score",
            field=models.IntegerField(
                blank=True, default=0, null=True, verbose_name="健康分數"
            ),
        ),
        migrations.AddField(
            model_name="participation",
            name="money",
            field=models.IntegerField(
                blank=True, default=0, null=True, verbose_name="金錢"
            ),
        ),
        migrations.AddField(
            model_name="participation",
            name="relationship_score",
            field=models.IntegerField(
                blank=True, default=0, null=True, verbose_name="關係分數"
            ),
        ),
        migrations.AddField(
            model_name="participation",
            name="skill_score",
            field=models.IntegerField(
                blank=True, default=0, null=True, verbose_name="技能分數"
            ),
        ),
        migrations.AddField(
            model_name="participation",
            name="steps",
            field=models.IntegerField(
                blank=True, default=-1, null=True, verbose_name="步數"
            ),
        ),
    ]
