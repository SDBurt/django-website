# Generated by Django 2.0.2 on 2018-02-12 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20180209_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='thumbnail',
            field=models.ImageField(blank=True, default='placeholder.jpg', upload_to=''),
        ),
    ]
