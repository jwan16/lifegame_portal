# Generated by Django 3.1.2 on 2020-12-14 12:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('player', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booth',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Participation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('health_score', models.IntegerField()),
                ('academic_score', models.IntegerField()),
                ('growth_score', models.IntegerField()),
                ('relationship_score', models.IntegerField()),
                ('joy_score', models.IntegerField()),
                ('money', models.IntegerField()),
                ('booth_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booth.booth')),
                ('player_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='player.player')),
            ],
        ),
    ]
