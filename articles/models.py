# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length = 100)
    slug =  models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add = True)
    thumb = models.ImageField(default = 'default.png', blank = True)
    author = models.ForeignKey(User, default = None)
    # add in thumbnail later
    # add in author later

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50] + '...'


# everytime we make model or change one we do on terminal
# python manage.py makemigrations
# python manage.py migrate
