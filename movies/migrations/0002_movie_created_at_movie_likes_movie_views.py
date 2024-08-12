# Generated by Django 5.0.7 on 2024-08-08 11:11

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movie',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='movie',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]