# Generated by Django 2.2.14 on 2020-07-21 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_sponsor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('description', models.TextField()),
            ],
        ),
    ]
