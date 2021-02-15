# Generated by Django 3.0.12 on 2021-02-12 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booth', '0016_auto_20201222_2319'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='boothrequirement',
            name='academic_score',
        ),
        migrations.RemoveField(
            model_name='boothrequirement',
            name='growth_score',
        ),
        migrations.RemoveField(
            model_name='boothrequirement',
            name='health_score',
        ),
        migrations.RemoveField(
            model_name='boothrequirement',
            name='joy_score',
        ),
        migrations.RemoveField(
            model_name='boothrequirement',
            name='money',
        ),
        migrations.RemoveField(
            model_name='boothrequirement',
            name='relationship_score',
        ),
        migrations.RemoveField(
            model_name='boothscoring',
            name='academic_score',
        ),
        migrations.RemoveField(
            model_name='boothscoring',
            name='growth_score',
        ),
        migrations.RemoveField(
            model_name='boothscoring',
            name='health_score',
        ),
        migrations.RemoveField(
            model_name='boothscoring',
            name='joy_score',
        ),
        migrations.RemoveField(
            model_name='boothscoring',
            name='money',
        ),
        migrations.RemoveField(
            model_name='boothscoring',
            name='relationship_score',
        ),
        migrations.RemoveField(
            model_name='participation',
            name='academic_score',
        ),
        migrations.RemoveField(
            model_name='participation',
            name='growth_score',
        ),
        migrations.RemoveField(
            model_name='participation',
            name='health_score',
        ),
        migrations.RemoveField(
            model_name='participation',
            name='joy_score',
        ),
        migrations.RemoveField(
            model_name='participation',
            name='money',
        ),
        migrations.RemoveField(
            model_name='participation',
            name='relationship_score',
        ),
        migrations.AddField(
            model_name='boothrequirement',
            name='overall_score',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='boothscoring',
            name='overall_score',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='participation',
            name='overall_score',
            field=models.IntegerField(default=0),
        ),
    ]
