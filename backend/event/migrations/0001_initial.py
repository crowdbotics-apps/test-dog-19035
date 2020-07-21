# Generated by Django 2.2.14 on 2020-07-21 15:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('amenities', models.TextField()),
                ('image', models.SlugField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField()),
                ('description', models.TextField()),
                ('track', models.TextField()),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedule_location', to='event.Location')),
            ],
        ),
        migrations.CreateModel(
            name='Presenter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('title', models.CharField(max_length=256)),
                ('schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='presenter_schedule', to='event.Schedule')),
            ],
        ),
        migrations.CreateModel(
            name='MySchedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='myschedule_schedule', to='event.Schedule')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='myschedule_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]