# Generated by Django 3.1.4 on 2020-12-16 14:57

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id_post', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=150)),
                ('contents', models.TextField()),
                ('image', models.TextField()),
                ('date_post', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
                'db_table': 'post',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id_role', models.IntegerField(primary_key=True, serialize=False)),
                ('type', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'role',
            },
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id_comment', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.TextField()),
                ('date_post', models.DateTimeField()),
                ('commentator', models.IntegerField()),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.post')),
            ],
            options={
                'db_table': 'comments',
            },
        ),
    ]
