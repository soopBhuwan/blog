# Generated by Django 3.2.5 on 2021-08-19 03:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='subtitle',
            field=models.TextField(default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_on',
            field=models.DateTimeField(verbose_name=datetime.datetime(2021, 8, 19, 3, 21, 43, 632796, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='updated_on',
            field=models.DateTimeField(verbose_name=datetime.datetime(2021, 8, 19, 3, 21, 43, 632711, tzinfo=utc)),
        ),
    ]
