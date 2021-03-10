# Generated by Django 3.1.2 on 2021-03-09 15:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('player', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Booth',
            fields=[
                ('id', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, max_length=1000, null=True)),
                ('url', models.CharField(blank=True, max_length=1000, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('booth_admins', models.ManyToManyField(related_name='booth_admins', to=settings.AUTH_USER_MODEL)),
                ('booth_in_charge', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='booth_in_charge', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BoothRequirement',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('overall_score', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='BoothScoring',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('overall_score', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Participation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('record_time', models.DateTimeField(auto_now_add=True)),
                ('remarks', models.TextField(blank=True, max_length=1000, null=True)),
                ('booth', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booth.booth')),
                ('marker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='player.player')),
                ('score', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booth.boothscoring')),
            ],
        ),
        migrations.CreateModel(
            name='BoothTraffic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('record_time', models.DateTimeField(auto_now_add=True)),
                ('booth', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booth.booth')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='booth',
            name='score_options',
            field=models.ManyToManyField(related_name='score_options', to='booth.BoothScoring'),
        ),
    ]
