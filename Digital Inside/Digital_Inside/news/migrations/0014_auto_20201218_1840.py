# Generated by Django 3.1.4 on 2020-12-18 15:40

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0013_auto_20201218_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_post',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 18, 15, 40, 52, 300379, tzinfo=utc)),
        ),
    ]
