# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Tweet(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.original != None
