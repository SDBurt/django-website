# Generated by Django 2.0.2 on 2018-02-21 22:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_auto_20180219_1937'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='draft',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='article',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 21, 22, 42, 42, 334454, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
