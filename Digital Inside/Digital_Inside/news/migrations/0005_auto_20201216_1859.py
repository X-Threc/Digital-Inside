# Generated by Django 3.1.4 on 2020-12-16 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20201216_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='commentator',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.IntegerField(default=1),
        ),
    ]
