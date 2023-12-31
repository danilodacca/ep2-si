from django.db import models
from django.conf import settings
from django.utils import timezone


class Post(models.Model):
    name = models.CharField(max_length=255)
    ingredientes = models.CharField(max_length=255)
    desc = models.CharField(max_length=1000, default="valor temporário")
    modo_de_preparo=models.CharField(max_length=1000)
    foto_url = models.URLField(max_length=200, null=True)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.name}'


class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    likes = models.IntegerField(default=0)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'"{self.text}" - {self.author.username}'

class Category(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    posts = models.ManyToManyField(Post)

    def __str__(self):
        return f'{self.name} by {self.author}'