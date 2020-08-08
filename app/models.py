# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Tweet(models.Model):
    original = models.ForeignKey("self", null=True, on_delete=models.SET_NULL)
    content = models.TextField()
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE) #many users can have many tweets
    image = models.ImageField(blank=True, null=True)
    likes = models.ManyToManyField(User, related_name='tweet_user',blank=True)

    class Meta:
        ordering = ['-id']

    @property
    def is_retweet(self):
        return self.original != None

    # Change the name of Tweet in django-admin web page
    def __str__(self):
        return self.original != None

    def serialize(self):
        return {
            "id": self.id,
            "content": self.content,
            "likes": 0,
        }