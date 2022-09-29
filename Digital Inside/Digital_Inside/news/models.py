from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
# Create your models here.


class Post(models.Model):
    id_post = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150)
    contents = models.TextField()
    image = models.ImageField(upload_to='news/media', blank=True)
    date_post = models.DateTimeField(default=timezone.now())
    author = models.ForeignKey(User, models.DO_NOTHING, db_column='author')

    class Meta:
        verbose_name='Новость'
        verbose_name_plural = 'Новости'
        db_table = 'post'


class Comments(models.Model):
    id_comment = models.AutoField(primary_key=True)
    content = models.TextField()
    date_post = models.DateTimeField(default=timezone.now())
    commentator = models.ForeignKey(User,models.DO_NOTHING,db_column='commentator')
    post = models.ForeignKey(Post, models.DO_NOTHING,db_column='post')

    class Meta:
        verbose_name='Комментарий'
        verbose_name_plural = 'Комментарии'
        db_table = 'comments'


class Role(models.Model):
    id_role = models.IntegerField(primary_key=True)
    type = models.CharField(max_length=20)

    class Meta:
        db_table = 'role'
